"""
URL configuration for mysite project.

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
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('EmpresaVentaPiezasCoche.urls')),
    path("__debug__/", include("debug_toolbar.urls")),
    path('accounts/', include('django.contrib.auth.urls')), #Django incluye las URLs de autenticación prediseñadas de Django en la URL
]

#handler404 = 'EmpresaVentaPiezasCoche.views.error_404_view'
#handler403 = 'EmpresaVentaPiezasCoche.views.error_403_view'
#handler400 = 'EmpresaVentaPiezasCoche.views.error_400_view'
#handler500 = 'EmpresaVentaPiezasCoche.views.error_500_view'
