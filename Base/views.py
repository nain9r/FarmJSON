from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *


class AllScenesChoicesView(APIView):
    def get(self, request):
        scene1_choices = {
            'scene1_choice1': Scene1Choice1Serializer(Scene1Choice1.objects.all(), many=True).data,
            'scene1_choice2': Scene1Choice2Serializer(Scene1Choice2.objects.all(), many=True).data,
            'scene1_choice3': Scene1Choice3Serializer(Scene1Choice3.objects.all(), many=True).data,
        }

        scene2_choices = {
            'scene2_choice1': Scene2Choice1Serializer(Scene2Choice1.objects.all(), many=True).data,
            'scene2_choice2': Scene2Choice2Serializer(Scene2Choice2.objects.all(), many=True).data,
            'scene2_choice3': Scene2Choice3Serializer(Scene2Choice3.objects.all(), many=True).data,
        }

        scene3_choices = {
            'scene3_choice1': Scene3Choice1Serializer(Scene3Choice1.objects.all(), many=True).data,
            'scene3_choice2': Scene3Choice2Serializer(Scene3Choice2.objects.all(), many=True).data,
            'scene3_choice3': Scene3Choice3Serializer(Scene3Choice3.objects.all(), many=True).data,
        }

        scene4_choices = {
            'scene4_choice1': Scene4Choice1Serializer(Scene4Choice1.objects.all(), many=True).data,
            'scene4_choice2': Scene4Choice2Serializer(Scene4Choice2.objects.all(), many=True).data,
            'scene4_choice3': Scene4Choice3Serializer(Scene4Choice3.objects.all(), many=True).data,
        }

        scene5_choices = {
            'scene5_choice1': Scene5Choice1Serializer(Scene5Choice1.objects.all(), many=True).data,
            'scene5_choice2': Scene5Choice2Serializer(Scene5Choice2.objects.all(), many=True).data,
            'scene5_choice3': Scene5Choice3Serializer(Scene5Choice3.objects.all(), many=True).data,
        }

        intro_step_data = {
            'intro_step': IntroStepSerializer(IntroStep.objects.all(), many=True).data,
        }

        intro1_data = {
            'intro1': Intro1Serializer(Intro1.objects.all(), many=True).data,
        }

        intro2_data = {
            'intro2': Intro2Serializer(Intro2.objects.all(), many=True).data,
        }

        all_choices = {
            'scene1': scene1_choices,
            'scene2': scene2_choices,
            'scene3': scene3_choices,
            'scene4': scene4_choices,
            'scene5': scene5_choices,
            'intro_step': intro_step_data,
            'intro1': intro1_data,
            'intro2': intro2_data
        }

        return Response(all_choices)
