from django.shortcuts import render

# Create your views here.
def pills(request):
    return render(request, 'searchpillapp/pills.html')