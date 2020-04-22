import pytest


class TestClass():
    @pytest.fixture(autouse=True)
    def _get_fixture(self, app):
        self.app = app

    def test_first(self):
        self.app.first.first_method()
        assert 1 == 1