from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework  import status
from .permissions import *
from .models import *
from .serializer import *
# Create your views here.


class ResultListCreate(APIView):
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
            result_serializer = ResultSerializer()
            return Response(result_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class UserOutstandingCourse(APIView):

    def get(self, request):
        user = request.user
        student = Student.objects.get(user=user)
        courses = OutstandingCourses.objects.get(user=student)
        if courses:
            serializer = OutstandingCourseSerializer(courses)
            return Response(serializer.data, status.HTTP_200_OK)
        return Response({"message": "Outstanding Courses will show here."}, status=status.HTTP_404_NOT_FOUND)


class AddOutstandingCourse(APIView):

    def post(self, request):
        serializer = AddOutstanidngCourseSerializer(data=request.data)
        if serializer.is_valid():
            course_id = serializer.validated_data["course_id"]
            student_id = serializer.validated_data["student_id"]
            try:
                course = Courses.objects.get(id=course_id)
            except Courses.DoesNotExist:
                return Response({"message": "Course not found."}, status=status.HTTP_404_NOT_FOUND)
            try:
                student = Student.objects.get(id=student_id)
            except Student.DoesNotExist:
                return Response({"message": "User with this ID does not exist."}, status.HTTP_404_NOT_FOUND)
            
            outstanding_course = OutstandingCourses.objects.get(user=student)
            outstanding_course.courses.add(course)
            return Response({"message": "Course added to Outstanding course."}, status.HTTP_200_OK)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)