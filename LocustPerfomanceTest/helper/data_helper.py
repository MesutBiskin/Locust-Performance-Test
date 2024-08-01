class DataHelper:

    @classmethod
    def get_header_payload(cls):
        header = {
            "accept": "application/json",
            "Content-Type": "application/json"
        }
        return header

    @classmethod
    def post_body_payload(cls):
        request_body = {
            "id": 6325264536892,
            "username": "Can12",
            "firstName": "Can",
            "lastName": "Seker",
            "email": "can@hotmail.com",
            "password": "erm123456",
            "phone": "84556860845",
            "userStatus": 1
        }
        return request_body

    @classmethod
    def post_update_body_payload(cls):
        request_body = {
            "id": 6325263562,
            "username": "mesutbbb",
            "firstName": "mesut",
            "lastName": "biskin",
            "email": "mbiskin@gmail.com",
            "password": "s934934",
            "phone": "7834374837",
            "userStatus": 0
        }
        return request_body

    @classmethod
    def get_params_body(cls):
        params_body = {
            "username": "mesutbbbjhjhjh",
            "password": "s934934"
        }
        return params_body

    @classmethod
    def post_user_create_with_array(cls):
        array_body = [
            {
                "id": 6437637463,
                "username": "ArasB",
                "firstName": "Aras",
                "lastName": "Biskin",
                "email": "a@gmail.com",
                "password": "arasbiskin",
                "phone": "736473647",
                "userStatus": 1
            },
            {
                "id": 643763748783,
                "username": "ElisaB",
                "firstName": "Elisa",
                "lastName": "Biskin",
                "email": "e@gmail.com",
                "password": "elisabiskin",
                "phone": "736767473647",
                "userStatus": 0
            }

        ]
        return array_body
