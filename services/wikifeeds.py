from locust import HttpLocust, TaskSet, task

import random

def random_year():
    return random.randrange(2016,2019)

def random_month():
    month = random.randrange(1,13)
    if month < 10:
        return "0%d" % (month)
    else:
        return "%d" % (month)

def random_day():
    day = random.randrange(1, 29)
    if day < 10:
        return "0%d" % (day)
    else:
        return "%d" % (day)

class UserBehavior(TaskSet):
    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """

    def on_stop(self):
        """ on_stop is called when the TaskSet is stopping """

    @task(1)
    def announcements(self):
        self.client.get("/en.wikipedia.org/v1/feed/announcements")

    @task(0)
    def availability(self):
        self.client.get("/en.wikipedia.org/v1/feed/availability")

    @task(1)
    def news(self):
        self.client.get("/en.wikipedia.org/v1/page/news")

    @task(23)
    def random(self):
        self.client.get("/en.wikipedia.org/v1/page/random/title")

    @task(8)
    def onthisday(self):
        self.client.get("/en.wikipedia.org/v1/feed/onthisday/selected/%s/%s" % (random_month(), random_day()))

    @task(3)
    def featured(self):
        self.client.get("/en.wikipedia.org/v1/page/featured/%d/%s/%s" % (random_year(), random_month(), random_day()))

    @task(3)
    def image_featured(self):
        self.client.get("/en.wikipedia.org/v1/media/image/featured/%d/%s/%s" % (random_year(), random_month(), random_day()))

    @task(3)
    def most_read(self):
        self.client.get("/en.wikipedia.org/v1/page/most-read/%d/%s/%s" % (random_year(), random_month(), random_day()))

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 10000
    max_wait = 60000