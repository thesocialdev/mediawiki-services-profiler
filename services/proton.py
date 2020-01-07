from locust import HttpLocust, TaskSet, task

import random

def random_title():
    titles = [ 'Obama', 'Brazil', 'Aidan_McAnespie', 'Cat', 'Dog', 'Wolf' ]
    return random.choice(titles)
    
class UserBehavior(TaskSet):
    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """

    def on_stop(self):
        """ on_stop is called when the TaskSet is stopping """

    @task(0)
    def legal_undefined(self):
        self.client.get("/en.wikipedia.org/v1/pdf/%s/legal" % (random_title()))

    @task(1)
    def letter_mobile(self):
        self.client.get("/en.wikipedia.org/v1/pdf/%s/letter/mobile" % (random_title()))

    @task(1)
    def letter_desktop(self):
        self.client.get("/en.wikipedia.org/v1/pdf/%s/letter/desktop" % (random_title()))

    @task(11)
    def a4_undefined(self):
        self.client.get("/en.wikipedia.org/v1/pdf/%s/a4" % (random_title()))

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 10000
    max_wait = 60000