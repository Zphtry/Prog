from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import serial


@csrf_exempt
def arduino(request):

  if request.method == 'GET':
    ser = serial.Serial('/dev/ttyUSB0', 9600)
    ser.write(b'config.enable')
    ser.write(b'AT')
    return JsonResponse({'mne': ser.readlines()})

  # elif request.method == 'POST':
  #     data = JSONParser().parse(request)
  #     serializer = SnippetSerializer(data=data)
  #     if serializer.is_valid():
  #         serializer.save()
  #         return JsonResponse(serializer.data, status=201)
  #     return JsonResponse(serializer.errors, status=400)