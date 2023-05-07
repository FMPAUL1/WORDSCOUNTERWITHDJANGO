from django import forms

class SentenceForm(forms.Form):
    sentence =forms.CharField(label='Enter or Paste Sentence Here',max_length=1000)
    
       
    