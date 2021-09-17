class Config:
    DEBUG = False
    SECRET_KEY=b'_5#y2L"F4Q8z\n\xec]/'


class ProductionConfig(Config):
    pass
class DevelopmentConfig(Config):
    ENV = 'development'
    ENVIRONMENT = 'development'
    Environment = 'development'
    DEBUG = True
    TESTING = True
    DEVELOPMENT = True

CONFIGS = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "default": Config,
}