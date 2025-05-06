from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, Django - das ist ein erster Testversuch von Hoda")
