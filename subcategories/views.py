from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.utils.text import slugify
from rest_framework import status

from .models import SubCategory
from .serializers import SubCategorySerializer
from categories.models import Category


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_subcategory(request, pk):
    if request.user.is_staff:
        serializer = SubCategorySerializer(data=request.data)
        category = Category.objects.get(pk=pk)
        if serializer.is_valid():
            name = serializer.validated_data['name']
            slug = slugify(name)
            serializer.save(category=category,slug=slug)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)

@api_view(['GET'])
def get_subcategories(request):
    subcategories = SubCategory.objects.all()
    serializer = SubCategorySerializer(subcategories, many=True)
    return Response({'subcategories': serializer.data})

@api_view(['GET'])
def get_subcategories_by_category(request, pk):
    subcategories = SubCategory.objects.filter(category=pk)
    serializer = SubCategorySerializer(subcategories, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_subcategory(request, pk):
    subcategory = SubCategory.objects.get(pk=pk)
    serializer = SubCategorySerializer(subcategory, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def search(request):
    query = request.query_params.get('query')
    if query is None:
        query = ''
    subcategories = SubCategory.objects.filter(name__icontains=query)
    serializer = SubCategorySerializer(subcategories, many=True)
    return Response({'subcategories': serializer.data})

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def edit_subcategory(request, pk):
    subcategory = SubCategory.objects.get(pk=pk)
    if request.user.is_staff:
        serializer = SubCategorySerializer(subcategory, data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data['name']
            slug = slugify(name)
            serializer.save(slug=slug)
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_subcategory(request, pk):
    subcategory = SubCategory.objects.get(pk=pk)
    if request.user.is_staff:
        subcategory.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)
