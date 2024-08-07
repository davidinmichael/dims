from rest_framework.response import Response
from rest_framework.views import APIView
from course.permissions import CourseWriteOrRead
from rest_framework  import status
from .models import Faculty
from .serializers import FacultySerializer

# Create your views here.

class FacultyView(APIView):
    premission_classes = [CourseWriteOrRead]

    def get(self, request):
        faculty = Faculty.objects.all()
        if faculty:
            serializer = FacultySerializer(faculty, many=True)
            return Response(serializer.data, status.HTTP_200_OK)
        return Response({"message": "No Department Added Yet."}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        serializer = FacultySerializer(data=request.data)
        if serializer.is_valid():
            faculty = serializer.save()
            faculty_serializer = FacultySerializer(faculty)
            return Response(faculty_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FacultyDetail(APIView):
    permission_classes = [CourseWriteOrRead]

    def get_object(self, pk):
        try:
            return Faculty.objects.get(pk=pk)
        except Faculty.DoesNotExist:
            return None
        
    def get(self, request, pk):
        faculty = self.get_object(pk)
        if faculty:
            serializer = FacultySerializer(faculty)
            return Response(serializer.data, status.HTTP_200_OK)
        return Response({"message": "Department not found."}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        faculty = self.get_object(pk)
        if faculty:
            serializer = FacultySerializer(faculty, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"message": "Department not found."}, status=status.HTTP_404_NOT_FOUND)
    
    def delete(self, request, pk):
        # TODO: Deleted courses should be added to a recycle bin
        faculty = self.get_object(pk)
        if faculty:
            faculty.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({"message": "Department not found."}, status=status.HTTP_404_NOT_FOUND)