from django.urls import path
from .views import monthly_challenge, monthly_challenge_number, index

urlpatterns = [
    path("", index, name='index'),
    # Dynamic months for numbers(<identifier>)
    path('<int:month>', monthly_challenge_number),
    # Dynamic months for strings(<identifier>)
    path('<str:month>', monthly_challenge, name="month_challenge"),

]
