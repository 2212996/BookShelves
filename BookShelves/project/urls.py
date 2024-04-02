from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('Bookshelves.urls')), # appのurls.pyを指定
    path('api/v2/', include('getBookData.urls'))
]

if settings.DEBUG:
    # 画像表示用
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
