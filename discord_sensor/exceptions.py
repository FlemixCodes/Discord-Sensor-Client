class DiscordSensorException(Exception):
    pass


class DiscordSensorHTTPException(DiscordSensorException):
    pass


class DiscordSensorAPIException(DiscordSensorException):
    pass
