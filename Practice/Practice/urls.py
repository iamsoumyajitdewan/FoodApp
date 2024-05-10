"""
URL configuration for Practice project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,include
from django.contrib.auth import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('food/',include('Foodapp.urls')),

    path('users/',include('users.urls')),

    path('login/',views.LoginView.as_view(template_name='users/login.html'),name='login'),

    path('logout/',views.LogoutView.as_view(template_name='users/logout.html'),name='logout'),
]
# getting error in logout page : This page isn’t working  - HTTP ERROR 405

urlpatterns += [
    # ... the rest of your URLconf goes here ...
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# not getting the image in profile