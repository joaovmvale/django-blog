from django.urls import path

from . import views

app_name = "blog" #Serve pra referenciar as urls do arquivo

urlpatterns = [ #Lista de padroes de url
    path("", views.PostListView.as_view(), name="list"),
    path("<slug:slug>/", views.PostDetailView.as_view(), name="detail"),
]