import mongoengine as me

class Clients(me.EmbeddedDocument):
    name = me.StringField()
