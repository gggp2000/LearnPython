import functools

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text,func.__name__))
            func(*args,**kw)
            print('End Call %s():' % func.__name__)
        return wrapper
    return decorator

@log('Begin Call')
def now():
    print('2017-8-28')
                
