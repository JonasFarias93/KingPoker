from django.db import models

class Participant(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, blank=False, null=False)
    points = models.IntegerField()
    is_member = models.BooleanField(default=True)
    count_for_ranking = models.BooleanField(default=True)
    city = models.CharField(max_length=30, blank=False, null=False, default='Cidade não Informada')

    def __str__(self):
        return self.name


class MonthlyFee(models.Model):
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    date_paid = models.DateField()

