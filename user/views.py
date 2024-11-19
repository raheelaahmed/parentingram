from django.shortcuts import render
from .models import Profile
from django.contrib.auth.models import User
from blog.models import Post 
from django.views.generic.edit import UpdateView
from django.contrib import messages
from django.urls import reverse
from .forms import UpdateProfileForm
from django.shortcuts import redirect

# Create your views here.

def profile(request):
    queryset = Post.objects.all()
    template_name = 'profile.html'

   
    return render(request,'profile.html')



class EditProfileView(UpdateView):
    model = Profile
    template_name = 'edit-profile.html'
    pk_url_kwarg = 'pk'
    form_class = UpdateProfileForm  # Assuming you have an UpdateProfileForm

    def form_valid(self, form):
        form.save()  # Save the updated profile data
        messages.success(self.request, 'Your profile has been updated successfully!')  # Add success message (optional)
        return redirect('profile')  # Redirect to the profile page

