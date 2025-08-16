def with_context(func):
    def binder(ctx):
        def wrapped(*args, **kwargs):
            return func(ctx, *args, **kwargs)
        return wrapped
    return binder
