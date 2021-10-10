from rest_framework import serializers
from api.models import Snippet, Shedule, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User

class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ['title',]
        
class SheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shedule
        fields = ['text',]

class UserSerializer(serializers.ModelSerializer):
    groups = serializers.StringRelatedField(many=True)

    class Meta:
        model = User
        fields = ['username', 'groups', 'first_name', 'last_name', 'email']
