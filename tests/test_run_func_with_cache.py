# -*- coding: utf-8 -*-
import time
import pandas as pd

from rqalpha import run_func
from rqalpha.api import *
from rqalpha.utils.datetime_func import convert_int_to_datetime
from rqalpha.utils.logger import user_system_log

frequency = "1d"


def init(context):
    logger.info("init")
    context.s1 = "000002.XSHE"
    update_universe(context.s1)
    context.fired = False


def before_trading(context):
    pass


def handle_bar(context, bar_dict):
    print(context.now)
    # print(bar_dict[context.s1])
    # print(pd.DataFrame(history_bars(context.s1, 5, "1d", include_now=True)))
    array = history_bars(context.s1, 5, "1" + frequency[-1], skip_suspended=False, include_now=True)
    # print(array)
    data = pd.DataFrame(array)
    print(data)
    data.set_index(data["datetime"].map(convert_int_to_datetime), inplace=True)
    print(data)
    if not context.fired:
        # order_percent并且传入1代表买入该股票并且使其占有投资组合的100%
        order_percent(context.s1, 1)
        context.fired = True


config = {
    "base": {
        "start_date": "2015-12-17",
        "end_date": "2015-12-31",
        "accounts": {"stock": 100000},
        "frequency": frequency,
        "benchmark": None,
        "strategy_file": __file__
    },
    "extra": {
        "log_level": "verbose",
    },
    "mod": {
        "sys_analyser": {
            "enabled": True,
            # "report_save_path": ".",
            "plot": True
        },
        "sys_simulation": {
            "enabled": True,
            # "matching_type": "last"
        },
        "fxdayu_source": {
            "enabled": True,
            "source": "mongo",
            "mongo_url": "mongodb://192.168.0.101:27017",
            "enable_cache": True,
            "cache_length": 10000
        }
    }
}

config["mod"]["fxdayu_source"] = {
    "enabled": True,
    "source": "bundle",
    "enable_cache": True,
    "cache_length": 10000
}


start = time.time()
# 您可以指定您要传递的参数
run_func(init=init, before_trading=before_trading, handle_bar=handle_bar, config=config)
print("Time Cost: %s seconds" % (time.time() - start))
# 如果你的函数命名是按照 API 规范来，则可以直接按照以下方式来运行
# run_func(**globals())
