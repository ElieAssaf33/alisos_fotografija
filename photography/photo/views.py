from django.shortcuts import render, redirect
from django.http import HttpRequest, JsonResponse
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages
from . import models
from .forms import ContactForm, ReviewForm
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_protect
from django.template.defaultfilters import date
import logging

logger = logging.getLogger(__name__)


def index(request:HttpRequest):
    # Get one photo from each category
    portrait_gallery = models.PhotoGallery.objects.filter(category='portrait').first()
    nature_gallery = models.PhotoGallery.objects.filter(category='nature').first()
    wedding_gallery = models.PhotoGallery.objects.filter(category='wedding').first()
    street_gallery = models.PhotoGallery.objects.filter(category='street').first()
    family_gallery = models.PhotoGallery.objects.filter(category='family').first()
    events_gallery = models.PhotoGallery.objects.filter(category='events').first()

    context = {
        'portrait_photo': portrait_gallery.photos.first() if portrait_gallery else None,
        'nature_photo': nature_gallery.photos.first() if nature_gallery else None,
        'wedding_photo': wedding_gallery.photos.first() if wedding_gallery else None,
        'street_photo': street_gallery.photos.first() if street_gallery else None,
        'family_photo': family_gallery.photos.first() if family_gallery else None,
        'events_photo': events_gallery.photos.first() if events_gallery else None,
    }
    return render(request,'photo/index.html', context)

def portfolio(request:HttpRequest):
    # Get one photo from each category for the portfolio cards
    portrait_gallery = models.PhotoGallery.objects.filter(category='portrait').first()
    nature_gallery = models.PhotoGallery.objects.filter(category='nature').first()
    wedding_gallery = models.PhotoGallery.objects.filter(category='wedding').first()
    street_gallery = models.PhotoGallery.objects.filter(category='street').first()
    family_gallery = models.PhotoGallery.objects.filter(category='family').first()
    events_gallery = models.PhotoGallery.objects.filter(category='events').first()

    context = {
        'portrait_photo': portrait_gallery.photos.first() if portrait_gallery else None,
        'nature_photo': nature_gallery.photos.first() if nature_gallery else None,
        'wedding_photo': wedding_gallery.photos.first() if wedding_gallery else None,
        'street_photo': street_gallery.photos.first() if street_gallery else None,
        'family_photo': family_gallery.photos.first() if family_gallery else None,
        'events_photo': events_gallery.photos.first() if events_gallery else None,
    }
    return render(request,'photo/portfolio.html', context=context)

def prices(request:HttpRequest):
    # Get one photo from each category for the pricing cards
    portrait_gallery = models.PhotoGallery.objects.filter(category='portrait').first()
    nature_gallery = models.PhotoGallery.objects.filter(category='nature').first()
    wedding_gallery = models.PhotoGallery.objects.filter(category='wedding').first()
    street_gallery = models.PhotoGallery.objects.filter(category='street').first()

    context = {
        'portrait_photo': portrait_gallery.photos.first() if portrait_gallery else None,
        'nature_photo': nature_gallery.photos.first() if nature_gallery else None,
        'wedding_photo': wedding_gallery.photos.first() if wedding_gallery else None,
        'street_photo': street_gallery.photos.first() if street_gallery else None,
    }
    return render(request,'photo/prices.html', context=context)

def contacts(request:HttpRequest):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Get form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            
            # Prepare email content
            email_subject = f'New Contact Form Submission: {subject}'
            email_message = f'''New message from {name} ({email})

{message}'''
            
            # Send email
            try:
                send_mail(
                    email_subject,
                    email_message,
                    'eliesamazingphotography@gmail.com',  # From email
                    ['eliesamazingphotography@gmail.com'],  # To email
                    fail_silently=False,
                )
                messages.success(request, 'Your message has been sent successfully!')
                return redirect('contacts')
            except Exception as e:
                messages.error(request, 'There was an error sending your message. Please try again later.')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ContactForm()
    
    return render(request, 'photo/contacts.html', {'form': form})

def wedding(request:HttpRequest):
    wedding_galleries = models.PhotoGallery.objects.filter(category='wedding')
    context = {
        'wedding_galleries': wedding_galleries,
        'section_title': 'Wedding Photography',
        'section_description': 'Preserving precious moments of your special day with elegance and style.'
    }
    return render(request,'photo/wedding.html', context=context)

