from django.conf.urls import url, include
from . import views

urlpatterns = [
# root route to index method
    url(r'^$', views.index),

# calls index method to display all the users
    url(r'^users$', views.index),


# calls new method to display create-new-user form on new.html
    # url(r'^users/new$', views.new),
    url(r'new$', views.new),


# calls edit method to display edit-user form on edit.html
    # url(r'^\d/edit$', views.edit),
# this captures the user data by id; the url above doesn't
    url(r'^users/(?P<user_id>\d+)/edit$', views.edit),

# calls show method to display info for user with a given id entered into keyword field
    # url(r'^\d', views.show),
    # url(r'^users/\d', views.show),
# this captures the user data by id; the urls above don't:
    url(r'^users/(?P<user_id>\d+)/show$', views.show),


# calls create method to insert new a user record into database
    url(r'^users/create$', views.create),

# calls deletecheck method to render deletecheck.html
    url(r'^users/(?P<user_id>\d+)/deletecheck$', views.deletecheck),

# calls destroy method to delete user with a given id entered into keyword field
    # url(r'^\d$/destroy$', views.destroy),
# this captures the user data by id; the url above doesn't
    url(r'^users/(?P<user_id>\d+)/destroy$', views.destroy),

# calls update method to update the changes submitted from the edit.html form
    # url(r'^update$', views.update),
# this captures the user data by id; the url above doesn't
    url(r'^users/(?P<user_id>\d+)/update$', views.update),
]
