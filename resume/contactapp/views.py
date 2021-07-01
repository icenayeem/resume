from django.shortcuts import render
def contact(request):
    context = {'cont':'active'}
    return render(request,'contact/contact.html',context)
