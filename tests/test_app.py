import os
from unittest import TestCase

from investing_algorithm_framework.core.workers import Strategy
from investing_algorithm_framework import TradingDataTypes, TradingTimeUnit, \
    AlgorithmContext
from eltyer_investing_algorithm_framework import create_app


class StrategyOne(Strategy):
    has_ohlcv_data = False
    has_ohlcvs_data = False
    has_ticker_data = False
    has_tickers_data = False
    has_order_book_data = False
    has_order_books_data = False
    has_orders = False
    has_positions = False
    has_unallocated = False

    def __init__(self):
        super(StrategyOne, self).__init__(
            worker_id="strategy_one",
            trading_symbol="usdt",
            trading_data_types=[
                TradingDataTypes.OHLCV,
                TradingDataTypes.TICKER,
                TradingDataTypes.ORDER_BOOK
            ],
            target_symbols=["BTC", "DOT"],
            market="BINANCE",
            limit=100,
            trading_time_unit=TradingTimeUnit.ONE_DAY
        )

    def apply_strategy(
        self,
        context: AlgorithmContext,
        ticker=None,
        tickers=None,
        order_book=None,
        order_books=None,
        ohlcv=None,
        ohlcvs=None,
        **kwargs
    ):

        if ohlcv is not None:
            StrategyOne.has_ohlcv_data = True

        if ohlcvs is not None:
            StrategyOne.has_ohlcvs_data = True

        if ticker is not None:
            StrategyOne.has_ticker_data = True

        if tickers is not None:
            StrategyOne.has_tickers_data = True

        if order_book is not None:
            StrategyOne.has_order_book_data = True

        if order_books is not None:
            StrategyOne.has_order_books_data = True

        orders = context.get_orders()

        if orders is not None:
            StrategyOne.has_orders = True

        positions = context.get_positions()

        if len(positions) > 0:
            StrategyOne.has_positions = True

        unallocated = context.get_unallocated()

        if unallocated.get_amount() > 0:
            StrategyOne.has_unallocated = True

    @staticmethod
    def reset():
        StrategyOne.has_ohlcv_data = False
        StrategyOne.has_ohlcvs_data = False
        StrategyOne.has_ticker_data = False
        StrategyOne.has_tickers_data = False
        StrategyOne.has_order_book_data = False
        StrategyOne.has_order_books_data = False
        StrategyOne.has_orders = False
        StrategyOne.has_positions = False
        StrategyOne.has_unallocated = False


class Test(TestCase):
    resources_dir = os.path.join(
        os.path.abspath(os.path.dirname(__file__)), 'resources'
    )

    def setUp(self) -> None:
        self.app = create_app(
            resource_directory=Test.resources_dir,
            key="cbnu5EUlzF3empnASvYvQzTwSsiQTiAXiKIvDvT7ZLM3wXhYha"
                "G2vTAlKFL4tNYn"
        )

    def tearDown(self) -> None:
        self.app.reset()

    def test_stateless_check_online(self):
        response = self.app.start(
            stateless=True, payload={"action": "CHECK_ONLINE"}
        )
        self.assertEqual(response["statusCode"], 200)

        response = self.app.start(
            stateless=True, payload={"ACTION": "CHECK_ONLINE"}
        )
        self.assertEqual(response["statusCode"], 200)

    def test_stateless_run_strategy(self):
        self.app.algorithm.add_strategy(StrategyOne)
        self.app.start(stateless=True, payload={"action": "RUN_STRATEGY"})

        self.assertTrue(StrategyOne.has_ohlcvs_data)
        self.assertFalse(StrategyOne.has_ohlcv_data)
        self.assertTrue(StrategyOne.has_order_books_data)
        self.assertFalse(StrategyOne.has_order_book_data)
        self.assertTrue(StrategyOne.has_tickers_data)
        self.assertFalse(StrategyOne.has_ticker_data)
        self.assertTrue(StrategyOne.has_orders)
        self.assertTrue(StrategyOne.has_positions)
        self.assertTrue(StrategyOne.has_unallocated)
