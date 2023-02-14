from django.db import models


class Task(models.Model):
    description = models.TextField(max_length=200, null=False, blank=False, verbose_name='description')
    status = models.CharField(max_length=10, null=False, blank=False, verbose_name='status', default='new')
    completion_date = models.DateField(null=True, blank=True, verbose_name='Completion time')

    def __str__(self):
        return f'{self.description} = {self.status}'
