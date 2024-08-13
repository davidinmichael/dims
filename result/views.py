from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework  import status
from course.permissions import *
from .models import *
from .serializer import *
# Create your views here.


class ResultListCreate(APIView):
    permission_classes = [CourseWriteOrRead]
    def get (self, request):
        result = Result.objects.all()
        if result:
            serializer = ResultSerializer(result, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"message": "No result available."}, status=status.HTTP_404_NOT_FOUND)
    
    def post(self, request):
        student_first_name = request.data.get("student_first_name")
        student_last_name = request.data.get("student_last_name")
        student_level_year = request.data.get("student_level_year")
        matric_number = request.data.get("matric_number")
        
        try:
            account = Account.objects.get(first_name=student_first_name, last_name=student_last_name)
        except Account.DoesNotExist:
            return Response({"message": "Student does not exist"}, status=status.HTTP_404_NOT_FOUND)
        
        try:
            student = Student.objects.get(matric_number=matric_number, level_year=student_level_year, account=account)
        except Student.DoesNotExist:
            return Response({"message": "Student does not exist"}, status=status.HTTP_404_NOT_FOUND)
        
        request.data['student'] = student.id
        
        serializer = ResultSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            result_serializer = ResultSerializer(Result)
            return Response(result_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
