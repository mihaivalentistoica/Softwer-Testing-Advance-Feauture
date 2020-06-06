from locust import HttpUser, TaskSet, task


class TestEndpoints(TaskSet):
    @task
    def test_homepage(self):
        self.client.get("/")

    @task
    def test_about(self):
        self.client.get("/about")

    @task
    def test_form(self):
        self.client.post("/form", data={"user": "random"})

    @task
    def test_admin(self):
        self.client.get("/admin")

    def wait_time(self):
        return 1


class MyLocust(HttpUser):
    tasks = [TestEndpoints]
