from django.db import models

STATUS_CHOICES = (
    ('new', 'Новая'),
    ('in_progress', 'В процессе'),
    ('done', 'Сделано')
)


class Tasks(models.Model):
    description = models.CharField(max_length=200, null=False, blank=False, verbose_name='Описание')

    status = models.CharField(max_length=40, null=False, blank=False, default=STATUS_CHOICES[0][0],
                              choices=STATUS_CHOICES, verbose_name='Статус')

    created_at = models.DateField(null=True, blank=True, verbose_name='Время создания')


    def __str__(self):
        return "{}. {}".format(self.pk, self.description)