import os

from investing_algorithm_framework import TimeUnit, AlgorithmContext, \
    TradingDataTypes
from investing_algorithm_framework.configuration.constants import BINANCE

from eltyer_investing_algorithm_framework.setup import create_app

dir_path = os.path.abspath(os.path.join(os.path.realpath(__file__), os.pardir))

app = create_app(
    resources_directory=dir_path,
    key="cbnu5EUlzF3empnASvYvQzTwSsiQTiAXiKIvDvT7ZLM3wXhYhaG2vTAlKFL4tNYn"
)


@app.algorithm.strategy(
    time_unit="SECOND",
    interval=5,
    market=BINANCE,
    target_symbol="BTC",
)
def perform_strategy(context: AlgorithmContext, ticker):
    print("Running my strategy")


if __name__ == "__main__":
    app.start()