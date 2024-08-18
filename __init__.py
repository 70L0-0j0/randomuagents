"""
UA Module

This module provides the UA class to fetch random user agents.

Usage:
    import randomuagents

    ua_instance = randomuagents.UA("desktop")
    random_ua = ua_instance._uGet()
    print(random_ua)

Class UA:
    This class allows fetching random user agents based on the specified type.

    Attributes:
        ua_type (str): The type of user agent desired ("desktop", "mobile", etc.).

    Methods:
        _uGet():
            Returns a random user agent of the specified type.

Example:
    ua_instance = UA("desktop")
    random_ua = ua_instance._uGet()
    print(random_ua)
"""

from randomuagents._d import ua
class UA():
    """
    UA Class

    Allows fetching random user agents based on the specified type.

    Attributes:
        ua_type (str): The type of user agent desired ("desktop", "mobile", etc.).
    """

    def __init__(self, ua_type=None):
        """
        Initializes an instance of the UA class.

        Parameters:
            ua_type (str, optional): The type of user agent desired ("desktop", "mobile", etc.). Defaults to None.
                                     If None, ua_type will be randomly selected.
        """
        self.ua_type = ua_type

    def _uGet(self):
        """
        Returns a random user agent of the specified type.

        Returns:
            str: A random user agent.
        """
        return ua(self.ua_type)
