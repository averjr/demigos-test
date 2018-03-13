import schedule
import time
import threading

from .models import Pair, Price
import requests


def get_price(first, second):
    url = "https://api.cryptonator.com/api/ticker/{}-{}".format(first, second)
    response = requests.get(url)
    if response.json()['success'] is True:
        return response.json()['ticker']['price']
    return False


def job():
    for p in Pair.objects.all():
        price = get_price(p.currency_first.code, p.currency_second.code)
        if price:
            Price.objects.create(pair=p, price=price)


class ScheduleThread(threading.Thread):
    def __init__(self, *pargs, **kwargs):
        super().__init__(*pargs, daemon=True, name="scheduler", **kwargs)

    def run(self):
        while True:
            schedule.run_pending()
            time.sleep(schedule.idle_seconds())


schedule.every(10).seconds.do(job)
ScheduleThread().start()
