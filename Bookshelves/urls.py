from django.urls import path, include

from rest_framework.routers import DefaultRouter
from Bookshelves.views import ImageViewSet

# ImageViewSetを設定
router = DefaultRouter()
router.register(r'image', ImageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
