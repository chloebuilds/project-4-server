from django.contrib import admin
from .models import DailyGratitude, SprintGoal, SprintHabit, DailyToDo, Sprint, Mood, Energy, WeeklyIntention


admin.site.register(Sprint)
admin.site.register(SprintGoal)
admin.site.register(SprintHabit)
admin.site.register(Mood)
admin.site.register(DailyToDo)
admin.site.register(Energy)
admin.site.register(WeeklyIntention)
admin.site.register(DailyGratitude)