def nature(request:HttpRequest):
    nature_galleries = models.PhotoGallery.objects.filter(category='nature')
    context = {
        'nature_galleries': nature_galleries,
        'section_title': 'Nature Photography',
        'section_description': 'Exploring the beauty of landscapes and wildlife through the lens.'
    }
    return render(request,'photo/nature.html', context=context)

def portrait(request:HttpRequest):
    portrait_galleries = models.PhotoGallery.objects.filter(category='portrait')
    context = {
        'portrait_galleries': portrait_galleries,
        'section_title': 'Portrait Photography',
        'section_description': 'Capturing personalities and moments in stunning detail'
    }
    return render(request,'photo/portrait.html', context=context)

def street(request:HttpRequest):
    street_galleries = models.PhotoGallery.objects.filter(category='street')
    context = {
        'street_galleries': street_galleries,
        'section_title': 'Street Photography',
        'section_description': 'Documenting urban life and candid moments in their raw authenticity.'
    }
    return render(request,'photo/street.html', context=context)

def about(request):
    reviews = models.Review.objects.all()
    
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for your review!')
            return redirect('about')
    else:
        form = ReviewForm()
    
    context = {
        'page_title': 'Apie mane',
        'intro_text': 'Labas, aš Alisa!',
        'bio': '''
        Esu Alisa, 21 metų fotografė, kuri tiki, kad kiekviena akimirka verta būti įamžinta. Fotografija mano gyvenime atsirado iš noro sustabdyti laiką ir įamžinti jausmus, kurie kartais būna nepastebėti. Šiuo metu studijuoju fotografiją, nuolat tobulinu savo įgūdžius ir siekiu, kad kiekvienas mano darbas būtų ne tik techniškai puikus, bet ir emociškai įkvepiantis.

Mano specializacija:

 Portretai –  kiekvienas žmogus turi savo unikalumą, ir mano tikslas – tai užfiksuoti natūraliai ir tiksliai.
 Vestuvės – šventė, kupina emocijų, kur nuotraukos turi papasakoti visą istoriją.
 Krikštynos – švelnios akimirkos, pilnos šilumos ir artumo.
 Šventės ir gimtadieniai – džiaugsmas, juokas ir šventinė nuotaika užfiksuojama su meile.
 Asmeninės fotosesijos – proga atsiskleisti ir pasijusti ypatingu.

Mano stilius – natūralus, šviesus ir šiltas. Stengiuosi sukurti jaukią atmosferą, kad fotosesija būtų ne tik apie nuotraukos, bet ir apie tikras emocijas.

Dirbu Klaipėdoje, Palangoje, Kretingoje ir visuomet atvira kūrybiniams projektams. Kiekviena fotosesija su manimi – tai bendras kūrybinis procesas, kurio tikslas – užfiksuoti tavo istoriją.
        ''',
        'reviews': reviews,
        'form': form
    }
    return render(request, 'photo/about.html', context)

def family(request:HttpRequest):
    family_galleries = models.PhotoGallery.objects.filter(category='family')
    context = {
        'family_galleries': family_galleries,
        'section_title': 'Family Photography',
        'section_description': 'Capturing precious family moments and creating lasting memories.'
    }
    return render(request,'photo/family.html', context=context)

def events(request:HttpRequest):
    events_galleries = models.PhotoGallery.objects.filter(category='events')
    context = {
        'events_galleries': events_galleries,
        'section_title': 'Event Photography',
        'section_description': 'Documenting special occasions and celebrations with style.'
    }
    return render(request,'photo/events.html', context=context)

def reviews(request:HttpRequest):
    reviews = models.Review.objects.all()
    context = {
        'reviews': reviews,
    }
    return render(request, 'photo/reviews.html', context)


def submit_review(request):
    if request.method == 'POST':
        logger.info(f"Request data: {request.POST}")
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                review = form.save()
                return JsonResponse({'status': 'success', 'message': 'Review submitted successfully!'})
            except Exception as e:
                return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
        else:
            return JsonResponse({'status': 'error', 'message': 'Invalid form data.'}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'}, status=405)