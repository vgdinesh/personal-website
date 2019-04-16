from django.shortcuts import render

def index(request):
    return render(request,'personal/home.html')

def contact(request):
    return render(request, 'personal/basic.html',{'content':['If you would like to contact me, please email me.',]})

def  resume(request):
    return render(request,'personal/resume.html',{'content':['Due to some Security Reasons of Information,.so i am working with an it, so sorry for your request..THANK YOU! VISIT AGAIN!#']})
				
