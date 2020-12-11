from django.urls import path

from . import views

urlpatterns = [
    path('', views.InvitateeListView.as_view(), name="invitee-list"),
    path('add/', views.InvitateeAddView.as_view(), name="invitee-add"),
    path(
        'delete/<int:pk>/', views.InvitateeDeleteView.as_view(),
        name="invitee-delete"
    ),
    path('send/', views.InvitationSendView.as_view(), name="invitation-send")
]
