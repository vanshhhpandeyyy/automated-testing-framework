import pytest


def pytest_configure(config):
    config.addinivalue_line(
        "markers", "edge_case: mark test as an edge case scenario"
    )
