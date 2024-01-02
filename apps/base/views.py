from django.shortcuts import render, redirect
from apps.base import models
from apps.contact.models import User
from apps.secondary.models import Contact, Photo, Reservation
from django.core.mail import send_mail

# Create your views here.

def index(request):
    # Base
    slide = models.Slide.objects.all()
    condition=models.Condition.objects.latest('id')
    news=models.News.objects.latest('id')
    servis = models.Service.objects.latest('id')
    boss = models.Boss.objects.latest('id')
    comands = models.Comands.objects.all()
    ass = models.Ass.objects.latest('id')
    video = models.Video.objects.latest('id')

    # contact
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        date = request.POST.get('date')
        contact = User.objects.create(name = name, email = email, phone = phone, date = date)
    return render(request, 'index.html', locals())


def about(request):
    condition = models.Condition.objects.latest('id')
    servis = models.Service.objects.latest('id')
    comands = models.Comands.objects.all()
    ass = models.Ass.objects.latest('id')
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        date = request.POST.get('date')
        contact = User.objects.create(name = name, email = email, phone = phone, date = date)
    return render(request, 'about.html', locals())


def team(request):
    comands = models.Comands.objects.all()
    ass = models.Ass.objects.latest('id')
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        date = request.POST.get('date')
        contact = User.objects.create(name = name, email = email, phone = phone, date = date)
    return render(request, 'team.html', locals())


def gallery(request):
    ass = models.Ass.objects.latest('id')
    photo = Photo.objects.latest('id')

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        date = request.POST.get('date')
        contact = User.objects.create(name=name, email=email, phone=phone, date=date)
    return render(request, 'gallery.html', locals())


def news(request):
    ass = models.Ass.objects.latest('id')
    news = models.News.objects.latest('id')
    ass = models.Ass.objects.latest('id')
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        date = request.POST.get('date')
        contact = User.objects.create(name=name, phone=phone, email=email, date=date)
    return render(request, 'news.html', locals())


def contact(request):
    ass = models.Ass.objects.latest('id')
    contacts = Contact.objects.latest('id')
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        date = request.POST.get('date')
        contact = User.objects.create(name=name, phone=phone, email=email, date=date)
    return render(request, 'contact.html', locals())

    # send_mail(
    #             f"""Здравствуйте {name}!
    #             Спасибо за обратную связь. Мы скоро с вами свяжемся!
    #             Ваша почта {email}""")
    #         return redirect('home')



def list(request):
    ass = models.Ass.objects.latest('id')
    setting = Reservation.objects.latest('id')
    contacts = Contact.objects.latest('id')
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        date = request.POST.get('date')
    return render(request, 'list.html', locals())

def post(request, id):
    ass = models.Ass.objects.latest('id')
    blog = models.News.objects.get(id=id)
    return render(request, 'post.html', locals())