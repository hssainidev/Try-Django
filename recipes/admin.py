from django.contrib import admin
from .models import Recipe, RecipeIngredient
from django.contrib.auth import get_user_model

User = get_user_model()


class RecipeIngredientInline(admin.StackedInline):
    model = RecipeIngredient
    extra = 0
    readonly_fields = ["quantity_as_float", "as_mks", "as_imperial"]
    # fields = ['name', 'quantity', 'unit', 'directions']


class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientInline]
    list_display = ["name", "user"]
    readonly_fields = ["timestamp", "updated"]
    raw_id_fields = ["user"]


admin.site.register(Recipe, RecipeAdmin)
