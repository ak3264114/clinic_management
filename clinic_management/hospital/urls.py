from . import views
from django.urls import path

urlpatterns = [
        path('',  views.home , name='home'),
        path("signin/",views.signin, name="signin"),
        path("signup/", views.signup, name="signup"),
        path("signout/", views.signout, name="logout"),
        path("details-doctors/", views.details_doctors, name="logout"),
        path("doctor-dashboard/", views.doctors_dashboard, name="doctor_dashboard"),
        path("profile/", views.profile, name="profile"),
        path("add-details/", views.add_details, name="add_details"),
        path("edit-details/", views.edit_details, name="edit_details"),


]