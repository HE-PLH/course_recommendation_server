from django.db.models import Prefetch, Subquery, OuterRef
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import status

from .models import Student, Subject, StudentSubject, StudentWeight, SubjectWeight
from .serializers import StudentSerializer, SubjectSerializer, StudentSubjectSerializer, StudentWeightSerializer, \
    SubjectWeightSerializer
from .decorators import validate_student_data, validate_subject_data, validate_student_subject_data, \
    validate_student_weight_data, validate_student_weight_data

# Create your views here.
import sys

sys.path.append("..")

from chatbot.models import Responses
from chatbot.models import Weight, Tags
from chatbot.serializers import WeightSerializer, ResponsesSerializer
from courses.models import Course
from courses.serializers import CourseSerializer
from chatbot.serializers import TagsSerializer





class ListCreateSubjectWeightView(generics.ListCreateAPIView):
    """
    GET Chats/
    POST Chats/
    """

    queryset = SubjectWeight.objects.all()
    serializer_class = SubjectWeightSerializer
    permission_classes = (permissions.IsAuthenticated,)

    @validate_student_weight_data
    def post(self, request, *args, **kwargs):
        course_instance = Course.objects.get(id=request.data["course"])
        response_instance = Responses.objects.get(id=request.data["response"])
        a_SubjectWeight = SubjectWeight.objects.create(
            name=request.data["value"],
            course=course_instance,
            response=response_instance
        )
        return Response(
            data=SubjectWeightSerializer(a_SubjectWeight).data,
            status=status.HTTP_201_CREATED
        )


class SubjectWeightDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET Chats/:id/
    PUT Chats/:id/
    DELETE Chats/:id/
    """
    queryset = SubjectWeight.objects.all()
    serializer_class = SubjectWeightSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        try:
            a_SubjectWeight = self.queryset.get(pk=kwargs["pk"])
            return Response(SubjectWeightSerializer(a_SubjectWeight).data)
        except Tags.DoesNotExist:
            return Response(
                data={
                    "message": "SubjectWeight with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )

    @validate_student_weight_data
    def put(self, request, *args, **kwargs):
        try:
            a_SubjectWeight = self.queryset.get(pk=kwargs["pk"])
            serializer = TagsSerializer()
            updated_SubjectWeight = serializer.update(a_SubjectWeight, request.data)
            return Response(SubjectWeightSerializer(updated_SubjectWeight).data)
        except SubjectWeight.DoesNotExist:
            return Response(
                data={
                    "message": "SubjectWeight with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )

    def delete(self, request, *args, **kwargs):
        try:
            a_SubjectWeight = self.queryset.get(pk=kwargs["pk"])
            a_SubjectWeight.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except SubjectWeight.DoesNotExist:
            return Response(
                data={
                    "message": "SubjectWeight with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )




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
        res = Student.objects.filter(index=request.data["index"])
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


class ListCreateStudentSubjectView(generics.ListCreateAPIView):
    """
    GET Chats/
    POST Chats/
    """
    queryset = StudentSubject.objects.all()
    serializer_class = StudentSubjectSerializer
    permission_classes = (permissions.IsAuthenticated,)

    @validate_student_subject_data
    def post(self, request, *args, **kwargs):
        students_data = request.data
        temp = []
        for student_data in students_data:
            temp.append(
                StudentSubjectSerializer(StudentSubject.objects.create(
                    user=Student.objects.get(id=student_data["user"]),
                    subject=student_data["subject"],
                    grade=student_data["grade"]
                )).data)
        # a_tag = StudentSubject.objects.create(
        #     user=request.data["user"],
        #     subject=request.data["subject"],
        #     grade=request.data["grade"],
        # )

        return Response(
            data=temp,
            status=status.HTTP_201_CREATED
        )


class StudentSubjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET Chats/:id/
    PUT Chats/:id/
    DELETE Chats/:id/
    """
    queryset = StudentSubject.objects.all()
    serializer_class = StudentSubjectSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        try:
            a_student_subject = self.queryset.get(pk=kwargs["pk"])
            return Response(StudentSubjectSerializer(a_student_subject).data)
        except StudentSubject.DoesNotExist:
            return Response(
                data={
                    "message": "StudentSubject with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )

    @validate_student_subject_data
    def put(self, request, *args, **kwargs):
        try:
            a_tag = self.queryset.get(pk=kwargs["pk"])
            serializer = StudentSubjectSerializer()
            updated_student_subject = serializer.update(a_tag, request.data)
            return Response(StudentSubjectSerializer(updated_student_subject).data)
        except StudentSubject.DoesNotExist:
            return Response(
                data={
                    "message": "StudentSubject with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )

    def delete(self, request, *args, **kwargs):
        try:
            a_student_subject = self.queryset.get(pk=kwargs["pk"])
            a_student_subject.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except StudentSubject.DoesNotExist:
            return Response(
                data={
                    "message": "StudentSubject with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )


class ListCreateStudentWeightView(generics.ListCreateAPIView):
    """
    GET Chats/
    POST Chats/
    """
    queryset = StudentWeight.objects.all()
    serializer_class = StudentWeightSerializer
    permission_classes = (permissions.IsAuthenticated,)

    @validate_student_weight_data
    def post(self, request, *args, **kwargs):
        students_data = request.data
        temp = []
        for student_data in students_data:
            for resp in student_data:
                temp.append(
                    StudentWeightSerializer(StudentWeight.objects.create(
                        user=Student.objects.get(id=resp["user"]),
                        response=Responses.objects.get(id=resp["response"])
                    )).data)
        # a_tag = StudentWeight.objects.create(
        #     user=request.data["user"],
        #     subject=request.data["subject"],
        #     grade=request.data["grade"],
        # )

        return Response(
            data=temp,
            status=status.HTTP_201_CREATED
        )


class StudentWeightDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET Chats/:id/
    PUT Chats/:id/
    DELETE Chats/:id/
    """
    queryset = StudentWeight.objects.all()
    serializer_class = StudentWeightSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        try:
            a_student_weight = self.queryset.get(pk=kwargs["pk"])
            return Response(StudentWeightSerializer(a_student_weight).data)
        except StudentWeight.DoesNotExist:
            return Response(
                data={
                    "message": "StudentWeight with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )

    @validate_student_weight_data
    def put(self, request, *args, **kwargs):
        try:
            a_tag = self.queryset.get(pk=kwargs["pk"])
            serializer = StudentWeightSerializer()
            updated_student_weight = serializer.update(a_tag, request.data)
            return Response(StudentWeightSerializer(updated_student_weight).data)
        except StudentWeight.DoesNotExist:
            return Response(
                data={
                    "message": "StudentWeight with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )

    def delete(self, request, *args, **kwargs):
        try:
            a_student_weight = self.queryset.get(pk=kwargs["pk"])
            a_student_weight.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except StudentWeight.DoesNotExist:
            return Response(
                data={
                    "message": "StudentWeight with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )


class ListCreateNextTagView(generics.ListCreateAPIView):
    """
    GET Chats/
    POST Chats/
    """
    queryset = StudentWeight.objects.all()
    serializer_class = StudentWeightSerializer
    permission_classes = (permissions.IsAuthenticated,)

    @validate_student_weight_data
    def post(self, request, *args, **kwargs):
        students_data = request.data
        temp = []
        # for student_data in students_data:
        #     for resp in student_data:
        #         temp.append(
        #             StudentWeightSerializer(StudentWeight.objects.create(
        #                 user=Student.objects.get(id=resp["user"]),
        #                 response=Responses.objects.get(id=resp["response"])
        #             )).data)

        for student_data in students_data:
            for resp in student_data:
                user = Student.objects.get(id=resp["user"]),
                response = Responses.objects.get(id=resp["response"])
                weights = Weight.objects.filter(response=response)
                for weight in weights:
                    weight_data = WeightSerializer(weight).data
                    weight_course = weight_data["course"]
                    weight_value = weight_data["value"]
                    weight_response = weight_data["response"]
                    the_course = Course.objects.get(id=weight_course)

                    print(weight_course)
                    if int(weight_value) < 0:
                        course_data = CourseSerializer(the_course).data
                        print("course_data", course_data)
                        course_category = course_data["category"]
                        all_category_courses = Course.objects.filter(category=course_category)
                        c = []
                        for course in all_category_courses:
                            # c.append(CourseSerializer(course).data)
                            _weights = Weight.objects.filter(course=course)
                            for w in _weights:
                                w_data = WeightSerializer(w).data
                                c = w_data["course"]
                        responses_object = Responses.objects.get(id=weight_response)
                        print(responses_object)
                        temp.append(TagsSerializer(ResponsesSerializer(responses_object).data['tag']).data)
                        # course_object = Course.objects.get(id=weight_course)
                        # course_data = CourseSerializer(course_object).data
                        # print("course_data", course_data)
                        # course_category = course_data["category"]
                        #
                        # all_category_courses = Course.objects.filter(category=course_category)
                        # c = []
                        # for course in all_category_courses:
                        #     c.append(CourseSerializer(course).data)
                        #     _weights = Weight.objects.filter(course=course)
                        # print("courses in category", c)

                # temp.append({
                #     # "user": user,
                #     # "response": response,
                #     # "weight": Weight,
                #     "courses": c,
                # })

        return Response(
            data=temp,
            status=status.HTTP_201_CREATED
        )


class NextTagDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET Chats/:id/
    PUT Chats/:id/
    DELETE Chats/:id/
    """
    queryset = StudentWeight.objects.all()
    serializer_class = StudentWeightSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        try:
            a_student_weight = self.queryset.get(pk=kwargs["pk"])
            return Response(StudentWeightSerializer(a_student_weight).data)
        except StudentWeight.DoesNotExist:
            return Response(
                data={
                    "message": "StudentWeight with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )

    @validate_student_weight_data
    def put(self, request, *args, **kwargs):
        try:
            a_tag = self.queryset.get(pk=kwargs["pk"])
            serializer = StudentWeightSerializer()
            updated_student_weight = serializer.update(a_tag, request.data)
            return Response(StudentWeightSerializer(updated_student_weight).data)
        except StudentWeight.DoesNotExist:
            return Response(
                data={
                    "message": "StudentWeight with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )

    def delete(self, request, *args, **kwargs):
        try:
            a_student_weight = self.queryset.get(pk=kwargs["pk"])
            a_student_weight.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except StudentWeight.DoesNotExist:
            return Response(
                data={
                    "message": "StudentWeight with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )
        
        
        


class ListCreateRecommendationView(generics.ListCreateAPIView):
    """
    GET Chats/
    POST Chats/
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = (permissions.IsAuthenticated,)

    @validate_student_weight_data
    def post(self, request, *args, **kwargs):
        courses_data = request.data
        temp = []
        # for course_data in courses_data:
        #     for resp in course_data:
        #         temp.append(
        #             CourseSerializer(Course.objects.create(
        #                 user=course.objects.get(id=resp["user"]),
        #                 response=Responses.objects.get(id=resp["response"])
        #             )).data)

        bad_Categories = []
        wanted_Categories = []
        for course_data in courses_data:
            for resp in course_data:
                response = Responses.objects.get(id=resp["response"])
                weights = Weight.objects.filter(response=response)

                for weight in weights:
                    print(weight)
                    weight_data = WeightSerializer(weight).data
                    weight_course = weight_data["course"]
                    weight_value = weight_data["value"]
                    weight_response = weight_data["response"]
                    the_course = Course.objects.get(id=weight_course)

                    # print(weight_course)
                    if int(weight_value) < 0:
                        course_data = CourseSerializer(the_course).data
                        # print("course_data", course_data)
                        course_category = course_data["category"]
                        bad_Categories.append(course_category)
                        # all_category_courses = Course.objects.filter(category=course_category)
                        # c = []
                        # for course in all_category_courses:
                        #     # c.append(courseSerializer(course).data)
                        #     _weights = Weight.objects.filter(course=course)
                        #     for w in _weights:
                        #         w_data = WeightSerializer(w).data
                        #         c = w_data["course"]
                        # responses_object = Responses.objects.get(id=weight_response)
                        # print(responses_object)
                        # temp.append(TagsSerializer(ResponsesSerializer(responses_object).data['tag']).data)
                        # course_object = course.objects.get(id=weight_course)
                        # course_data = courseSerializer(course_object).data
                        # print("course_data", course_data)
                        # course_category = course_data["category"]
                        #
                        # all_category_courses = course.objects.filter(category=course_category)
                        # c = []
                        # for course in all_category_courses:
                        #     c.append(courseSerializer(course).data)
                        #     _weights = Weight.objects.filter(course=course)
                        # print("courses in category", c)
                    else:
                        # print("onneeeeee")
                        course_data = CourseSerializer(the_course).data
                        # print("course_data", course_data)
                        course_category = course_data["category"]

                        all_category_courses = Course.objects.filter(category=course_category)
                        c = []
                        for course in all_category_courses:
                            c.append(CourseSerializer(course).data)

                        wanted_Categories.append(c)

                # temp.append({
                #     # "user": user,
                #     # "response": response,
                #     # "weight": Weight,
                #     "courses": c,
                # })

        return Response(
            data={"wantedCourses":wanted_Categories, "unwantedCategories": bad_Categories},
            status=status.HTTP_201_CREATED
        )

