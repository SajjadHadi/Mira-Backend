import torch
from peft import PeftModel
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig

from config import settings


class MentalDisorderPredictor:
    def __init__(self):
        quant_config = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_use_double_quant=True,
            bnb_4bit_compute_dtype=torch.bfloat16,
            bnb_4bit_quant_type="nf4"
        )
        self.tokenizer = AutoTokenizer.from_pretrained(
            settings.BASE_MODEL,
            token=settings.HF_TOKEN,
            trust_remote_code=True
        )
        self.tokenizer.pad_token = self.tokenizer.eos_token
        self.tokenizer.padding_side = "right"

        self.base_model = AutoModelForCausalLM.from_pretrained(
            settings.BASE_MODEL,
            quantization_config=quant_config,
            device_map="auto",
            attn_implementation="eager",
            token=settings.HF_TOKEN,
            trust_remote_code=True
        )
        self.base_model.generation_config.pad_token_id = self.tokenizer.pad_token_id
        self.fine_tuned_model = PeftModel.from_pretrained(self.base_model, settings.FINE_TUNED_MODEL)
        self.fine_tuned_model.eval()
        self.response_template = "Based on the context, the disorder may be:"
        self.max_length = 512

    def predict(self, patient_statement: str) -> str:
        input_text = f"The Patient statement is: {patient_statement} {self.response_template}"
        inputs = self.tokenizer.encode(input_text, return_tensors="pt", truncation=True, max_length=512).to("cuda")
        attention_mask = torch.ones(inputs.shape, device="cuda")

        with torch.no_grad():
            outputs = self.fine_tuned_model.generate(
                inputs,
                attention_mask=attention_mask,
                max_new_tokens=5,
                num_return_sequences=1,
                pad_token_id=self.tokenizer.eos_token_id
            )

        prediction = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        disorder = prediction.split(self.response_template)[1].split('.')[0].split(' ')[2]
        return disorder


predictor = None


def get_predictor():
    global predictor
    if predictor is None:
        predictor = MentalDisorderPredictor()
    return predictor


def clear_predictor():
    global predictor
    if predictor is not None:
        del predictor.fine_tuned_model
        del predictor.base_model
        del predictor.tokenizer
        torch.cuda.empty_cache()
    predictor = None
