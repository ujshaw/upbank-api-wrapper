from . import UP_ENDPOINT, session
import json


class CategoriesIDMissingError(Exception):
    pass

class Categories(object):
    """
    Categories
    ~~~~~~~~~~~~~~~~~~~~~
    Categories enable understanding where your money goes by driving powerful insights in Up. All categories in Up are pre-defined and are automatically assigned to new purchases in most cases. A parent-child relationship is used to represent categories, however parent categories cannot be directly assigned to transactions.
    """
    def __init__(self, filter=None, id=None):
        """
        ``filter[parent] = string``\n
        The unique identifier of a parent category for which to return only its children. Providing an invalid category identifier results in a 404 response.\n
        e.g. ?filter[parent]=good-life

        ``id = string``\n
        The unique identifier for the category.\n
        e.g. restaurants-and-cafes
        """
        if filter is None:
            self.categories_filter = None
        else:
            self.categories_filter = f"filter[parent]={filter}"
        if id is None:
            self.categories_id = None
        else:
            self.categories_id = f"{id}"

    def list_categories(self):
        """
        Retrieve a list of all categories and their ancestry. The returned list is not paginated.
        """
        if self.categories_filter:
            path = f"{UP_ENDPOINT}/categories?{self.categories_filter}"
            response = session.get(path)
            print(path)
            return response
        else:
            path = f"{UP_ENDPOINT}/categories"
            response = session.get(path)
            print(path)
            return response

    def retrieve_categories(self):
        """
        Retrieve a specific category by providing its unique identifier.
        """
        if self.categories_id:
            path = f"{UP_ENDPOINT}/accounts/{self.categories_id}"
            response = session.get(path)
            print(path)
            return response
        else:
            raise CategoriesIDMissingError(
                "Categories ID required for this request"
            )