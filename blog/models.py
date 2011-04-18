#from django.db import models
from mongoengine import *
# Create your models here.

class User(Document):
    name = StringField()
    nick_name = StringField()
    password = StringField()


class EmbedComment(EmbeddedDocument):
    user = ReferenceField(User)
    content = StringField()
    created_at = DateTimeField()

class Blog(Document):
    title = StringField()
    content = StringField()
    created_at = DateTimeField()
    comments = ListField(EmbeddedDocumentField(EmbedComment))

class Author(EmbeddedDocument):
    name = StringField()

class PaintingComment(EmbeddedDocument):
    user_id = ObjectIdField()
    nick_name = StringField()
    content = StringField()
    time = DateTimeField()

class Scorer(EmbeddedDocument):
    user_id = ObjectIdField()
    nick_name = StringField()
    grade = IntField()

class Painting(Document):
    name = StringField()
    author = EmbeddedDocumentField(Author)
    join_time = DateTimeField()
    end_time = DateTimeField()
    rating = FloatField()
    tee_count = IntField()
    sweater_count = IntField()
    comments = ListField(EmbeddedDocumentField(PaintingComment))
    scorer = ListField(EmbeddedDocumentField(Scorer))

class MerchandisePainting(EmbeddedDocument):
    painting_id = ObjectIdField()
    painting_name = StringField()
    author_id = ObjectIdField()
    author_name = StringField()

class MerchandiseSubClass(EmbeddedDocument):
    subclass_id = ObjectIdField()
    subclass_name = StringField()
    gender = IntField()
    color = IntField()
    style = IntField()
    s_left_count = IntField()
    m_left_count = IntField()
    l_left_count = IntField()
    xl_left_count = IntField()
    xxl_left_count = IntField()
    xxxl_left_count = IntField()
    original_price = FloatField()
    sell_price = FloatField()
    vip_price = FloatField()
    special_price = FloatField()

class Merchandise(Document):
    name = StringField()
    catalog = IntField()
    trade_mark = StringField()
    sn = IntField()
    detail = StringField()
    join_time = DateTimeField()
    painting = EmbeddedDocumentField(MerchandisePainting)
    subclass = EmbeddedDocumentField(MerchandiseSubClass)
    rank0_count = IntField()
    rank1_count = IntField()
    rank2_count = IntField()
    rank3_count = IntField()
    rank4_count = IntField()
    rank5_count = IntField()
    scorers = ListField(EmbeddedDocumentField(Scorer))
    
    