
#import logging
#from flask import Flask
from flask import Flask, jsonify
#from werkzeug.wsgi import ClosingIterator


# Configure logging
#logging.basicConfig(level=logging.INFO)


flask_app = Flask(__name__)


# "BY DEFAULT", the route decorator responds to HTTP GET requests. If you want to be able to handle other HTTP methods, you can explicitly specify them using the METHODS parameter 
# @flask_app.route('/', methods=['GET', 'POST', 'PUT']) 
@flask_app.route('/', methods=['GET'])
def index_page():    
    return jsonify(message= "NATOU es-tu la? ALORS Manifeste toi  !!!")

# When deploying a Flask application with Zappa, you don't need to include the host, port, and debug parameters b/c the Flask development server (app.run()) is not suitable for use in
# a production environment like AWS Lambda serverless.
# Zappa handles the deployment of your Flask application on AWS Lambda and its execution BY CREATING a Lambda function that is triggered by "API Gateway events".It takes care of the     
#necessary configurations  
#if __name__ == '__main__':        
    #flask_app.run(host='0.0.0.0', port=8000, debug=False)
    # flask_app.run()


# Always LAST statements of the file
# Zappa requires the handler function to be named `lambda_handler`
def lambda_handler(event, context):
    return flask_app(event, context)


