from django.forms import model_to_dict
from rest_framework import serializers

from .models import Student, Subject, StudentSubject, StudentWeight, SubjectWeight


import sys
sys.path.append("..")

from chatbot.serializers import ResponsesSerializer
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        # fields = "__all__"
        fields = ["id", "index", "lastname", "firstname", "middlename", "password", "school", "email"]

    def update(self, instance, validated_data):
        instance.index = validated_data.get("index", instance.index)
        instance.lastname = validated_data.get("lastname", instance.lastname)
        instance.firstname = validated_data.get("firstname", instance.firstname)
        instance.middlename = validated_data.get("middlename", instance.middlename)
        instance.password = validated_data.get("password", instance.password)
        instance.school = validated_data.get("school", instance.school)
        instance.email = validated_data.get("email", instance.email)

        instance.save()
        return instance

class StudentSubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentSubject
        user = StudentSerializer()
        # fields = "__all__"
        fields = ["id", "user", "subject", "grade"]

    def update(self, instance, validated_data):
        instance.user = validated_data.get("user", instance.user)
        instance.subject = validated_data.get("subject", instance.subject)
        instance.grade = validated_data.get("grade", instance.grade)


        instance.save()
        return instance

class StudentWeightSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentWeight
        user = StudentSerializer()
        # fields = "__all__"
        fields = ["id", "user", "response"]

    def update(self, instance, validated_data):
        instance.user = validated_data.get("user", instance.user)
        instance.subject = validated_data.get("response", instance.response)

        instance.save()
        return instance

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        # fields = "__all__"
        fields = ["id", "name"]

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)

        instance.save()
        return instance



class SubjectWeightSerializer(serializers.ModelSerializer):
    # response = serializers.ReadOnlyField()

    class Meta:
        model = SubjectWeight
        subject = SubjectSerializer()
        fields = ["id", "value", "subject", "courses"]

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.save()
        return instance

