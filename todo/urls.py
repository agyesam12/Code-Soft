from django.urls import path
from django.contrib.auth import views as auth_view
from . import views
from .views import CreateTodo, ViewTodos


urlpatterns = [
    path('', views.signin,name="signin"),
    path('home/', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('signup/', views.signup, name='signup'),
    path('signout/', views.signout, name='signout'),
    path('CreateTodo/', CreateTodo.as_view(), name='CreateTodo'),
    path('Viewtodos/', ViewTodos.as_view(), name='ViewTodos')
]