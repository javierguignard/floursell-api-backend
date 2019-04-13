from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from django.utils.translation import gettext as _

from .models import Account


# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class Accountnline(admin.StackedInline):
    model = Account
    can_delete = False
    verbose_name_plural = _('Tipo de Cuenta')


# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (Accountnline,)


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
