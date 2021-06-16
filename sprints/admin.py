from django.contrib import admin
from .models import  Sprint, SprintGoal, SprintHabit
from .models import WeeklyIntention
from .models import DailyToDo,  DailyMood, DailyEnergy, DailyGratitude

admin.site.register(Sprint)
admin.site.register(SprintGoal)
admin.site.register(SprintHabit)
admin.site.register(WeeklyIntention)
admin.site.register(DailyToDo)
admin.site.register(DailyMood)
admin.site.register(DailyEnergy)
admin.site.register(DailyGratitude)
