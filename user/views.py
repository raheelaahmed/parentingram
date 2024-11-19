from django.shortcuts import render
from .models import Profile
from django.contrib.auth.models import User
from blog.models import Post, Comment
from django.views.generic.edit import UpdateView
from django.contrib import messages
from django.urls import reverse
from .forms import UpdateProfileForm
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin

# Create your views here.

def profile(request):
    queryset = Post.objects.all()
    template_name = 'profile.html'

   
    return render(request,'profile.html')


  
  


#class EditProfileView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
   # model = Profile
    #template_name = 'edit-profile.html'
   # pk_url_kwarg = 'pk'
    #form_class = UpdateProfileForm

    #def has_permission(self):
        # Check if the user can edit their own profile
      #  return self.request.user.has_perm('auth.change_profile')  # Adapt permission name as needed

    #login_url = 'login/'  # Redirect to login if not authenticated


   
    




"""class EditProfileView(UpdateView):
    model = Profile
    profile=User.profile
    template_name = 'edit-profile.html'
    pk_url_kwarg = 'pk'
    if  user.is_super user or user
    form_class = UpdateProfileForm  # Assuming you have an UpdateProfileForm

    def form_valid(self, form):
        form.save()  # Save the updated profile data
        messages.success(self.request, 'Your profile has been updated successfully!')  # Add success message (optional)
        return redirect('profile')  # Redirect to the profile page"""




class EditProfileView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Profile
    template_name = 'edit-profile.html'
    fields = [ 'image','username','email']  # Adjust fields as needed
    pk_url_kwarg = 'pk'

    def get_object(self):
        return self.request.user.profile

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Your profile has been updated successfully!')
        return redirect('profile')

    def test_func(self):
        # Allow superusers to edit any profile
        if self.request.user.is_superuser:
            return True
        # Allow regular users to edit only their own profiles
        return self.get_object().user == self.request.user



def delete_profile(request):

    model = profile
    

    if request.method == 'POST':
        user.profile.delete()
        messages.success(request, 'Profile deleted successfully!')
        return redirect('home')  # Replace 'home' with the desired URL name

    return render(request, 'profile_delete.html', {'profile': profile}) 

