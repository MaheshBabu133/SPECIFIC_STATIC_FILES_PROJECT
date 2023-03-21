from django.shortcuts import render

# Create your views here.
def specific_static(reqest):
    return render(reqest,'specific_static.html')