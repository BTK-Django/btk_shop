from django.contrib import admin
from product.models import Category

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    list_filter = ['status']
    # fields = ['status']


admin.site.register(Category, CategoryAdmin)