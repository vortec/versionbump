import re

_LEVELS = ['major', 'minor', 'patch']
_REGEX = re.compile('^(?P<major>[0-9]+)'
                    '\.(?P<minor>[0-9]+)'
                    '\.(?P<patch>[0-9]+)$')

class VersionBump(object):
    def __init__(self, version):
        self.version_info = self.parse(version)

    def __str__(self):
        ret = '<{} \'{}\'>'.format(self.__class__.__name__, self.get_version())
        return ret

    def bump(self, level='patch'):
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
        return version

    def get_level(self, level):
        """ Return value of given level. """
        return self.version_info[level]

    def parse(self, version):
        match = _REGEX.match(version)
        if match is None:
            raise ValueError('Invalid version: {}'.format(version))

        version_info = {}
        for level, number in match.groupdict().iteritems():
            if number:
                version_info[level] = int(number)
            else:
                version_info[level] = None
        return version_info
