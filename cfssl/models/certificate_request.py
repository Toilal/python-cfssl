# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

from .host import Host
from .config_key import ConfigKey
from .subject_info import SubjectInfo


class CertificateRequest(object):
    """ It provides a Certificate Request compatible with CFSSL. """

    def __init__(self, common_name, names=None, hosts=None, key=None):
        self.common_name = common_name
        self.names = names or []
        self.hosts = hosts or []
        self.key = key or KeyConfig()

    def to_api(self):
        """ It returns an object compatible with the API. """
        return {
            'CN': self.common_name,
            'names': [
                name.to_api() for name in self.names
            ],
            'hosts': [
                host.to_api() for host in self.hosts
            ],
            'key': self.key.to_api(),
        }
