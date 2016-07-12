import os
import json
from elasticsearch import Elasticsearch
import docx2txt


def index(path):
    """
    the function will iterate through a given folder and return a Json for each file
    :param path:
    :type path:
    :return:
    :rtype:
    """
    es = Elasticsearch([{'host': '10.0.0.2', 'port': 9677}])
    id = 0
    for i in os.listdir(path):
        if i.endswith(".docx"):
            id += 1
            file_path = path + "/" + i
            raw_doc = docx2txt.process(file_path)
            dic = {'path': file_path, 'doc': raw_doc}
            json_dict = json.dumps(dic)
            print json_dict
            es.index(index='wiki', doc_type="article", id=id, body=dic)
            print i


def main():
    index('/Users/rongolberg/PycharmProjects/Duck/DuckDuckGo/wiki')


if __name__ == '__main__':
    main()
