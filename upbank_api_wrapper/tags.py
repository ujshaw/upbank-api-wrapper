from . import UP_ENDPOINT, session
import json


class AccountIDMissingError(Exception):
    pass

class Tags(object):
    """
    Tags
    ~~~~~~~~~~~~~~~~~~~~~
    Tags are custom labels that can be associated with transactions on Up. Within the Up application, tags provide additional insight into spending. For example, you could have a "Take Away" tag that you apply to purchases from food delivery services. The Up API allows you to manage the tags associated with transactions. Each transaction may have up to 6 tags.
    
    Tags are identified by their labels, which are unique strings, so the tag "Holiday" has also the id "Holiday".
    """
    def __init__(self, pageSize=None, transactionID=None):
        """
        ``page[size] = integer``\n
        The number of records to return in each page.\n
        e.g. ?page[size]=50

        ``transactionId = string``\n
        The unique identifier for the transaction.\n
        e.g. bef487f7-3d02-4f2c-831e-a231d34be371
        """
        if pageSize is None:
            self.tags_pagesize = None
        else:
            self.tags_pagesize = f"page[size]={pageSize}"
        if id is None:
            self.transaction_id = None
        else:
            self.transaction_id = f"{transactionID}"

    def list_tags(self):
        """
        Retrieve a list of all tags currently in use. The returned list is paginated and can be scrolled by following the next and prev links where present. Results are ordered lexicographically. The transactions relationship for each tag exposes a link to get the transactions with the given tag.
        """
        if self.tags_pagesize:
            path = f"{UP_ENDPOINT}/tags?{self.tags_pagesize}"
            response = session.get(path)
            print(path)
            return response
        else:
            path = f"{UP_ENDPOINT}/tags"
            print(path)
            response = session.get(path)
            return response

    def add_tags(self):
        """
        Associates one or more tags with a specific transaction. No more than 6 tags may be present on any single transaction. Duplicate tags are silently ignored. An HTTP 204 is returned on success. The associated tags, along with this request URL, are also exposed via the tags relationship on the transaction resource returned from /transactions/{id}.
        """
        pass

    def remove_tags(self):
        """
        Disassociates one or more tags from a specific transaction. Tags that are not associated are silently ignored. An HTTP 204 is returned on success. The associated tags, along with this request URL, are also exposed via the tags relationship on the transaction resource returned from /transactions/{id}.
        """
        pass