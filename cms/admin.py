from django.contrib import admin
from .models import Client, BannerImage, Customize,Post,PostImage,Contact

class PostImageAdmin(admin.StackedInline):
    model=PostImage
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines=[PostImageAdmin]

    class Meta:
        model=Post

@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    pass


# Register your models here.
admin.site.register(Client)
admin.site.register(BannerImage)
admin.site.register(Customize)
admin.site.register(Contact)


