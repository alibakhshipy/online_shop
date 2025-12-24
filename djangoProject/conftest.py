# conftest.py
import pytest

def pytest_addoption(parser):
    parser.addoption(
        "--runslow", action="store_true", default=False, help="run slow tests"
    )

def pytest_collection_modifyitems(config, items):
    if config.getoption("--runslow"):
        # اگر --runslow زده شد، همه تست‌ها اجرا می‌شوند
        return
    skip_slow = pytest.mark.skip(reason="نیاز به --runslow دارد")
    for item in items:
        if "slow" in item.keywords:
            item.add_marker(skip_slow)