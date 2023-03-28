from django.urls import path

from members import views

urlpatterns = [
    path('login/', views.login, name="login"),
    path('registration/', views.register, name="registration"),
    path('registration/register/', views.add),
    path('logon/', views.logon, name="logon"),
    path('logout/', views.logout, name="logout"),
    path('profile/', views.profile, name="profile"),
]
