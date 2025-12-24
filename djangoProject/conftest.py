# conftest.py
import pytest
from django.conf import settings

@pytest.fixture(autouse=True)
def disable_caching():
    settings.CACHES = {
        "default": {
            "BACKEND": "django.core.cache.backends.dummy.DummyCache",
        }
    }