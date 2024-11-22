from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from django_summernote.admin import SummernoteModelAdmin
from django.views.generic.edit import UpdateView
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from .models import Post, Comment 
from .forms import CommentForm
from .forms import PostForm
from django.views.generic import View

# Create your views here.






#home
    
class PostList(generic.ListView):
        queryset = Post.objects.filter(status=1)
        template_name = "blog/index.html"
        paginate_by = 12


#post detail

def post_detail(request,slug):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/post_detail.html`"
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )
    else:
        comment_form = CommentForm()
  # Initialize comment form only on GET requests

    like_count = post.likes.count()  # Update like count for display

    return render(request, 'blog/post_detail.html', {
        "post": post,
        "comments": comments,
        "comment_count": comment_count,
        "comment_form": comment_form,
        "like_count": like_count,  # Add like count to context
    })

    return redirect(post.get_absolute_url())


 #comment edit
def comment_edit(request, slug, comment_id):
    """
    view to edit comments
    """
    if request.method == "POST":

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR,
                                 'Error updating comment!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))
#comment delete

def comment_delete(request, slug, comment_id):
    """
    view to delete comment
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))

  #create post
def create_post(request, slug):
    model = Post
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
           
            post.save()
            success_message = "Your message has been sent successfully!"
    else:
        form = PostForm()  

    return render(request,
        "blog/create_post.html",
        {
            "form": form,
        },
    )

def get_absolute_url(slug):
        return reverse('post_detail', kwargs={'slug': self.object.slug})
      



  # update post 

class postUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/update_post.html'



    def get_success_url(self): 

        messages.success(self.request, "  your Post updated successfully!")
        
        return reverse('post_detail', kwargs={'slug': self.object.slug})




#delete post
def delete_post(request, slug):
    post = get_object_or_404(Post, slug=slug)

    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Post deleted successfully!')
        return redirect('home')
  # Redirect to the home page
    else:
        return render(request, 'blog/post_delete.html', {'post': post})




  #search  
def searchpost(request):
    query = request.GET.get('q')

    if query:
        posts = Post.objects.filter(title__icontains=query) | Post.objects.filter(content__icontains=query) |  Post.objects.filter(author__username__icontains=query)
    else:
        posts = []

    return render(request, 'blog/search_post.html', {'posts': posts, 'query': query})

#post like
"""class PostLike(View):
    
    def post(self, request, slug, *args, **kwargs):
        model = Post
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))"""

def post_like(request, slug):
    post = get_object_or_404(Post, slug=slug)

    if request.method == 'POST':
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))










    



