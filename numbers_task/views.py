from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from random import randint

from numbers_task import serializers
from numbers_task.models import Number
from numbers_task.serializers import NumberSerializer


class NumbersView(APIView):

    serializer_class = serializers.NumberSerializer

    def get(self, request):
        numbers = Number.objects.all()
        serializer = NumberSerializer(numbers, many=True)
        return Response(serializer.data)

    def post(self, request):
        num = randint(1, 100)
        number = Number(number=num)
        number.save()
        print('Created number: ' + str(num))
        return Response(status=status.HTTP_201_CREATED)
