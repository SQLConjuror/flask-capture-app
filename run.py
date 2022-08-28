"""
This script runs the flasknotely application using a development server.
"""

from os import environ
from flaskcapture import app

if __name__ == '__main__':
    app.run('0.0.0.0', debug=True )
