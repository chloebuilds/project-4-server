# from jwt_auth.models import User
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

#! SPRINT MODEL
class Sprint(models.Model):
    sprint_name = models.CharField(max_length=50)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField()
    owner = models.ForeignKey(
        'jwt_auth.User',
        related_name='created_sprints',
        on_delete=models.PROTECT
    )
    def __str__(self):
        return f'Sprint {self.id}: {self.sprint_name}'


#! DAILY MODELS
#* Daily To-Do 
class DailyToDo(models.Model):
    to_do_item = models.CharField(max_length=50, blank = True, null = True, unique = False)
    is_done = models.BooleanField(default=False)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField()
    sprint = models.ForeignKey(
        Sprint,
        related_name='to_dos',
        on_delete=models.CASCADE,
        null=True
    )
    def __str__(self):
        return f'To-Do: {self.to_do_item}'

#* Daily Mood
class DailyMood(models.Model):
    mood_name = models.CharField(max_length=50)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField()
    sprint = models.ForeignKey(
        Sprint,
        related_name='moods',
        on_delete=models.CASCADE,
        null=True
    )
    def __str__(self):
        return f"{self.mood_name}"

#* Daily Energy Level
class DailyEnergy(models.Model):
    energy_level = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField()
    sprint = models.ForeignKey(
        Sprint,
        related_name='energy_levels',
        on_delete=models.CASCADE,
        null=True,
        default=1
    )
    def __str__(self):
        return f"{self.energy_level}"

#* Daily Gratitude
class DailyGratitude(models.Model):
    daily_gratitude = models.CharField(max_length=200)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField()
    sprint = models.ForeignKey(
            Sprint,
            related_name="daily_gratitudes",
            on_delete=models.PROTECT,
            null=True
        )
    def __str__(self):
        return f"{self.daily_gratitude}"

#! WEEKLY MODELS
#* Weekly Intentions
class WeeklyIntention(models.Model):
    weekly_intention = models.CharField(max_length=200)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField()
    sprint = models.ForeignKey(
            Sprint,
            related_name="weekly_intentions",
            on_delete=models.PROTECT,
            null=True
        )
    def __str__(self):
        return f"{self.weekly_intention}"

#! SPRINT-LENGTH MODELS
#* Sprint Habits
class SprintHabit(models.Model):
    habit_name = models.CharField(max_length=50 )
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField()
    is_done = models.BooleanField(default=False)
    sprint = models.ForeignKey(
        Sprint,
        related_name='sprint_habits',
        on_delete=models.CASCADE,
        null=True
    )
    def __str__(self):
        return f"{self.habit_name}"

#* Sprint Goals
class SprintGoal(models.Model):
    goal_name = models.CharField(max_length=50)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField()
    goal_description = models.CharField(max_length=250)
    is_done = models.BooleanField(default=False)
    sprint = models.ForeignKey(
        Sprint,
        related_name='sprint_goals',
        on_delete=models.CASCADE,
        null=True
    )
    def __str__(self):
        return f"{self.goal_name}"
