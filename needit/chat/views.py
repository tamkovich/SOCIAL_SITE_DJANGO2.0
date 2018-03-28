from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Message
from .forms import MessageForm
from django.db.models import Q
from django.utils.safestring import mark_safe
import json

from django.views.generic import TemplateView

# Create your views here.
class ChatView(TemplateView):
	dialog = 'dialog'
	conversation = 'conversation'
	template_name = 'chat/chat.html'

	def get(self, request, room_name):
		chat_type, fpk, lpk = room_name.split('-')
		if chat_type==self.dialog:
			pk = fpk if request.user.id == int(lpk) else lpk
			form = MessageForm()
			myself = request.user
			interlocutor = User.objects.get(pk=pk)
			messages = Message.objects.filter(Q(sender_user=myself, recipient_user=interlocutor) |
																				Q(sender_user=interlocutor, recipient_user=myself)).order_by('created')
			args = {
				'form': form,
				'messages': messages,
				'myself': myself,
				'interlocutor': interlocutor,
				'room_name_json': mark_safe(json.dumps(room_name)),
			}
			return render(request, self.template_name, args)
			

	def post(self, request, room_name):
		chat_type, fpk, lpk = room_name.split('-')
		pk = fpk if request.user.id == int(lpk) else lpk
		form = MessageForm(request.POST)
		if form.is_valid():
			message = form.save(commit=False)
			message.sender_user = request.user
			message.recipient_user = User.objects.get(pk=pk)
			message.save()
			text = form.cleaned_data['content']
			form = MessageForm()
			return redirect('/chat/'+room_name)

		args = {
			'form': form,
			'text': text,
		}
		return render(request, self.template_name, args)