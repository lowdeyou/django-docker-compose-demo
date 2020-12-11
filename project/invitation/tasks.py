from celery import shared_task
from .models import Invitee
from django.core.mail import send_mass_mail


@shared_task
def send_invitations():
    """
    Celery function to send customized invitation emails to every invitees
    in the invitation list
    """
    invitee_list = Invitee.objects.all()
    subject = "You are invited to my event!"
    email_tuples = ()

    for invitee in invitee_list:
        message = "Dear {} {}, You are invited to my event!".format(
            invitee.first_name, invitee.last_name)

        invitee_email = (
            subject,
            message,
            None,  # None will default to using the settings.DEFAULT_FROM_EMAIL
            [invitee.email]
        )
        email_tuples += (invitee_email,)

    send_mass_mail(email_tuples)
