import mongoengine as me
from models.user_model import User


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
    user = me.ReferenceField(User)
    weeks = me.ListField(me.EmbeddedDocumentField(Week))
