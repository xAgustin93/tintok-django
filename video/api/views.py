from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from video.models import Video, VideoLike
from video.api.serializers import VideoSerializer, VideoActionsSerializer, VideoLikeSerializer
from follow.models import Follow


class VideoApiViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = VideoSerializer
    queryset = Video.objects.all()
    http_method_names = ['get', 'post']
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    filterset_fields = ['user']
    ordering = ['-created_at']


class VideoActionsApiViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = VideoActionsSerializer
    queryset = Video.objects.all()
    http_method_names = ['put']


class VideoLikeApiViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = VideoLikeSerializer
    queryset = VideoLike.objects.all()
    http_method_names = ['get', 'post', 'delete']
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user', 'video']


class GetFollowingsVideosView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        followings = Follow.objects.filter(
            user=user).values_list('user_followed', flat=True)
        followings_ids = list(followings)

        videos_followings = Video.objects.filter(
            user__in=followings_ids
        ).order_by("-created_at")
        videos_followings_serializer = VideoSerializer(
            data=videos_followings, many=True)
        videos_followings_serializer.is_valid()
        data = videos_followings_serializer.data

        return Response(data)
