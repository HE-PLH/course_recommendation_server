from django.forms import model_to_dict
from rest_framework import serializers

from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        # fields = "__all__"
        fields = ["index", "lastname", "firstname", "middlename", "password", "school", "email"]

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



