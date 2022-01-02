from datetime import timedelta
from flask import Flask, render_template, redirect, url_for, session, jsonify
# Blueprints
from server import model
from user import user
from upload import upload_file
from property import dynamic_view

# from flask_session import Session
from flask_cors import CORS, cross_origin
# from flask_mail import Mail

app = Flask(__name__)

api_v1_cors_config = {
    "origins": ["http://127.0.0.1:5000"]
}
CORS(app, resources={
    r"/*": api_v1_cors_config
})
app.config['CORS_HEADERS'] = 'Content-Type'

app.register_blueprint(model, url_prefix="/model")
app.register_blueprint(user, url_prefix="")
app.register_blueprint(upload_file, url_prefix="")
app.register_blueprint(dynamic_view, url_prefix="")

# app.config["SESSION_PERMANENT"] = False
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=5)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SESSION_TYPE'] = 'filesystem'

## creating an instance of session
# sess = Session()

# create tables
@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/', methods=['POST','GET'])
def index():
    return render_template('index.html')

@app.route('/Contact',methods=['POST','GET'])
def Contact():
    return render_template('Contact.html')

if __name__ == '__main__':
    
    ## servide-side session.
    app.secret_key = "012#!APaAjaBoleh)(*^%"

    ## initialising the db
    from db import db
    db.init_app(app)

    ## Initialising session
    # app.secret_key = 'super secret key'
    # app.config['SESSION_TYPE'] = 'filesystem'
    # # sess.init_app(app)

    ## initialising the mail instance
    # from mail import mail
    # mail.init_app(app)

    app.run(debug=True)