"""tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from rest_framework import routers
from tutorial.quickstart import views

from rest_framework_extensions.routers import ExtendedDefaultRouter

from tutorial.quickstart.router import SwitchDetailRouter
from tutorial.quickstart.views import UserTweetsViewSet, FollowViewSet, UserFollowsViewSet, UserFollowedViewSet

switch_router = SwitchDetailRouter()

router = ExtendedDefaultRouter()
UsersRegister = router.register(r'users', views.UserViewSet)
UsersRegister.register(r'tweets', UserTweetsViewSet, 'user-tweets', ['username'])
UsersRegister.register(r'follows', UserFollowsViewSet, 'user-follows', ['username'])
UsersRegister.register(r'followed', UserFollowedViewSet, 'user-followed', ['username'])
router.register(r'dags', views.DagViewSet)
router.register(r'tweets', views.TweetViewSet)
router.register(r'feed', views.FeedViewSet)
switch_router.register(r'follow', FollowViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('v1/', include(switch_router.urls)),
    path('v1/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]