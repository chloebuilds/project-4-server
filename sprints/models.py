from django.db import models


#! SPRINT MODEL

class Sprint(models.Model):
    sprint_name = models.CharField(max_length=50)
    start_date = models.DateField()

    def __str__(self):
        return f"{self.sprint_name}"


#! DAILY MODELS
#* Daily To-Do 

class DailyToDo(models.Model):
    to_do_item = models.CharField(max_length=50, blank = True, null = True, unique = False)
    isDone = models.BooleanField(default=False)
    start_date = models.DateTimeField(auto_now_add=True)
    sprint = models.ForeignKey(
        Sprint,
        related_name='daily_to_do',
        on_delete=models.CASCADE
    )
    def __str__(self):
        return f'To-Do: {self.to_do_item}'

#* Daily Mood
class Mood(models.Model):
    mood_name = models.CharField(max_length=50)
    sprint = models.ForeignKey(
        Sprint,
        related_name='moods',
        on_delete=models.CASCADE
    )
    def __str__(self):
        return f"{self.mood_name}"

#* Daily Energy Level
#* Daily Gratitude

#! WEEKLY MODELS
#* Weekly Intentions

#! SPRINT-LENGTH MODELS
#* Sprint Habits
class SprintHabit(models.Model):
    habit_item = models.CharField(max_length=50)
    habit_description = models.CharField(max_length=250)
    isDone = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Habit: {self.habit_item}'

#* Sprint Goals
class SprintGoal(models.Model):
    goal_name = models.CharField(max_length=50)
    goal_description = models.CharField(max_length=250)
    start_date = models.DateField()
    end_date = models.DateField()        
    sprint = models.ForeignKey(
        Sprint,
        related_name='sprint_goals',
        on_delete=models.CASCADE
    )
    def __str__(self):
        return f"{self.goal_name}"
