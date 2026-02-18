from django.db import models


class Category(models.Model):
    work = "wk"
    learn = "ln"
    home = "hm"
    category_ = [
        (work,'Работа'),
        (learn,'Учеба'),
        (home,'Дом'),
    ]

    name = models.CharField(max_length=2,
                          choices=category_,
                          default=home,)
    
    def __str__(self):
        for t in self.category_:
            if t[0] == self.name:
                return t[1]
        return f'{self.name}'
    
class Task(models.Model):
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



