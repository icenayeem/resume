from django.shortcuts import render
def education(request):
    context = {'edu':'active'}
    return render(request,'edu/education.html',context)
