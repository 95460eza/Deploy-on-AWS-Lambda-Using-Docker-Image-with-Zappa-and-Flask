
import logging
#from flask import Flask
from flask import Flask, jsonify
#from werkzeug.wsgi import ClosingIterator


# Configure logging
logging.basicConfig(level=logging.INFO)


flask_app = Flask(__name__)

@flask_app.route('/')
def index():
    return jsonify(message='NATOU est tu la? Manifeste toi !!!')
    #return 'NATOU est tu la? Manifeste toi  !!!'


# Zappa requires the handler function to be named `lambda_handler`
def lambda_handler(event, context):
    # Use the Flask app's WSGI handler
    # With this return statement, you allow the "Flask app" to process the Lambda-generated event and context as if on a traditional web server by using Flask's WSGI handler  
    logging.info("The event generated by the Lambda function HAS BEEN PARSED successfully: %s", event)
    return flask_app(event, context)