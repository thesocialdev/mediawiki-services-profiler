import os
from locust import HttpUser, task, between


class LinkRecommendation(HttpUser):
    wait_time = between(5, 9)

    @task
    def get_link_recommendatoins(self):
        payload = open(os.path.abspath('fixtures/linkrecommendationpayload.json'), 'r').read()
        headers = {'content-type': 'application/json'}
        self.client.post("/query", data=payload, headers=headers)
