from google.appengine.ext import ndb

class Film(ndb.Model):
    name = ndb.StringProperty()
    year = ndb.IntegerProperty()
    genre = ndb.StringProperty()
    rating = ndb.IntegerProperty()
    image = ndb.StringProperty()

