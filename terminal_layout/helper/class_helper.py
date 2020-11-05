import sys
import inspect

if sys.version_info >= (3, 0):
    from functools import wraps


    def instance_variables(f):
        """
        Decorator to define a function as a class.

        Args:
            f: (todo): write your description
        """
        sig = inspect.signature(f)

        @wraps(f)
        def wrapper(self, *args, **kwargs):
            """
            Wrapper around the given a function with the wrapped in - place.

            Args:
                self: (todo): write your description
            """
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
        """
        Decorator for a function call. func.

        Args:
            func: (todo): write your description
        """
        def return_func(*args, **kwargs):
            """
            Return a dictionary of the function func.

            Args:
            """
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
    """
    Decorator for a function call. func.

    Args:
        func: (todo): write your description
    """
    def return_func(*args, **kwargs):
        """
        Return a dictionary of the function func.

        Args:
        """
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
