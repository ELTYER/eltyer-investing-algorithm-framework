import os
from unittest import TestCase
from eltyer_investing_algorithm_framework import create_app
from eltyer_investing_algorithm_framework.configuration import constants
from eltyer_investing_algorithm_framework.exceptions \
    import EltyerInvestingAlgorithmFrameworkException


class Test(TestCase):
    resources_dir = os.path.join(
        os.path.abspath(os.path.dirname(__file__)), 'resources'
    )

    def test_config_with_create_app(self):
        app = create_app(resource_directory=Test.resources_dir, key="test")
        self.assertIsNotNone(app.config.get(constants.ELTYER_API_KEY))

    def test_config_without_api_key(self):

        with self.assertRaises(EltyerInvestingAlgorithmFrameworkException):
            create_app(resource_directory=Test.resources_dir)
