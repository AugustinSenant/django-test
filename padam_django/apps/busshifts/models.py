from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.exceptions import ValidationError

class BusShift(models.Model):
    bus = models.ForeignKey('fleet.Bus', on_delete=models.PROTECT, related_name='shifts')
    driver = models.ForeignKey('fleet.Driver', on_delete=models.PROTECT, related_name='shifts')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def clean(self):
        if self.start_time is not None and self.end_time is not None:
            if self.start_time >= self.end_time:
                raise ValidationError('L\'heure de fin doit être après l\'heure de début.')

        # Vérifier les chevauchements de bus
        overlapping_shifts = BusShift.objects.filter(
            bus=self.bus,
            start_time__lt=self.end_time,
            end_time__gt=self.start_time,
        ).exclude(pk=self.pk)
        if overlapping_shifts.exists():
            raise ValidationError('Le bus est déjà assigné à un autre trajet durant cette période.')

        # Vérifier les chevauchements de chauffeur
        overlapping_shifts = BusShift.objects.filter(
            driver=self.driver,
            start_time__lt=self.end_time,
            end_time__gt=self.start_time,
        ).exclude(pk=self.pk)
        if overlapping_shifts.exists():
            raise ValidationError('Le chauffeur est déjà assigné à un autre trajet durant cette période.')

    def __str__(self):
        return f'Trajet {self.id} ({self.bus.licence_plate} - {self.driver.user})'
    

class BusStop(models.Model):
    name = models.CharField(max_length=100)
    shift = models.ForeignKey('BusShift', on_delete=models.CASCADE, related_name='stops')
    order = models.PositiveIntegerField()
    arrival_time = models.DateTimeField()

    class Meta:
        ordering = ['order']
        unique_together = ['shift', 'order']

    def __str__(self):
        return f'{self.name} (Ordre: {self.order})'



