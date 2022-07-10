import databases
import sqlalchemy
from decouple import config

DATABASE_URL = f"postgresql://{config('DB_USER')}:{config('DB_PASS')}@localhost:{config('DB_PORT')}/{config('SERVICE_NAME')}"

database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()
