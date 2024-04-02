from rest_framework import serializers
from .models import ISBN

class ISBNSerializer(serializers.ModelSerializer):

    class Meta:
        model = ISBN
        fields = "__all__"
