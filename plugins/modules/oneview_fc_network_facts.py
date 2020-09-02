#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2017 Google
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# ----------------------------------------------------------------------------
#
#     ***     AUTO GENERATED CODE    ***    AUTO GENERATED CODE     ***
#
# ----------------------------------------------------------------------------
#
#     This file is automatically generated by Magic Modules and manual
#     changes will be clobbered when the file is regenerated.
#
# ----------------------------------------------------------------------------

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type
ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: oneview_fc_network_facts
short_description: Retrieve the facts about one or more of the OneView Fibre Channel Networks
description:
    - Retrieve the facts about one or more of the Fibre Channel Networks from OneView.
version_added: '2.4.0'
requirements:
    - hpOneView >= 5.0.0
author: "Felipe Bulsoni (@fgbulsoni)"
options:
    name:
      description:
        - Fibre Channel Network name.
      type: str
    config:
      description:
        - Path to a .json configuration file containing the OneView client configuration.
          The configuration file is optional. If the file path is not provided, the configuration will be loaded from
          environment variables.
      required: false
      type: path
    params:
        description:
        - List of params to delimit, filter and sort the list of resources.
        - "params allowed:
            C(start): The first item to return, using 0-based indexing.
            C(count): The number of resources to return.
            C(filter): A general filter/query string to narrow the list of items returned.
            C(sort): The sort order of the returned data set."
        required: false
        type: dict
    api_version:
        description:
            - List with the api_version.
        required: false
        type: int
    hostname:
        description:
            - List with the hostname.
        required: false
        type: str
    image_streamer_hostname:
        description:
            - List with the image_streamer_hostname.
        required: false
        type: str
    password:
        description:
            - List with the password.
        required: false
        type: str
    auth_login_domain:
        description:
            - List with the auth_login_domain.
        required: false
        type: str
    username:
        description:
            - List with the username.
        required: false
        type: str
notes:
    - "A sample configuration file for the config parameter can be found at:
       U(https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json)"
    - "Check how to use environment variables for configuration at:
       U(https://github.com/HewlettPackard/oneview-ansible#environment-variables)"
    - "Additional Playbooks for the HPE OneView Ansible modules can be found at:
       U(https://github.com/HewlettPackard/oneview-ansible/tree/master/examples)"
    '''

EXAMPLES = '''
- name: Gather facts about all Fibre Channel Networks
  oneview_fc_network_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 1200
  delegate_to: localhost

- debug: var=fc_networks

- name: Gather paginated, filtered and sorted facts about Fibre Channel Networks
  oneview_fc_network_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 1200
    params:
      start: 1
      count: 3
      sort: 'name:descending'
      filter: 'fabricType=FabricAttach'
  delegate_to: localhost
- debug: var=fc_networks

- name: Gather facts about a Fibre Channel Network by name
  oneview_fc_network_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 800
    name: network name
  delegate_to: localhost

- debug: var=fc_networks
'''

RETURN = '''
fc_networks:
    description: Has all the OneView facts about the Fibre Channel Networks.
    returned: Always, but can be null.
    type: dict
'''

from ansible_collections.hpe.oneview.plugins.module_utils.oneview import OneViewModule


class FcNetworkFactsModule(OneViewModule):
    def __init__(self):

        argument_spec = dict(
            name=dict(required=False, type='str'),
            params=dict(required=False, type='dict')
        )

        super(FcNetworkFactsModule, self).__init__(additional_arg_spec=argument_spec)

        self.resource_client = self.oneview_client.fc_networks

    def execute_module(self):

        if self.module.params['name']:
            fc_networks = self.resource_client.get_by('name', self.module.params['name'])
        else:
            fc_networks = self.resource_client.get_all(**self.facts_params)

        return dict(changed=False, ansible_facts=dict(fc_networks=fc_networks))


def main():
    FcNetworkFactsModule().run()


if __name__ == '__main__':
    main()
