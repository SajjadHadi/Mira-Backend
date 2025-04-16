from alembic import context
from sqlalchemy import create_engine, pool

from config import settings
from db import Base

DATABASE_URL = settings.SQLALCHEMY_DATABASE_URL

target_metadata = Base.metadata


def run_migrations_online():
    engine = create_engine(DATABASE_URL, poolclass=pool.NullPool)

    with engine.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()


run_migrations_online()
