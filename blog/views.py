from django.shortcuts import render, get_object_or_404, redirect
from . import models, forms
from django.core.paginator import Paginator
from django.contrib import messages
from taggit.models import Tag

def post_list(request, tag_slug=None):
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        posts = models.Post.objects.filter(status='published', tags__in=[tag]).order_by('title')
    else:
        posts = models.Post.objects.filter(status='published').order_by('title')

    paginator = Paginator(posts, 3)  # 3 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, "post_list.html", {
        'page_obj': page_obj
    })


def post_detail(request, slug):
    post = get_object_or_404(
        models.Post,
        slug=slug,
        status='published'
    )

    new_comment = None
    comment_form = forms.CommentForm(request.POST or None)
    if request.method == 'POST':

        if request.method == 'POST' and comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()

            messages.success(
                request,
                "Your comment has been submitted and is awaiting approval."
            )
            return redirect(post.get_absolute_url())
        else:
            comment_form = forms.CommentForm()

    return render(request, "post_detail.html", context={
            'post': post,
            'comment_form': comment_form,
            'new_comment': new_comment,
        })


def contact_me(request):
    context = {}
    return render (request, "contact_me.html", context=context)