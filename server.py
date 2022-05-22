# Import all controllers that will be using app.routes #
import flask_app
from flask_app.controllers import user_controller
from flask_app.controllers import movie_controller
from flask_app.controllers import favorite_controller
from flask_app.controllers import queue_controller

import os
print( os.environ.get("movie_api_key") )

# Without app server WILL NOT run #
from flask_app import app

if __name__ == "__main__":
    app.run(debug=True)