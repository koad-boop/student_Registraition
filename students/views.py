from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import student


def student_form(request):
    if request.method == "POST":
        n = request.POST.get('namee')
        e = request.POST.get('email')
        a = request.POST.get('age')
        g = request.POST.get('gender')
        q = request.POST.get('qual')
        
        # Handle file upload
        if 'fil' in request.FILES:
            i = request.FILES['fil']
        else:
            i = None

        print(n,e,a,g,q)
        
        # Create a new student object and save it
        o = student(name=n, email=e, age=a, gender=g, qualification=q, img=i)
        o.save()
        s = student.objects.all()
        return render(request, 'student.html',{"s":s,'n':n})

        
    if request.method=="GET":
        n=request.GET.get('name',0)
        s = student.objects.all()
    return render(request, 'student.html',{"s":s,'n':n})

def del_view(request , id):
    d= student.objects.get(id=id)
    d.delete()
    s=student.objects.all()
    return render(request,"student.html",{'s':s})

def edit_view(request,id):
    v=student.objects.get(id=id)
    if request.method == "POST":
        a = request.POST.get('name')
        m = request.POST.get('emaill')
        g = request.POST.get('agee')
        e = request.POST.get('genderr')
        u = request.POST.get('quall')
        
         # Handle file upload
        if 'fil' in request.FILES:
            f = request.FILES['fil']
        else:
            f = None
        s = student(id=id, name=a, email=m, age=g, gender=e, qualification=u, img=f)
        s.save()
        return HttpResponseRedirect("/student/?name=iics")
    return render(request,'edit.html',{"v":v})