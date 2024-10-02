from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.paginator import Paginator


from manager.models import uploadmodel, viewdetailsmodel
from manager.forms import UploadnewsForm, viewdetailsform
from user.forms import userForm, viewnewsdetailsform
from user.models import users


def userlogin(request):
    return render(request,'user/userlogin.html')

def userpage(request):
    return render(request,'user/userpage.html')

def userregister(request):
    if request.method=='POST':
        form1=userForm(request.POST)
        if form1.is_valid():
            form1.save()
            return render(request, "user/userlogin.html")
            #return HttpResponse("registreration succesfully completed")
        else:
            print("form not valied")
            return HttpResponse("form not valied")
    else:
        form=userForm()
        return render(request,"user/userregister.html",{"form":form})

def addnewss(request):
    if request.method == 'POST':
        form = UploadnewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('user/uploadnews_list.html')
    else:
        form = UploadnewsForm()
    return render(request, 'user/uploadnews.html', {'form': form})



def userlogincheck(request):
    if request.method == "POST":
        email = request.POST.get('uname')
        pswd = request.POST.get('upasswd')
        print("Email = ", email, ' Password = ', pswd)
        try:
            check = users.objects.get(email=email,password=pswd)
            print("check",check)
            request.session['email'] = check.email
            print("email",check.email)
            request.session['id'] = check.id
            print(check.id)
            """status = check.status
            print('Status is = ', status)
            if status == "Activated":
                request.session['id'] = check.id
                request.session['name'] = check.firstname
                request.session['email'] = check.email
                print("User id At", check.id, status)"""
            return render(request, 'user/userpage.html', {})
            """else:
                messages.success(request, 'Your Account Not at activated')
                return render(request, 'user/userlogin.html')"""
            # return render(request, 'user/userpage.html',{})
        except Exception as e:
            print('Exception is ', str(e))
            pass
        messages.success(request, 'Invalid Email id and password')
    return render(request, 'user/userlogin.html')

def news(request):
    check = uploadmodel.objects.all()
    for x in check:
        print(x.id)
    return render(request,'user/userviewnews.html',{'news':check})

def userviewdetails(request):
    if request.method == "POST":
        forms = viewnewsdetailsform(request.POST)
        if forms.is_valid():
            forms.save()

            #messages.success(request, 'successfully ')
            return render(request,'user/userpage.html',{})
        else:
            #print('Invalid Form')
            category = request.POST.get('category')
            title = request.POST.get('title')
            description = request.POST.get('description')
            location = request.POST.get('location')
            review = request.POST.get('review')
            form = viewdetailsmodel(category=category, title=title, description=description, location=location,review=review)
            #form.save()
            print("form savved")
            news = viewdetailsmodel.objects.all()
            return render(request,'user/usersuccess.html',{'news':news})
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
            #name= request.session['userid']
            #  print("name",name)
            print('category = ',category,' title',title,'title',title)
            data = uploadmodel.objects.get(id=id)

            print("data image url =",type(data.file))
            data2 = {'title': data.title, 'category': data.category,  'description':data.description,'location':data.location}
            viewadds = viewnewsdetailsform(data2)
            return render(request, 'user/userviewdetails.html', {'news': viewadds,'image':data.file})


# def usersearchresult(request):
#     title = request.GET.get('title')
#     print('title is', type(title))
#     """a_string = title or "title"
#     print("Meghana",a_string)
#     final_new_menu = list(dict.fromkeys(a_string))
#     print("final list",final_new_menu)"""
#     #print("meghana",title.split(","))
#     dict = {}
#     check = uploadmodel.objects.filter(title=title)
#     print("check",check)
#     #print("meghana", check.split(","))
#     # paginator = Paginator(check,100)
#     # print("paginator",paginator)
#     # for i in paginator.page_range:
#     #     data = iter(paginator.get_page(i))
#     #     print("data",data)
#     object = check.filter(title=title)
#     return render(request, 'user/usersearchresult.html', {"news": check})

def usersearchresult(request):
    title = request.GET.get('title')
    print('title is',title)
    check = uploadmodel.objects.filter(title=title)
    s=''
    for y in check:
        s=y
    print("s:",s)
    chk1=uploadmodel.objects.all()
    count=0
    # if check.exists():
    for x in chk1:
        print(x.title)
        if x.title == title:
            count+=1
            print('count',count)

    print("final-count:",count)
    if count>1:
        messages.success(request, 'duplicates not allowed')
        return render(request, 'user/usersearchresult.html')
    # print("check",check)
    return render(request, 'user/usersearchresult.html', {"news": check})

"""def usersearchresult(request):
    title = request.GET.get('title')
    print('title is', title)
    idno = request.session['id']
    print(idno)
    news = uploadmodel.objects.filter(id=idno)
    print("title",title)
    return render(request, 'user/usersearchresult.html', {"news": news})"""

def newsdeletes(request):
    id=request.GET.get('id')
    op=uploadmodel.objects.filter(id=id)
    print("value",op)
    op.delete()
    check = uploadmodel.objects.all()
    return render(request,'user/userviewnews.html',{'news':check})


