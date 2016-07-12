import os
import json
import docx2txt
from elastic import connect

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
            dic = {'name': file_path, 'data': raw_doc}
            json_dict = json.dumps(dic)
            print json_dict
            connection.index(index='wiki', doc_type="article", id=id, body=dic)
            print i


def main():
    connection = connect.connect()
    index(connection)

if __name__ == '__main__':
    main()