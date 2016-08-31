from __future__ import print_function
import os

#
# data directory structure
#

nfmt='%06d'

def get_temp_dir():
    """
    temporary directory

    for wq we want to use TMPDIR for wq log files to
    prevent too many open files on gpfs
    """
    return os.environ['TMPDIR']

def get_basedir():
    """
    The base directory $WOMBAT_DIR.

    Runs are held under bad/run
    """
    if 'WOMBAT_DIR' not in os.environ:
        raise ValueError("WOMBAT_DIR environment variable is not set")

    return os.environ['WOMBAT_DIR']

def get_rundir(run):
    """
    The run directory $WOMBAT_DIR/run
    """
    bdir=get_basedir()
    return os.path.join(bdir, run)

def get_script_dir(run):
    """
    The script directory $WOMBAT_DIR/{run}/scripts
    """
    bdir=get_basedir()
    return os.path.join(bdir, run, 'scripts')

def get_script_file(run, index):
    """
    get the script file path
    """
    dir=get_script_dir(run)
    fmt='wombat-%s-'+nfmt+'.sh'
    fname=fmt % (run, index)
    return os.path.join(dir, fname)

def get_wq_dir(run):
    dir=get_temp_dir()
    return os.path.join(dir, 'wombat', run, 'wq')

def get_wq_file(run, index):
    """
    get the script file path
    """

    dir=get_wq_dir(run)
    fmt='wombat-%s-'+nfmt+'.yaml'
    fname=fmt % (run, index)
    return os.path.join(dir, fname)


def get_output_dir(run):
    """
    The script directory $WOMBAT_DIR/{run}/output
    """
    bdir=get_basedir()
    return os.path.join(bdir, run, 'output')

def get_meds_file_pattern():
    """
    get the pattern for star files
    """
    return 'wombat-%s-'+nfmt+'.fits'

def get_meds_file(run, index):
    """
    get the path to the meds output file
    """
    dir=get_output_dir(run)
    pattern=get_meds_file_pattern()
    fname=pattern % (run, index)

    return os.path.join(dir, fname)

def get_truth_file_pattern():
    """
    get the pattern for star files
    """
    return 'wombat-truth-%s-'+nfmt+'.fits'

def get_truth_file(run, index):
    """
    get the path to a truth file
    """
    dir=get_output_dir(run)
    pattern=get_truth_file_pattern()
    fname=pattern % (run, index)

    return os.path.join(dir, fname)


def get_log_file(run, index):
    """
    location of the log file
    """
    oname=get_meds_file(run, index)
    fname=oname.replace('.fits', '.log')
    assert oname != fname
    return fname


#
# configuration files
#

def get_config_dir():
    """
    get the value of the $WOMBAT_CONFIG_DIR environement variable
    """
    if 'WOMBAT_CONFIG_DIR' not in os.environ:
        raise ValueError("WOMBAT_CONFIG_DIR environment variable is not set")

    return os.environ['WOMBAT_CONFIG_DIR']

def get_config_file(run):
    """
    the path to the stars config file
    """

    cdir=get_config_dir()
    fname='%s.yaml' % run
    return os.path.join(cdir, fname)

def read_config(run):
    """
    read the yaml config file
    """
    fname= get_config_file(run)
    return read_yaml(fname)

def read_yaml(fname):
    """
    wrapper to read yaml files
    """
    import yaml
    print("reading:",fname)
    with open(fname) as fobj:
        data=yaml.load( fobj )

    return data

