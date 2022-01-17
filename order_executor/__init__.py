import logging

from investing_algorithm_framework import OrderExecutor, Order, OrderStatus
from investing_algorithm_framework.core import OperationalException
from eltyer import Client, ClientException
from configuration.constants import ELTYER_CLIENT

logger = logging.getLogger(__name__)


class EltyerOrderExecutor(OrderExecutor):

    def execute_limit_order(self, order: Order, algorithm_context,
                            **kwargs) -> bool:
        client: Client = algorithm_context.config[ELTYER_CLIENT]
        try:
            eltyer_order = client.create_limit_order(
                target_symbol=order.target_symbol,
                amount=order.amount_target_symbol,
                side=order.order_side,
                price=order.initial_price
            )
            order.order_reference = eltyer_order.id
            return True
        except ClientException as e:
            logger.exception(e)
            return False

    def execute_market_order(self, order: Order, algorithm_context,
                             **kwargs) -> bool:
        client: Client = algorithm_context.config[ELTYER_CLIENT]

        try:
            eltyer_order = client.create_market_order(
                order.target_symbol, order.amount_target_symbol
            )
            order.order_reference = eltyer_order.id
            return True
        except ClientException as e:
            logger.exception(e)
            return False

    def get_order_status(self, order: Order, algorithm_context,
                         **kwargs) -> OrderStatus:
        client: Client = algorithm_context.config[ELTYER_CLIENT]

        try:
            order = client.get_order(reference_id=order.order_reference)
            return OrderStatus.from_string(order.status)
        except ClientException as e:
            logger.error(e)
            raise OperationalException(
                "Could not get order status from eltyer"
            )
