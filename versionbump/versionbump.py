import re

_LEVELS = ['major', 'minor', 'patch', 'pre']
_REGEX = re.compile('^'
                    '(?P<major>[0-9]+)'
                    '\.(?P<minor>[0-9]+)'
                    '\.(?P<patch>[0-9]+)'
                    '(-(?P<label>[a-z]+)\.(?P<pre>[0-9]+))?'
                    '$')

def parse_version(version):
    match = _REGEX.match(version)
    if match is None:
        raise ValueError('Invalid version: {}'.format(version))

    version_info = {}
    for level, number in match.groupdict().items():
        if level in _LEVELS and number:
            version_info[level] = int(number)
        else:
            version_info[level] = None

    version_info['label'] = "aa"
    return version_info


class VersionBump(object):
    def __init__(self, version):
        self.version_info = parse_version(version)

    def __str__(self):
        ret = '<{0} \'{1}\'>'.format(self.__class__.__name__,
                                     self.get_version())
        return ret

    @property
    def pre_release(self):
        """ Return true if version is a pre-release. """
        label = self.version_info.get('label', False)
        pre = self.version_info.get('pre', False)

        return True if (label and pre) else False

    def bump(self, level='patch', label=None):
        """ Bump version following semantic versioning rules. """
        self.version_info[level] += 1
        self.zeroize_after_level(level)

    def zeroize_after_level(self, base_level):
        """ Set all levels after ``base_level`` to zero. """
        index = _LEVELS.index(base_level) + 1
        for level in _LEVELS[index:]:
            self.version_info[level] = 0

    def get(self, level=None):
        """ Return complete version string if called with no parameters.
            Return value of given level if ``level`` is given.
        """
        if level:
            return self.get_level(level)
        else:
            return self.get_version()

    def get_version(self):
        """ Return complete version string. """
        version = '{major}.{minor}.{patch}'.format(**self.version_info)

        if self.pre_release:
            version = '{}-{label}.{pre}'.format(version, **self.version_info)
        return version

    def get_level(self, level):
        """ Return value of given level. """
        return self.version_info[level]

