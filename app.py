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

@app.route('/add_user',methods=['GET','POST'])
def add_user():
    if request.method == 'POST':
        name = request.form['name']
        status = request.form['status']
        new_user = User(name=name,status=status)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_user.html')

@app.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', users=users)

@app.route('/update_user/<int:user_id>',methods=['GET','POST'])
def update_user(user_id):
    user = User.query.get_or_404(user_id)
    if request.method=='POST':
        user.status = request.form['status']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('update_user.html',user=user)

@app.route("/delete_user/<int:user_id>",methods=['POST'])
def delete_user(user_id):
    user= User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('index'))
        
if __name__ == '__main__':
    app.run(debug=True)
