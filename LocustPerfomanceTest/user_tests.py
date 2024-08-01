from locust import HttpUser, between, task
from helper.data_helper import DataHelper


class PetStoreUser(HttpUser):
    wait_time = between(5, 15)

    @task
    def user_create(self):
        self.client.post("/v2/user", json=DataHelper.post_body_payload())

    @task
    def user_info(self):
        self.client.get("/v2/user/Can")

    @task
    def user_update(self):
        self.client.put("/v2/user/mbiskin", json=DataHelper.post_update_body_payload(),
                        headers=DataHelper.get_header_payload())

    @task
    def user_delete(self):
        self.client.post("/v2/user", json=DataHelper.post_body_payload())
        self.client.delete("/v2/user/Can12", headers=DataHelper.get_header_payload())

    @task
    def user_login(self):
        self.client.get("/v2/user/login?", headers=DataHelper.get_header_payload(), params=DataHelper.get_params_body())

    @task
    def user_logout(self):
        self.client.get("/v2/user/logout", headers=DataHelper.get_header_payload())

    @task
    def user_create_with_array(self):
        self.client.post("/v2/user/createWithArray", json=DataHelper.post_user_create_with_array(),
                         headers=DataHelper.get_header_payload())

    @task
    def user_create_with_list(self):
        self.client.post("/v2/user/createWithArray", json=DataHelper.post_user_create_with_array(),
                         headers=DataHelper.get_header_payload())
