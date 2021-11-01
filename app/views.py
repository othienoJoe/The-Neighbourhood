from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from PIL import Image
from .models import Profile, User
from.forms import *
from .emails import *

# Create your views here.
def index(request):
	try:
		if not request.user.is_authenticated:
			return redirect('/accounts/login/')
		current_user = request.user
		profile = Profile.objects.get(username=current_user)
	except ObjectDoesNotExist:
		return redirect('create-profile')
	return render(request,'index.html')

@login_required(login_url='/accounts/login/')
def my_profile(request):
	current_user = request.user
	profile = Profile.objects.get(username=current_user)
	return render(request,'profile/user_profile.html',{"profile":profile})

@login_required(login_url='/accounts/login/')
def user_profile(request,username):
	user = User.objects.get(username=username)
	profile = Profile.objects.get(username=user)

@login_required(login_url='/accounts/login/')
def create_profile(request):
	current_user=request.user
	if request.method=="POST":
		form = ProfileForm(request.POST,request.FILES)
		if form.is_valid():
			profile = form.save(commit = False)
			profile.username = current_user
			profile.save()
		return HttpResponseRedirect('/')
	else:
		form = ProfileForm()
		return render(request,'profile/profile_form.html',{"form":form})

@login_required(login_url='/accounts/login/')
def update_profile(request):
	current_user=request.user
	if request.method=="POST":
		instance = Profile.objects.get(username=current_user)
		form =ProfileForm(request.POST,request.FILES,instance=instance)
		if form.is_valid():
			profile = form.save(commit = False)
			profile.username = current_user
			profile.save()

		return redirect('Index')

	elif Profile.objects.get(username=current_user):
		profile = Profile.objects.get(username=current_user)
		form = ProfileForm(instance=profile)
	else:
		form = ProfileForm()

	return render(request,'profile/update_profile.html',{"form":form})

@login_required(login_url='/accounts/login/')
def blog(request):
    current_user=request.user
    profile=Profile.objects.get(username=current_user)
    blogposts = BlogPost.objects.filter(neighborhood = profile.neighborhood)

    return render(request,'blog/blogs.html',{"blogposts":blogposts})

@login_required(login_url='/accounts/login/')
def view_blog(request,id):
	current_user = request.user

	try:
		comments = Comment.objects.filter(post_id=id)
	except:
		comments =[]

	blog = BlogPost.objects.get(id=id)
	if request.method =='POST':
		form = CommentForm(request.POST,request.FILES)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.username = current_user
			comment.post = blog
			comment.save()
	else:
		form = CommentForm()

	return render(request,'blog/view_blog.html',{"blog":blog,"form":form,"comments":comments})

@login_required(login_url='/accounts/login/')
def new_blogpost(request):
	current_user=request.user
	profile =Profile.objects.get(username=current_user)

	if request.method=="POST":
		form =BlogPostForm(request.POST,request.FILES)
		if form.is_valid():
			blogpost = form.save(commit = False)
			blogpost.username = current_user
			blogpost.neighborhood = profile.neighborhood
			blogpost.profpic = profile.profpic
					
		return HttpResponseRedirect('/blog')
	else:
		form = BlogPostForm()

	return render(request,'blog/blogpost_form.html',{"form":form})
