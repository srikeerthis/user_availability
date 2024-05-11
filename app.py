from flask import Flask, render_template, jsonify, request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///users.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

db= SQLAlchemy(app)
migrate = Migrate(app, db)

class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(50),nullable=False)
    status = db.Column(db.String(50),nullable=False)

    def __repr__(self):
        return f'<User {self.name}>'

@app.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', users=users)

@app.route('/api/users')
def api_users():
    return jsonify(users)

if __name__ == '__main__':
    app.run(debug=True)
