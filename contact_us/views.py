from django.shortcuts import render
from .models import Contact
from .forms import ContactForm

# Create your views here.
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Handle form submission (e.g., send email, save data)
            form.save()  # Save the contact form data (if you have a Contact model)
            return  render( request, 'contact_success.html')  # Redirect to a success page
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})




