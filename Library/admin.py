from django.contrib import admin

# import your model
from Library.models import Book, Social, Upload


class BookAdmin(admin.ModelAdmin):
    model = Book
    list_display = ('name', 'description',)
    prepopulated_fields = {'slug': ('name',)}


class SocialAdmin(admin.ModelAdmin):
    model = Social
    list_display = ('network', 'username',)


class UploadAdmin(admin.ModelAdmin):
    list_display = ('book',)
    list_display_links = ('book',)


admin.site.register(Book, BookAdmin)
admin.site.register(Social, SocialAdmin)
admin.site.register(Upload, UploadAdmin)
