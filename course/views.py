from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CourseSerializer
from .models import *
from rest_framework  import status
from .permissions import *



class CourseListCreate(APIView):
    premission_classes = [CourseWriteOrRead]

    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            course = serializer.save(created_by=request.user)
            course_serializer = CourseSerializer(course)
            return Response(course_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

   
class CourseView(APIView):
    premission_classes = [CourseWriteOrRead]

    def get(self, request):
        courses = Courses.objects.all(user=request.user)
        if courses:
            serializer = CourseSerializer(courses, many=True)
            return Response(serializer.data, status.HTTP_200_OK)
        return Response({"message": "No courses available."}, status=status.HTTP_404_NOT_FOUND)


class CourseDetail(APIView):
    permission_classes = [CourseWriteOrRead]

    def get_object(self, pk):
        try:
            return Courses.objects.get(pk=pk)
        except Courses.DoesNotExist:
            return None
        
    def get(self, request, pk):
        course = self.get_object(pk)
        if course:
            serializer = CourseSerializer(course)
            return Response(serializer.data, status.HTTP_200_OK)
        return Response({"message": "Course not found."}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        course = self.get_object(pk)
        if course:
            serializer = CourseSerializer(course, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"message": "Course not found."}, status=status.HTTP_404_NOT_FOUND)
    
    def delete(self, request, pk):
        course = self.get_object(pk)
        if course:
            course.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({"message": "Course not found."}, status=status.HTTP_404_NOT_FOUND)