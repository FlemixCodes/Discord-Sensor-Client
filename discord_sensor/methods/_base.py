from ..request_client import RequestClient


class BaseCategory:
    def __init__(self, requets_client: RequestClient):
        self.request_client = requets_client
