from django.db import models


class Category(models.Model):
    work = "Работа"
    learn = "Учеба"
    home = "Дом"
    category_ = [
        ('wk',work),
        ('ln',learn),
        ('hm',home),
    ]

    name = models.CharField(max_length=2,
                          choices=category_,
                          default='wk',)
class tasks(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    status = models.BooleanField(default=False,
                                 blank=True,
                                 null=True)
    category = models.ForeignKey(Category,
                                 on_delete=models.SET_NULL,
                                 null=True,
                                 blank=True)
    date = models.DateField(auto_now_add=True)



