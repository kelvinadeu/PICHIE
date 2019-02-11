from flask_sqlalchemy import SQLALCHEMY

bootstrap = Bootstrap()
db = SQLALCHEMY()

def create_app(config_name):
    app = Flask(__name__)

    #Initializingflaskextensions
    bootstrap.init_app(app)
    db.init_app(app)
