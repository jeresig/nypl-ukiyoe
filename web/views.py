from flask import Flask
from flask_pymongo import PyMongo
from lib import NYPLViewsLib

app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'nypl'
mongo = PyMongo(app)
nypl = NYPLViewsLib()


@app.route('/')
def index():
    return nypl.render_index(mongo.db)

# if __name__ == '__main__':
#     app.run(debug=True, port=5006)
