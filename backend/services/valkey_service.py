from backend.utils.config import settings
import valkey


class ValkeyService:

    def __init__(self):
        self.client = valkey.Valkey(
            host=settings.VALKEY_HOST,
            port=settings.VALKEY_PORT
        )

    def set(self, key, value):
        self.client.set(key, value)

    def get(self, key):
        return self.client.get(key)