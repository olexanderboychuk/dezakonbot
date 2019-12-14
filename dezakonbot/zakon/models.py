import dateutil.parser
from django.db import models


class RegisteredZakonModel(models.Model):

    reg_id = models.CharField(max_length=50)
    date = models.DateField(auto_now=False, auto_now_add=False)
    name = models.TextField()
    authors = models.TextField()
    mailing_status = models.CharField(default='new', max_length=50)

    def __str__(self):
        return f"{self.reg_id}: {self.name}"

    @classmethod
    def create_from_dict(cls, zakon_dict):
        if not cls.objects.filter(reg_id=zakon_dict['id']).exists():
            zakon = cls.objects.create(
                reg_id=zakon_dict['id'],
                date=dateutil.parser.parse(zakon_dict['date']),
                name=zakon_dict['name'],
                authors=zakon_dict['authors']
            )

    @classmethod
    def get_new_laws(cls):

        return cls.objects.filter(mailing_status='new')


class AcceptedZakonModel(models.Model):

    reg_id = models.CharField(max_length=50)
    date = models.DateField(auto_now=False, auto_now_add=False)
    name = models.TextField()
    number_act = models.CharField(max_length=50)
    date_act = models.DateField(auto_now=False, auto_now_add=False)
    mailing_status = models.CharField(default='new', max_length=50)

    def __str__(self):
        return f"{self.number_act}: {self.name}"

    @classmethod
    def create_from_dict(cls, zakon_dict):
        if not cls.objects.filter(reg_id=zakon_dict['id']).exists():
            zakon = cls.objects.create(
                reg_id=zakon_dict['id'],
                date=dateutil.parser.parse(zakon_dict['date']),
                name=zakon_dict['name'],
                number_act=zakon_dict['number_act'],
                date_act=dateutil.parser.parse(zakon_dict['date_act'])
            )

    @classmethod
    def get_new_laws(cls):

        return cls.objects.filter(mailing_status='new')
