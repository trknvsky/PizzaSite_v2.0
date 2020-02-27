from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect
import time
from ipware.ip import get_ip
from django.contrib.auth import authenticate, login, logout


class LogOutMiddleware(MiddlewareMixin):

    def process_request(self, request):
        if request.user.is_authenticated and request.session.get('last_request'):
            counter = time.time() - request.session['last_request']
            if counter > 60:
                del request.session['last_request']
                logout(request)
        request.session['last_request'] = time.time()


# class MyStopBotMiddleware(MiddlewareMixin):

#     def process_request(self, request):
#         requests_count = request.session.get('requests_count')
#         time_now = request.session.get('time_now')

        # if 'media/' in request.path:
        #     return

#         if not requests_count:
#             request.session['requests_count'] = 1
#         else:
#             request.session['requests_count'] += 1

#         if request.session.get('requests_count') > 120 and request.path != '/stop_spam':
#             return redirect('/stop_spam')

#         if not request.session['time_now']:
#             request.session['time_now'] = int(time.time())

#         if request.session['time_now'] + 20 < int(time.time()):
#             request.session['requests_count'] = 0
#             request.session['time_now'] = int(time.time())

#         print(requests_count)

#         ip = get_ip(request, right_most_proxy=True)
#         print(ip)

#         def process_response(self, request, response):
#             print('process_response')
#             return response
