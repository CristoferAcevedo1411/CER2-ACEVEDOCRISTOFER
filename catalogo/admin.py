from django.contrib import admin

# Register your models here.
from .models import Categoria, LugarPatrimonial


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)


@admin.register(LugarPatrimonial)
class LugarPatrimonialAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'ubicacion', 'anio_construccion')
    list_filter = ('categoria',)
    search_fields = ('nombre', 'ubicacion')