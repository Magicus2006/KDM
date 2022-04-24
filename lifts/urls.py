from django.urls import path
from .views import Lifts, detail

app_name = "articles"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('', Lifts.as_view()),
    path('1', detail),
    #path('aventos/<int:pk>', ArticleView.as_view())
]