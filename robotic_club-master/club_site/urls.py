"""club_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from basic_app import views
# from chat import views as views_chat
from django.conf import settings

from django.conf.urls import url
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.Index_page.as_view(),name='index_page'),
    # path("index_chat/",views_chat.index, name='index_chat'),
    # url(r'^(?P<room_name>[^/]+)/$', views_chat.room, name='room'),

    path("index/",include("basic_app.urls")),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)