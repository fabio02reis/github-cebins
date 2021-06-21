from django.contrib import admin

# Registrar a classe do model para aparecer na sessão do admin do django.
from.models import Post


# admin.site.register(Post)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title","slug","author","created","updated")
    prepopulated_fields = {"slug":("title",)}