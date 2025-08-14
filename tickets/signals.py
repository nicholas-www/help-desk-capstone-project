from django.contrib.auth import get_user_model
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from tickets.models import Ticket

Users = get_user_model().objects.all()

