from .linux_common import common_parse_info


def setup_command():
    return None


def info_command(packages):
    return 'zypper --xmlout info {}'.format(' '.join(packages))


def parse_info(output):
    return common_parse_info('zypper', output)
