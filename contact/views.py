from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import ContactForm
from .models import Contact


# contact view for sending emails
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
                message=request.POST['message'],
            )

            form.save()

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
