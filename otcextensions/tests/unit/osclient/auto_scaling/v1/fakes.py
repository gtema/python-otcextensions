#   Copyright 2013 Nebula Inc.
#
#   Licensed under the Apache License, Version 2.0 (the "License"); you may
#   not use this file except in compliance with the License. You may obtain
#   a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#   WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#   License for the specific language governing permissions and limitations
#   under the License.
#

import copy
import datetime
import random
import uuid

import mock
# from osc_lib import utils as common_utils

from openstackclient.tests.unit import fakes
from openstackclient.tests.unit import utils

# from otcextensions.sdk.auto_scaling.v1.group import Group
# from otcextensions.sdk.obs.v1.object import Object

# from otcextensions.obs.v1.api import API


class Fake(object):

    @classmethod
    def create_one(cls, attrs=None):
        """Create a fake resource.

        :param Dictionary attrs:
            A dictionary with all attributes
        :param Dictionary methods:
            A dictionary with all methods
        :return:
            A FakeResource object, with id, name, metadata, and so on
        """
        attrs = attrs or {}

        new_attrs = cls.generate()

        new_attrs.update(attrs)

        new_resource = fakes.FakeResource(
            info=copy.deepcopy(new_attrs),
            loaded=True)

        return new_resource

    @classmethod
    def create_multiple(cls, count=2, attrs=None):
        """Create multiple fake resources.

        :param Dictionary attrs:
            A dictionary with all attributes
        :param int count:
            The number of address scopes to fake
        :return:
            A list of FakeResource objects faking the address scopes
        """
        objects = []
        for i in range(0, count):
            objects.append(
                cls.create_one(attrs))

        return objects


class TestAutoScaling(utils.TestCommand):

    def setUp(self):
        super(TestAutoScaling, self).setUp()

        self.app.client_manager.auto_scaling = mock.Mock()

        # s3api = API(client=self.app.client_manager.obs)
        # self.app.client_manager.obs.api = s3api

        self.group_mock = FakeGroup
        # self.configuratio_mock = FakeConfiguration


class FakeGroup(Fake):
    """Fake one or more Group"""

    @classmethod
    def generate(cls):
        object_info = {
            'create_time': datetime.datetime(
                random.randint(2000, 2020),
                random.randint(1, 12),
                random.randint(1, 28)
            ),
            'name': 'group-' + uuid.uuid4().hex,
            'id': 'id-' + uuid.uuid4().hex,
            'status': 'SOME STATUS',
            'detail': 'detail-' + uuid.uuid4().hex,
            'vpc_id': 'vpc-' + uuid.uuid4().hex,
        }
        return object_info
