from django.contrib import admin
from .models import Sprint, SprintGoal, Mood, Energy


admin.site.register(Sprint)
admin.site.register(SprintGoal)
admin.site.register(Mood)
admin.site.register(Energy)
