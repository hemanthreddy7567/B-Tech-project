from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
from manager.forms import UploadnewsForm, viewdetailsform
from manager.models import uploadmodel, viewdetailsmodel
from user.models import users


def managerlogin(request):
    return render(request,'manager/managerlogin.html')

def managerhome(request):
    return render(request,'manager/managerhome.html')

def managerloginaction(request):
    if request.method == "POST":
        if request.method == "POST":
            usid = request.POST.get('username')
            print(usid)
            pswd = request.POST.get('password')
            if usid == 'Manager' and pswd == 'Manager':
                return render(request, 'manager/managerhome.html')
            else:
                messages.success(request, 'Invalid user id and password')
    return render(request, 'manager/managerlogin.html')


def viewuserdata(request):
    check=users.objects.all()
    return render(request,"manager/viewuserdata.html",{"object":check})

def addnews(request):
    if request.method == 'POST':
        form = UploadnewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('manager/uploadnews_list.html')
    else:
        form = UploadnewsForm()
    return render(request, 'manager/uploadnews.html', {'form': form})

def viewnews(request):
    check = uploadmodel.objects.all()
    for x in check:
        print(x.id)
    return render(request,'manager/viewnews.html',{'news':check})

def viewdetails(request):
    if request.method == "POST":
        forms = viewdetailsform(request.POST)
        if forms.is_valid():
            forms.save()
            #messages.success(request, 'successfully ')
            return render(request,'manager/managerhome.html')
        else:
            print('Invalid Form')
            category = request.POST.get('category')
            title = request.POST.get('title')
            description = request.POST.get('description')
            location = request.POST.get('location')
            form = viewdetailsmodel(category=category,title=title,description=description,location=location)
            form.save()
            print("form savved")
            return render(request,'manager/viewnews.html',{'news':form})
    else:
        if request.method =='GET':
            print("get method taking")
            id = request.GET.get('id')
            print('Image Id  = ',id)
            category = request.GET.get('category')
            title = request.GET.get('title')
            description = request.GET.get('description')
            location = request.GET.get('location')
            file = request.GET.get('file')
            print('category = ',category,' title=',title,'description = ',description,'location = ',location)
            data = uploadmodel.objects.get(id=id)
            print("data image url =",type(data.file))
            data2 = {'title': data.title, 'category': data.category,'description': data.description,'location': data.location, }
            viewadds = viewdetailsform(data2)

            return render(request, 'manager/viewnewsdetails.html', {'news': viewadds,'image':data.file})

"""def newsdelete(request):
    role = request.session['role']
    return render(request,'manager/managerhome.html')"""

# def newsdelete(request,id):
#     request.session['id'] = id
#
#     if id == 'id':
#         print("id",id)
#         data = uploadmodel.objects.get(id=id)
#         data.delete()
#         return render(request,'manager/managerhome.html')
#     else:
#         return render(request, 'manager/managerlogin.html')

def newsdelete(request):
    id=request.GET.get('id')
    op=uploadmodel.objects.filter(id=id)
    print("value",op)
    op.delete()
    check = uploadmodel.objects.all()
    return render(request,'manager/viewnews.html',{'news':check})



