from django.contrib import admin
from .models import *


class ReactionAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Reaction._meta.fields]

    class Meta:
        model = Reaction


class DifficultyLevelAdmin(admin.ModelAdmin):
    list_display = [field.name for field in DifficultyLevel._meta.fields]

    class Meta:
        model = DifficultyLevel


admin.site.register(Reaction, ReactionAdmin)
admin.site.register(DifficultyLevel, DifficultyLevelAdmin)
