from flask import Flask, jsonify, request

# Initialize the Flask application
app = Flask(__name__)

# Route for the home page
@app.route('/')
def home():
    return "Welcome to the Flask Application!"

# API route for an example
@app.route('/api', methods=['GET'])
def api_example():
    return jsonify({
        'message': 'This is a sample API response.',
        'status': 'success'
    })
from flask import Flask, jsonify, request

# Initialize the Flask application
app = Flask(__name__)

# Route for the home page
@app.route('/')
def home():
    return "Welcome to the Flask Application!"

# API route for an example
@app.route('/api', methods=['GET'])
def api_example():
    return jsonify({
        'message': 'This is a sample API response.',
        'status': 'success'
    })

# Run the app and listen on all interfaces
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

