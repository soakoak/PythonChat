# -*- coding: iso-8859-15 -*-
from google.appengine.ext import ndb


class ChatMessage(ndb.Model):
    user = ndb.StringProperty(required=True)
    timestamp = ndb.DateTimeProperty(auto_now_add=True)
    message = ndb.TextProperty(required=True)
    chat = ndb.StringProperty(required=True)