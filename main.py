import os

from investing_algorithm_framework import TimeUnit, AlgorithmContext, \
    TradingDataTypes
from investing_algorithm_framework.configuration.constants import BINANCE

from setup import create_app

dir_path = os.path.abspath(os.path.join(os.path.realpath(__file__), os.pardir))

app = create_app(
    resources_directory=dir_path,
)


@app.algorithm.strategy(
    time_unit=TimeUnit.SECONDS,
    interval=5,
    data_provider_identifier=BINANCE,
    target_symbol="BTC",
    trading_data_type=TradingDataTypes.TICKER,
)
def perform_strategy(context: AlgorithmContext, ticker):
    # order = context.create_limit_buy_order(
    #     symbol="BTC",
    #     price=10,
    #     amount=1,
    #     execute=True,
    # )
    portfolio = context.get_portfolio()
    print(context.get_orders())
    print(context.get_positions())


if __name__ == "__main__":
    app.start()
