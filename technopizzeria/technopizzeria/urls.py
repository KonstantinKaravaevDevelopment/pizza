"""technopizzeria URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static

from pizzeria.views import DaniaAPIViewSet
from pizzeria.views import ConfigurationAPIViewSet
from pizzeria.views import CategoryAPIViewSet
from pizzeria.views import LanguageAPIViewSet

urlpatterns = [
    path('admin/', admin.site.urls),
    # V1.0
    path('api/v1/pizza/', DaniaAPIViewSet.as_view({'get': 'list'})),
    # V2.0
    path('api/v2/pizza/configuration/', ConfigurationAPIViewSet.as_view({'get': 'list'})),
    path('api/v2/pizza/dania/', DaniaAPIViewSet.as_view({'get': 'list'})),
    path('api/v2/pizza/category/', CategoryAPIViewSet.as_view({'get': 'list'})),
    path('api/v2/pizza/language/', LanguageAPIViewSet.as_view({'get': 'list'}))
] + static(settings.IMAGES_URL, document_root = settings.IMAGES_ROOT)
