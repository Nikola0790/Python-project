from django.contrib import admin
from .models import Category, Article


# 1. Create an Inline class for Articles
class ArticleInline(admin.TabularInline):
    model = Article.category.through # This targets the hidden many-to-many join table
    extra = 1 # Shows 1 empty row by default to add an article
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    inlines = [ArticleInline] # Adds the Articles section inside the Category edit page

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'content', 'status', 'date_added', 'publish_date', 'removal_date')
    filter_horizontal = ('category',) # Adds a nice side-by-side selector widget for categories