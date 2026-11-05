from django.test import TestCase


class TaskApiTests(TestCase):
    def test_health(self):
        r = self.client.get("/health/")
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["status"], "ok")

    def test_create_and_list_task(self):
        r = self.client.post("/tasks/", data='{"title": "learn CI/CD"}', content_type="application/json")
        self.assertEqual(r.status_code, 201)
        r = self.client.get("/tasks/")
        self.assertEqual(r.json()["tasks"][0]["title"], "learn CI/CD")

    def test_title_required(self):
        r = self.client.post("/tasks/", data="{}", content_type="application/json")
        self.assertEqual(r.status_code, 400)
