"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,include,re_path
from . import view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('api.urls')),
    re_path('api/signup',view.signup,name='signup'),
    re_path('api/login',view.login,name='login'),
    re_path('api/test-token',view.test_token,name='test-token'),
    re_path('api/logout',view.logout,name='logout'),
    
    #  user crud
    path('api/users',view.get_users,name='get-users'),
    path('api/users/<int:pk>',view.get_user,name='get-user'),
    path('api/users/<int:pk>/delete',view.delete_user,name='delete-user'),
    path('api/users/<int:pk>/update',view.update_user,name='update-user'),
    
]
