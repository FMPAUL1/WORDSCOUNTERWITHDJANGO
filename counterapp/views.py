
from .form import SentenceForm
from django.views.generic.edit import FormView
from django.views.generic import TemplateView

# Create your views here.





class created(FormView):
    template_name='created.html'
    form_class=SentenceForm
    success_url='/count-result/'
    
    def form_valid(self,form):
        sentence=form.cleaned_data['sentence']
        word_count={}
        for word in sentence.split():
            if word in word_count:
                word_count[word]+=1
            else:
                word_count[word]=1
        sort_word_counts=sorted(word_count.items(),key=lambda x:x[1],reverse=True)
    
        self.request.session['word_count']=sort_word_counts
        return super().form_valid(form)


class CountResultView(TemplateView):
    template_name='listitem.html'
    
    def get_context_data(self,**Kwargs):
        context=super().get_context_data(**Kwargs)
        context['word_count']=self.request.session.get('word_count',[])
        return context


# def createdviewd(request):
    
#     context={}
#     post=request.POST
#     splitted=str(post).split()
#     for items in splitted:
#         if items in context:
#             context[items]+=1
#         else:
#             context[items]=1
#         db=Sentence(context)
#         return redirect('views')
        
#     return render(request,'created.html',{"form":context})

# # def createdviewd(request):
# #     context={}
# #     form=SentenceForm(request.POST or None) 
# #     abel=str(form).split()
# #     for w in abel:
# #         if w in context:
# #             context[w]+=1
# #         else:
# #             context[w]=1
# #     if context.is_valid():
# #         context.save()
# #         redirect('views')
# #         context['form']=context
# #     return render(request,'created.html',context)

# def getviews(request):
#     items=Sentence.objects.all()
#     context={'item':items}
#     return render(request,'listitem.html',context)