import sys
import inspect

if sys.version_info >= (3, 0):
    from functools import wraps


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

        return wrapper
else:
    def instance_variables(func):
        def return_func(*args, **kwargs):
            self_var = args[0]

            arg_spec = inspect.getargspec(func)
            argument_names = arg_spec[0][1:]
            defaults = arg_spec[3]
            if defaults is not None:
                default_arg_dict = dict(zip(reversed(argument_names), reversed(defaults)))
                self_var.__dict__.update(default_arg_dict)

            arg_dict = dict(zip(argument_names, args[1:]))
            self_var.__dict__.update(arg_dict)

            valid_keywords = set(kwargs) & set(argument_names)
            kwarg_dict = {k: kwargs[k] for k in valid_keywords}
            self_var.__dict__.update(kwarg_dict)

            func(*args, **kwargs)

        return return_func


def instance_variables(func):
    def return_func(*args, **kwargs):
        self_var = args[0]

        arg_spec = inspect.getargspec(func)
        argument_names = arg_spec[0][1:]
        defaults = arg_spec[3]
        if defaults is not None:
            default_arg_dict = dict(zip(reversed(argument_names), reversed(defaults)))
            self_var.__dict__.update(default_arg_dict)

        arg_dict = dict(zip(argument_names, args[1:]))
        self_var.__dict__.update(arg_dict)

        valid_keywords = set(kwargs) & set(argument_names)
        kwarg_dict = {k: kwargs[k] for k in valid_keywords}
        self_var.__dict__.update(kwarg_dict)

        func(*args, **kwargs)

    return return_func
