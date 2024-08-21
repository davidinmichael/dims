from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework  import status
from .permissions import *
from .models import *
from .serializer import *
# Create your views here.


class Result(APIView):

    def get(self, request):
        user = request.user
        result = Result.objects.get(user=user)
        if result:
            serializer = ResultSerializer(result, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"message": "No result available."}, status=status.HTTP_404_NOT_FOUND)



class ResultCreate(APIView):
    
    permission_classes = [IsLecturerOfCourse]

    def get (self, request):
        result = Result.objects.all()
        if result:
            serializer = ResultSerializer(result, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"message": "No result available."}, status=status.HTTP_404_NOT_FOUND)
    
    def post(self, request):
        
        serializer = ResultSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            result_serializer = ResultSerializer(serializer)
            return Response(result_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)