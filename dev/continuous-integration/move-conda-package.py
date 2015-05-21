import sys
import os
import yaml
import glob
import shutil
from conda_build import config

with open(os.path.join(sys.argv[1], 'meta.yaml')) as f:
    name = yaml.load(f)['package']['name']

if not os.path.exists(config.bldpkgs_dir):
    print('Cannot find path: %s' % config.bldpkgs_dir)
else:
    print('Files in path: %r' % os.listdir(config.bldpkgs_dir))
    print('(looking for {0}*.tar.bz2)'.format(name))

binary_package_glob = os.path.join(config.bldpkgs_dir, '{0}*.tar.bz2'.format(name))
binary_package = glob.glob(binary_package_glob)[0]

shutil.move(binary_package, '.')
