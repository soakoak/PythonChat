# -*- coding: iso-8859-15 -*-
import datetime
import operator

from google.appengine.api import users

from environment import CHATS
from models.chatmessage import ChatMessage
from oma_tzinfo import UTC_tzinfo, EE_tzinfo


def msg2EE(messages):
    for msg in messages:
        msg.timestamp = msg.timestamp.replace(tzinfo=UTC_tzinfo())
        msg.timestamp = msg.timestamp.astimezone(EE_tzinfo())
    return messages
        
def getMessages(chat = None, deltatime = None):
    messages = ChatMessage.query()
    
    if chat:
        messages = messages.filter( ChatMessage.chat == CHATS[ chat ] )
        
    if deltatime:
        c_time = datetime.datetime.now() - datetime.timedelta(minutes=deltatime)
        messages = messages.filter( ChatMessage.timestamp >= c_time )
                  
    messages = messages.order( -ChatMessage.timestamp ).fetch ( 20 )                     
    return msg2EE(messages)

def defaultParams(chat_name, requested_chat = None):
    template_values = {
        'requested_chat': requested_chat,
        'chatname': chat_name,
        #'title': chat_name,
        # http://stackoverflow.com/a/613218
        'chats': sorted( CHATS.iteritems(), key=operator.itemgetter(1) ),
        'now': datetime.datetime.now()
    }   
    
    if users.get_current_user():
        template_values['user'] = users.get_current_user().nickname()
        template_values["url_text"] = 'Logout'
        template_values["url"] = users.create_logout_url('/')
    else:
        template_values['user'] = None
        template_values["url_text"] = "Login"
        template_values["url"] = users.create_login_url('/')
    
    return template_values