from celery.task.schedules import crontab
from celery.decorators import periodic_task
import pickle
import requests
from django.core.mail import send_mail
from django.template.loader import render_to_string
import datetime
import pytz
from .models import FullAccessSubscription, AdminSetting
import decimal
from . import const
from app_rama import settings
from django.contrib.sites.models import Site


@periodic_task(run_every=(crontab(minute='*/60')))
def main():
    set = AdminSetting.objects.all()
    if len(set) > 0:
        update_hour = set.first().check_hour
    else:
        update_hour = 1
    tz = pytz.timezone('Europe/Warsaw')
    warsaw_now = datetime.datetime.now(tz)
    print(warsaw_now)
    current_hour = decimal.Decimal(warsaw_now.hour)
    print("current:", current_hour)
    print("update hour", update_hour)

    if not current_hour == update_hour:
        return 'other time'

    old_subscriptions = FullAccessSubscription.objects.filter(end_at__lte=warsaw_now, status=const.SUBSCRIPTION_ACTIVE)
    message_text = 'Your subscription is expired, Please subscribe other plan.'
    send_user = []
    for item in old_subscriptions:
        item.status = const.SUBSCRIPTION_FINISH
        item.save()
        send_user.append(item.user.email)

    if len(old_subscriptions) > 0:
        send_mail('Subscription is expired', message_text, settings.DEFAULT_FROM_EMAIL, send_user)
        context = {
            'products': old_subscriptions,
            'domain': Site.objects.get_current().domain
        }
        message_html = render_to_string('email.html', context)
        send_mail('Some subscriptions are expired', '', settings.ADMIN_EMAIL, [settings.DEFAULT_FROM_EMAIL, ], message_html)
        return 'Some Subscription expired'

    return 'No old Subscription'
