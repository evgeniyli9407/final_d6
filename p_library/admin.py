from django.contrib import admin
from p_library.models import Redaction, Book, Author, Inspiration, Friends

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):

    @staticmethod
    def author_full_name(obj):
        return obj.author.full_name

    list_display = ('title', 'author_full_name',)
    fields = ('ISBN', 'title', 'description', 'year_release', 'author', 'price', 'copy_count', 'redaction', 'friend_to')


@admin.register(Redaction)
class RedactionAdmin(admin.ModelAdmin):
    pass

@admin.register(Friends)
class FriendsAdmin(admin.ModelAdmin):
    pass

@admin.register(Inspiration)
class InspirationAdmin(admin.ModelAdmin):
    pass