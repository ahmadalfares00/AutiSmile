"""AutiSmileAPI URL Configuration

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

from django.urls import path
from . import views
from django.urls import path,include
from rest_framework import routers

router = routers.DefaultRouter()
router.register('ASD for children' ,views.AutismRecordView)
urlpatterns = [
      path('',include('djoser.urls')),
      path('',include('djoser.urls.authtoken')),

      path('testAuth', views.testAuth),
      path('signup', views.signup),
      path('asd',include(router.urls)),
      path('asd_child' , views.childrenAutismSpectrumTest),
      path('getUserRecord',views.getUserTestRecords),
      path('test',views.hhh),
      # path('test' , )
]
