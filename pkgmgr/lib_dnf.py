import dnf


def update_deps(base, pkg_name, exclude_pkg_names, dep_set, logger):
    logger.debug("{}: processing".format(pkg_name))

    pkg = base.sack.query().filter(provides=pkg_name).run()[0]
    dep_set.add(pkg)

    for req in pkg.requires:
        req_name = req.name
        logger.debug("{}: found dep: {}".format(pkg_name, req_name))

        if 'rpmlib' in req_name:
            # by design of the rpm package it's shown as a dependency
            # it's supposed to be satisfied by the toolchain itself
            # but the rpm package doesn't provide rpmlib
            continue

        # identify what package provides this requirement
        dep = base.sack.query().filter(provides=req).run()[0]
        logger.debug("{}: {} is provided by: {} {}".format(pkg_name, req_name, dep.name, dep.version))

        if dep.name in exclude_pkg_names:
            logger.debug("{}: {} is in the exclude list - skipping".format(pkg_name, dep.name))
            continue

        if dep in dep_set:
            continue

        update_deps(base, req_name, exclude_pkg_names, dep_set, logger)


def get_deps(in_pkg_names, exclude_pkg_names, logger):
    base = dnf.Base()
    base.conf.substitutions['rltype'] = ''
    base.read_all_repos()
    base.fill_sack()

    dep_set=set()
    for pkg_name in in_pkg_names:
        update_deps(base, pkg_name, exclude_pkg_names, dep_set, logger)

    logger.debug("found packages original format: {}".format(sorted(dep_set)))
    out_pkgs = [str(dep) for dep in sorted(dep_set)]
    logger.debug("found packages in standard format: {}".format(out_pkgs))

    return(out_pkgs)
