from __future__ import unicode_literals
from .models import User
from django.shortcuts import render, HttpResponse, redirect



# routing OK
def index(request):
    print("Index method in views.py")
# saving users group in context; users list is displayed on index.html
    context = {
        'users': User.objects.all()
    }
    return render(request, 'users_app/index.html', context)


# routing OK
def new(request):
    print("New method in views.py: Displays a form on page new.html that allows user to create a new user")
    return render(request, 'users_app/new.html')


# Gets User object by id and sends it to edit.html for a user to edit
def edit(request, user_id):
    print("Edit method in views.py: Allows a user on page edit.html to edit an existing user with the given id")
    context = {
        'user': User.objects.get(id=user_id)
    }
    print("user_id is:", user_id)
    return render(request, 'users_app/edit.html', context)


def show(request, user_id):
    print("Show method in views.py: Displays the info for a user with a given id on page show.html")
# saving an individual user in context
    context = {
        'user': User.objects.get(id=user_id)
    }
    print("User is:", user_id)
    return render(request, 'users_app/show.html', context)


def create(request):
    print("Create method in views.py: Inserts a new user record into the database")
    User.objects.create(
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        email=request.POST['email'],
    )
    # returns to display page to display new user
    return redirect('/')


def deletecheck(request, user_id):
    print("Deletecheck method in views.py: Asks admin whether he/she wants to delete a user record")
    context = {
        "user": User.objects.get(id=user_id)
    }
    return render(request, 'users_app/deletecheck.html', context)


# Deletes a user by id; working
def destroy(request, user_id):
    print("Destroy method in views.py: Allows a user on page edit.html to remove a user with a given id")
    print("User ID is:", user_id)
    User.objects.get(id=user_id).delete()
    return redirect('/users')


# Sends edited user data to the database from edit.html when the "Update" button is pressed
def update(request, user_id):
    print("Update method in views.py: Updates the changes submitted from the edit form")
# updating user information
    update_user = User.objects.get(id=user_id)
    update_user.first_name = request.POST['first_name']
    update_user.last_name = request.POST['last_name']
    update_user.email = request.POST['email']
    update_user.save()
    return redirect('/users')
