from django import forms

class SentenceForm(forms.Form):
    sentence =forms.CharField(label='please enter the sentences here',max_length=1000)
    
       
    