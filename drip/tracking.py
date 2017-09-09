"""
Utilities used to track
users and usage on app
"""


def tracking_string(uri, location):
    """
    Builds a string with the
    uri and location where 
    an action was taken
    """
    return f"URI {uri}, Location: {location}"