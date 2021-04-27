from django.shortcuts import render,HttpResponse
from django.contrib import messages
from home.models import User
# Create your views here.
def signin(request):
    #return HttpResponse("this is check")
    if request.method=="POST":
        email=request.POST.get('email')
        pswd1=request.POST.get('password')
        try:
            temp = User.objects.get(email=email)
        except User.DoesNotExist:
            temp = None
        if temp is None:
            messages.warning(request, 'User Not Found')
            return render(request,'signin.html')

        if temp.pswd==pswd1:
            # messages.success(request, "Success")
            return render(request,'chatpage.html')
        else: 
            messages.warning(request, 'In-Valid Credentials')
            # return render(request,'signin.html')
    return render(request,'signin.html')