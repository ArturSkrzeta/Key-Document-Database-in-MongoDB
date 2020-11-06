import mongoengine as me

USER = 'artur'
PASSWORD = 'artur'
CLUSTER= 'newcluster'
DATABASE = 'company'
ALIAS = 'db'
DB_STRING = f'mongodb+srv://{USER}:{PASSWORD}@{CLUSTER}.4ybna.mongodb.net/{DATABASE}?retryWrites=true&w=majority'

class Clients(me.EmbeddedDocument):
    name = me.StringField()

    meta = {
        'db_alias': 'db',
        'collection': 'clients'
    }

    def to_json(self):
        return {
            'name': self.name,
        }


class Products(me.Document):
    name = me.StringField()
    price = me.FloatField()
    clients = me.EmbeddedDocumentListField(Clients) # to check if it's embedded automatically

    meta = {
        'db_alias': 'db',
        'collection': 'products'
    }

    def to_json(self):
        return {
            'name': self.name,
            'price': self.price
        }


def connect_to_db():
    me.connect(host=DB_STRING, alias=ALIAS)

def terminate_db():
    me.disconnect(alias=ALIAS)

def create_document(class_name, **kwargs):
    entity = class_name(**kwargs)
    entity.save()
    return entity

def count_documents(class_name):
    print(class_name.objects().count())


def main():

    connect_to_db()

    create_document(Clients, name="Important Company")
    create_document(Products, name="Phone", price="1999.99")

    count_documents(Clients)
    count_documents(Products)

    terminate_db()


if __name__ == '__main__':
    main()


### NOTES

# class name Products - collection name products

# in python there is prod.id
# in db prod document has _id

# state.py
# from client import Clients
# active_client: Clients = None
#
# program.py
# import state
# state.active_client = scv.create_client(...)



# def find_client_by_email(email: str) -> Clients:
#   client = Clients.objects(email=email).first()
#   return client




# class CLient(Document):
#   prod_ids = mongoengine.ListField()
#
# ...
#
#  client.prod_ids.append(prod.id)
