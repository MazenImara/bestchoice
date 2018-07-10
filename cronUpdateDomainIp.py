#!/usr/bin/python
# coding=utf-8

import os


# Start execution here!
if __name__ == '__main__':
    print("Starting...")

    # load settings
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fann.settings')

    from updatePublicIp import updateRecordsIp
    updateRecordsIp()






