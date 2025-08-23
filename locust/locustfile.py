from locust import HttpUser, between, task

class QuickStartUser(HttpUser):
    wait_time = between(1, 5)

    def on_start(self):
        response = self.client.post("/accounts/api/v2/jwt/create/", data={
            "username": "mohamad",
            "password": "Nima4030#"
        }).json()
        
        self.client.headers = {'Authorization': f"Bearer {response.get('access', None)}"}

    @task
    def api_list(self):
        self.client.get("/products/api/v1/post/")
        
    @task
    def api_category(self):
        self.client.get("/products/api/v1/category/")