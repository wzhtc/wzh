from mongoengine import *
import datetime

connect(db='test', alias='test')


class Post(Document):
    title = StringField()
    subtitle = StringField()
    meta = StringField()
    postdate = DateTimeField(default=datetime.datetime.now)
    tags = ListField(StringField())
    url = StringField()
    fileid = StringField()

    meta = {'db_alias': 'test'}