__author__ = "Shaden ALharbi"
__email__ = "391202175@qu.edu.sa"

"""
A getting started code that establish a flask app with some
predefined configuration. 

There is only one route which returns a simple text to indicate
the server is working. No malicious link or missing files handling. 
"""
from flask import Flask
from flask import render_template
from flask import abort
import os

app = Flask(__name__)

STATUS_OK = "HTTP/1.0 200 OK\n\n"
STATUS_FORBIDDEN = "HTTP/1.0 403 Forbidden\n\n"
STATUS_NOT_FOUND = "HTTP/1.0 404 Not Found\n\n"
STATUS_NOT_IMPLEMENTED = "HTTP/1.0 401 Not Implemented\n\n"

@app.route("/<link>")
def hello(link):
    #checks //, ~, .., returns 403 if any hits
    #print(link)
    if "//" in link or "~" in link or ".." in link: 
        abort(403)
        
    
    source_path = "templates/" + link
    if os.path.isfile(source_path):
        return render_template(link)
    else:
        abort(404) 

@app.errorhandler(404)
def error_404(error):
    return render_template('404.html'), 404 

@app.errorhandler(403)
def error_403(error):
    return render_template('403.html'), 403

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')