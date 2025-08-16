handlers = []

def register_handler(
    filters,
    group=0,
    handler_type="on_message",
):
    def decorator(func):
        handlers.append({
            "function": func,
            "filters": filters,
            "group": group,
            "type": handler_type,
        })
        return func
    return decorator
