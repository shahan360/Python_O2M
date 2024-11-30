from flask import Flask
app = Flask(__name__)
print(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

#quickstart guide to flask app: https://flask.palletsprojects.com/en/stable/quickstart/

#flask templates: http://flask.palletsprojects.com/en/1.1.x/quickstart/#rendering-templates

#flask static files: http://flask.palletsprojects.com/en/1.1.x/quickstart/#static-files

#flask favicon: http://flask.palletsprojects.com/en/1.1.x/patterns/favicon/

#flask jinja2: https://en.wikipedia.org/wiki/Jinja_(template_engine)
#flask jinja2: https://jinja.palletsprojects.com/en/2.11.x/

#create dynamic URLs: https://stackoverflow.com/questions/7478366/create-dynamic-urls-in-flask-with-url-for
#variable rules: https://flask.palletsprojects.com/en/1.1.x/quickstart/#variable-rules



@app.route('/thoughts')
def thoughts():
    return 'It starts from 0ne and taken to 1ne!'

@app.route('/thoughts2')
def thoughts2():
    return 'It starts from 0ne and taken to 1ne!'
