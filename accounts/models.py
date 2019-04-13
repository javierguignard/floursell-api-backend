from django.db import models
from django.utils.translation import gettext as _

from django.contrib.auth.models import User

class Account(models.Model):
    USER_TYPES = ((0,_('Vendedor')),
                  (1, _('Producción')),
                  (2, _('Admin')),)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.IntegerField(_('Tipo de usuario'),choices=USER_TYPES)