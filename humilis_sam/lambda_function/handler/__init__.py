"""Lambda function entry point."""

# preprocessor:jinja2

import logging

import lambdautils.utils as utils
import raven
from werkzeug.utils import import_string  # noqa

logger = logging.getLogger()


def produce_fct_callables():
    """Produces function callables for each endpoint."""
    if utils.in_aws_lambda():
        try:
            globs = dict(import_string=import_string, fct=None)
            exec(
                """
fct = [
    {% for f in meta_functions %}
    {
        {% for k, v in f.items() %}
        {% if k == 'fct' %}
        '{{k}}': '{{v or ''}}' and import_string('{{v}}'),
        {% else %}
        '{{k}}': '{{v or ''}}',
        {% endif %}
        {% endfor %}
    },
    {% endfor %}
]
            """, globs)
            return globs["fct"]
        except:
            logger.error("Unable to produce fct callables")
            dsn = utils.get_secret("sentry.dsn",
                                   environment="{{_env.name}}",
                                   stage="{{_env.stage}}")
            if not dsn:
                logger.error("Unable to retrieve Sentry DSN")
            else:
                client = raven.Client(dsn)
                client.captureException()
            # This is a critical error: must re-raise
            raise


def lambda_handler(event, context):
    """Lambda function."""
    if event.get("event_type", "") == "keep_warm":
        return event

    try:
        functions = produce_fct_callables()
    except Exception as exception:
        raise utils.CriticalError(exception)

    response = {}
    req_path = event.get("path", "")
    req_method = event.get("httpMethod", "").lower()
    for f in functions:
        if f["api_path"] == req_path and f["http_method"] == req_method:
            fct = f.get("fct")
            response = fct(event, context)

    if response:
        return response
    else:
        raise utils.CriticalError("Didn't find any function to process "
                                  "event '{}'" .format(event))
