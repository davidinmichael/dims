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
            serializer = CourseOutputSerializer(courses, many=True)
            return Response(serializer.data, status.HTTP_200_OK)
        return Response({"message": "No courses available."}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            course = serializer.save(created_by=request.user, last_updated_by=request.user)
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
            serializer = CourseOutputSerializer(course)
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
        try:
            student = Student.objects.get(user=user)
        except Student.DoesNotExist:
            return Response({"message": "No Course Count for Non-student Accounts"}, status.HTTP_200_OK)
        course_count = total_and_semester_courses_count(student)
        return Response(course_count, status.HTTP_200_OK)


class StudentCurrentSemesterCourses(APIView):

    def get(self, request):
        user = request.user
        student = Student.objects.get(user=user)
        courses = Courses.objects.filter(level=student.level_year, semester=student.current_semester)
        if courses:
            serializer = CourseOutputSerializer(courses, many=True)
            return Response(serializer.data, status.HTTP_200_OK)
        return Response({"message": "Course not found."}, status=status.HTTP_404_NOT_FOUND)



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


class CoursesByLevelAndSemester(APIView):
    def get(self, request, level, semester):
        courses = Courses.objects.filter(level=level, semester=semester)
        if courses.exists():
            serializer = CourseOutputSerializer(courses, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"message": "No courses found for this level and semester."}, status=status.HTTP_404_NOT_FOUND)