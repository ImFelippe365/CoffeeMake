from src.CoffeeMaker import CoffeeMaker
import pytest

class BaseTest:

    @pytest.fixture
    def setUp(self):
        coffeeMaker = CoffeeMaker()
        return coffeeMaker


