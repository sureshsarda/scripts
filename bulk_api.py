import string
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk, streaming_bulk
import random
import time

def get_es_client(hosts=['127.0.0.1:9200']):
    return Elasticsearch(hosts=hosts)


def generate_doc(count=10):
    """
    Creates a document with random username, random salary amount, random profession and a date of birth
    :param count: number of documents to return 
    :return: generator object for user documents
    """

    def generate_username():
        return ''.join(random.choice(string.ascii_lowercase) for _ in range(10))

    def generate_profession():
        return random.choice(['Accountant', 'Doctor', 'Engineer', 'Realtor', 'Writer'])

    def generate_user_doc():
        return dict(
            username=generate_username(),
            profession=generate_profession(),
            salary=random.randint(1000, 100000)
        )

    random.seed(33)

    for i in range(count):
        yield generate_user_doc()


def process_document(document):
    # No processing currently
    return document


def create_bulk_api_query(document_generator, index, type, action='index'):
    for doc in document_generator:
        d = dict(
            _op_type=action,
            _index=index,
            _type=type,
            _source=doc
        )
        #        yield json.dumps(d, default=date_handler)
        yield d


def insert_bulk(client, documents, index, type):
    success, failed = bulk(client, create_bulk_api_query(documents, index=index, type=type))
    print("Success: {success}, Failed: {failed}".format(success=success, failed=failed))


def insert_one_by_one(client, documents, index, type):
    for item in documents:
        client.index(body=item, index=index, doc_type=type)


if __name__ == '__main__':
    es_client = get_es_client()

    # Generally, bulk API's are used where we have something generating the data, we need to process the data in some
    # way and then store it
    # Steps:
    # 1. Fetch phase ( a data generator that will create data, it should emit documents)
    # 2. Processing ( change structure of document)
    # 3. Create bulk API query
    #   a. Update the document to include index and other information required by bulk API
    # 4. Call

    index = 'dummy'
    type = 'users'

    print('Deleting index...')
    response = es_client.indices.delete(index=index, ignore=[400, 401])
    print(response)

    documents = generate_doc(100000)

    start = time.time()
    insert_one_by_one(es_client, documents, index, type)
    end = time.time()

    print(end - start)

