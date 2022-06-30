allowedIps = ['129.0.0.1', '127.0.0.1']
def allow_by_ip(view_func):
    def authorize(request, *args, **kwargs):
        user_ip = request.META['REMOTE_ADDR']
        for ip in allowedIps:
            if ip==user_ip:
                return view_func(request, *args, **kwargs)
        return HttpResponse('Invalid Ip Access!')
    return authorize