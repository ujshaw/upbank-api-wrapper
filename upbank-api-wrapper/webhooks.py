from . import UP_ENDPOINT, session
import json


class AccountIDMissingError(Exception):
    pass

class Webhooks(self):
    """
    Webhooks
    ~~~~~~~~~~~~~~~~~~~~~
    Webhooks provide a mechanism for a configured URL to receive events when transaction activity occurs on Up. You can think of webhooks as being like push notifications for your server-side application.
    """  
    """
    list_webhooks = "/webhooks"
    create_webhook = "POST /webhooks"
    retrieve_webhook = "/webhooks/{id}"
    delete_webhook = "DELETE /webhooks/{id}"
    ping_webhook = "POST /webhooks/{webhookId}/ping"
    list_webhook_logs = "/webhooks/{webhookId}/logs"
    """      
    def __init__(self, pageSize=None, id=None, webhookID=None):
        """
        ``page[size] = integer``\n
        The number of records to return in each page.\n
        e.g. ?page[size]=30
        
        ``id = string``\n
        The unique identifier for the webhook.\n
        e.g. e5327e26-084f-41ed-842e-a538820ed155

        ``webhookId = string``\n
        The unique identifier for the webhook.\n
        e.g. ee77dad8-4213-40f3-a217-aed603477f64
        """
        if pageSize is None:
            self.webhooks_pagesize = None
        else:
            self.webhooks_pagesize = f"page[size]={pageSize}"
        if id is None:
            self.webhooks_id = None
        else:
            self.webhooks_id = f"{id}"
        if webhookID is None:
            self.webhooks_webhook_id is None
        else:
            self.webhooks_webhook_id = f"{webhookID}"

    def list_webhooks(self):
        """
        Retrieve a list of configured webhooks. The returned list is paginated and can be scrolled by following the next and prev links where present. Results are ordered oldest first to newest last.
        """
        if self.webhooks_pagesize:
            path = f""
            response = session.get(path)
            print(path)
            return response

        else:
            path = f""
            response = session.get(path)
            print(path)
            return response

    def create_webhook(self):
        """
        Create a new webhook with a given URL. The URL will receive webhook events as JSON-encoded POST requests. The URL must respond with a HTTP 200 status on success.

        There is currently a limit of 10 webhooks at any given time. Once this limit is reached, existing webhooks will need to be deleted before new webhooks can be created.

        Event delivery is retried with exponential backoff if the URL is unreachable or it does not respond with a 200 status. The response includes a secretKey attribute, which is used to sign requests sent to the webhook URL. It will not be returned from any other endpoints within the Up API. If the secretKey is lost, simply create a new webhook with the same URL, capture its secretKey and then delete the original webhook. See Handling webhook events for details on how to process webhook events.

        It is probably a good idea to test the webhook by sending it a PING event after creating it.
        """
        #POST
        pass

    def retrieve_webhook(self):
        """
        Retrieve a specific webhook by providing its unique identifier.
        """
        if self.webhooks_id:
            path = f""
            response = session.get(path)
            print(path)
            return response
        else:
            raise WebhooksIDMissingError(
                "Webhooks ID required for this request"
            )

    def delete_webhook(self):
        """
        Delete a specific webhook by providing its unique identifier. Once deleted, webhook events will no longer be sent to the configured URL.
        """
        if self.webhooks_id:
            path = f""
            response = session.get(path)
            print(path)
            return response
        else:
            raise WebhooksIDMissingError(
                "Webhooks ID required for this request"
            )

    def ping_webhook(self):
        """
        Send a PING event to a webhook by providing its unique identifier. This is useful for testing and debugging purposes. The event is delivered asynchronously and its data is returned in the response to this request.
        """
        if self.webhooks_webhook_id:
            path = f""
            response = session.get(path)
            print(path)
            return response
        else:
            raise WebhooksWebhookIDMissingError(
                "Webhooks Webhook ID required for this request"
            )

    def list_webhook_logs(self):
        """
        Retrieve a list of delivery logs for a webhook by providing its unique identifier. This is useful for analysis and debugging purposes. The returned list is paginated and can be scrolled by following the next and prev links where present. Results are ordered newest first to oldest last. Logs may be automatically purged after a period of time.
        """
        if self.webhooks_webhook_id:
            if self.webhooks_pagesize:
                path = f""
                response = session.get(path)
                print(path)
                return response
            else:
                path = f""
                response = session.get(path)
                print(path)
        else:
            raise WebhooksWebhookIDMissingError(
                "Webhooks Webhook ID required for this request"
            )

        