from __future__ import absolute_import, unicode_literals

from datetime import timedelta

from celery import shared_task
from celery.decorators import periodic_task

from zakon.parser import ZakonParser

from zakon.models import AcceptedZakonModel, RegisteredZakonModel



@periodic_task(run_every=timedelta(minutes=1))
def check_new_registered_laws():

    ZakonParser.parse_registered_laws()


@periodic_task(run_every=timedelta(minutes=1))
def check_new_accepted_laws():

    ZakonParser.parse_accepted_laws()


@periodic_task(run_every=timedelta(minutes=2))
def accepted_laws_mailing():

    laws = AcceptedZakonModel.get_new_laws()

    for law in laws:
        law.mailing_status = 'pending'
        law.save()
        # TODO send message
        law.mailing_status = 'mailed'
        law.save()


@periodic_task(run_every=timedelta(minutes=2))
def registered_laws_mailing():

    laws = AcceptedZakonModel.get_new_laws()

    for law in laws:
        law.mailing_status = 'pending'
        law.save()
        # TODO send message
        law.mailing_status = 'mailed'
        law.save()
