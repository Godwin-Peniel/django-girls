from django.contrib import admin

# impopting the Post model from the models.py file in the same directory (blog app) so it can be registered with the Django admin site and managed through the admin interface.

from .models import Post

# Register your models here.
admin.site.register(Post)
