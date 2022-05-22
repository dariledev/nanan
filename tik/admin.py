
from django.contrib import admin
from .models import Postes, User, Demandeur, Comment

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'titre', 'desc')

    @admin.display(empty_value='???')
    def view_desc(self, obj):
        return obj.desc

admin.site.register(User)
admin.site.register(Postes)
admin.site.register(Demandeur)
admin.site.register(Comment)
