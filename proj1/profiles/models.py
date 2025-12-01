from django.db import models

class Users(models.Model):
    username = models.CharField('Имя пользователя', max_length=30, blank=False, unique=False)
    password = models.CharField('Пароль', max_length=35)
    birthday = models.DateField('Дата рождения')
    email = models.EmailField('Адрес электронной почты', max_length=254, unique=False)
    regday = models.DateField('Дата регистрации', auto_now_add=True)

    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'