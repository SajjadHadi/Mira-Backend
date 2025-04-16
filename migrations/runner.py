import logging

from alembic import command
from alembic.config import Config

logger = logging.getLogger(__name__)


def run_migrations():
    logger.info("Running Alembic migrations")
    try:
        alembic_cfg = Config("alembic.ini")
        command.upgrade(alembic_cfg, "head")
        logger.info("Migrations applied successfully")
    except Exception as e:
        logger.error(f"Migration failed: {str(e)}")
        raise RuntimeError(f"Migration failed: {str(e)}")
