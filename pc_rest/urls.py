"""pc_rest URL Configuration

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
from django.urls import path, include
from rest_framework.decorators import api_view
from rest_framework.response import Response

urlpatterns = [
    path('cpu/', include('cpu.urls')),
    path('motherboard/', include('motherboard.urls')),
    path('admin/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),
]


# temporary
@api_view(['GET'])
def all_urls(request):
    urls = [url := request.build_absolute_uri()]
    for i in range(len(urlpatterns) - 2):
        urls.append(url + urlpatterns[i].pattern.regex.pattern[1:])
    return Response(urls)


urlpatterns.append(path('', all_urls))
