from django.contrib import admin
from django.utils.html import format_html
from django.utils.translation import gettext as _
from production.models import Product, ProductPrice, ProducedReport, ProducedItems
# Register your models here.
admin.site.site_header = format_html(_('<img src="http://icons.iconarchive.com/icons/aha-soft/desktop-buffet/128/Pizza-icon.png"><br>Sistema de Gestión Fabrica de Pizzas'))
class ProductPriceAdmin(admin.TabularInline):
    exclude=('created_by',)
    model=ProductPrice
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductPriceAdmin]


class ProducedProductAdmin(admin.TabularInline):
    model=ProducedItems
    extra = 1

@admin.register(ProducedReport)
class ProducedReportAdmin(admin.ModelAdmin):
    inlines = [ProducedProductAdmin]