
from django.urls import path
from .views import home_view,homeloan_view,personalloan_view,goldloan_view,educationloan_view,vehicleloan_view,endpage_view
from . import views
urlpatterns = [
    
    path('home/',home_view, name='home'),
    path('homeloan/',homeloan_view, name='homeloan'),
    path('personalloan/',personalloan_view, name='personalloan'),
    path('goldloan/',goldloan_view, name='goldloan'),
    path('educationloan/',educationloan_view, name='educationloan'),
    path('vehicleloan/',vehicleloan_view, name='vehicleloan'),
    path('details/',views.create, name='details'),
    path('payments/',views.payment_details, name='payments'),
    path('endpage/',endpage_view, name='endpage'),
    path('register/', views.register, name='register'),
    path('', views.login, name='login'),
]
