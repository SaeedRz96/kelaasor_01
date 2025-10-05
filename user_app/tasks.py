from celery import shared_task
from time import sleep
from user_app.models import Basket

@shared_task(bind=True)
def send_email_to_user(self):
    sleep(60)
    

@shared_task(bind=True)
def send_promotion_sms(self):
    ...


@shared_task(bind=True, default_retry_delay= 30)
def check_basket_status(self):
    try:
        Basket.objects.filter(is_paid=True).delete()
    except Exception as e:
        raise self.retry(exc=e, max_retries=4)
    