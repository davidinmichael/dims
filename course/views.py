from urllib import response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework  import status

from .serializers import *
from .models import *
from .permissions import *
from .utils import *


class CourseListCreate(APIView):
    premission_classes = [CourseWriteOrRead]

    def get(self, request):
        courses = Courses.objects.all()
        if courses:
            serializer = CourseSerializer(courses, many=True)
            return Response(serializer.data, status.HTTP_200_OK)
        return Response({"message": "No courses available."}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            course = serializer.save(created_by=request.user)
            course_serializer = CourseSerializer(course)
            return Response(course_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
            serializer = CourseSerializer(course, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save(last_updated_by=request.user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"message": "Course not found."}, status=status.HTTP_404_NOT_FOUND)
    
    def delete(self, request, pk):
        # TODO: Deleted courses should be added to a recycle bin
        course = self.get_object(pk)
        if course:
            course.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({"message": "Course not found."}, status=status.HTTP_404_NOT_FOUND)
    

class CourseCounts(APIView):

    def get(self, request):
        user = request.user
        course_count = total_and_semester_courses_count(user)
        return Response(course_count, status.HTTP_200_OK)


class UserOwnCourses(APIView):

    def get(self, request):
        user = request.user
        courses = Courses.objects.filter(level=user.level_year, semester=user.current_semester)
        if courses:
            serializer = CourseSerializer(courses, many=True)
            return Response(serializer.data, status.HTTP_200_OK)
        return Response({"message": "Course not found."}, status=status.HTTP_404_NOT_FOUND)


class UserOutstandingCourse(APIView):

    def get(self, request):
        user = request.user
        courses = OutstandingCourses.objects.get(user=user)
        if courses:
            serializer = OutstandingCourseSerializer(courses)
            return Response(serializer.data, status.HTTP_200_OK)
        return Response({"message": "Outstanding Courses will show here."}, status=status.HTTP_404_NOT_FOUND)


class AddOutstandingCourse(APIView):

    def post(self, request):
        serializer = AddOutstanidngCourseSerializer(data=request.data)
        if serializer.is_valid():
            course_id = serializer.validated_data["course_id"]
            user_id = serializer.validated_data["user_id"]
            try:
                course = Courses.objects.get(id=course_id)
            except Courses.DoesNotExist:
                return Response({"message": "Course not found."}, status=status.HTTP_404_NOT_FOUND)
            try:
                user = Account.objects.get(id=user_id)
            except Account.DoesNotExist:
                return Response({"message": "User with this ID does not exist."}, status.HTTP_404_NOT_FOUND)
            
            outstanding_course = OutstandingCourses.objects.get(user=user)
            outstanding_course.courses.add(course)
            return Response({"message": "Course added to Outstanding course."}, status.HTTP_200_OK)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    
    
class CoursesByLevelAndSemester(APIView):
    def get(self, request, level, semester):
        courses = Courses.objects.filter(level=level, semester=semester)
        if courses.exists():
            serializer = CourseSerializer(courses, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"message": "No courses found for this level and semester."}, status=status.HTTP_404_NOT_FOUND)