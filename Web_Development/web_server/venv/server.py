#quickstart guide to flask app: https://flask.palletsprojects.com/en/stable/quickstart/

#flask templates: http://flask.palletsprojects.com/en/1.1.x/quickstart/#rendering-templates

#flask static files: http://flask.palletsprojects.com/en/1.1.x/quickstart/#static-files

#flask favicon: http://flask.palletsprojects.com/en/1.1.x/patterns/favicon/

#flask jinja2: https://en.wikipedia.org/wiki/Jinja_(template_engine)
#flask jinja2: https://jinja.palletsprojects.com/en/2.11.x/

#create dynamic URLs: https://stackoverflow.com/questions/7478366/create-dynamic-urls-in-flask-with-url-for
#variable rules: https://flask.palletsprojects.com/en/1.1.x/quickstart/#variable-rules

#information about MIME types: https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types



from flask import Flask, render_template

app = Flask(__name__)

# Print the name of the module for debugging purposes
print(__name__)

# Route for the homepage
@app.route('/')
def home():
    # Render an HTML template for the homepage
    return render_template('index.html')

# Route for the first thoughts page
@app.route('/thoughts')
def thoughts():
    # Return a simple text response
    return 'It starts from 0ne and taken to 1ne!'

# Route for the second thoughts page
@app.route('/thoughts2')
def thoughts2():
    # Return a simple text response
    return 'It starts from 0ne and taken to 1ne!'

if __name__ == '__main__':
    # Run the Flask app in debug mode for development
    app.run(debug=True)
