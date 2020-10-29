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


class Recipe(me.Document):
    name = me.StringField(required=True, max_length=50)
    steps = me.ListField(me.StringField(max_length=300))


class Food(me.EmbeddedDocument):
    food = me.StringField(max_length=100)
    quantity = me.StringField(max_length=20)
    comments = me.StringField(max_length=200)


class Meal(me.EmbeddedDocument):
    moment = me.StringField(max_length=20)
    foods = me.ListField(me.EmbeddedDocumentField(Food))
    quantity = me.StringField(max_length=20)
    comments = me.StringField(max_length=200)


class Day(me.EmbeddedDocument):
    date = me.DateTimeField(required=True)
    meals = me.ListField(me.EmbeddedDocumentField(Meal))
    comments = me.StringField(max_length=200)


class Week(me.EmbeddedDocument):
    number = me.IntField()
    monday = me.EmbeddedDocumentField(Day)
    tuesday = me.EmbeddedDocumentField(Day)
    wednesday = me.EmbeddedDocumentField(Day)
    thursday = me.EmbeddedDocumentField(Day)
    friday = me.EmbeddedDocumentField(Day)
    saturday = me.EmbeddedDocumentField(Day)
    sunday = me.EmbeddedDocumentField(Day)


class Calendar(me.Document):
    users = me.ListField(me.ReferenceField(User))
    weeks = me.ListField(me.EmbeddedDocumentField(Week))

