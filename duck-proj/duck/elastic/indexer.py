import os
import json
from elasticsearch import Elasticsearch
import docx2txt

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


def index(connection, path='/Users/rongolberg/PycharmProjects/Duck/DuckDuckGo/wiki'):
    """
    the function will index a folder of docs in the provided elastic search host ip and port
    :param connection: the host connection
    :type connection: Elasticsearch object
    :param path: path we want to index
    :type path: str
    :return: None
    :rtype: None
    """
    id = 0
    for i in os.listdir(path):
        if i.endswith(".docx"):
            id += 1
            file_path = path + "/" + i
            raw_doc = docx2txt.process(file_path)
            dic = {'path': file_path, 'doc': raw_doc}
            json_dict = json.dumps(dic)
            print json_dict
            connection.index(index='wiki', doc_type="article", id=id, body=dic)
            print i
