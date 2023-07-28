from rest_framework import serializers
from .models import *


class Scene1Choice1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Scene1Choice1
        fields = [
            'text',
            'consequence',
        ]


class Scene1Choice2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Scene1Choice2
        fields = [
            'text',
            'consequence',
        ]


class Scene1Choice3Serializer(serializers.ModelSerializer):
    class Meta:
        model = Scene1Choice3
        fields = [
            'text',
            'consequence',
        ]


class Scene2Choice1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Scene2Choice1
        fields = [
            'text',
            'consequence',
        ]


class Scene2Choice2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Scene2Choice2
        fields = [
            'text',
            'consequence',
        ]


class Scene2Choice3Serializer(serializers.ModelSerializer):
    class Meta:
        model = Scene2Choice3
        fields = [
            'text',
            'consequence',
        ]


class Scene3Choice1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Scene3Choice1
        fields = [
            'text',
            'consequence',
        ]


class Scene3Choice2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Scene3Choice2
        fields = [
            'text',
            'consequence',
        ]


class Scene3Choice3Serializer(serializers.ModelSerializer):
    class Meta:
        model = Scene3Choice3
        fields = [
            'text',
            'consequence',
        ]


class Scene4Choice1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Scene4Choice1
        fields = [
            'text',
            'consequence',
        ]


class Scene4Choice2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Scene4Choice2
        fields = [
            'text',
            'consequence',
        ]


class Scene4Choice3Serializer(serializers.ModelSerializer):
    class Meta:
        model = Scene4Choice3
        fields = [
            'text',
            'consequence',
        ]


class Scene5Choice1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Scene5Choice1
        fields = [
            'text',
            'consequence',
        ]


class Scene5Choice2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Scene5Choice2
        fields = [
            'text',
            'consequence',
        ]


class Scene5Choice3Serializer(serializers.ModelSerializer):
    class Meta:
        model = Scene5Choice3
        fields = [
            'text',
            'consequence',
        ]


class IntroStepSerializer(serializers.ModelSerializer):
    class Meta:
        model = IntroStep
        fields = ['introStep']


class Intro1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Intro1
        fields = ['intro13']


class Intro2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Intro2
        fields = ['intro2']