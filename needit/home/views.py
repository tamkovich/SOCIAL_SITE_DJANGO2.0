from django.shortcuts import render, redirect
from django.http import HttpResponse
from home.forms import HomeForm
from home.models import Post, Friend
from django.contrib.auth.models import User
from django.db.models import Q

from django.views.generic import TemplateView

from django.utils.safestring import mark_safe
import json

# Create your views here.
class HomeView(TemplateView):
	template_name = 'home/home.html'

	def get(self, request):
		form = HomeForm()
		posts = Post.objects.all().order_by('-created')
		users = User.objects.exclude(id=request.user.id)
		try:
			friend = Friend.objects.get(current_user=request.user)
			friends = friend.users.all()
		except:
			friends = None

		your_id = request.user.id

		args = {
			'form': form,
			'posts': posts,
			'users': users,
			'friends': friends,
			'your_id': your_id,
		}
		return render(request, self.template_name, args)

	def post(self, request):
		form = HomeForm(request.POST)
		# print(form.is_valid(), form.errors)
		if form.is_valid():
			post = form.save(commit=False)
			post.user = request.user
			post.save()
			text = form.cleaned_data['post']
			form = HomeForm()
			return redirect('home:home')

		args = {
			'form': form,
			'text': text,
		}
		return render(request, self.template_name, args)

def change_friends(request, operation, pk):
	friend = User.objects.get(pk=pk)
	if operation == 'add':
		Friend.make_friend(request.user, friend)
		Friend.make_friend(friend, request.user)
	elif operation == 'remove':
		Friend.lose_friend(request.user, friend)
		Friend.lose_friend(friend, request.user)
	return redirect('home:home')

def room(request, room_name):
  return render(request, 'home/room.html', {
      'room_name_json': mark_safe(json.dumps(room_name))
  })
