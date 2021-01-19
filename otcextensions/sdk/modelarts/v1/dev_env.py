# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
from openstack import resource


class AutoStopSpec(resource.Resource):
    #: Auto Stop properties
    #: Running duration in seconds
    #: Value ranges from 3600 to 86400s
    duration = resource.Body('duration', type='int')
    #: Whether to enablee the auto stop function or not
    #: True: enabled
    #: False: disabled
    enable = resource.Resource('enable', type='bool')


class LocationSpec(resource.Resource):
    #: Location properties
    #: Storage path
    path = resource.Body('path')


class StorageSpec(resource.Resource):
    #: Storage properties
    #: Storage location
    #: Mandatory parameter if obs is used as type
    location = resource.Body('location', type=LocationSpec)
    #: Storage type.
    #: Currently, obs is the only supported storage type
    type = resource.Body('type')


class NotebookSpec(resource.Resource):
    #: Notebook properties
    #: Label information which can be extended.
    #: By default this parameter is left blank.
    annotations = resource.Body('annotations', type='dict')
    #: Auto stop parameter
    auto_stop = resource.Body('auto_stop', type=AutoStopSpec)
    #: Storage path
    storage = resource.Body('storage', type=StorageSpec)


class WorkspaceSpec(resource.Resource):
    #: Workspace properties
    #: Workspace identifier
    #: Default value: 0
    id = resource.Body('id', default="0")


class DevEnv(resource.Resource):
    """Modelarts Development Environment Resource"""

    base_path = '/demanager/instances'

    # capabilities
    allow_create = True
    allow_list = True
    allow_fetch = True
    allow_delete = True
    allow_commit = True

    _query_mapping = resource.QueryParameters(
        'zone_type', 'limit', 'marker', 'offset', 'tags',
        zone_type='type')

    #: Properties
    #: Description
    description = resource.Body('description')
    #: Instance flavor
    flavor = resource.Body('flavor')
    #: Name of the development environment
    name = resource.Body('name')
    #: Configuration ID of the profile
    profile_id = resource.Body('profile_id')
    #: Instance specification where the notebook spec is the only available one
    spec = resource.Body('spec', type=NotebookSpec)
    #: Workspace
    workspace = resource.Body('workspace', type=WorkspaceSpec)
