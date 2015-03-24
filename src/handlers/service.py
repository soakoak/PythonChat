# -*- coding: iso-8859-15 -*-
from environment import JINJA_ENVIRONMENT
from handlers.basehandler import BaseHandler
from utils.chat_utils import getMessages
from utils.utils import representsInt


class JsonDeliverer(BaseHandler):
    def get(self):
        self.response.headers["Content-Type"] = "text/html;charset=utf-8"
        
        delta = self.request.get( "delta", default_value = None )
        req_chat = self.request.get( "chat", default_value = None )
        stampf = self.request.get( "format", default_value = "%d-%m-%Y %H:%M" )
        
        if delta: 
            if not representsInt( delta ):
                delta = None
            else:
                delta = int( delta )
        
        messages = getMessages( req_chat, delta )
        
        """logging.info( u"Chätti = " + str( req_chat ) )
        logging.info( "Viestit = " + str( messages ))
        logging.info( "Ajan leimausformaatti = " + str( stampf ) )
        #"""
        template_values = {
            'msg_list' : messages,
            'timestmpf' : stampf            
        }
        
        template = JINJA_ENVIRONMENT.get_template('./messages.json')
        page = template.render(template_values) #"""
        self.response.out.write(page)