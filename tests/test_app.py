import os
from unittest import TestCase

from eltyer_investing_algorithm_framework import create_app


class Test(TestCase):
    resources_dir = os.path.join(
        os.path.abspath(os.path.dirname(__file__)), 'resources'
    )

    def test_start(self):
        app = create_app(
            resource_directory=Test.resources_dir,
            key="cbnu5EUlzF3empnASvYvQzTwSsiQTiAXiKIvDvT7ZLM3wXhYha"
                "G2vTAlKFL4tNYn"
        )
        app.start()
