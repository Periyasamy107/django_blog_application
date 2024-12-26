from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import (
    PostListAPIView,
    PostListCreateAPIView,
    PostRetrieveAPIView,
    PostRetrieveDestroyAPIView,
    PostRetrieveUpdateAPIView,
    CommentListAPIView,
    CommentListCreateAPIView,
    CommentRetrieveDestroyAPIView,
    UserCreate,
    CommentRetrieveUpdateAPIView,
    likePost,
)

from rest_framework.schemas import get_schema_view
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny

schema_view = get_schema_view(
    openapi.Info(
        title="DJANGO BLOG API",
        default_version="v1",
        description="API Documentation for Django Blog Application",
    ),
    public=True,
    permission_classes=(AllowAny,),
)

# Register your app urls here.

urlpatterns = [
    path("registration/", UserCreate.as_view(), name="registration"),
    path("api/token/", TokenObtainPairView.as_view(), name="api_token_obtain_view"),
    path(
        "api/token/refresh/", TokenRefreshView.as_view(), name="api_token_refresh_view"
    ),
    path("posts/", PostListAPIView.as_view()),
    path("posts/add/", PostListCreateAPIView.as_view()),
    path("posts/<int:pk>/", PostRetrieveAPIView.as_view()),
    path("posts/change/<int:pk>/", PostRetrieveUpdateAPIView.as_view()),
    path("posts/remove/<int:pk>/", PostRetrieveDestroyAPIView.as_view()),
    path("posts/<int:pk>/likes/", likePost, name="post_likes"),
    path("comments/", CommentListAPIView.as_view()),
    path("comments/add/", CommentListCreateAPIView.as_view()),
    path("comments/change/<int:pk>/", CommentRetrieveUpdateAPIView.as_view()),
    path("comments/remove/<int:pk>/", CommentRetrieveDestroyAPIView.as_view()),
    path(
        "blogDocs/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
]
