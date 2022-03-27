from django.contrib import admin
from books import models

# Register your models here.
admin.site.register(models.Account)
admin.site.register(models.Request)
admin.site.register(models.Review)
admin.site.register(models.Library)
admin.site.register(models.Book)
admin.site.register(models.BookOwned)
admin.site.register(models.Borrow)
admin.site.register(models.Transaction)
admin.site.register(models.SocialRating)