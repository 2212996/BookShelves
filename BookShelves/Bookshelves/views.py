from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Image
from .serializers import ImageSerializer

class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

		# 以下を追加します
    def create(self, request, *args, **kwargs):
	      # 画像登録処理
        img_data = request.data['imageData']
        if img_data is not None:
            img = Image.objects.create(image=img_data)
            return Response(img.image.url,
                            status=status.HTTP_200_OK)

        return Response("Failed to register image.",
                        status=status.HTTP_400_BAD_REQUEST)
