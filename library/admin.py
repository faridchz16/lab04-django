from django.contrib import admin
from .models import Author, AuthorProfile, Category, Publisher, Book, Publication

class AuthorProfileInline(admin.StackedInline):
    model = AuthorProfile
    can_delete = False
    verbose_name_plural = 'Perfil'

class AuthorAdmin(admin.ModelAdmin):
    inlines = [AuthorProfileInline,]
    list_display = ('first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name', 'email')

class PublicationInline(admin.TabularInline):
    model = Publication
    extra = 1

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
    list_filter = ('categories',)
    search_fields = ('title',)
    inlines = [PublicationInline,]
    filter_horizontal = ('categories',)

admin.site.register(Author, AuthorAdmin)
admin.site.register(Category)
admin.site.register(Publisher)
admin.site.register(Book, BookAdmin)
admin.site.register(Publication)
