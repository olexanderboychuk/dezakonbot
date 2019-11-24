from django.db import models
import dateutil.parser

class RegisteredZakonModel(models.Model):

    reg_id = models.CharField(max_length=50)
    date = models.DateField(auto_now=False, auto_now_add=False)
    name = models.TextField()
    authors = models.TextField()

    def __str__(self):
        return self.reg_id

    @classmethod
    def create_from_dict(cls, zakon_dict):
        if not cls.objects.filter(reg_id=zakon_dict['id']).exists():
            cls.objects.create(
                reg_id=zakon_dict['id'],
                date=dateutil.parser.parse(zakon_dict['date']),
                name=zakon_dict['name'],
                authors=zakon_dict['authors']
            )


class AcceptedZakonModel(models.Model):

    reg_id = models.CharField(max_length=50)
    date = models.DateField(auto_now=False, auto_now_add=False)
    name = models.TextField()
    number_act = models.CharField(max_length=50)
    date_act = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.number_act

    @classmethod
    def create_from_dict(cls, zakon_dict):
        if not cls.objects.filter(reg_id=zakon_dict['id']).exists():
            cls.objects.create(
                reg_id=zakon_dict['id'],
                date=dateutil.parser.parse(zakon_dict['date']),
                name=zakon_dict['name'],
                number_act=zakon_dict['number_act'],
                date_act=dateutil.parser.parse(zakon_dict['date_act'])
            )
