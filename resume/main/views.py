from django.shortcuts import render
def home(request):
    context = {'home':'active'}
    return render(request,'main/home.html',context)
