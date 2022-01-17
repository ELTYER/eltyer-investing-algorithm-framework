import logging

from configuration.constants import ELTYER_API_KEY
from investing_algorithm_framework import AlgorithmContextInitializer, \
    AlgorithmContext
from investing_algorithm_framework.core.exceptions import ImproperlyConfigured
from eltyer import Client

from configuration.constants import ELTYER_CLIENT

logger = logging.getLogger(__name__)


class EltyerInitializer(AlgorithmContextInitializer):

    def initialize(self, algorithm: AlgorithmContext) -> None:
        client = Client()
        client.config.API_KEY = algorithm.config.get(ELTYER_API_KEY)
        client.start()
        environment = client.get_environment()

        if environment is None:
            raise ImproperlyConfigured(
                "Could not retrieve algorithm environment from ELTYER"
            )

        algorithm.config.set(ELTYER_CLIENT, client)
