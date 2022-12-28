from functools import wraps
import inspect

"""
instance_variables

-----------------------------         ------------------------------                        
|def __init__(self, a, b):  |         | @instance_variables        |
|    self.a=a               |   ==>   | def __init__(self, a, b):  |
|    self.b=b               |         |     pass                   |
-----------------------------         ------------------------------ 

"""

def instance_variables(f):
    sig = inspect.signature(f)

    @wraps(f)
    def wrapper(self, *args, **kwargs):
        values = sig.bind(self, *args, **kwargs)
        for k, p in sig.parameters.items():
            if k != 'self':
                if k in values.arguments:
                    val = values.arguments[k]
                    if p.kind in (inspect.Parameter.POSITIONAL_OR_KEYWORD, inspect.Parameter.KEYWORD_ONLY):
                        setattr(self, k, val)
                    elif p.kind == inspect.Parameter.VAR_KEYWORD:
                        for k, v in values.arguments[k].items():
                            setattr(self, k, v)
                else:
                    setattr(self, k, p.default)
        
        f(self, *args, **kwargs)
    return wrapper
