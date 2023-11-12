from django.urls import path
from . import views
urlpatterns = [
    # ex: /polls/

    path("", views.index, name="index"),

#     blog linkleri

    path("hakkimizda", views.hakkimizda, name="hakkimizda"),
    path("referanslar", views.referanslar, name="referanslar"),
    path("iletisim", views.iletisim, name="iletisim"),

    # ex: /polls/5/
    # path("<int:question_id>/", views.detail, name="detail"),
    # ex: /polls/5/results/
    # path("<int:question_id>/results/", views.results, name="results"),
    # ex: /polls/5/vote/
    # path("<int:question_id>/vote/", views.vote, name="vote"),
]