# Author: Jack Hermanson
import logging
import os
import sys
from logging.handlers import TimedRotatingFileHandler

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from application.config import Config
from logger import StreamLogFormatter, FileLogFormatter

db = SQLAlchemy()
migrate = Migrate(compare_type=True)
logging.basicConfig(level=logging.DEBUG)


def create_app(config_class=Config):
    # set up file paths for static resources
    app = Flask(__name__, static_url_path="/static", static_folder="web/static", template_folder="web/templates")

    # set up environment variables
    app.config.from_object(config_class)

    # models
    import application.modules.main.models

    # database
    db.app = app
    db.init_app(app)
    migrate.init_app(app, db)

    # todo routes and blueprints
    from application.modules.main.routes import main

    for blueprint in [main]:
        app.register_blueprint(blueprint)

    # return the app
    print("RUNNING APPLICATION")
    logger.debug("LOGGING IS RUNNING")
    logger.info(f"Running app in environment '{os.environ.get('ENVIRONMENT')}'")
    logger.info(f"FLASK_ENV: '{os.environ.get('FLASK_ENV')}'")
    return app


# Set up logging
logging.basicConfig()
logger = logging.getLogger("RNO")
logger.propagate = False
sh = logging.StreamHandler(sys.stdout)
sh.setFormatter(StreamLogFormatter())

log_dir = "logs"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

fh = TimedRotatingFileHandler(os.path.join(log_dir, "logs.txt"), when="midnight", interval=1, backupCount=7)
fh.setFormatter(FileLogFormatter())
fh.suffix += ".txt"
fh.namer = lambda name: name.replace(".txt", "") + ".txt"

logger.addHandler(fh)
logger.addHandler(sh)
logger.setLevel(
    logging.DEBUG
    if (os.environ.get("FLASK_ENV") == "dev" or os.environ.get("FLASK_ENV") == "development")
    else logging.INFO
)
