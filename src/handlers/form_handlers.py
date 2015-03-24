# -*- coding: iso-8859-15 -*-
from google.appengine.api import users

from environment import CHATS
from models.chatmessage import ChatMessage
from handlers.basehandler import BaseHandler


#START: ChatRoomPoster
class ChatRoomPoster(BaseHandler):
    def post(self):
        user = users.get_current_user()
        msgtext = self.request.get("message")
        chat = self.request.get("chat")

        if user and chat in CHATS:
            msg = ChatMessage( user = user.nickname(), message = msgtext, chat = CHATS[ chat ] )
            msg.put() 
        self.redirect('/enterchat?chat=%s' % chat)
    
    def get(self):
        self.redirect('/')    
#END: ChatRoomPoster