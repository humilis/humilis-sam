""" Dummy api backend to test SAM layer."""


def get(event, *args, **kwargs):
    """Test get path."""
    return {
            "statusCode": 200,
            "headers": {"response_status": "ok"},
            "body": "Get has been called"
           }


def put(event, *args, **kwargs):
    """Test put path."""
    return {
            "statusCode": 544,
            "headers": {"response_status": "YOLO"},
            "body": "Put has been called"
           }


def delete(event, *args, **kwargs):
    """Test delete path."""
    return {
            "statusCode": 504,
            "headers": {"yolo_header": "timeout"},
            "body": "Delete has been called"
           }
