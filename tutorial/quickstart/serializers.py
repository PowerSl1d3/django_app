from django.contrib.auth.models import User
from rest_framework import serializers
from tutorial.quickstart.models import Dag, Tweet, Follow


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'first_name', 'last_name']
        extra_kwargs = {'url': {'lookup_field': 'username'}}


class DagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dag
        fields = ['url', 'name', 'owner']


class TweetSerializer(serializers.HyperlinkedModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = Tweet
        fields = ['url', 'id', 'text', 'photo', 'created', 'author']


class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = []


class UserFollowsSerializer(serializers.ModelSerializer):
    # Определяет как будет сериализовано поле в fields, в данном случае оно будет сериализоваться как UserSerializer
    follows = UserSerializer()

    class Meta:
        model = Follow
        fields = ['follows', 'followed']


class UserFollowedSerializer(serializers.ModelSerializer):
    # Определяет как будет сериализовано поле в fields, в данном случае оно будет сериализоваться как UserSerializer
    follower = UserSerializer()

    class Meta:
        model = Follow
        fields = ['follower', 'followed']
