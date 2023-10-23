from django.shortcuts import render
from .models import Story, Word
from django.template import loader
from django.http import HttpResponse
from .forms import StoryForm, AddStoryForm, AddWordDescriptions

# Create your views here.

def index(request):
  return render(request, 'main/index.html')

def stories(request):
  story_list = Story.objects.all()
  template = loader.get_template('main/stories.html')
  return HttpResponse(template.render({'story_list': story_list}, request))

def storyForm(request, story_id):
  story = Story.objects.get(pk=story_id)
  word_list = Word.objects.filter(story=story_id).order_by('wordOrder')
  form = StoryForm(word_list)
  template = loader.get_template('main/storyForm.html')
  return HttpResponse(template.render({'story': story, 'form': form}, request))

def addStoryForm(request):
    form = AddStoryForm(request.POST or None)

    if form.is_valid():
        form.save()
        form = AddStoryForm()
    return render(request, 'Main/addStoryForm.html', {'form': form})

def addWordDescriptions(request):
    #print(request.POST)

    storyString = request.POST.get('text')
    wordCount = storyString.count('{')

    form = AddWordDescriptions(wordCount)

    if request.method == 'POST':
        print(request.POST)
        Story.objects.create(title=request.POST.get('title'), text=request.POST.get('text'))

    if form.is_valid():
        form.save()
        form = AddWordDescriptions()
    return render(request, 'Main/addWordDescriptions.html', {'form': form})

def addWords(request):
    
    if request.method == 'POST':
      word_list = request.POST.dict()
      (k := next(iter(word_list)), word_list.pop(k))
      (k := next(iter(word_list)), word_list.pop(k))
      index = 0
      for word in word_list.values():
        Word.objects.create(story=Story.objects.last(), typeOfWord=word, wordOrder=index)
        index += 1
      print(request.POST)


    story_list = Story.objects.all()
    template = loader.get_template('main/stories.html')
    return HttpResponse(template.render({'story_list' : story_list}, request))

def results(request, story_id):
    # get the story object based on the story_id
    story = Story.objects.get(id=story_id)
    
    wordList = request.POST.dict()
    (k := next(iter(wordList)), wordList.pop(k))
    storyString = story.text.format(*wordList.values())

    context = {
        'story': story,
        'storyString': storyString,
    }
    return render(request, 'Main/story.html', context)