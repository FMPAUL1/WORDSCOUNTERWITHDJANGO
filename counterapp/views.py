
from .form import SentenceForm
from django.views.generic.edit import FormView
from django.views.generic import TemplateView

from collections import Counter
import string

# Create your views here.





class created(FormView):
    template_name='created.html'
    form_class=SentenceForm
    success_url='/count-result/'
    
    def form_valid(self,form):
        sentence=form.cleaned_data['sentence']
        word_count={}
        
       
        for word in sentence.split():
            #i had to strip it to remove leading spaces and newline char
            word=word.strip()
            word=word.lower()
            #removing punctuation marks
            word=word.translate(word.maketrans("","",string.punctuation))
            
    
            if word in word_count:
                 word_count[word]+=1
            else:
                word_count[word]=1
                
                    
                
          
        
        
        sort_word_counts=sorted(word_count.items(),key=lambda x:x[1],reverse=True)
     
      
        
    
          
        self.request.session['counted']=  {p:len(p) for p in word_count}
        
       
        self.request.session['word_count']=sort_word_counts
        return super().form_valid(form)


class CountResultView(TemplateView):
    template_name='listitem.html'
    
    def get_context_data(self,*args,**Kwargs):
        context=super().get_context_data(*args,**Kwargs)
        context['word_count']=self.request.session.get('word_count',[])
        context['counted']=self.request.session.get('counted',[])
        
       
   
        
        
        return context


