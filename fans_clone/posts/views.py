from django.shortcuts import render, get_object_or_404, redirect

from .models import Post, PostFileContent, Stream, Likes, Bookmark
from .forms import NewTierForm
from tier.models import Tier, Subscription

from django.core.paginator import Paginator

from django.contrib.auth.decorators import login_required

from django.http import HttpResponseRedirect
from django.urls import reverse

from comments.models import Comments
from comments.forms import CommentForm


@login_required
def index_view(request):
	user = request.user 

	stream_items = Stream.objects.filter(user=user).order_by('-date')

	# #Pagination
	paginator = Paginator(stream_items,8)
	page_number = request.GET.get('page')
	stream_data = paginator.get_page(page_number)

	streamlist = []

	for stream in stream_data:

		if user != stream.post.user:

			subscriber = Subscription.objects.get(subscriber=request.user, subscribed=stream.post.user)

			if (subscriber.tier.number >= stream.post.tier.number):

				stream.visible = True

			else:
				stream.visible = False

		else:
			stream.visible = True
	

		streamlist.append(stream)

		

	content = {
		'stream_data': streamlist,

	}

	return render(request, 'posts/index.html',content)

@login_required
def post_details(request, post_id):
	user = request.user
	post = get_object_or_404(Post, id=post_id)


	if Likes.objects.filter(post=post, user=user).exists():
		liked = True
	else:
		liked = False

	#comment form

	comments = Comments.objects.filter(post=post).order_by('-date')

	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.post = post
			comment.user = user
			comment.save()
			post.comments_count += 1
			post.save()
			return HttpResponseRedirect(reverse('postdetails', args=[post_id]))

	else:
		form = CommentForm()

	#to Validate that the user can see the post
	if user != post.user:
		subscriber = Subscription.objects.get(subscriber=request.user, subscribed=post.user)

		if (subscriber.tier.number >= post.tier.number):

			visible = True
		else:
			visible = False
	else:
		visible = True


	context = {
		'post':post,
		'visible':visible,
		'liked': liked,
		'form':form,
		'comments':comments,
	}

	return render(request, 'posts/post_detail.html', context)


def new_post_view(request):
	user = request.user
	files_objs = []

	if request.method == 'POST':
		form = NewTierForm(request.POST, request.FILES)
		if form.is_valid():
			files = request.FILES.getlist('content')
			title = form.cleaned_data.get('title')
			caption = form.cleaned_data.get('caption')
			tier = form.cleaned_data.get('tier')
			tiers = get_object_or_404(Tier, id=tier.id)

			for file in files:
				file_instance = PostFileContent(file=file, user=user, tier=tiers)
				file_instance.save()
				files_objs.append(file_instance)

			p, created = Post.objects.get_or_create(title=title, caption=caption, user=user, tier=tiers)
			p.content.set(files_objs)
			p.save()

			return redirect('index')

	else:
		form = NewTierForm()
		form.fields['tier'].queryset = Tier.objects.filter(user=user)

	context = {

		'form':form
	}

	return render(request, 'posts/new_posts.html', context)

@login_required
def likes(request, post_id):
	user = request.user
	post = get_object_or_404(Post, id=post_id)
	current_likes = post.likes_count

	liked = Likes.objects.filter(user=user , post=post).count()

	if not liked:
		like = Likes.objects.create(user=user, post=post)
		current_likes += 1
	else:
		Likes.objects.filter(user=user, post=post).delete()
		current_likes -= 1

	post.likes_count = current_likes
	post.save()


	return HttpResponseRedirect(reverse('postdetails', args=[post_id]))


@login_required
def bookmark(request, post_id):
    user = request.user
    post = get_object_or_404(Post, id=post_id)
    current_bookmarks = post.favorites_count



    try:
        b, created = Bookmark.objects.get_or_create(user=user)
        if b.posts.filter(id=post_id).exists():
            b.posts.remove(post)
            current_bookmarks = current_bookmarks - 1
        else:
            b.posts.add(post)
            current_bookmarks = current_bookmarks + 1
        post.favorites_count = current_bookmarks
        post.save()
        return HttpResponseRedirect(reverse('postdetails', args=[post_id]))
    except Exception as e:
        raise e

@login_required
def bookmarkList(request):
	
    bookmark_list = Bookmark.objects.get(user=request.user)

    #Pagination
    paginator = Paginator(bookmark_list.posts.all(), 9)
    page_number = request.GET.get('page')
    bookmark_data = paginator.get_page(page_number)

    context = {
        'bookmark_data': bookmark_data,
    }

    return render(request, 'posts/bookmarklist.html', context)










