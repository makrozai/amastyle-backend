from rest_framework import serializers
from .models import Variant, Images
from colors.serializers import ColorSerializer
from sizes.serializers import SizeSerializer

class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Images
        fields = "__all__"

class VariantSerializer(serializers.ModelSerializer):
    color = ColorSerializer(read_only=True)
    size = SizeSerializer(read_only=True)
    images = serializers.SerializerMethodField(read_only=True)

    def get_images(self, obj):
        images = obj.images_set.all()
        serializer = ImageSerializer(images, many=True)
        return serializer.data

    class Meta:
        model = Variant
        fields = "__all__"
