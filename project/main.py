import mongoengine as me
from clients import Clients
from products import Products

USER = 'artur'
PASSWORD = 'artur'
CLUSTER= 'newcluster'
DATABASE = 'company'
ALIAS = 'db'
DB_STRING = f'mongodb+srv://{USER}:{PASSWORD}@{CLUSTER}.4ybna.mongodb.net/{DATABASE}?retryWrites=true&w=majority'

def connect_to_db():
    me.connect(host=DB_STRING, alias=ALIAS)

def terminate_db():
    me.disconnect(alias=ALIAS)

def create_document(class_name, **kwargs):
    object = class_name(**kwargs)
    try:
        object.save()
    except:
        pass
    return object

def count_documents(class_name):
    print(class_name.objects().count())


def main():

    connect_to_db()

    client1 = create_document(Clients, name="Important Company")
    client2 = create_document(Clients, name="Small Company")
    product1 = create_document(Products, name="TV", price="6999.99", clients=[client1,client2])

    count_documents(Products)
    terminate_db()

if __name__ == '__main__':
    main()
