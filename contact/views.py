from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings

from django.core.mail import send_mail
import os
from .forms import ContactForm
from .models import Contact


"""Created an env var for the admin email so not in code. """
ADMINS_EMAIL = os.environ.get('ADMINS_EMAIL')


def contact(request):
    """
    Create the contact view. Check if the user is authenticated, pass
    values to the contact form based on it.
    When Post, An email should then be sent to the admins.
    If not post pass through a blank version of the form.
    """
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
                message=request.POST['message'],
            )

            form.save()

        send_mail(
            'Hello!',
            'You have a new message. See admin panel for details.',
            os.environ.get('SITE_EMAIL'),
            [ADMINS_EMAIL],
            fail_silently=False,
        )

        messages.success(request,
                         'Your email has been submitted,'
                         'our team will get back to you as soon as possible.')
        return redirect('contact')

    else:
        if request.user.is_authenticated:
            form = ContactForm(
                initial={
                    'email': request.user.email
                    },
            )
        else:
            form = ContactForm()

    context = {
        'form': form,
    }

    return render(request, 'contact/contact.html', context)
