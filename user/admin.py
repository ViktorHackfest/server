from django.contrib import admin
from . import models

@admin.register(models.UserModel)
class UserAdmin(admin.ModelAdmin):
    fields = [
        'displayName',
        'email',
        'phoneNumber',
        'photoURL',
    ]
    list_display = [
        'id',
        'displayName',
        'email',
        'phoneNumber',
        'photoURL',
    ]
    save_as = True