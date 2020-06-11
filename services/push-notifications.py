import json
from locust import HttpUser, task, between

# Profiling class for the Wikimedia Page Content Service (mobileapps).
# Endpoint request weighting is taken from the average request rate over 6 hours as reported on
# https://grafana.wikimedia.org/d/000000183/mobileapps?orgId=1&fullscreen&panelId=1.
class PushNotifications(HttpUser):
    wait_time = between(5, 9)
    
    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """

    def on_stop(self):
        """ on_stop is called when the TaskSet is stopping """

    @task
    def fcmSendMessage(self):
        payload = {"deviceTokens":["TOKEN"],"messageType":"checkEchoV1","dryRun":True}
        headers = {'content-type': 'application/json'}
        self.client.post("/v1/message/fcm", data=json.dumps(payload), headers=headers);
