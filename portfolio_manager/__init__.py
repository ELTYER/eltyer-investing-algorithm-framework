from investing_algorithm_framework import SQLLitePortfolioManager
from configuration.constants import ELTYER_CLIENT
from eltyer import Client


class EltyerPortfolioManager(SQLLitePortfolioManager):

    def get_unallocated_synced(self, algorithm_context):
        client: Client = algorithm_context.config.get(ELTYER_CLIENT)
        return client.get_portfolio().unallocated

    def get_positions_synced(self, algorithm_context):
        client: Client = algorithm_context.config.get(ELTYER_CLIENT)
        positions = client.get_positions(json=True)
        return positions
