def search(connection, search_value, search_type):
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
    if search_type == "name":
        result = connection.search(index='wiki', body={
            "query": {
                "match": {
                    "name": search_value}
            },
            "highlight" : {
                "pre_tags": ["<em>"],
                "post_tags": ["</em>"],
                "fields": {
                    "_all": {}
                }
            }
        })
    if search_type == "data":
        result = connection.search(index='wiki', body={
            "query": {
                "match": {
                    "data": search_value}
            },
            "highlight" : {
                "pre_tags": ["<em>"],
                "post_tags": ["</em>"],
                "fields": {
                    "_all": {}
                }
            }
        })    return result

