from channels.auth import AuthMiddleware
from channels.routing import ProtocolTypeRouter,URLRouter

import A_chatroom.routing

#instead of using urlpatters
#when we get a WS this is how to route it

application = ProtocolTypeRouter({
#since we want to use auth 
# we wrap urls in auth 
# to distinguish user
    'websocket':AuthMiddleware(
        URLRouter(
                A_chatroom.routing
        )
                               ),

})