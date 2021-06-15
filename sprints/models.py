from django.db import models


class Sprint(models.Model):
    sprint_name = models.CharField(max_length=50)
    # start_date = models.DateField()
    # end_date = models.DateField()
    def __str__(self):
        return f"{self.sprint_name}"

class SprintGoal(models.Model):
    goal_name = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    goal_description = models.CharField(max_length=250)
    sprint = models.ForeignKey(
        Sprint,
        related_name='sprint_goals',
        on_delete=models.CASCADE,
    )
    def __str__(self):
        return f"{self.goal_name}"

class Mood(models.Model):
    mood_name = models.CharField(max_length=50)
    sprint = models.ForeignKey(
        Sprint,
        related_name='moods',
        on_delete=models.CASCADE,
    )
    def __str__(self):
        return f"{self.mood_name}"

class WeeklyIntention(models.Model):
    weekly_intention = models.CharField(max_length=200)
    start_date = models.DateTimeField(auto_now_add=True)
    sprint = models.ForeignKey(
            Sprint,
            related_name="weekly_intentions",
            on_delete=models.PROTECT,
        )
    def __str__(self):
        return f"{self.weekly_intention}"

class DailyGratitude(models.Model):
    daily_gratitude = models.CharField(max_length=200)
    start_date = models.DateTimeField(auto_now_add=True)
    sprint = models.ForeignKey(
            Sprint,
            related_name="daily_gratitudes",
            on_delete=models.PROTECT,
        )
    def __str__(self):
        return f"{self.daily_gratitude}"