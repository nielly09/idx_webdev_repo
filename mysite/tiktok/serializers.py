from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer
from django.contrib.auth.models import User  # Ensure correct import
from .models import Video, Comment, Heart

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username') 

class VideoSerializer(WritableNestedModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)  
    video = VideoSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'

class CommentCreateSerializer(WritableNestedModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all()) 
    video = serializers.PrimaryKeyRelatedField(queryset=Video.objects.all())

    class Meta:
        model = Comment
        fields = '__all__'

class HeartSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)  
    video = VideoSerializer(read_only=True)

    class Meta:
        model = Heart
        fields = '__all__'

class HeartCreateSerializer(WritableNestedModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all()) 
    video = serializers.PrimaryKeyRelatedField(queryset=Video.objects.all())

    class Meta:
        model = Heart
        fields = '__all__'
