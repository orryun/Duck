def search_name(connection, search_value):
    """
    the function will search for the provided value in the given elastic search object connection
    :param connection: the host connection
    :type connection: Elasticsearch object
    :param search_value: value we want to find
    :type search_value: str
    :param search_type: type of search (doc\path)
    :type search_type: str
    :return: result
    :rtype: JSON
    """
    result = connection.search(index='wiki', body={
        "query": {
            "match": {
                "name": search_value
            }
        },
        "highlight": {
            "pre_tags": ["<em>"],
            "post_tags": ["</em>"],
            "fields": {
                "name": {}
            }
        }
    })
    return result


def search_data(connection, search_value):
    """
    the function will search for the provided value in the given elastic search object connection
    :param connection: the host connection
    :type connection: Elasticsearch object
    :param search_value: value we want to find
    :type search_value: str
    :param search_type: type of search (doc\path)
    :type search_type: str
    :return: result
    :rtype: JSON
    """
    result = connection.search(index='wiki', body={
        "query": {
            "match": {
                "data": search_value
            }
        },
        "highlight": {
            "pre_tags": ["<em>"],
            "post_tags": ["</em>"],
            "fields": {
                "data": {}
            }
        }
    })
    return result


def autocomplete(connection, search_value):
    """
    the function will autocomplete for the provided value in the given elastic search object connection
    :param connection: the host connection
    :type connection: Elasticsearch object
    :param search_value: value we want to find
    :type search_value: str
    :param search_type: type of search (doc\path)
    :type search_type: str
    :return: result
    :rtype: JSON
    """
    result = connection.search(index='wiki', body={
        "data-suggest": {
            "text": search_value,
            "completion": {
                "field": "suggest"
            }
        }
    })
    return result

