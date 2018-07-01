import os


class BaseConfig:
    """Base config"""
    TESTING = False


class DevelopmentConfig(BaseConfig):
    """Development config"""
    DATABASE_URI = os.getenv("DATABASE_URI")


class TestingConfig(BaseConfig):
    """Testing config"""
    TESTING = True
    DATABASE_URI = os.getenv("TEST_DATABASE_URI")


class ProductionConfig(BaseConfig):
    """Production config"""
    DATABASE_URI = os.getenv("DATABASE_URI")
