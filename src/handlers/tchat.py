# -*- coding: iso-8859-15 -*-
import logging

from environment import JINJA_ENVIRONMENT, CHATS
from handlers.basehandler import BaseHandler
from utils.chat_utils import defaultParams, getMessages


def mdate(requested_chat):
        template_values = defaultParams("Counted-room", requested_chat)
        template_values['msg_list'] = getMessages()
        template = JINJA_ENVIRONMENT.get_template('count.html')
        return template.render(template_values)
    
def error(requested_chat):
    return render_template('error.html', "404", requested_chat)

def mchat(requested_chat):
    return render_template('multichat.html', CHATS[ requested_chat ], requested_chat, True)

def landing(requested_chat):
    return render_template('landing.html', 'Aula')

#START: GenericChat
class GenericChatPage(BaseHandler):
    options = {
               'None' : landing,
               'error' : error,
               'mdate' : mdate,
               'book' : mchat,
               'main' : mchat,
               'games' : mchat
               }
            
    def get(self):
        self.response.headers["Content-Type"] = "text/html;charset=utf-8"
        requested_chat = self.request.get("chat", default_value=None)
        """    
        logging.info( u"Chätti = " + str( requested_chat ) )
        logging.info( "boolean tulos = " + str( ( str( requested_chat ) != 'None' ) and ( requested_chat not in CHATS ) ))
        #"""    
        #unicode kettuilee: u'None' - http://stackoverflow.com/a/9310951
        if ( str( requested_chat ) != 'None' ) and ( requested_chat not in CHATS ):
            logging.info( "Boom" )
            requested_chat = 'error'

        page = self.options[ str( requested_chat ) ]( str(  requested_chat ) )      

        self.response.out.write(page)
#END: GenericChat

def render_template(temp_path, title, requested_chat=None, room_spec_msgs=False):
        template_values = defaultParams(title, requested_chat)
        if room_spec_msgs:
            template_values['msg_list'] = getMessages(chat = requested_chat)
        else:
            template_values['msg_list'] = getMessages()
        template = JINJA_ENVIRONMENT.get_template(temp_path)
        return template.render(template_values)