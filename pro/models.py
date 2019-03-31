from django.db import models
from django.urls import reverse
from django import forms


class Team(models.Model):
	team_creator = models.CharField(max_length=250)
	team_name = models.CharField(max_length=250)

	def __str__(self):
		return self.team_name + ' - ' + self.team_creator

	def get_absolute_url(self):
		return reverse('pro:index')

class Comment(models.Model):
	username = models.CharField(max_length=250)
	comment = models.CharField(max_length=500)

class Team_mem(models.Model):
	team = models.ForeignKey(Team, on_delete=models.CASCADE)
	mem = models.CharField(max_length=250)

	def __str__(self):
		return self.mem 

	def get_absolute_url(self):
		return reverse('pro:index')
 	

class Task(models.Model):
	team = models.ForeignKey(Team, on_delete=models.CASCADE)	
	title = models.CharField(max_length=250)
	description = models.CharField(max_length=500)
	assignee = models.CharField(max_length=250)
	status = models.CharField(max_length=250,default='planned')
	task_creator = models.CharField(max_length=250)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('pro:index')		
	

	
