from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Diag
from .serializers import DiagSerializer
from digonal.func import *

class DiagView (APIView):

    def get (self, request, cols, rows, args):
        dg = Diag(cols,rows,args, diag(cols,rows,args))
        serializer_for_request = DiagSerializer(instance=dg)
        return Response(serializer_for_request.data)
# Create your views here.
