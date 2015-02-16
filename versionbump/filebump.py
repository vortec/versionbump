from versionbump import VersionBump


class FileBump(object):
    file_cache = ''

    def __init__(self, fo, version):
        self.vb = VersionBump(version)
        self.fo = fo
        self.file_cache = self.fo.read()
        self.validate_cache()

    def __str__(self):
        ret = '<{0} \'{1}\'>'.format(self.__class__.__name__,
                                     self.current_version)
        return ret

    @property
    def current_version(self):
        return self.vb.get_version()

    def validate_cache(self):
        if self.current_version not in self.file_cache:
            raise ValueError('Version not in file.')

    def bump(self, level='minor'):
        old_version = self.current_version
        self.vb.bump(level)
        self.replace_version_in_cache(old_version, self.current_version)
        self.write_cache_to_file()

    def write_cache_to_file(self):
        self.fo.seek(0)
        self.fo.write(self.file_cache)

    def replace_version_in_cache(self, old_version, new_version):
        self.file_cache = self.file_cache.replace(old_version, new_version)
