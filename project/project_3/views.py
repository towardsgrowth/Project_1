from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.

def greeting(request:HttpRequest):
    return HttpResponse("<h1 align='center' style='color: blue;'>Assalomu alaykum!</h1>"
                        "<h1 align='center' style='color: yellow'>Mening ismim Bakir Bakirov</h1>")

def contact(request:HttpRequest):
    return HttpResponse("<h1 align='center' style= 'color: green' href='https://t.me/aazmmv'>Biz bilan bog'laning!</h1>")

def channel(request: HttpRequest):
    return HttpResponse("<h1 href='https://erp.student.najottalim.uz/#/login'>Bizning o'quv markazimiz</h1>")

#
