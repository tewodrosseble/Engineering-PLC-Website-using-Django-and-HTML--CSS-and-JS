from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/',views.about, name='about' ),
    path('contact', views.contact, name='contact'),
    path('services', views.services, name='services'),
    # path("gallary", views.gallary, name='gallary'),
    path('blog', views.blog, name='blog'),
    path('gallary', views.gallery, name='gallary'),
    path('Project-reference', views.reference, name='reference'),
    path('Certificates', views.certificate,name='certificates'),
    path('videos', views.video,name='videos'),
    path('profiles', views.profiles, name='profiles')
]

