import os

class config:
    """
    General configuration parent class
    """
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SECRET_KEY = "Adeu"

    #simple made configuration
    


    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringaschool:0713730881@localhost/pitchie'
