from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
import serial
# Create your views here.
class IndexTemplateView_1(TemplateView):
    template_name = "index.html"
#postっていうのを定義して、その中のnameが”LED”であれば、値をシリアル通信で返す。
    def post(self,request):
        if request.method == 'POST':
            if 'LED_OFF' in request.POST:
                #ser = serial.Serial('/dev/cu.usbmodem141301', 9600)
                ser = serial.Serial("COM3", 9600,dsrdtr=True)
                #ser=serial.Serial()
                #ser.port="COM3"
                #ser.baudrate=9600
                #ser.setDTR(False)
                #ser.open()
                #ser.write(1)
                temperature_pre=ser.read()
                val=int.from_bytes(temperature_pre,"big")
                #ser.write(1)
                humit_pre=ser.read()
                val_1=int.from_bytes(humit_pre,"big")
                #val_1=64
                #ser.write(1)
                DI_pre=ser.read()
                val_2=int.from_bytes(DI_pre,"big")
                #val_2=50
                #temperature=temperature_100/100;
                my_distance={
                'temperature':val,
                "humit":val_1,
                "DI":val_2,
                }
                ser.close()
        return render(request, self.template_name,my_distance)

# class IndexTemplateView_2(TemplateView):
#     template_name="index.html"
#
#     def post(self,request):
#         if request.method=="POST":
#             if"LED_ON"in request.POST:
#                 ser=serial.Serial("COM3",9600)
#                 ser.write(0)
#                 ser.close()
#         return render (request,self.template_name)


# class SampleCopyView(TemplateView):
#     template_name = "index.html"
