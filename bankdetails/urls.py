from django.urls import path
from . import views

urlpatterns = [
    path('data/', views.import_data),
    path('branches/autocomplete', views.ListBranch.as_view(), name="list-branch"), 
    path("branches", views.SearchBranch.as_view(), name="search-branch"),
    path("branches/city", views.SearchBranchCity.as_view(), name="search-branch-city"),
    path("bank/<int:id>", views.BranchDetail.as_view(), name="branch-detail"),
    path("invert-favourite/",views.invert_favourite, name="invert-favourite"),
    path('get-favourite/', views.FavouriteBranchReturn.as_view(), name="favourite-branches"),
]
