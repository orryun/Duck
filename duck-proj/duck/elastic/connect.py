from elasticsearch import Elasticsearch


def connect(host='10.0.0.2', port=9677):
    """
    the function will connect to a provided elastic search indexer
    :param host: ip of the elastic search host
    :type host: str
    :param port: port of the elastic search host
    :type port: int
    :return: elastic search object
    :rtype: Elasticsearch object
    """
    es = Elasticsearch([{'host': host, 'port': port}])
    return es
