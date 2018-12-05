#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Libraries
import os
import click

@click.command()
@click.argument('paths', nargs=-1)
@click.option('-cd/--change', is_flag=True, default=False, help='After creating the directories, change to the new deeper directory.')
def advance_touch(paths, cd):
    """ Make folders and files """
    for path in paths:
        # Make folders
        new_dirs = '/'.join(path.split('/')[0:-1])
        if not os.path.exists(new_dirs) and new_dirs != '':
            os.makedirs(new_dirs)
        # Change directory
        if cd:
            cd_path = os.path.join(os.getcwd(), new_dirs) + '/'
            os.chdir(cd_path)

        # Make file
        if not path.endswith('/') and not os.path.isfile(path):
            try:
                open(path, 'w+').close()
            except IsADirectoryError:
                pass

if __name__ == '__main__':
    advance_touch()
