import flask
from flask.templating import render_template



# create instance of Flask app
app = flask.Flask(__name__)


# create route that renders index.html template
@app.route('/', methods=['GET'])
def home():
    return render_template ('index.html')


if __name__ == '__main__':

       app.run(threaded=True, port=5500)