from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.utils.text import slugify
from rest_framework import status

from .models import Variant, Images
from .serializers import VariantSerializer, ImageSerializer

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_variant(request):
    if request.user.is_staff:
        serializer = VariantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_image_variant(request, pk):
    if request.user.is_staff:
        serializer = ImageSerializer(data=request.data)
        variant = Variant.objects.get(pk=pk)
        if serializer.is_valid():
            serializer.save(variant=variant)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_image(request, pk):
    image = Images.objects.get(pk=pk)
    if request.user.is_staff:
        image.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)

@api_view(['GET'])
def get_variants(request):
    variants = Variant.objects.all()
    serializer = VariantSerializer(variants, many=True)
    return Response({'variants': serializer.data})

@api_view(['GET'])
def get_variants_by_product(request, pk):
    variants = Variant.objects.filter(product=pk)
    serializer = VariantSerializer(variants, many=True)
    return Response({'variants': serializer.data})

@api_view(['GET'])
def get_variant(request, pk):
    variant = Variant.objects.get(pk=pk)
    serializer = VariantSerializer(variant, many=False)
    return Response(serializer.data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def edit_variant(request, pk):
    variant = Variant.objects.get(pk=pk)
    if request.user.is_staff:
        serializer = VariantSerializer(variant, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_variant(request, pk):
    variant = Variant.objects.get(pk=pk)
    if request.user.is_staff:
        variant.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)

