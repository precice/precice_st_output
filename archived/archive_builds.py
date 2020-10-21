"""
### WIP ###
Script for managing build folders in the precice_st_output repository.

Checks repository for build folders, folders other than the most recent ones
get moved into a compressed archive.

Should be run regularly through a .travis.yml cron job
"""

from jinja2 import Template
from urllib.request import Request, urlopen
import argparse, os, sys, time
import subprocess
from contextlib import contextmanager

@contextmanager
def chdir(path):
    """ Changes and restores the current working directory. """
    oldpwd = os.getcwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(oldpwd)

def call(cmd, **kwargs):
    """ Runs cmd in a shell, returns its return code. """
    print("EXECUTING:", cmd)
    cp = subprocess.run(cmd, shell=True, **kwargs)
    return cp.returncode

def ccall(cmd,  **kwargs):
    """ Runs cmd in a shell, returns its return code. Raises exception on error """
    return call(cmd, check = True, **kwargs)


def add_readme(
        job_path,
        output=False,
        output_missing=False,
        logs_missing=False,
        message=None
        ):
    """
    Create a README.md at the location specified by readme_path.
    """
    job_link = os.environ["TRAVIS_JOB_WEB_URL"]
    job_name = os.environ["TRAVIS_JOB_NAME"]
    job_success = True if (os.environ["TRAVIS_TEST_RESULT"] == '0') else False

    if (output_missing or logs_missing or message):
        additional_info = True
    else:
        additional_info = False

    with open(os.path.join('templates','test_template', 'README.md')) as f:
        tmp = Template(f.read())
        readme_rendered = tmp.render(locals())

    with chdir(job_path):
        with open("README.md", "w") as f:
            f.write(readme_rendered)
        ccall("git add README.md")


if __name__ == "__main__":

    repo_folder = "precice_st_output"
    maximum_builds = 10
    default_st_branch = "EderK-push_files"

    parser = argparse.ArgumentParser(description="Clean up repository by archiving older build folders.")
    parser.add_argument('-b', '--branch', type=str, help="Branch of precice_st_output to clean.", default=default_st_branch)
    parser.add_argument('-n', '--num-builds', type=int, help="Number of build folders to preserve.", default=maximum_builds)

    args = parser.parse_args()

    # TODO: change default to master branch when merging
    ccall("git clone -b {branch} https://github.com/precice/precice_st_output".\
        format(branch=args.branch))

    # Path to repository folder
    repo_path = os.path.join(os.getcwd(), repo_folder)
    # identify build folders
    build_folders = os.listdir(repo_path)
    for folder in build_folders:
        if not folder.isdecimal():
            build_folders.remove(folder)
    # move older folders to 'archived'
    build_folders.sort()
    folders_to_archive = build_folders[:-maximum_builds]
    with chdir(repo_path):
        # decompress existing tar.gz archive
        ccall("mkdir -p archived")
        if os.path.isfile("archived/archive.tar.gz"):
            ccall("gzip -d archived/archive.tar.gz")
        # add build folders to tar archive
        unpacked_folders = " ".join(folders_to_archive)
        ccall("tar -rf archived/archive.tar {folders}".format(folders=unpacked_folders))
        # compress tar archive
        ccall("gzip -9 archived/archive.tar")
        # remove archived folders
        ccall("git rm -r {folders}".format(folders=unpacked_folders))


    os.chdir(repo_path)
    ccall("git add -A")

    commit_msg = "Archive {} build folders".format(len(folders_to_archive))

    ccall("git commit -m '{}'".format(commit_msg))
    ccall("git config user.name 'Precice Bot'")
    ccall("git config user.email ${PRECICE_BOT_EMAIL}")
    ccall("git remote set-url origin https://${GH_TOKEN}@github.com/precice/precice_st_output.git > /dev/null 2>&1")


    failed_push_count = 0
    failed_push_limit = 10
    # push, retry if failed
    while call("git push"):
        ccall("git pull --rebase")
        failed_push_count += 1
        if failed_push_count >= failed_push_limit:
            break
