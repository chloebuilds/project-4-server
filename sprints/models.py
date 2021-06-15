from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Sprint(models.Model):
    sprint_name = models.CharField(max_length=50)
    start_date = models.DateTimeField(auto_now_add=True)
    # end_date = models.DateField()

    def __str__(self):
        return f"{self.sprint_name}"


class SprintGoal(models.Model):
    goal_name = models.CharField(max_length=50)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateField()
    goal_description = models.CharField(max_length=250)
    sprint = models.ForeignKey(
        Sprint,
        related_name='sprint_goals',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.goal_name}"


class Mood(models.Model):
    mood_name = models.CharField(max_length=50)
    start_date = models.DateTimeField(auto_now_add=True)
    sprint = models.ForeignKey(
        Sprint,
        related_name='moods',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.mood_name}"


class Energy(models.Model):
    energy_level = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )
    start_date = models.DateTimeField(auto_now_add=True)
    sprint = models.ForeignKey(
        Sprint,
        related_name='energy_levels',
        on_delete=models.CASCADE,
          default=1
    )

    def __str__(self):
        return f"{self.energy_level}"

