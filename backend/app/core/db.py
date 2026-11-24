from sqlalchemy import create_engine

from .config import Settings

# pool_pre_ping checks that a pooled connection is still alive before using it
engine = create_engine(str(Settings.DATABASE_URL), pool_pre_ping=True)
