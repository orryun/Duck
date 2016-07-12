import os
import json
from elasticsearch import Elasticsearch
import docx2txt


def connect(host='10.0.0.2', port=9677):
    """
    :param host:
    :type host:
    :param port:
    :type port:
    :return:
    :rtype:
    """
    es = Elasticsearch([{'host': host, 'port': port}])
    return es


def search(connection, search_value, search_type):
    """
    :param connection:
    :type connection:
    :param search_value:
    :type search_value:
    :return:
    :rtype:
    """
    if search_type == "path":
        result = connection.search(index='wiki', body={"query": {"match": {"path": search_value}}})
    if search_type == "doc":
        result = connection.search(index='wiki', body={"query": {"match": {"doc": search_value}}})
    return result

def main():
    connection = connect()
    result = search(connection, search_value, )

if __name__ == '__main__':
    main()
