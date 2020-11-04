import mongoengine as me


class AccountInfo(me.EmbeddedDocument):
    mail = me.StringField(required=True)
    password = me.StringField(required=True)
    username = me.StringField(required=True)


class Measure(me.EmbeddedDocument):
    date = me.DateTimeField()
    weight = me.DecimalField()
    bmi = me.DecimalField()
    ffmi = me.DecimalField()
    fat_perc = me.DecimalField()


class Client(me.EmbeddedDocument):
    first_name = me.StringField(max_length=50)
    last_name = me.StringField(max_length=50)
    age = me.IntField()
    initial_weight = me.DecimalField()
    height = me.DecimalField()
    info = me.StringField(max_length=300)
    measures = me.ListField(me.EmbeddedDocumentField(Measure))


class User(me.Document):
    uuid = me.UUIDField(required=True)
    account_info = me.EmbeddedDocumentField(AccountInfo)
    client = me.EmbeddedDocumentField(Client)
    active = me.BooleanField(default=True)