from django import forms
from .models import Story, Word

class StoryForm(forms.ModelForm):
  class Meta:
    model = Story
    exclude = ['title', 'text']
  def __init__(self, word_list, *args, **kwargs):
    super(StoryForm, self).__init__(*args, **kwargs)
    for word in word_list:
      self.fields[word.typeOfWord + str(word.wordOrder)] = forms.CharField(label=word.typeOfWord, max_length=100)

class AddStoryForm(forms.ModelForm):
  class Meta:
    model = Story
    fields = ['title', 'text']

class AddWordDescriptions(forms.ModelForm):
  class Meta:
    model = Word
    exclude = ['wordOrder']
  
  def __init__(self, numberOfWords, *args, **kwargs):
    super(AddWordDescriptions, self).__init__(*args, **kwargs)
    for i in range(numberOfWords - 1):
      self.fields['typeOfWord' + str(i)] = forms.CharField(label='Type of Word ' + str(i + 1), max_length=100)