import pytest
from versionbump import VersionBump

@pytest.fixture
def vb():
    return VersionBump('2.0.1')


def test_same_version_after_parsing(vb):
    assert vb.get_version() == '2.0.1'

def test_level_access(vb):
    assert vb.get_level('major') == 2
    assert vb.get_level('minor') == 0
    assert vb.get_level('patch') == 1

def test_bump():
    vb = VersionBump('2.0.1')
    vb.bump()
    assert vb.get('patch') == 2

def test_zeroize():
    vb = VersionBump('1.2.3')
    vb.zeroize_after_level('major')
    assert vb.get_version() == '1.0.0'

def test_print_output(vb):
    expected_string = '<VersionBump \'{}\'>'.format('2.0.1')
    assert str(vb) == expected_string
    assert unicode(vb) == expected_string

def test_invalid_version():
    with pytest.raises(ValueError):
        VersionBump('2.0.1.0')

def test_get_invalid_level(vb):
    with pytest.raises(KeyError):
        vb.get_level('foo')

def test_bump_invalid_level():
    vb = VersionBump('2.0.1')
    with pytest.raises(KeyError):
        vb.bump('foo')
