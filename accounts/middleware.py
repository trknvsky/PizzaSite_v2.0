from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect
from tracking.models import Visitor
from tracking.utils import get_ip_address


class VisitorIpMiddleware(MiddlewareMixin):

    cache_users = {}

    def process_request(self, request):
        if 'media/' in request.path:
            return
        ip_address = get_ip_address(request)
        user = request.user
        ips = request.session.get('ips')
        session_key = request.session.session_key
        user_agent = request.META.get('HTTP_USER_AGENT', None)
        visitor = Visitor(pk=session_key, ip_address=ip_address, user=user, user_agent=user_agent)
        if not self.cache_users.get(visitor.user.email):
            self.cache_users[visitor.user.email] = visitor.ip_address
            print(self.cache_users)
        if self.cache_users[visitor.user.email] != visitor.ip_address:
            print('ВХОД С ДРУГОГО УСТРОЙСТВА:\n', visitor.user_agent, '\nIP: ', visitor.ip_address)

