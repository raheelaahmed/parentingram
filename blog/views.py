from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from django_summernote.admin import SummernoteModelAdmin
from django.views.generic.edit import UpdateView
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseForbidden
from .models import Post, Comment
from .forms import CommentForm
from .forms import PostForm
from django.views.generic import View
from django.contrib.auth.decorators import login_required


# Create your views here.


# Profile Views
def profile(request):
    if request.user.is_authenticated:
        # Filter posts for the currently logged-in user
        queryset = Post.objects.filter(author=request.user)
    else:
        # Handle case where user is not logged in (optional)
        queryset = None  # or redirect to login page

    template_name = "blog/profile.html"
    context = {"posts": queryset}  # Add queryset to context for template
    return render(request, template_name, context)
   
# Home Views
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "blog/index.html"
    paginate_by = 6


# post detail view

def post_detail(request, slug):
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


# comment edit
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

# comment delete


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

# create post


def create_post(request, slug):
    model = Post

    if request.method == 'POST':
        # Create form with current user as author (if applicable)
        if request.user.is_authenticated:
            author = request.user
        else:
            # Handle case where user is not authenticated (optional)
            author = None  # Or set a default author if desired

        form = PostForm(request.POST, request.FILES, initial={'author': author})

        if form.is_valid():
            post = form.save(commit=False)
            post.author = author
            post.save()
            success_message = "Your post has been created successfully!"
            return redirect('post_detail', slug=post.slug)  # Redirect to detail view

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

class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/update_post.html'

    def form_valid(self, form):
        """
        Updates the post only if the current user is the author.
        """
        post = form.save(commit=False)  # Don't save immediately

        if post.author == self.request.user:
            post.save()
            messages.success(self.request, 'Post Updated!')
            return redirect('post_detail', slug=post.slug)  # Redirect with slug
        else:
            messages.error(self.request, 'You are not authorized to update this post.')
            return self.render_to_response(self.get_context_data(form=form))  # Re-render form

    def get_success_url(self):
        """
        Returns the success URL after a successful update.
        """
        messages.success(self.request, "Your Post updated successfully!")
        return reverse('post_detail', kwargs={'slug': self.object.slug})  # Use object.slug

# delete post


def delete_post(request, slug):
    post = get_object_or_404(Post, slug=slug)

    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Post deleted successfully!')
        return redirect('home')
# Redirect to the home page
    else:
        return render(request, 'blog/post_delete.html', {'post': post})


# search view
def searchpost(request):
    query = request.GET.get('q')

    if query:
        posts = Post.objects.filter(title__icontains=query) | Post.objects.filter(content__icontains=query) | Post.objects.filter(author__username__icontains=query)
    else:
        posts = []

    return render(request, 'blog/search_post.html', {'posts': posts, 'query': query})

# post like view


def post_like(request, slug):
    post = get_object_or_404(Post, slug=slug)

    if request.method == 'POST':
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))











    












    



