class MikrotikAPI:

    def __init__(
        self,
        ip="",
        port=8728,
        user="",
        password=""
    ):

        self.ip = ip
        self.port = port
        self.user = user
        self.password = password

    def connect(self):

        return True

    def get_profiles(self):

        return [
            "20GB",
            "50GB",
            "100GB"
        ]
