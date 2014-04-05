import pytest
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO
from versionbump import FileBump

test_version = '2.4.1'

@pytest.fixture
def fb():
    fo = StringIO(test_version)
    fb = FileBump(fo, test_version)
    return fb

def test_file_gets_parsed_correctly(fb):
    assert fb.current_version == test_version

def test_file_cache(fb):
    assert fb.file_cache == test_version

def test_bump():
    version = '2.4.1'
    fo = StringIO(version)
    fb = FileBump(fo, version)
    fb.bump('patch')
    assert fb.current_version == '2.4.2'

def test_cache_write_to_file():
    version = '0.0.0'
    match_against = 'something completely unrelated'
    fo = StringIO(version)
    fb = FileBump(fo, version)
    fb.file_cache = match_against
    fb.write_cache_to_file()
    fo.seek(0)
    assert fo.read() == match_against

def test_it_doesnt_find_the_version():
    empty_fo = StringIO('')
    with pytest.raises(ValueError):
        FileBump(empty_fo, '1.2.3')
