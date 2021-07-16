from . import UP_ENDPOINT, session 
import json


class AccountIDMissingError(Exception):
    pass

class Accounts(object):
    """
    Accounts
    ~~~~~~~~~~~~~~~~~~~~~
    Accounts represent the underlying store used to track balances and the transactions that have occurred to modify those balances over time. Up currently has two types of account: SAVER—used to earn interest and to hit savings goals, and TRANSACTIONAL—used for everyday spending.
    """
    def __init__(self, pageSize=None, id=None):
        """
        ``page[size] = integer``\n
        The number of records to return in each page.\n
        e.g. ?page[size]=30

        ``id = string``\n
        The unique identifier for the account.\n
        e.g. cf840ed9-b393-4d06-b445-88362b1c4a83
        """
        if pageSize is None:
            self.accounts_pagesize = None
        else:
            self.accounts_pagesize = f"page[size]={pageSize}"
        if id is None:
            self.accounts_id = None
        else:
            self.accounts_id = f"{id}"

    def list_accounts(self):
        """
        Retrieve a paginated list of all accounts for the currently authenticated user. The returned list is paginated and can be scrolled by following the prev and next links where present.
        """
        if self.accounts_pagesize:
            path = f"{UP_ENDPOINT}/accounts?{self.accounts_pagesize}"
            response = session.get(path)
            print(path)
            return response
        else:
            path = f"{UP_ENDPOINT}/accounts"
            print(path)
            response = session.get(path)
            return response

    def retrieve_accounts(self):
        """
        Retrieve a specific account by providing its unique identifier.
        """
        if self.accounts_id:
            path = f"{UP_ENDPOINT}/accounts/{self.accounts_id}"
            response = session.get(path)
            print(path)
            return response
        else:
            raise AccountIDMissingError(
                "Account ID required for this request"
            )