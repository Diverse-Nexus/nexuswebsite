from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField # For Fields/attributes
from wtforms.validators import DataRequired,Length,Email,EqualTo #for validators

class RegistrationForm(FlaskForm):
    username=StringField('Username',validators=[DataRequired(),Length(min=3,max=20)]) #validators- to have limits for username
    
    email=StringField('Email',validators=[DataRequired(),Email()])
    
    password=PasswordField('Password',validators=[DataRequired()])
    
    confirm_password=PasswordField('Confirm Password',validators=[DataRequired(),EqualTo('password')])
    
    submit=SubmitField('Sign Up')
    
    
class LoginForm(FlaskForm):
     
    email=StringField('Email',validators=[DataRequired(),Email()])
    
    password=PasswordField('Password',validators=[DataRequired()])
    
    rememberme=BooleanField('Remember Me') #to stay logged in for sometime after browser closes
    
    submit=SubmitField('Login')
    
    