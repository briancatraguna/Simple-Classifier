class BaseFactory:
    registry = {}

    @classmethod
    def register(cls, name):
        def inner_wrapper(wrapped_class):
            if name in cls.registry:
                raise ValueError(f"{wrapped_class.__name__} {name} already exists")
            cls.registry[name] = wrapped_class
            return wrapped_class
        return inner_wrapper

    @classmethod
    def create_instance(cls, name, **kwargs):
        if name not in cls.registry:
            raise ValueError(f"No {cls.__name__.lower()} registered for {name}")
        class_ = cls.registry[name]
        instance = class_(**kwargs)
        return instance
