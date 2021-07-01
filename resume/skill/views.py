from django.shortcuts import render
def skills(request):
    context = {'skill':'active'}
    return render(request,'skill/skills.html',context)
def projects(request):
    context = {'pro':'active'}
    return render(request,'skill/projects.html',context)
