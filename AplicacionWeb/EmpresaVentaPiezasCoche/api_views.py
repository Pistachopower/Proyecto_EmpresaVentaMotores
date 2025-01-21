from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .forms import *

@api_view(['GET'])
def listar_clientes(request):
    cliente = Cliente.objects.select_related('empleado').all()
    serializer= ClienteSerializer(cliente, many=True)
    return Response(serializer.data)
