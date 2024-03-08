from flask import Flask,render_template,url_for,flash,redirect
from forms import RegistrationForm,LoginForm

app = Flask(__name__) 

app.config['SECRET_KEY']='474534cac076e805a1ac91b2d683a8e3'

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