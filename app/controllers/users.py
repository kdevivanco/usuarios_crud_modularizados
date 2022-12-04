from flask import Flask, render_template, request, redirect, Blueprint
from app.models.users import User



users = Blueprint('users', __name__, template_folder='templates')


@users.route('/')
def show_users():
    users = User.get_all()
    for user in users:
        print(user.first_name)
    return render_template('users.html',users=users)

@users.route('/create')
def show_create_page():
    users = User.get_all()
    return render_template('create.html',users=users)

@users.route('/create',methods = ["POST"])
def create_new_user():
    new_user = User.create_new(request.form)
    
    return redirect('/')

@users.route('/user/<id>')
def show_user(id):
    selected_user = User.get_one(id)
    selected_user = selected_user[0]
    return render_template('singleuser.html', selected_user = selected_user)


@users.route('/user/<id>/edit')
def edit_page(id):
    return render_template('edit.html',id=id)

@users.route('/user/<id>/edit',methods=["POST"])
def edit_user(id):
    id = id 
    print(request.form)
    User.edit_user(id,request.form)
    return redirect('/')

@users.route('/user/<id>/delete')
def delete_user(id):
    id = id 
    print(request.form)
    deleted = User.delete_user(id)
    if deleted:
        print("User deleted")
    return redirect('/')
