import wrapt


def cache_function(key=None, timeout=None, alias="default"):
    """
    低粒度缓存：缓存函数返回值
    :param key: 键
    :param timeout: 超时时间
    :param alias: 缓存配置
    """

    @wrapt.decorator
    def wrapper(wrapped, instance, args, kwargs):
        from django.core.cache import caches
        client = caches[alias]
        value = client.get(key)
        if not value:
            value = wrapped(*args, **kwargs)
            client.set(key, value, timeout)
        return value

    return wrapper
