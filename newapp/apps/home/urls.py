from django.urls import path
from . import views

urlpatterns = [
    path('index/',views.index,name="index"),
    path('register/',views.registerUser,name="register"),
    path('about/',views.about,name="about"),
    path('login/',views.loginUser,name="login"),
    path('logout/',views.logout,name="logout"),
    path('login/upload/',views.upload,name="upload"),
    path('profile/',views.profile,name="profile"),
    path('profile/edit',views.edit,name="edit"),
    path('profile/manage_edit',views.manage_edit,name="manage_edit")
]