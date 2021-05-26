from rest_framework import serializers
from .models import Application


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ('id', 'user', 'title', 'company', 'resume', 'interview', 'date', 'result')


class AddApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ('user', 'title', 'company', 'resume')


class UpdateApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ('title', 'company', 'resume', 'interview', 'date', 'result')