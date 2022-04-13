"""from django.urls import path
from .views import CurrencyAPI

app_name = "articles"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    #path('aventos/', AventosTypeView.as_view())
    #path('aventos/<int:pk>', ArticleView.as_view())
    path("", CurrencyAPI.as_view())
]"""