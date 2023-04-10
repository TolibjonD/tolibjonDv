from django.contrib import admin
from .models import Comments, Posts, PostComments

# Register your models here.


class CustomCommentsAdmin(admin.ModelAdmin):
    model = Comments


class PostsAdmin(admin.ModelAdmin):
    model = Posts
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Comments, CustomCommentsAdmin)
admin.site.register(Posts, PostsAdmin)
admin.site.register(PostComments)
