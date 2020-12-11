from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DeleteView
from django.views import View
from django.urls import reverse_lazy
from .tasks import send_invitations
from .models import Invitee


class InvitateeListView(ListView):
    """View to lists all invitees in the invitation list"""

    model = Invitee
    template_name = 'invitation/index.html'


class InvitateeAddView(CreateView):
    """View to add new invitees to the invitation list"""

    model = Invitee
    fields = ['first_name', 'last_name', 'email']
    success_url = reverse_lazy('invitee-list')


class InvitateeDeleteView(DeleteView):
    """View to delete invitees from the invitation list"""
    model = Invitee
    success_url = reverse_lazy('invitee-list')


class InvitationSendView(View):
    """
    View to send out invitation emails to all the invitees in the
    invitation list
    """

    def get(self, request, *args, **kwargs):
        return render(request, 'invitation/invitation_send.html')

    def post(self, request, *args, **kwargs):
        send_invitations.delay()  # Use celery to send emails
        return redirect('invitee-list')
