import mongoengine as me

class Products(me.Document):
    name = me.StringField()
    price = me.FloatField()
    clients = me.ListField(me.EmbeddedDocumentField(Clients)) # to check if it's embedded automatically

    meta = {
        'db_alias': 'db',
        'collection': 'products'
    }

    def to_json(self):
        return {
            'name': self.name,
            'price': self.price
        }
