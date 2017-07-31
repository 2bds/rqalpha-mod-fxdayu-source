__config__ = {
    "source": "mongo",
    "mongo_url": "mongodb://127.0.0.1:27017",
    "bundle_path": None,
    "enable_cache": True,
    "cache_length": None,
    "max_cache_space": None,
    "priority": 200,
}


def load_mod():
    from .mod import FxdayuSourceMod
    return FxdayuSourceMod()
