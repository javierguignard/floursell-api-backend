from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _


class GenericModel(models.Model):
    created_by = models.ForeignKey(get_user_model(),
                                   verbose_name=_('Creador'),
                                   on_delete=models.SET_NULL,
                                   null=True,
                                   blank=True)
    creation_date = models.DateTimeField(_('Fecha de Creación'), auto_now_add=True)
    last_modification_date = models.DateTimeField(_('Fecha de Modificación'), auto_now=True)
    last_modification_date = models.DateTimeField(_('Fecha de Modificación'), auto_now=True)

    class Meta:
        abstract = True