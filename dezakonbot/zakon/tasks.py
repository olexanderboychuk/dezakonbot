from __future__ import absolute_import, unicode_literals

from datetime import timedelta

from celery import shared_task
from celery.decorators import periodic_task

from .parser import ZakonParser


@periodic_task(run_every=timedelta(minutes=1))
def check_new_registered_laws():
    
    ZakonParser.parse_registered_laws()


@periodic_task(run_every=timedelta(minutes=1))
def check_new_accepted_laws():
    
    ZakonParser.parse_accepted_laws()
