from . import UP_ENDPOINT, session
import json


class AccountIDMissingError(Exception):
    pass

class Transactions(self):
    """
    Transactions
    ~~~~~~~~~~~~~~~~~~~~~
    Transactions represent the movement of money into and out of an account. They have many characteristics that vary depending on the kind of transaction. Transactions may be temporarily HELD (pending) or SETTLED, typically depending on which payment method was used at the point of sale.
    """   
    def __init__(self, pageSize=None, filterStatus=None, filterSince=None, filterUntil=None, filterCategory=None, filterTag=None, transactionID=None, accountID=None):
        """
        ``page[size] = integer``\n
        The number of records to return in each page.\n
        e.g. ?page[size]=30
        
        ``filter[status] = string``\n
        The transaction status for which to return records. This can be used to filter HELD transactions from those that are SETTLED.\n
        e.g. ?filter[status]=HELD

        ``filter[since] = string``\n
        The start date-time from which to return records, formatted according to rfc-3339. Not to be used for pagination purposes.\n
        e.g. ?filter[since]=2020-01-01T01:02:03+10:00

        ``filter[until] = string``\n
        The end date-time up to which to return records, formatted according to rfc-3339. Not to be used for pagination purposes.\n
        e.g. ?filter[until]=2020-02-01T01:02:03+10:00

        ``filter[category] = string``\n
        The category identifier for which to filter transactions. Both parent and child categories can be filtered through this parameter. Providing an invalid category identifier results in a 404 response.\n
        e.g. ?filter[category]=good-life

        ``filter[tag] = string``\n
        A transaction tag to filter for which to return records. If the tag does not exist, zero records are returned and a success response is given.\n
        e.g. ?filter[tag]=Holiday
        """

    def list_transactions(self):
        """
        Retrieve a list of all transactions across all accounts for the currently authenticated user. The returned list is paginated and can be scrolled by following the next and prev links where present. To narrow the results to a specific date range pass one or both of filter[since] and filter[until] in the query string. These filter parameters should not be used for pagination. Results are ordered newest first to oldest last.
        """
        pass

    def retrieve_transaction(self):
        """
        Retrieve a specific transaction by providing its unique identifier.
        """
        pass

    def list_transactions_by_account(self):
        """
        Retrieve a list of all transactions for a specific account. The returned list is paginated and can be scrolled by following the next and prev links where present. To narrow the results to a specific date range pass one or both of filter[since] and filter[until] in the query string. These filter parameters should not be used for pagination. Results are ordered newest first to oldest last.
        """
        pass