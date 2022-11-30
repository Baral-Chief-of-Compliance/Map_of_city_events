from django.db import models
from datetime import datetime
from geopy import Yandex
# Create your models here.


class Event(models.Model):
    name = models.CharField('Название мероприятие', max_length=255)
    dt_of_start = models.DateTimeField('Дата и время начала мероприятия', default=datetime.now)
    dt_of_end = models.DateTimeField('Дата и время окончания мероприятия', default=datetime.now)
    town = models.CharField('Город проведения мероприятия', default='Мурманск', max_length=255)
    street = models.CharField('Улица проведения мероприятия', max_length=255)
    house = models.CharField('Дом проведения мероприятия', max_length=3, blank=True)
    frame = models.CharField('Корпус мероприятия', max_length=2, blank=True)
    description = models.TextField('Описание мероприятия', blank=True)
    url = models.URLField('Ссылка на сайте мероприятия', max_length=500, blank=True)
    organizers = models.CharField('Организаторы', max_length=255, blank=True)
    latitude = models.CharField('Широта', max_length=255, null=True, blank=True)
    longitude = models.CharField('Долгота', max_length=255, null=True, blank=True)
    paid = models.BooleanField('Платное')
    price = models.CharField('Цена', max_length=10, blank=True)
    age_limit = models.CharField('Возрастное ограничение', max_length=5)
    def save(self, *args, **kwargs):
        place = f"{self.street} {self.house} {self.frame}, {self.town}"
        location = Yandex(api_key='aaca613a-fe9d-47d2-95f3-cd1714593fff').geocode(place)
        self.latitude = location.latitude
        self.longitude = location.longitude
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} - адрес: улица {self.street}, дом {self.house}, корпус {self.frame}"

    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'
        ordering = ["-dt_of_start"]


def upload_to(instance, filename):
    return 'event_img/%s/%s' % (instance.events.name, filename)


class EventImg(models.Model):
    events = models.ForeignKey(Event, verbose_name='Мероприятие', on_delete=models.CASCADE)
    name = models.CharField('Подпись к изображению', max_length=255, blank=True)
    img = models.ImageField('Изображение к мероприятию', upload_to=upload_to)

    def __str__(self):
        return f"Мероприятие {self.events}"

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'