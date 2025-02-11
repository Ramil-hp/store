from django.contrib import admin

# Register your models here.
from products.models import Basket, Product, ProductCategory

admin.site.register(ProductCategory)

# ТУТ РАБОТА С АДМИНКОЙ,ВЫВОД  ДЛЯ КРАСОТЫ И УДОБСТВА ПО СТРОЧНО
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # ТУТ ПИШЕМ ЧТО ХОТИМ ВИДЕТЬ В АДМИНКЕ-КАКИЕ ТОВ
    list_display = ('name','price','quantity', 'category')
    # ЧТО ИМЕННО БУДЕТ ПОКЗАННО В КАЖДОМ ИЗ ОТДЕЛОВ
    fields = ('image', 'name', 'description', 'price', 'quantity', 'category')
    # какие строки чисто для чтения
    readonly_fields = ('description',)
    # добавление поисковой строки по крит
    search_fields = ('name',)
    # сортировка
    ordering = ('name',)
class BasketAdmin(admin.TabularInline):
    model= Basket
    fields = ('product','quantity')
    extra = 0


