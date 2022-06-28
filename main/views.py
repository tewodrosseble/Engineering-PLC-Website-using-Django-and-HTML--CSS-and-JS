from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger
from django.conf import settings
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

def index(request):
    cover= Coverphoto.objects.order_by('-date')[:1]
    blg = Blog.objects.order_by('-date')[:2]
    service = Services.objects.order_by('-date')[:2]
    reference = Reference.objects.order_by('id')[:1]
    return render(request,'web/index.html', {'blg':blg, 'cover':cover, 'service':service, 'reference':reference})

def about(request):
    return render(request,'web/about.html')

def contact(request):
    return render(request,'web/contact.html')

def blog(request):
    blg = Blog.objects.order_by("-date")
    return render(request,'web/blog.html', {'blg':blg})

def services(request):
    
    servicelist = Services.objects.all()

    # p = Paginator(servicelist, 2)
    # page_num = request.GET.get("page", 1)
    # try:
    #     product = p.page(page_num)
    # except EmptyPage:
    #     product = p.page(1)
    # except PageNotAnInteger:
    #     product = p.page(1)

    # context ={"services": product}

    return render(request,'web/services.html', {"servicelist":servicelist})

def gallary(request):
    gallery = Gallery.objects.order_by('-date')
    return render(request,'web/gallery.html', {"gallery" : gallery})

def gallery(request):
    gallery_list = Gallery.objects.all()
    paginator = Paginator(gallery_list,7)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'web/gallery_list.html', {'page_obj':page_obj})

def reference(request):
    refer  = Reference.objects.all()
    return render(request, 'web/reference.html', {'refer':refer})

def certificate(request):
    cert = Certificate.objects.all()
    return render(request, 'web/cert.html', {"cert":cert})

def video (request):
    vid = Video.objects.all()
    return render(request, 'web/video.html', {'vid':vid})

def display_video(request,vid=None):
    if vid is None:
        return HttpResponse("No Video")

    try:
        video_object = get_object_or_404(videos, pk = vid)
    except videos.DoesNotExist:
        return HttpResponse("Id doesn't exists.")

    file_name = video_object.file_name
    #getting full url - 
    video_url = settings.MEDIA_URL+file_name

    return render(request, "video_template.html", {"url":video_url})

@login_required
def profiles(request):
    return render(request, 'web/profiles.html')
