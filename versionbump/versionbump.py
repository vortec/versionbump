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
        if level in _LEVELS and number is not None:
            version_info[level] = int(number)
        else:
            version_info[level] = number

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
        label = self.version_info.get('label', None)
        pre = self.version_info.get('pre', None)

        return True if (label is not None and pre is not None) else False

    def _bump(self, level, label):
        """ """
        if self.pre_release:
            self.remove_pre_release()
            if level == 'patch':  # 2.0.3-dev.1 -> bump 'patch' -> 2.0.3
                return

        self.version_info[level] += 1
        self.zeroize_after_level(level)

    def _bump_pre(self, level, label):
        """ """
        if not label:
            label = 'dev'

        if not self.pre_release:
            self.bump('patch', label=label)
            self.version_info['label'] = label
            self.version_info['pre'] = 0
        else:
            self.version_info[level] += 1

    def bump(self, level='patch', label=None):
        """ Bump version following semantic versioning rules. """
        bump = self._bump_pre if level == 'pre' else self._bump
        bump(level, label)

    def zeroize_after_level(self, base_level):
        """ Set all levels after ``base_level`` to zero. """
        index = _LEVELS.index(base_level) + 1
        for level in _LEVELS[index:]:
            self.version_info[level] = 0

    def remove_pre_release(self):
        """ Remove pre release attributes. """
        self.version_info['label'] = None
        self.version_info['pre'] = None

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
