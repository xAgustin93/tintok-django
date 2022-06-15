from django.urls import path
from rest_framework.routers import DefaultRouter
from follow.api.views import FollowApiViewSet, FollowedsCountView, FollowersCountView

router_follow = DefaultRouter()

router_follow.register(prefix="follow", basename="follow",
                       viewset=FollowApiViewSet)

urlpatterns = [
    path('follow/followeds/count/<int:id_user>/', FollowedsCountView.as_view()),
    path('follow/followers/count/<int:id_user>/', FollowersCountView.as_view()),
]
