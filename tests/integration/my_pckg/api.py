""" Dummy api backend to test SAM layer."""


def get(event, *args, **kwargs):
    """Test get path."""
    return {"body": "Get has been called"}


def put(event, *args, **kwargs):
    """Test put path."""
    return {"body": "Put has been called"}


def delete(event, *args, **kwargs):
    """Test delete path."""
    return {"body": "Delete has been called"}
