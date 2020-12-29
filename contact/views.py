from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
import os
from .forms import ContactForm
from .models import Contact

ADMINS_EMAIL = os.environ.get('ADMINS_EMAIL')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')

print(ADMINS_EMAIL)
print(EMAIL_HOST_USER)


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
            os.environ.get('EMAIL_HOST_USER'),
            ['ADMINS_EMAIL'],
            fail_silently=False
        )
        print(ADMINS_EMAIL)
        print(EMAIL_HOST_USER)
        messages.success(
            request, 'Your email has been submitted. Our team will get back to \
                you as soon as possible.')
        return redirect('contact')

    else:
        if request.user.is_authenticated:
            form = ContactForm()
        else:
            form = ContactForm()

        context = {
            'form': form,
        }

        return render(request, 'contact/contact.html', context)
