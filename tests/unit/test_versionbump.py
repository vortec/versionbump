import pytest
from versionbump import VersionBump

test_version = '2.0.1'
test_pre_version = '2.0.1-dev.3'


@pytest.fixture
def vb():
    return VersionBump(test_version)


@pytest.fixture
def vb_pre():
    return VersionBump(test_pre_version)


def test_same_version_after_parsing(vb):
    assert vb.get_version() == test_version


def test_level_access(vb):
    assert vb.get_level('major') == 2
    assert vb.get_level('minor') == 0
    assert vb.get_level('patch') == 1
    assert vb.get_level('pre') is None


def test_is_pre_release(vb, vb_pre):
    assert vb_pre.pre_release is True
    assert vb.pre_release is False


def test_pre_level_access(vb_pre):
    assert vb_pre.get_level('pre') == 3


def test_pre_bump(vb):
    vb.bump('pre', label='dev')
    assert vb.get_version() == '2.0.2-dev.0'
    vb.bump('pre')
    assert vb.get_version() == '2.0.2-dev.1'
    vb.bump('patch')
    assert vb.get_version() == '2.0.2'
    vb.bump('pre', label='alpha')
    assert vb.get_version() == '2.0.3-alpha.0'
    vb.bump('minor')
    assert vb.get_version() == '2.1.0'


def test_bump():
    vb = VersionBump('2.0.1')
    vb.bump()
    assert vb.get('patch') == 2


def test_zeroize():
    vb = VersionBump('1.2.3')
    vb.zeroize_after_level('major')
    assert vb.get_version() == '1.0.0'


def test_print_output(vb):
    expected_string = '<VersionBump \'{0}\'>'.format(test_version)
    assert str(vb) == expected_string


def test_invalid_version():
    with pytest.raises(ValueError):
        VersionBump('2.0.1.0')


def test_get_invalid_level(vb):
    with pytest.raises(KeyError):
        vb.get_level('foo')


def test_bump_invalid_level(vb):
    with pytest.raises(KeyError):
        vb.bump('foo')
