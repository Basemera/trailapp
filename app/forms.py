from flask_wtf import Form
from wtforms import validators, ValidationError, TextField, IntegerField, PasswordField, TextAreaField, SubmitField, RadioField, SelectField, BooleanField
from wtforms.validators import (DataRequired, ValidationError, Email,
                                Length, EqualTo)

class LoginForm(Form):
   Username = TextField("Username",[validators.Required("Please enter your username.")])
   Password = PasswordField("Password", [validators.Required('Please enter your password')])
   submit = SubmitField("Send")
   
class RegistrationForm(Form):
    Username = TextField("Username", [validators.Required("Please enter your username.")])
    Email = TextField("Email", [validators.Required("Please enter your email address"), validators.Email("Please enter your email address")])
    Password = PasswordField("Password", [validators.Required('Please enter your password')])
    Password2 = PasswordField("re-type Password", [validators.Required('Please enter your password'), validators.equal_to(Password)])
    submit = SubmitField("Send")

class ShoppingListForm(Form):
    ListName = TextField("ListName",[validators.Required("Please give your shopping list a name.")])
    Description = TextField("Description", [validators.Required("Please give your shopping list a brief description."), validators.Length(min = 10)])
    submit = SubmitField("Send")
    

class additemsForm(Form):
    itemname = TextField("Item name",[validators.Required("Please enter an item name")])
    Price = IntegerField("Price")
    Quantity = IntegerField("Quantity")
    submit = SubmitField("Send")