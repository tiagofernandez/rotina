def get_or_none(model, **kwargs):
    try:
        return model.objects.get(**kwargs)
    except model.DoesNotExist:
        return None

def get_attr_or_none(model, attr, **kwargs):
    try:
        instance = model.objects.get(**kwargs)
        if hasattr(instance, attr):
            return getattr(instance, attr)
    except model.DoesNotExist:
        pass
    return None
