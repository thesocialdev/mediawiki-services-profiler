from locust import HttpUser, TaskSet, task
import os
import random

# Profiling class for the Mediawiki Service Geoshapes
# Endpoint request weighting is taken from the average request rate over 6 hours as reported on
# https://grafana.wikimedia.org/goto/QzkPE4E7k?orgId=1
# 
# Geospatial data used in this test: https://download.geofabrik.de/europe/malta-latest.osm.pbf
class UserBehavior(HttpUser):
    min_wait = 10000
    max_wait = 60000

    line_ids = ['Q12233910','Q3739495','Q3739500']
    polygon_ids = ['Q233','Q20199405','Q47499270']

    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """

    def on_stop(self):
        """ on_stop is called when the TaskSet is stopping """

    # Geoshapes.ids
    @task(2) # ~14.4 req/s
    def geoshapesIds(self):
        ids = random.sample(self.polygon_ids, random.randint(1, len(self.polygon_ids)))
        self.client.get("/geoshape?ids=%s" % ','.join(ids))
    
    # # Geoshapes.wdqs
    # @task(5) # ~0.25 req/s
    # def mobileSectionsLead(self):
    #     self.client.get("/geoshapes?%s" % random.sample(self.ids, random.randint(1, len(this.ids))))
    
    # Geolines.ids
    @task(1) # ~6.68 req/s
    def geolinesIds(self):
        ids = random.sample(self.line_ids, random.randint(1, len(self.line_ids)))
        self.client.get("/geoline?ids=%s" % ','.join(ids))

    # # Geolines.wdqs
    # @task(1) # ~0.05 req/s
    # def mobileHtml(self):
    #     self.client.get("/geoline?%s" % random.sample(self.ids, random.randint(1, len(this.ids))))
