from locust import HttpUser, between, task

class QuickStartUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def api_list(self):
        self.client.get("/products/api/v1/post/")
    @task
    def api_category(self):
        self.client.get("/products/api/v1/category/")