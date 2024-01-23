from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.utils.text import slugify
from rest_framework import status

from .models import Store
from .serializers import StoreSerializer

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_store(request):
    if request.user.is_staff:
        serializer = StoreSerializer(data=request.data)
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
def get_stores(request):
    stores = Store.objects.all()
    serializer = StoreSerializer(stores, many=True)
    return Response({'stores': serializer.data})

@api_view(['GET'])
def get_store(request, pk):
    store = Store.objects.get(pk=pk)
    serializer = StoreSerializer(store, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def search(request):
    query = request.query_params.get('query')
    if query is None:
        query = ''
    stores = Store.objects.filter(name__icontains=query)
    serializer = StoreSerializer(stores, many=True)
    return Response({'stores': serializer.data})

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def edit_store(request, pk):
    store = Store.objects.get(pk=pk)
    if request.user.is_staff:
        serializer = StoreSerializer(store, data=request.data)
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
def delete_store(request, pk):
    store = Store.objects.get(pk=pk)
    if request.user.is_staff:
        store.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)

