def info_command(packages):
    if 'clang' in packages:
        packages[packages.index('clang')] = 'llvm'

    'sudo pkg update --quiet && sudo pkg rquery "%n %v %dn=%dv" {}'.format(' '.join(packages))

    return cmd


def parse_info(output):
    info = {}

    output = output.strip()
    lines = output.split("\n")
    for line in lines:
        pkg, version, dep = line.split(' ')
        if dep.startswith(pkg):
            realpkg, version = dep.split('=')
        version = version.split('_')[0]
        info[pkg] = version

        # clang is provided by the 'llvm<version>' package, in FreeBSD
        if pkg == 'llvm':
            info['clang'] = version + '(via {})'.format(realpkg)

    return info
