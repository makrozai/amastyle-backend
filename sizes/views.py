from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.utils.text import slugify
from rest_framework import status

from .models import Size
from .serializers import SizeSerializer

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_size(request):
    if request.user.is_staff:
        serializer = SizeSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data['name']
            slug = slugify(name)
            serializer.save(slug=slug)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)

@api_view(['GET'])
def get_sizes(request):
    sizes = Size.objects.all()
    serializer = SizeSerializer(sizes, many=True)
    return Response({'sizes': serializer.data})

@api_view(['GET'])
def get_size(request, pk):
    size = Size.objects.get(pk=pk)
    serializer = SizeSerializer(size, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def search(request):
    query = request.query_params.get('query')
    if query is None:
        query = ''
    sizes = Size.objects.filter(name__icontains=query)
    serializer = SizeSerializer(sizes, many=True)
    return Response({'sizes': serializer.data})

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def edit_size(request, pk):
    size = Size.objects.get(pk=pk)
    if request.user.is_staff:
        serializer = SizeSerializer(size, data=request.data)
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
def delete_size(request, pk):
    size = Size.objects.get(pk=pk)
    if request.user.is_staff:
        size.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)

