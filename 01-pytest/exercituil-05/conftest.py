import tempfile
import pytest

@pytest.fixture(scope="session")
def tmp_file():
    f = tempfile.TemporaryFile("w+t")
    yield f
    if not f.closed:
        f.close()