from django.urls import path
from . import views

app_name='pro'

urlpatterns = [ 
   #/music/
  
   path('', views.IndexView.as_view(),name='index'),

   path('task/', views.TaskDisplay.as_view(),name='task'),

   
   #/music/<album.id>/
   path('<int:pk>/',views.DetailView.as_view(),name='detail'),

   #/music/album/add/
   path('task/add/', views.TaskCreate.as_view(),name='add-task'),

   path('team/add/', views.TeamCreate.as_view(),name='add-team'),

   path('mem/add/', views.TeamMem.as_view(),name='add-mem'),

   path('comment/', views.comment_view, name='add-comment'),

   path('edit/<int:pk>/', views.TaskUpdate.as_view(),name='task-update'),

]