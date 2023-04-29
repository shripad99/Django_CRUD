from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("loginuser", views.loginuser, name="loginuser"),
    # path("display", views.display, name="display"),
    path('delete/<int:pk>/', views.delete_data, name='deletedata'),
    path('update/<int:pk>/', views.update_data, name='updatedata')
]
