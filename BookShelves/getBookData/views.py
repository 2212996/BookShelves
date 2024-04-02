from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import BookData
from .serializers import BookDataSerializer

class BookDataViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.all()
    serializer_class = BookDataSerializer

    def create(self, request, *args, **kwargs):
        isbn = request.data['ISBN']
        title = request.data['Title']
        author = request.data['Author']
        publisher = request.data['Publisher']
        if isbn is not None:
            BookData.objects.create(isbn=isbn, title=title, author=author, publisher=publisher)
            # BookData.objects.create(isbn=isbn)
            return Response(status=status.HTTP_200_OK)

        return Response("Failed to register image.",
                        status=status.HTTP_400_BAD_REQUEST)