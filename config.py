import os # Module allowing our application to interact with the operating system dependent functionality.
class Config:
    '''
    General configuration parent class
    '''
    NEWS_SOURCES_BASE_URL = 'https://newsapi.org/v1/sources?language=en&category={}'
    NEWS_ARTICLES_BASE_URL = 'https://newsapi.org/v1/articles?source={}&apiKey={}'
    NEWS_API_KEY = 'a463576900664bcb87cc440c2cb22785'
   
    

class ProdConfig(Config):
    '''
    Production  configuration child class
    Args:
    Config: The parent configuration class with General configuration settings
    '''
    pass

class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
    Config: The parent configuration class with General configuration settings
    '''
    DEBUG = True

config_options = {
    # A to help us access different configuration option classes.
    'development' : DevConfig,
    'production' : ProdConfig
}