__config__ = {
    "mongo_url": "mongodb://127.0.0.1:27017",
    "enable_cache": False,
    "cache_length": None,
    "max_cache_space": None,
    "priority": 200,
}


def load_mod():
    from .mod import MongoDataMod
    return MongoDataMod()
