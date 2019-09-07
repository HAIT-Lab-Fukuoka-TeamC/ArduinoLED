from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
import serial
# Create your views here.
class IndexTemplateView(TemplateView):
    template_name = "index.html"

    def post(self,request):
        if request.method == 'POST':
            if 'LED' in request.POST:
                #ser = serial.Serial('/dev/cu.usbmodem141301', 9600)
                ser = serial.Serial("COM3", 9600)
                ser.write(1)
                ser.close()
        return render(request, self.template_name)
