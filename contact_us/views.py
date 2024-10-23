from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError

# Create your views here.



def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():

            subject = form.cleaned_data['subject']

            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            try:
                send_mail(
                    subject=subject,
  # Use the subject from the form
                    message=message,
                    from_email=email,  # Use the sender's email from the form
                    recipient_list=['rania.crochet@gmail.com'],  # Replace with admin email
                )
            except BadHeaderError:
                return HttpResponse('Invalid header found in form input')

            form.save()  # Save contact information to database (if applicable)
            return redirect('contact')  # Redirect using URL pattern name
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})









