from django.urls import include, path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    ServiceDetailDetail,
    ServiceDetailViewSet,
    UserPostListView
)

from .views import WorkerListAPIView
from . import views
from .views import ServiceDetailViewSet
from rest_framework.routers import DefaultRouter
from .views import WorkerViewSet, generate_qr_code


router = DefaultRouter()
router.register(r'service-details', ServiceDetailViewSet, basename='service-detail')
router.register(r'workers', WorkerViewSet, basename='worker')
urlpatterns = [
    path('', PostListView.as_view(), name='service_details-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='service_details-about'),
    path('api/workers/', WorkerListAPIView.as_view(), name='worker-list'),
    path('service-details/', views.service_details, name='service_details'),
    path('api/', include(router.urls)),
    path('qrcode/<str:name>/', generate_qr_code, name='generate_qr_code'),
]

