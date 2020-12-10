from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.core.files.storage import FileSystemStorage
from cms.models import BannerImage, Client, Customize,Post,PostImage

# Create your views here.


def signup(request):
    if request.method == 'POST':
        # check password confirm equal
        if request.POST['password'] == request.POST['c_password']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'cms/signup.html', {'error': 'User is alredy exist'})
            except User.DoesNotExist:
                user = User.objects.create_user(
                    request.POST['username'], request.POST['password'])
                auth.login(request, user)
                return redirect('login')

        else:
            return render(request, 'cms/signup.html', {'error': 'Password does not match'})
    else:
        return render(request, 'cms/signup.html')


def login(request):
    if request.method == 'POST':
        user = auth.authenticate(
            username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            # session create
            request.session['username'] = user.first_name
            return redirect('dashboard')
        else:
            return render(request, 'cms/login.html', {'error': 'username or password is incorrect'})
    return render(request, 'cms/login.html')


def logout(request):
    try:
        del request.session['username']
    except:
        pass
    return redirect('login')

def dashboard(request):
    if request.session.has_key('username'):
        username = request.session['username']
        portfolio = Post.objects.all()
        client = Client.objects.all()
        return render(request,'cms/dashboard.html',{'username':username,'portfolio':portfolio,'client':client})
    else:
        return render(request, 'cms/login.html')

def imgupload(request):
    if request.session.has_key('username'):
        username = request.session['username']
        if request.method== 'POST':
            length = request.POST.get('length')
            title = request.POST.get('title')
            description = request.POST.get('description')
            category = request.POST.get('category')
            image=request.FILES.get(f'images{0}')
            
            print(length)
            post = Post.objects.create(
                title=title,
                desc=description,
                category=category,
                image = image
            )
              
            for file_num in range(0, length):
                PostImage.objects.create(
                    post=post,
                    image=request.FILES.get(f'images{file_num}')
            )

        
        return render(request, 'cms/imgupload.html',{'username':username})
    else:
        return render(request, 'cms/login.html')

def client_upload(request):
    if request.session.has_key('username'):
        username = request.session['username']
        if request.method == 'POST':
            cimage_title = request.POST['cimage_title']
            uploaded_file = request.FILES['cimage']
            client = Client(cimage_title=cimage_title,cimage=uploaded_file)
            client.save()

        return render(request, 'cms/client_upload.html', {'username': username})
    else:
        return render(request, 'cms/login.html')

def banner_image(request):
    if request.session.has_key('username'):
        username = request.session['username']
        if request.method == 'POST':
            bimage_title = request.POST['bimage_title']
            bimage_desc = request.POST['bimage_desc']
            uploaded_file = request.FILES['bimage']
            banner_image = BannerImage(bimage_title=bimage_title,bimage_desc=bimage_desc,bimage=uploaded_file)
            banner_image.save()
        return render(request, 'cms/banner_image.html', {'username': username})
    else:
        return render(request, 'cms/login.html')

def customize(request):
    if request.session.has_key('username'):
        username = request.session['username']
        if request.method == 'POST':
            founder_message = request.POST['founder_message']
            how_we_work = request.POST['how_we_work']
            customize = Customize.objects.get(id=8)
            customize.founder_message = founder_message
            customize.how_we_work = how_we_work
            customize.save()

        main_info = Customize.objects.all()
        return render(request, 'cms/customize.html', {'main_info': main_info,'username': username})
    else:
        return render(request, 'cms/login.html')
        return render(request, 'cms/login.html')
