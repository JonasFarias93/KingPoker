from django.db import models

class Participant(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, blank=False, null=False)
    points = models.IntegerField()
    is_member = models.BooleanField(default=True)
    count_for_ranking = models.BooleanField(default=True)