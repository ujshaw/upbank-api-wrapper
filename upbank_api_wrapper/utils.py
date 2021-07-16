from . import UP_ENDPOINT, session


class Utils(self):
    """
    Utils
    ~~~~~~~~~~~~~~~~~~~~~
    Some endpoints exist not to expose data, but to test the API itself. Currently there is only one endpoint in this group: ping!
    """
    def __init__(self):
        pass

    def ping(self):
        """
        Make a basic ping request to the API. This is useful to verify that authentication is functioning correctly. On authentication success an HTTP 200 status is returned. On failure an HTTP 401 error response is returned.
        """
        pass