from django.urls import path, include
from api import views
from rest_framework.urlpatterns import format_suffix_patterns

#   Snippets
urlpatterns = [
    path('snippets/', views.SnippetAPI.SnippetList.as_view()),
    path('snippet/<int:pk>/', views.SnippetAPI.SnippetDetail.as_view()),
]
#   Users
urlpatterns += [
    path('users/', views.UserAPI.UserList.as_view()),
    path('user/<str:username_>/', views.UserAPI.UserDetail.as_view()),
    ]
#AUTH
urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]

urlpatterns = format_suffix_patterns(urlpatterns)