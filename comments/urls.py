from django.urls import path
from .views import MessagesPage, PostCreateView, PostDetailView

urlpatterns = [
    path("messages/dashboard/all-messages/", MessagesPage.as_view(), name="messages"),
    path(
        "posts/dashboard-admin-licens/create-post-2023/",
        PostCreateView.as_view(),
        name="create",
    ),
    path("posts/<slug:slug>/", PostDetailView.as_view(), name="detail"),
]
