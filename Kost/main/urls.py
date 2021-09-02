from . import views
from django.conf.urls import include, url
from django.urls import path, re_path
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    path(r'post/new/', views.post_new, name='post_new'),
    path(r'^notes/$', views.NotesFilter.NoteFilter, name='notes'),
    path(r'^note/(?P<pk>\d+)$', views.NoteDetailView.as_view(), name='note-detail'),
    #path('^note/update', views.NoteDetailView.update_note, name='update-note'),
]
#   TestRegion
urlpatterns += [
    path('test/', views.Profile.profileUpdate, name='test'),
    ]

#   Profile
urlpatterns += [
    path('profile/', views.Profile.profile, name='profile'),
    ]
#   Auth
urlpatterns += [
    path('auth/', views.MultipleFormAuth.mulitpleForms, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    ]

#   Chat
urlpatterns += [
    path('chat/', views.Chat.index, name='chat'),
    ]

#   Tokens
urlpatterns += [
    path(r'^register-tokens/$', views.RegtokenListView.as_view(), name='reg-tokens'),
    path('token/new/', views.TokenCreation.reg_token_create, name='reg-token-create'),
    path('token/check/', views.tokenInput, name='reg-token-check'),
]
    
#   Password-Reset
urlpatterns += [
    url(r'^password-change/$', auth_views.PasswordChangeView.as_view(), name='password_change'),
    url(r'^password-change/done/$', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    url(r'^password-reset/done/$', auth_views.PasswordResetDoneView, name='password_reset_done'),
    url(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$', auth_views.PasswordResetConfirmView, name='password_reset_confirm'),
    url(r'^password-reset/complete/$', auth_views.PasswordResetCompleteView, name='password_reset_complete'),
]
handler404 = "main.views.page_not_found_view"