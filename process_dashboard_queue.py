from exceptions import ShortRetryException


def process_property_message(message):
    try:
        articles._store_property(message.get('property_type'), message.get('name'), message.get('value'),
                                 message.get('item_identifier'), message.get('version'),
                                 message.get('message_id'))
    except ShortRetryException as e:
        #logging.info("Error processing property message: %s", message)
        raise ShortRetryException("Short retry: %s", e)
    except Exception:
        #logger.exception("Error processing property message: %s", message)