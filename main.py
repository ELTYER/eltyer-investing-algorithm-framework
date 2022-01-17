import os

from investing_algorithm_framework import App, TimeUnit, AlgorithmContext, \
    TradingDataTypes
from investing_algorithm_framework.configuration.constants import BINANCE, \
    BINANCE_API_KEY, BINANCE_SECRET_KEY, TRADING_SYMBOL
from initializer import EltyerInitializer as Initializer
from order_executor import EltyerOrderExecutor as OrderExecutor
from portfolio_manager import EltyerPortfolioManager as PortfolioManager
from configuration.constants import ELTYER_API_KEY
dir_path = os.path.abspath(os.path.join(os.path.realpath(__file__), os.pardir))

# Create an application (manages your algorithm, rest api, etc...)
app = App(
    resources_directory=dir_path,
    config={
        BINANCE_API_KEY: "<BINANCE_API_KEY>",
        BINANCE_SECRET_KEY: "<BINANCE_SECRET_KEY>",
        TRADING_SYMBOL: "USDT",
        ELTYER_API_KEY: "<ELTYER_API_KEY>"
    }
)

app.algorithm.add_initializer(Initializer)
app.algorithm.add_order_executor(OrderExecutor)
app.algorithm.add_portfolio_manager(PortfolioManager)

if __name__ == "__main__":
    app.start()
