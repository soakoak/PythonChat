# -*- coding: iso-8859-15 -*-
from google.appengine.ext.webapp.util import run_wsgi_app
import webapp2

from handlers.form_handlers import ChatRoomPoster
from handlers.service import JsonDeliverer
from handlers.tchat import GenericChatPage


if __name__ == "__main__":
    routes = [
      ('/', GenericChatPage),
      ('/talk', ChatRoomPoster),
      ('/enterchat', GenericChatPage),
      ('/query', JsonDeliverer )
    ]
    # http://webapp-improved.appspot.com/api/webapp2_extras/sessions.html
    config = {}
    config['webapp2_extras.sessions'] = {
                 'secret_key': 'apina&gorilla-torilla',
    }
    run_wsgi_app( webapp2.WSGIApplication( routes, False, config ) )