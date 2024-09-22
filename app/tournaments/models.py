from django.db import models
from players.models import Participant


class Tornament(models.Model):
    year = models.PositiveIntegerField()
    name_tornament = models.CharField(max_length=30, blank=False, null=False, default='Nome do Torneio não Informado.')
    description = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.name_tornament

class Arena(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, blank=False, null=False, default='Nome Não Informado')
    adress = models.CharField(max_length=150, blank=False, null=False, default='Endereço não Informado')
    city = models.CharField(max_length=30, blank=False, null=False, default='Cidade não Informada')
    description = models.CharField(max_length=500, blank=True, null=True)
    latitude = models.DecimalField(max_digits=10, decimal_places=6, null=True)
    longitude = models.DecimalField(max_digits=10, decimal_places=6, null=True)

    def __str__(self):
        return self.name

class Round(models.Model):
    tornament = models.ForeignKey(Tornament, on_delete=models.CASCADE)
    number = models.PositiveIntegerField()
    date = models.DateField()
    extra = models.BooleanField(default=False)
    arena = models.ForeignKey(Arena, on_delete=models.PROTECT, blank=True, null=True)

    def __str__(self):
        return self.number

class ParticipantRound(models.Model):
    round = models.ForeignKey(Round, on_delete=models.CASCADE)
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    points = models.IntegerField()
    position = models.PositiveIntegerField()

    def __str__(self):
        return self.participant

class FinalRanking(models.Model):
    tornament = models.ForeignKey(Tornament, on_delete= models.CASCADE)
    participant = models.ForeignKey(Participant, on_delete= models.CASCADE)
    points = models.IntegerField()
    position = models.PositiveIntegerField()

    def __str__(self):
        return self.participant

class NivelBlind(models.Model):
    tornament = models.ForeignKey(Tornament, on_delete=models.CASCADE)
    number = models.PositiveSmallIntegerField()
    small_blind = models.DecimalField(max_digits=10, decimal_places=2)
    big_blind = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.PositiveIntegerField()

    def __str__(self):
        return self.number

