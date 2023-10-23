from django.urls import path, include
from . import views

app_name = 'Main'

urlpatterns = [
  path('', views.index, name='index'),
  path('stories/', views.stories, name='stories'),
  path('stories/<int:story_id>/', views.storyForm, name='storyForm'),
  path('results/<int:story_id>/', views.results, name='results'),
  path('addStory/', views.addStoryForm, name='addStoryForm'),
  path('addWordDescriptions/', views.addWordDescriptions, name='addWordDescriptions'),
  path('addWords/', views.addWords, name='addWords'),
]