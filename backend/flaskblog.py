import os
from datetime import datetime #for current datetime
from flask import Flask,render_template,url_for,flash,redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm,LoginForm


app = Flask(__name__) 
app.config['SECRET_KEY']='474534cac076e805a1ac91b2d683a8e3'
#path for database
instance_path = os.path.join(app.root_path, 'instance')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(instance_path, 'site.db')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
#instance for database
db=SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True) #backref to access the user who created the post(post.author->displays author of the post)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"
    
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"
   

posts= [
    {
        'author':'Cohen',
        'title':'Death',
        'year':2024,
        'content':'Death is inevitable'
    },
    
    {
        'author':'Brian',
        'title':'Life',
        'year':2020,
        'content':'Life is to give'
    }
    
]

@app.route("/") # / is the homepage of site       
@app.route("/home")     
def home():
    return render_template('home.html',posts=posts)

@app.route("/about")
def about():
    return render_template('about.html',title='About')

@app.route("/register",methods=['GET','POST']) #to accept post request in the route
def register():
    form=RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!','success') #flash msg
        return redirect(url_for('home')) #to redirect to home after registering 
    return render_template('register.html',title='Register',form=form)

@app.route("/login",methods=['GET','POST']) #we need the post request as we use validate_on_submit
def login():
    form=LoginForm()
    if form.validate_on_submit():
            if form.email.data =='admin@blog.com' and form.password.data=='pass':
                flash('You have been logged in!','success')
                return redirect(url_for('home'))
            else:
                flash('Login Unsuccessful. Please check username and password','danger') #in bootstrap danger signifies a red alert
            
    return render_template('login.html',title='Login',form=form)

if __name__=='__main__':
    app.run(debug=True)
