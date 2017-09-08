# views.py
import os
from flask import Flask, request, render_template, flash, redirect, url_for, get_flashed_messages, session, abort
from .forms import LoginForm, RegistrationForm, ShoppingListForm, additemsForm
from . import app
from app.modals import User



@app.route('/', methods= ['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'user_id' in session:
            return redirect(url_for ('viewitems'))
    else:
        return redirect(url_for ('login'))

@app.route('/signin', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            if 'user_id' in session:
                return redirect(url_for('viewitems'))
            return redirect(url_for('showsignup'))
    
        else:
            if form.validate() == False:
                flash('All fields are required.')
                return render_template('signin.html', form = form)
    

    return render_template('signin.html', 
                           title='Sign In',
                           form = form)
    

@app.route('/signup', methods= ['GET', 'POST'])
def showsignup():
    
        form = RegistrationForm(request.form)

        if request.method == 'POST':
        
            if form.validate_on_submit():
                    #return error if email is already registered
                user_dict = User.users.items()
                existing_user = {k:v for k,v in user_dict if form.Email.data in v['email']}
                if existing_user:
                    flash('email exists please log in instead')
                    return render_template('signin.html', form = LoginForm())
                else:
                    #if email doesnot exist register user
                    new_user = User(form.Username.data, form.Email.data, form.Password.data, form.Password2.data)
                    new_user.create_user()
                  #assign a user_id
                #create a session
                    for key, value in user_dict:     # gets id, eg 2
                        if form.Email.data in value['email']:
                            session['user_id'] = key
                            flash('You have successfully signed up')
                            return redirect(url_for('login', form = LoginForm()))
                        
                

        
            elif form.errors:
                if form.Password.data != form.Password2.data:
                    flash({"message": "Your passwords don't match!"})
                    return render_template('signup.html', form = form)
                    
            
        
            
            
        elif request.method == 'GET':
            return render_template('signup.html', 
                           title='Sign up',
                           form=form)


@app.route('/create_shoppinglist', methods= ['GET', 'POST'])
def createshoppinglist():
    form = ShoppingListForm()
    if request.method == 'POST':
        if form.validate() == False:
            flash('All fileds requirred')
            return render_template('create_list.html', form = form)
        else:
            flash('You have successfully created a list')
            return redirect('/additem')
        
    elif request.method == 'GET':
        return render_template('create_shoppinglist.html', 
                           title='items',
                           form=form)

@app.route('/additem', methods= ['GET', 'POST'])
def additem():
    if request.method == "GET":
        form = additemsForm(request.form)
        return render_template('additem.html', form = form)
        flash("You have added an item to your shopping list")
    elif request.method == 'POST':
        return redirect('/viewitems')

@app.route('/viewitems', methods= ['GET', 'POST'])
def viewitems():
    form = additemsForm(request.form)
    if request.method == "POST":
        itemname = request.form['itemname']
        Quantity = request.form['Quantity']
        Price = request.form['Price']
        return render_template('viewitems1.html', itemname = itemname, Quantity = Quantity, Price = Price)
    elif request.method == "GET":
        return redirect('/additem')

    



