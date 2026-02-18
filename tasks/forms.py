from django import forms

class tasksForm(forms.Form):

    work = "wk"
    learn = "ln"
    home = "hm"
    category_ = [
        (work,'Работа'),
        (learn,'Учеба'),
        (home,'Дом'),
    ]

    name = forms.CharField(max_length=100,
                           label='Назваание',
                           min_length=1,
                           error_messages={
                              'max_length': 'Не больше 100 символов',
                              'min_length': 'Не мение 1 символа' 
                           })
    desk = forms.CharField(label='Описание',
                           min_length=1,
                           error_messages={
                              'max_length': 'Не больше 100 символов',
                              'min_length': 'Не мение 1 символа' 
                           },
                           widget=forms.Textarea
                           (attrs={
        'rows':2,
        'cols':20
    }))
    category = forms.CharField(label='Категория',
                               widget=forms.Select(choices=category_))
