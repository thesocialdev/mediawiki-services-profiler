from locust import HttpLocust, TaskSet, task
import os
import random

# Profiling class for the Wikimedia Page Content Service (mobileapps).
# Endpoint request weighting is taken from the average request rate over 6 hours as reported on
# https://grafana.wikimedia.org/d/000000183/mobileapps?orgId=1&fullscreen&panelId=1.
class UserBehavior(TaskSet):

    dogHtml = open(os.path.abspath('fixtures/Dog.html'))
    titles = ['Barack_Obama', 'Brazil', 'Aidan_McAnespie', 'Cat', 'Dog', 'Wolf']

    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """

    def on_stop(self):
        """ on_stop is called when the TaskSet is stopping """

    # Page content

    @task(64)
    def mobileSections(self):
        self.client.get("/en.wikipedia.org/v1/page/mobile-sections/%s" % random.choice(self.titles))

    @task(0)
    def mobileSectionsLead(self):
        self.client.get("/en.wikipedia.org/v1/page/mobile-sections-lead/%s" % random.choice(self.titles))

    @task(0)
    def mobileSectionsRemaining(self):
        self.client.get("/en.wikipedia.org/v1/page/mobile-sections-remaining/%s" % random.choice(self.titles))

    @task(57)
    def mobileHtml(self):
        self.client.get("/en.wikipedia.org/v1/page/mobile-html/%s" % random.choice(self.titles))

    @task(0)
    def mobileHtmlOfflineResources(self):
        self.client.get("/en.wikipedia.org/v1/page/mobile-html-offline-resources/%s" % random.choice(self.titles))

    @task(0)
    def transformHtmlToMobileHtml(self):
        self.client.post("/en.wikipedia.org/v1/transform/html/to/mobile-html/Dog", self.dogHtml)

    @task(4)
    def media(self):
        self.client.get("/en.wikipedia.org/v1/page/media/%s" % random.choice(self.titles))

    @task(58)
    def mediaList(self):
        self.client.get("/en.wikipedia.org/v1/page/media-list/%s" % random.choice(self.titles))

    @task(0)
    def metadata(self):
        self.client.get("/en.wikipedia.org/v1/page/metadata/%s" % random.choice(self.titles))

    @task(58)
    def references(self):
        self.client.get("/en.wikipedia.org/v1/page/references/%s" % random.choice(self.titles))

    @task(85)
    def summary(self):
        self.client.get("/en.wikipedia.org/v1/page/summary/%s" % random.choice(self.titles))

    # Wiktionary definitions

    @task(0)
    def definition(self):
        self.client.get("en.wiktionary.org/v1/page/definition/%s" % random.choice(self.titles))

    # Talk

    @task(1)
    def talk(self):
        self.client.get("/en.wikipedia.org/v1/page/talk/Talk:%s" % random.choice(self.titles))

    # CSS

    @task(0)
    def baseCss(self):
        self.client.get("/en.wikipedia.org/v1/data/css/mobile/base")

    @task(0)
    def siteCss(self):
        self.client.get("/en.wikipedia.org/v1/data/css/mobile/site")

    @task(0)
    def pageLibCss(self):
        self.client.get("/en.wikipedia.org/v1/data/css/mobile/pagelib")

    @task(0)
    def pcsCss(self):
        self.client.get("/en.wikipedia.org/v1/data/css/mobile/pcs")

    # JS

    @task(0)
    def pageLibJs(self):
        self.client.get("/en.wikipedia.org/v1/data/javascript/mobile/pagelib")

    @task(0)
    def pcsJs(self):
        self.client.get("/en.wikipedia.org/v1/data/javascript/mobile/pcs")


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 10000
    max_wait = 60000
