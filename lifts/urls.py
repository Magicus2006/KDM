from django.urls import path
from lifts.views import Lifts, ListLifts


app_name = "articles"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('', Lifts.as_view()),
    path('list/', ListLifts.as_view()),
    #path('aventos/<int:pk>', ArticleView.as_view())
]