from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('',views.home, name='home'),
    path('contact/',views.contact, name='contact'),
    path('signin/',views.signin, name='signin'),
    path('signup/',views.signup, name='signup'),
    path('about/',views.about, name='about'),
    path('signout/',views.signout, name='signout'),
    path('CreateContact/',CreateContact.as_view(), name='CreateContact'),
    path('ViewContacts/',ViewContacts.as_view(), name='ViewContacts'),
    path('DeleteContact/<str:pk>',DeleteContact.as_view(), name='DeleteContact'),
    path('DeleteContactSuccessPage/', DeleteContactSuccessPage.as_view(), name='DeleteContactSuccessPage'),
]