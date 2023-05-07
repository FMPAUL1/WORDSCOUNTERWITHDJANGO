from django.urls import path
from .views import created,CountResultView
urlpatterns = [
  
  path('',created.as_view(),name='count_sentence'),
  path('count-result/',CountResultView.as_view(),name='count_result')
    
]
