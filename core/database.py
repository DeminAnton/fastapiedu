from sqlalchemy import create_engine, MetaData, text
from config import Settings

settings = Settings()

# Create an engine instance
sync_engine = create_engine(
    url=settings.DATABASE_URL_psycopg,
    echo=True,
    pool_size=5,
    max_overflow=10,
)


with sync_engine.connect() as conn:
    res = conn.execute(text("SELECT VERSION()"))
    print(f"res = {res.first()}")
    conn.commit()

# Create a MetaData instance
metadata = MetaData()