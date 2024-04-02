from django.urls import path, include

from rest_framework.routers import DefaultRouter
from getBookData.views import BookDataViewSet

# ImageViewSetを設定
router = DefaultRouter()
router.register(r'bookdata', BookDataViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
