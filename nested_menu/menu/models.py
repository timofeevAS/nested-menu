from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menus'

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=200,
                           blank=True)
    parent = models.ForeignKey('self',
                               on_delete=models.CASCADE,
                               null=True,
                               blank=True,
                               related_name='children',
                               verbose_name='parent')
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE,
                             verbose_name='Menu')
    active = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'MenuItem'
        verbose_name_plural = 'MenuItems'

    def __str__(self):
        return self.name


