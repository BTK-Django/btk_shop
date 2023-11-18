from django.urls import path
from . import views

urlpatterns = [
    # ex: /polls/

    path("", views.index, name="index"),
    path("hakkimizda", views.hakkimizda, name="hakkimizda"),
    path("referanslar", views.referanslar, name="referanslar"),
    path("iletisim", views.iletisim, name="iletisim"),
    path("category/<int:id>/<slug:slug>", views.categoryProducts, name="categoryProducts"),
    path("product_detail/<int:id>/<slug:slug>", views.productDetail, name="productDetail"),

    # ex: /polls/5/
    # path("<int:question_id>/", views.detail, name="detail"),
    # ex: /polls/5/results/
    # path("<int:question_id>/results/", views.results, name="results"),
    # ex: /polls/5/vote/
    # path("<int:question_id>/vote/", views.vote, name="vote"),
]
