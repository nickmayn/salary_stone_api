from pydantic import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = 'Salary_Stone'
    ROOT_PATH: str = ''
    ELASTIC_URL = 'http://localhost:9200'
    CORS_ORIGINS: str = '*'

    class Config:
        env_file = '.env'

settings = Settings()
