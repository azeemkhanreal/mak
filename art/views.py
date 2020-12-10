from django.shortcuts import HttpResponse, render,get_object_or_404
from cms.models import BannerImage, Client, Customize,Post,PostImage,Contact
from django.core.mail import send_mail

def index(request):
    banner_image = BannerImage.objects.all()
    return render(request, 'art/index.html',{'banner_image':banner_image})

def about(request):
    main_info = Customize.objects.all()
    return render(request, 'art/about.html', {'main_info': main_info})
def portfolio(request):
    post= Post.objects.all()
    return render(request, 'art/portfolio.html',{'post':post})
def client(request):
    client_data = Client.objects.all()
    return render(request, 'art/client.html',{'client':client_data})
def contact(request):
    return render(request, 'art/contact.html')
def detail_view(request,id):
    post = get_object_or_404(Post,id=id)
    photos = PostImage.objects.filter(post=post)
    print(photos.values())
    return render(request,'art/post.html',{'post':post,'photos':photos})

def contact(request):
    if request.method=='POST':
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        phone = request.POST.get('phone','')
        message = request.POST.get('message','')
        contact = Contact(name=name,email=email,phone=phone,message=message)
        contact.save()
        send_mail(name,message,email,['azeemkhanreal@gmail.com',email])
        print(name,email,phone,message)
    return render(request, 'art/contact.html')
