"""
URL configuration for spltech project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from .views import (
    HomeView,
    AboutView,
    PostContactView,
    ServicesView,
    ActionKitView,
    DeliverabilityView,
    TrainingView,
)

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('about', AboutView.as_view(), name="about"),
    path('contact', PostContactView.as_view(), name="contact"),
    path('services', ServicesView.as_view(), name="services"),
    path('services/actionkit', ActionKitView.as_view(), name="actionkit"),
    path('services/deliverability', DeliverabilityView.as_view(), name="deliverability"),
    path('services/training', TrainingView.as_view(), name="training"),
]
