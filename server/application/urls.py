"""
URL configuration for SkinScan project.

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
from django.urls import path

from .views.change_password import ChangePassword
from .views.login import Login
from .views.register import Register
from .views.create_request import CreateRequest
from .views.add_data import AddData
from .views.models.all_models import GetAllModels
from .views.models.active_model import GetActiveModel
from .views.models.swap_model import SwapModel
from .views.jobs.retrain import Retrain
from .views.is_logged_in import IsLoggedIn
from .views.logout import Logout
from .views.is_admin import IsAdmin

urlpatterns = [
    path("login/", Login.as_view(), name="api-login"),
    path("register/", Register.as_view(), name="api-register"),
    path("change-password/", ChangePassword.as_view(), name="api-change-password"),
    path("create-request/", CreateRequest.as_view(), name="api-create-request"),
    path("add-data/", AddData.as_view(), name="add-data"),
    path("models/all-models/", GetAllModels.as_view(), name="api-all-models"),
    path("models/active-model/", GetActiveModel.as_view(), name="api-active-model"),
    path(
        "models/swap-model/<int:version>/", SwapModel.as_view(), name="api-swap-model"
    ),
    path("retrain/", Retrain.as_view(), name="api-retrain-model"),
    path("is_logged_in/", IsLoggedIn.as_view(), name="api-is-logged-in"),
    path("logout/", Logout.as_view(), name="api-logout"),
    path("is_admin/", IsAdmin.as_view(), name="api-is-admin"),
]
