from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    ORACLE_DB_USER = os.getenv("ORACLE_DB_USER")
    ORACLE_DB_PASSWORD = os.getenv("ORACLE_DB_PASSWORD")
    ORACLE_DB_HOST = os.getenv("ORACLE_DB_HOST")
    ORACLE_DB_PORT = os.getenv("ORACLE_DB_PORT")
    ORACLE_DB_SID = os.getenv("ORACLE_DB_SID")
