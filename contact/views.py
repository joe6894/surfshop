from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
import os
from .forms import ContactForm
from .models import Contact

ADMINS_EMAIL = os.environ.get('ADMINS_EMAIL')


def contact(request):
    if request.method == 'POST':
        if request.user.is_authenticated:

            form = Contact(
                full_name=request.POST['full_name'],
                subject=request.POST['subject'],
                email=request.POST['email'],
                message=request.POST['message'],
                query_user=request.user
            )

            form.save()

        else:
            form = Contact(
                full_name=request.POST['full_name'],
                subject=request.POST['subject'],
                email=request.POST['email'],
                message=request.POST['message']
            )

            form.save()

        send_mail(
            'Hello!',
            'You have a new message. See admin for more details',
            os.environ.get('SITE_EMAIL'),
            ['ADMINS_EMAIL'],
            fail_silently=False
        )
        messages.success(
            request, 'Your email has been submitted. Our team will get back to \
                you as soon as possible.')
        return redirect('contact')

    form = ContactForm()

    context = {
        'form': form,
    }

    return render(request, 'contact/contact.html', context)
