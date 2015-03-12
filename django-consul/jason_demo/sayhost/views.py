from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
import threading

lock = threading.Lock()
_count = 1

def count_up():
    global lock
    lock.acquire()

    global _count
    _count = _count + 1

    lock.release()

def get_count():
    global _count
    count = _count
    return count

def index(request):
    import socket
    import pytz
    from datetime import datetime

    host_name = socket.gethostname()
    template = loader.get_template('index.html')
    now = datetime.now(pytz.timezone('Asia/Tokyo'))
    now_str = now.strftime("%Y/%m/%d %H:%M:%S")
    context = RequestContext(request, {
        'host_name': host_name,
        'now': now_str,
        'count': get_count()
    })

    count_up()

    return HttpResponse(template.render(context))
