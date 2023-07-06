from django.db.models import Prefetch, Subquery, OuterRef
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import status

from .models import Student, Subject
from .serializers import StudentSerializer, SubjectSerializer
from .decorators import validate_student_data, validate_subject_data

# Create your views here.


class ListCreateCheckPinView(generics.ListCreateAPIView):
    """
        GET Chats/
        POST Chats/
        """

    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = (permissions.IsAuthenticated,)


    def post(self, request, *args, **kwargs):
        # tag_instance = Chats.objects.get()
        # a_pattern = ChatsSerializer.objects.create(
        #     name=request.data["name"]
        # )
        # Test the chatbot
        res=Student.objects.filter(index=request.data["index"])
        student = res.first()

        s = StudentSerializer(student)
        return Response(
            data=s.data,
            status=status.HTTP_201_CREATED
        )

class ListCreateStudentView(generics.ListCreateAPIView):
    """
    GET Chats/
    POST Chats/
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = (permissions.IsAuthenticated,)

    @validate_student_data
    def post(self, request, *args, **kwargs):
        a_tag = Student.objects.create(
            index=request.data["index"],
            lastname=request.data["lastname"],
            firstname=request.data["firstname"],
            middlename=request.data["middlename"],
            password=request.data["password"],
            school=request.data["school"],
            email=request.data["email"],
        )

        return Response(
            data=StudentSerializer(a_tag).data,
            status=status.HTTP_201_CREATED
        )

class StudentDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET Chats/:id/
    PUT Chats/:id/
    DELETE Chats/:id/
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        try:
            a_student = self.queryset.get(pk=kwargs["pk"])
            return Response(StudentSerializer(a_student).data)
        except Student.DoesNotExist:
            return Response(
                data={
                    "message": "Student with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )

    @validate_student_data
    def put(self, request, *args, **kwargs):
        try:
            a_tag = self.queryset.get(pk=kwargs["pk"])
            serializer = StudentSerializer()
            updated_student = serializer.update(a_tag, request.data)
            return Response(StudentSerializer(updated_student).data)
        except Student.DoesNotExist:
            return Response(
                data={
                    "message": "Student with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )

    def delete(self, request, *args, **kwargs):
        try:
            a_student = self.queryset.get(pk=kwargs["pk"])
            a_student.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Student.DoesNotExist:
            return Response(
                data={
                    "message": "Student with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )
class ListCreateSubjectView(generics.ListCreateAPIView):
    """
    GET Chats/
    POST Chats/
    """
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = (permissions.IsAuthenticated,)

    @validate_subject_data
    def post(self, request, *args, **kwargs):
        a_tag = Subject.objects.create(
            index=request.data["index"],
            lastname=request.data["lastname"],
            firstname=request.data["firstname"],
            middlename=request.data["middlename"],
            password=request.data["password"],
            school=request.data["school"],
            email=request.data["email"],
        )

        return Response(
            data=SubjectSerializer(a_tag).data,
            status=status.HTTP_201_CREATED
        )

class SubjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET Chats/:id/
    PUT Chats/:id/
    DELETE Chats/:id/
    """
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        try:
            a_subject = self.queryset.get(pk=kwargs["pk"])
            return Response(SubjectSerializer(a_subject).data)
        except Subject.DoesNotExist:
            return Response(
                data={
                    "message": "Subject with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )

    @validate_subject_data
    def put(self, request, *args, **kwargs):
        try:
            a_tag = self.queryset.get(pk=kwargs["pk"])
            serializer = SubjectSerializer()
            updated_subject = serializer.update(a_tag, request.data)
            return Response(SubjectSerializer(updated_subject).data)
        except Subject.DoesNotExist:
            return Response(
                data={
                    "message": "Subject with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )

    def delete(self, request, *args, **kwargs):
        try:
            a_subject = self.queryset.get(pk=kwargs["pk"])
            a_subject.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Subject.DoesNotExist:
            return Response(
                data={
                    "message": "Subject with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )