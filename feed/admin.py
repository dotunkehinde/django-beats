from django.contrib import admin
from .models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    pass

admin.site.register(Post, PostAdmin)
# This code registers the Post model with the Django admin site, allowing it to be managed through the admin interface. The PostAdmin class can be customized to change how the model is displayed in the admin interface.