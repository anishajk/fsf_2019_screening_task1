from django.shortcuts import render, redirect
from .models import Team, Task, Team_mem
from django.views import generic
from django.http import HttpResponse, Http404
from django.contrib.sessions.backends.db import SessionStore
from .forms import CommentForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.
class IndexView(generic.ListView):
	template_name = 'pro/index.html'
	context_object_name = 'all_teams'


	def get_queryset(self):
		return Team.objects.all()

class DetailView(generic.DetailView):
	model = Team
	template_name = 'pro/details.html'

class TaskDisplay(generic.ListView):
	model = Task , Team_mem
	template_name = 'pro/tasks.html'

	def get_queryset(self):
		user = self.request.session['un']
		a = Team_mem.objects.get(mem=user).team
		return Task.objects.filter(team=a)



class TaskCreate(CreateView):
	model = Task
	fields = ['title','description', 'assignee','team']
	template_name = 'pro/create_form.html'
	

class TaskUpdate(UpdateView):
	model = Task
	fields = ['title','description', 'assignee','status']
	template_name = 'pro/create_form.html'

	def __str__(self, request,no):
		user = self.request.session['un']
		a = Task.objects.get(pk=no).task_creator
		if not user == a:
			raiseHttp404("You cannot Edit")


class TeamCreate(CreateView):
	
	model = Team
	fields = ['team_creator','team_name']
	template_name = 'pro/create_form.html'

	def __str__(self):
		return redirect('index')


class TeamMem(CreateView):
	
	model = Team_mem
	fields = ['team', 'mem']
	template_name = 'pro/create_form.html'	


def comment_view(request):
	if request.method == 'POST':
		form = CommentForm(request.POST or None)
		if form.is_valid():
			cmt = form.save(commit=False)
			comment = form.cleaned_data.get('comment')
			cmt.set_comment(comment)
			cmt.save()
			return redirect('pro:task')
	else:
		form = CommentForm()
	template = 'pro/addcomment.html'
	context = {'form': form}
	return render(request, template, context)
	












