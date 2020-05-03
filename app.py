import os
from flask import Flask  # From module flask import class Flask
app = Flask(__name__)    # Construct an instance of Flask class for our webapp

PORT = int(os.environ.get('OPENSHIFT_PYTHON_PORT', 8080))


@app.route('/')   # URL '/' to be handled by main() route handler
def main():
    """Say hello"""
    return 'Hello World! Built with Source 2 Image Build Strategy.'

@app.route('/whoami')   # URL '/' to be handled by main() route handler
def whoami():
    """Who Am I"""
    return 'I am Batman!!'

if __name__ == '__main__':  # Script executed directly?
    print("Hello World! Built with Source 2 Image Build Strategy.")
    app.run(host='0.0.0.0', port=PORT)
