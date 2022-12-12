#!/usr/bin/env python

# type: ignore
'''
Hetzner Cloud API
openapi.json

contact:
  url: https://docs.hetzner.cloud/
description: Copied from the official API documentation for the Public Hetzner Cloud.
openapi: 3.0.3
version: 4ea4924-dirty

'''
result = 1
str_dflt = ''
timeout = 5
# -

class API:
    user, passw = '$user', '$password'
    host = 'https://api.hetzner.cloud/v1'
    base = ''
    hdrs = {}


id = 0
action_id = 0

# fmt:off
methods = lambda: ( # :clear :doc :all :single :wrap p = Tools.send({})
 '🟩', actions.get,
 '🟩', actions___id_.get,
 '🟩', certificates.get,
 '🟪', certificates.post,
 '🟥', certificates___id_.delete,
 '🟩', certificates___id_.get,
 '🟧', certificates___id_.put,
 '🟩', certificates___id___actions.get,
 '🟩', certificates___id___actions___action_id_.get,
 '🟪', certificates___id___actions__retry.post,
 '🟩', datacenters.get,
 '🟩', datacenters___id_.get,
 '🟩', firewalls.get,
 '🟪', firewalls.post,
 '🟥', firewalls___id_.delete,
 '🟩', firewalls___id_.get,
 '🟧', firewalls___id_.put,
 '🟩', firewalls___id___actions.get,
 '🟩', firewalls___id___actions___action_id_.get,
 '🟪', firewalls___id___actions__apply_to_resources.post,
 '🟪', firewalls___id___actions__remove_from_resources.post,
 '🟪', firewalls___id___actions__set_rules.post,
 '🟩', floating_ips.get,
 '🟪', floating_ips.post,
 '🟥', floating_ips___id_.delete,
 '🟩', floating_ips___id_.get,
 '🟧', floating_ips___id_.put,
 '🟩', floating_ips___id___actions.get,
 '🟩', floating_ips___id___actions___action_id_.get,
 '🟪', floating_ips___id___actions__assign.post,
 '🟪', floating_ips___id___actions__change_dns_ptr.post,
 '🟪', floating_ips___id___actions__change_protection.post,
 '🟪', floating_ips___id___actions__unassign.post,
 '🟩', images.get,
 '🟥', images___id_.delete,
 '🟩', images___id_.get,
 '🟧', images___id_.put,
 '🟩', images___id___actions.get,
 '🟩', images___id___actions___action_id_.get,
 '🟪', images___id___actions__change_protection.post,
 '🟩', isos.get,
 '🟩', isos___id_.get,
 '🟩', load_balancer_types.get,
 '🟩', load_balancer_types___id_.get,
 '🟩', load_balancers.get,
 '🟪', load_balancers.post,
 '🟥', load_balancers___id_.delete,
 '🟩', load_balancers___id_.get,
 '🟧', load_balancers___id_.put,
 '🟩', load_balancers___id___actions.get,
 '🟩', load_balancers___id___actions___action_id_.get,
 '🟪', load_balancers___id___actions__add_service.post,
 '🟪', load_balancers___id___actions__add_target.post,
 '🟪', load_balancers___id___actions__attach_to_network.post,
 '🟪', load_balancers___id___actions__change_algorithm.post,
 '🟪', load_balancers___id___actions__change_dns_ptr.post,
 '🟪', load_balancers___id___actions__change_protection.post,
 '🟪', load_balancers___id___actions__change_type.post,
 '🟪', load_balancers___id___actions__delete_service.post,
 '🟪', load_balancers___id___actions__detach_from_network.post,
 '🟪', load_balancers___id___actions__disable_public_interface.post,
 '🟪', load_balancers___id___actions__enable_public_interface.post,
 '🟪', load_balancers___id___actions__remove_target.post,
 '🟪', load_balancers___id___actions__update_service.post,
 '🟩', load_balancers___id___metrics.get,
 '🟩', locations.get,
 '🟩', locations___id_.get,
 '🟩', networks.get,
 '🟪', networks.post,
 '🟥', networks___id_.delete,
 '🟩', networks___id_.get,
 '🟧', networks___id_.put,
 '🟩', networks___id___actions.get,
 '🟩', networks___id___actions___action_id_.get,
 '🟪', networks___id___actions__add_route.post,
 '🟪', networks___id___actions__add_subnet.post,
 '🟪', networks___id___actions__change_ip_range.post,
 '🟪', networks___id___actions__change_protection.post,
 '🟪', networks___id___actions__delete_route.post,
 '🟪', networks___id___actions__delete_subnet.post,
 '🟩', placement_groups.get,
 '🟪', placement_groups.post,
 '🟥', placement_groups___id_.delete,
 '🟩', placement_groups___id_.get,
 '🟧', placement_groups___id_.put,
 '🟩', pricing.get,
 '🟩', primary_ips.get,
 '🟪', primary_ips.post,
 '🟥', primary_ips___id_.delete,
 '🟩', primary_ips___id_.get,
 '🟧', primary_ips___id_.put,
 '🟪', primary_ips___id___actions__assign.post,
 '🟪', primary_ips___id___actions__change_dns_ptr.post,
 '🟪', primary_ips___id___actions__change_protection.post,
 '🟪', primary_ips___id___actions__unassign.post,
 '🟩', server_types.get,
 '🟩', server_types___id_.get,
 '🟩', servers.get,
 '🟪', servers.post,
 '🟥', servers___id_.delete,
 '🟩', servers___id_.get,
 '🟧', servers___id_.put,
 '🟩', servers___id___actions.get,
 '🟩', servers___id___actions___action_id_.get,
 '🟪', servers___id___actions__add_to_placement_group.post,
 '🟪', servers___id___actions__attach_iso.post,
 '🟪', servers___id___actions__attach_to_network.post,
 '🟪', servers___id___actions__change_alias_ips.post,
 '🟪', servers___id___actions__change_dns_ptr.post,
 '🟪', servers___id___actions__change_protection.post,
 '🟪', servers___id___actions__change_type.post,
 '🟪', servers___id___actions__create_image.post,
 '🟪', servers___id___actions__detach_from_network.post,
 '🟪', servers___id___actions__detach_iso.post,
 '🟪', servers___id___actions__disable_backup.post,
 '🟪', servers___id___actions__disable_rescue.post,
 '🟪', servers___id___actions__enable_backup.post,
 '🟪', servers___id___actions__enable_rescue.post,
 '🟪', servers___id___actions__poweroff.post,
 '🟪', servers___id___actions__poweron.post,
 '🟪', servers___id___actions__reboot.post,
 '🟪', servers___id___actions__rebuild.post,
 '🟪', servers___id___actions__remove_from_placement_group.post,
 '🟪', servers___id___actions__request_console.post,
 '🟪', servers___id___actions__reset.post,
 '🟪', servers___id___actions__reset_password.post,
 '🟪', servers___id___actions__shutdown.post,
 '🟩', servers___id___metrics.get,
 '🟩', ssh_keys.get,
 '🟪', ssh_keys.post,
 '🟥', ssh_keys___id_.delete,
 '🟩', ssh_keys___id_.get,
 '🟧', ssh_keys___id_.put,
 '🟩', volumes.get,
 '🟪', volumes.post,
 '🟥', volumes___id_.delete,
 '🟩', volumes___id_.get,
 '🟧', volumes___id_.put,
 '🟩', volumes___id___actions.get,
 '🟩', volumes___id___actions___action_id_.get,
 '🟪', volumes___id___actions__attach.post,
 '🟪', volumes___id___actions__change_protection.post,
 '🟪', volumes___id___actions__detach.post,
 '🟪', volumes___id___actions__resize.post,
) 
# fmt:on


class Defs:
    class components_schemas_action:
        """#/components/schemas/action"""
        class R:
            required = ['id', 'command', 'status', 'progress', 'started', 'finished', 'resources', 'error']
            title = 'Action'
            type = 'object'
            description = 'Actions show the results and progress of asynchronous requests to the API.'
            _attrs = ['command', 'error', 'finished', 'id', 'progress', 'resources', 'started', 'status']
            command = {'example': 'start_server', 'type': 'string', 'descr': 'Command executed in the Action'}
            error = lambda: Defs.components_schemas_error
            finished = {'example': '2016-01-30T23:55:00+00:00', 'nullable': True, 'type': 'string', 'descr': 'Point in time when the Action was finished (in ISO-8601 format). Only set if the Action is finished otherwise null.'}
            id = {'example': 42, 'type': 'integer', 'descr': 'ID of the Resource'}
            progress = {'example': 100, 'type': 'number', 'descr': 'Progress of Action in percent'}
            resources = {'items': lambda: Defs.components_schemas_resource, 'type': 'array', 'descr': 'Resources the Action relates to'}
            started = {'example': '2016-01-30T23:55:00+00:00', 'type': 'string', 'descr': 'Point in time when the Action was started (in ISO-8601 format)'}
            status = {'enum': ['error', 'running', 'success'], 'type': 'string', 'descr': 'Status of the Action'}
        R.command = 'start_server'
        R.error = lambda: Defs.components_schemas_error
        R.finished = '2016-01-30T23:55:00+00:00'
        R.id = id
        R.progress = 100
        R.resources = [lambda: Defs.components_schemas_resource]
        R.started = '2016-01-30T23:55:00+00:00'
        R.status = 'error'
    class components_schemas_action_optional:
        """#/components/schemas/action_optional"""
        class R:
            nullable = True
            required = ['id', 'command', 'status', 'progress', 'started', 'finished', 'resources', 'error']
            title = 'NullableAction'
            type = 'object'
            description = 'Actions show the results and progress of asynchronous requests to the API.'
            _attrs = ['command', 'error', 'finished', 'id', 'progress', 'resources', 'started', 'status']
            command = {'example': 'start_server', 'type': 'string', 'descr': 'Command executed in the Action'}
            error = lambda: Defs.components_schemas_error
            finished = {'example': '2016-01-30T23:55:00+00:00', 'nullable': True, 'type': 'string', 'descr': 'Point in time when the Action was finished (in ISO-8601 format). Only set if the Action is finished otherwise null.'}
            id = {'example': 42, 'type': 'integer', 'descr': 'ID of the Resource'}
            progress = {'example': 100, 'type': 'number', 'descr': 'Progress of Action in percent'}
            resources = {'items': lambda: Defs.components_schemas_resource, 'type': 'array', 'descr': 'Resources the Action relates to'}
            started = {'example': '2016-01-30T23:55:00+00:00', 'type': 'string', 'descr': 'Point in time when the Action was started (in ISO-8601 format)'}
            status = {'enum': ['error', 'running', 'success'], 'type': 'string', 'descr': 'Status of the Action'}
        R.command = 'start_server'
        R.error = lambda: Defs.components_schemas_error
        R.finished = '2016-01-30T23:55:00+00:00'
        R.id = id
        R.progress = 100
        R.resources = [lambda: Defs.components_schemas_resource]
        R.started = '2016-01-30T23:55:00+00:00'
        R.status = 'error'
    class components_schemas_add_route_to_network_request:
        """#/components/schemas/add_route_to_network_request"""
        class R:
            dollar_ref = lambda: Defs.components_schemas_route
    class components_schemas_add_route_to_network_response:
        """#/components/schemas/add_route_to_network_response"""
        class R:
            required = ['action']
            title = 'ActionResponse'
            type = 'object'
            description = 'Response to POST https://api.hetzner.cloud/v1/networks/{id}/actions/add_route'
            _attrs = ['action']
            action = lambda: Defs.components_schemas_action
        R.action = lambda: Defs.components_schemas_action
    class components_schemas_add_server_to_placement_group_request:
        """#/components/schemas/add_server_to_placement_group_request"""
        class R:
            required = ['placement_group']
            title = 'AddToPlacementGroupRequest'
            type = 'object'
            description = 'Request for POST https://api.hetzner.cloud/v1/servers/{id}/actions/add_to_placement_group'
            _attrs = ['placement_group']
            placement_group = {'example': 1, 'type': 'integer', 'descr': 'ID of Placement Group the Server should be added to'}
        R.placement_group = 1
    class components_schemas_add_server_to_placement_group_response:
        """#/components/schemas/add_server_to_placement_group_response"""
        class R:
            required = ['action']
            title = 'ActionResponse'
            type = 'object'
            description = 'Response to POST https://api.hetzner.cloud/v1/servers/{id}/actions/add_to_placement_group'
            _attrs = ['action']
            action = lambda: Defs.components_schemas_action
        R.action = lambda: Defs.components_schemas_action
    class components_schemas_add_service_request:
        """#/components/schemas/add_service_request"""
        class R:
            dollar_ref = lambda: Defs.components_schemas_load_balancer_service
    class components_schemas_add_service_response:
        """#/components/schemas/add_service_response"""
        class R:
            required = ['action']
            title = 'ActionResponse'
            type = 'object'
            description = 'Response to POST https://api.hetzner.cloud/v1/load_balancers/{id}/actions/add_service'
            _attrs = ['action']
            action = lambda: Defs.components_schemas_action
        R.action = lambda: Defs.components_schemas_action
    class components_schemas_add_subnet_to_network_request:
        """#/components/schemas/add_subnet_to_network_request"""
        class R:
            dollar_ref = lambda: Defs.components_schemas_subnet
    class components_schemas_add_subnet_to_network_response:
        """#/components/schemas/add_subnet_to_network_response"""
        class R:
            required = ['action']
            title = 'ActionResponse'
            type = 'object'
            description = 'Response to POST https://api.hetzner.cloud/v1/networks/{id}/actions/add_subnet'
            _attrs = ['action']
            action = lambda: Defs.components_schemas_action
        R.action = lambda: Defs.components_schemas_action
    class components_schemas_add_target_request:
        """#/components/schemas/add_target_request"""
        class R:
            required = ['type']
            title = 'AddTargetRequest'
            type = 'object'
            description = 'Request for POST https://api.hetzner.cloud/v1/load_balancers/{id}/actions/add_target'
            _attrs = ['ip', 'label_selector', 'server', 'type', 'use_private_ip']
            ip = {'example': '203.0.113.1', 'type': 'string', 'descr': 'IP of a server that belongs to the same customer (public IPv4/IPv6) or private IP in a Subnetwork type vswitch.'}
            ip = {'properties': {'ip': {'description': 'IP of a server that belongs to the same customer (public IPv4/IPv6) or private IP in a Subnetwork type vswitch.', 'example': '203.0.113.1', 'type': 'string'}}, 'required': ['ip'], 'type': 'object', 'descr': 'IP targets where the traffic should be routed through. It is only possible to use the (Public or vSwitch) IPs of Hetzner Online Root Servers belonging to the project owner. IPs belonging to other users are blocked. Additionally IPs belonging to services provided by Hetzner Cloud (Servers, Load Balancers, ...) are blocked as well.'}
            label_selector = lambda: Defs.components_schemas_label_selector
            id = {'example': 80, 'type': 'integer', 'descr': 'ID of the Server'}
            server = {'additionalProperties': False, 'properties': {'id': {'description': 'ID of the Server', 'example': 80, 'type': 'integer'}}, 'required': ['id'], 'type': 'object', 'descr': 'Configuration for type Server, required if type is `server`'}
            type = {'enum': ['ip', 'label_selector', 'server'], 'type': 'string', 'descr': 'Type of the resource'}
            use_private_ip = {'example': True, 'type': 'boolean', 'descr': 'Use the private network IP instead of the public IP of the Server, requires the Server and Load Balancer to be in the same network. Default value is false.'}
        R.ip = dict(ip = '203.0.113.1')
        R.label_selector = lambda: Defs.components_schemas_label_selector
        R.server = dict(id = id)
        R.type = 'ip'
        R.use_private_ip = True
    class components_schemas_add_target_response:
        """#/components/schemas/add_target_response"""
        class R:
            required = ['action']
            title = 'ActionResponse'
            type = 'object'
            description = 'Response to POST https://api.hetzner.cloud/v1/load_balancers/{id}/actions/add_target'
            _attrs = ['action']
            action = lambda: Defs.components_schemas_action
        R.action = lambda: Defs.components_schemas_action
    class components_schemas_apply_to_resources_request:
        """#/components/schemas/apply_to_resources_request"""
        class R:
            required = ['apply_to']
            title = 'ApplyToResourcesRequest'
            type = 'object'
            description = 'Request for POST https://api.hetzner.cloud/v1/firewalls/{id}/actions/apply_to_resources'
            _attrs = ['apply_to']
            apply_to = {'items': lambda: Defs.components_schemas_firewall_resource, 'type': 'array', 'descr': 'Resources the Firewall should be applied to'}
        R.apply_to = [lambda: Defs.components_schemas_firewall_resource]
    class components_schemas_apply_to_resources_response:
        """#/components/schemas/apply_to_resources_response"""
        class R:
            required = ['actions']
            title = 'ActionsResponse'
            type = 'object'
            description = 'Response to POST https://api.hetzner.cloud/v1/firewalls/{id}/actions/apply_to_resources'
            _attrs = ['actions', 'meta']
            actions = {'items': lambda: Defs.components_schemas_action, 'type': 'array'}
            meta = lambda: Defs.components_schemas_meta
        R.actions = [lambda: Defs.components_schemas_action]
        R.meta = lambda: Defs.components_schemas_meta
    class components_schemas_assign_floating_ip_to_server_request:
        """#/components/schemas/assign_floating_ip_to_server_request"""
        class R:
            required = ['server']
            title = 'AssignFloatingIPRequest'
            type = 'object'
            description = 'Request for POST https://api.hetzner.cloud/v1/floating_ips/{id}/actions/assign'
            _attrs = ['server']
            server = {'example': 42, 'type': 'integer', 'descr': 'ID of the Server the Floating IP shall be assigned to'}
        R.server = 42
    class components_schemas_assign_floating_ip_to_server_response:
        """#/components/schemas/assign_floating_ip_to_server_response"""
        class R:
            required = ['action']
            title = 'ActionResponse'
            type = 'object'
            description = 'Response to POST https://api.hetzner.cloud/v1/floating_ips/{id}/actions/assign'
            _attrs = ['action']
            action = lambda: Defs.components_schemas_action
        R.action = lambda: Defs.components_schemas_action
    class components_schemas_assign_primary_ip_to_resource_request:
        """#/components/schemas/assign_primary_ip_to_resource_request"""
        class R:
            required = ['assignee_type', 'assignee_id']
            title = 'AssignPrimaryIPRequest'
            type = 'object'
            description = 'Request for POST https://api.hetzner.cloud/v1/primary_ips/{id}/actions/assign'
            _attrs = ['assignee_id', 'assignee_type']
            assignee_id = {'example': 4711, 'type': 'integer', 'descr': 'ID of a resource of type `assignee_type`'}
            assignee_type = {'enum': ['server'], 'example': 'server', 'type': 'string', 'descr': 'Type of resource assigning the Primary IP to'}
        R.assignee_id = 4711
        R.assignee_type = 'server'
    class components_schemas_assign_primary_ip_to_resource_response:
        """#/components/schemas/assign_primary_ip_to_resource_response"""
        class R:
            required = ['action']
            title = 'ActionResponse'
            type = 'object'
            description = 'Response to POST https://api.hetzner.cloud/v1/primary_ips/{id}/actions/assign'
            _attrs = ['action']
            action = lambda: Defs.components_schemas_action
        R.action = lambda: Defs.components_schemas_action
    class components_schemas_attach_iso_to_server_request:
        """#/components/schemas/attach_iso_to_server_request"""
        class R:
            required = ['iso']
            type = 'object'
            description = 'Request for POST https://api.hetzner.cloud/v1/servers/{id}/actions/attach_iso'
            _attrs = ['iso']
            iso = {'example': 'FreeBSD-11.0-RELEASE-amd64-dvd1', 'type': 'string', 'descr': 'ID or name of ISO to attach to the Server as listed in GET `/isos`'}
        R.iso = 'FreeBSD-11.0-RELEASE-amd64-dvd1'
    class components_schemas_attach_iso_to_server_response:
        """#/components/schemas/attach_iso_to_server_response"""
        class R:
            required = ['action']
            title = 'ActionResponse'
            type = 'object'
            description = 'Response to POST https://api.hetzner.cloud/v1/servers/{id}/actions/attach_iso'
            _attrs = ['action']
            action = lambda: Defs.components_schemas_action
        R.action = lambda: Defs.components_schemas_action
    class components_schemas_attach_load_balancer_to_network_request:
        """#/components/schemas/attach_load_balancer_to_network_request"""
        class R:
            required = ['network']
            type = 'object'
            description = 'Request for POST https://api.hetzner.cloud/v1/load_balancers/{id}/actions/attach_to_network'
            _attrs = ['ip', 'network']
            ip = {'example': '10.0.1.1', 'type': 'string', 'descr': 'IP to request to be assigned to this Load Balancer; if you do not provide this then you will be auto assigned an IP address'}
            network = {'example': 4711, 'type': 'integer', 'descr': 'ID of an existing network to attach the Load Balancer to'}
        R.ip = '10.0.1.1'
        R.network = 4711
    class components_schemas_attach_load_balancer_to_network_response:
        """#/components/schemas/attach_load_balancer_to_network_response"""
        class R:
            required = ['action']
            title = 'ActionResponse'
            type = 'object'
            description = 'Response to POST https://api.hetzner.cloud/v1/load_balancers/{id}/actions/attach_to_network'
            _attrs = ['action']
            action = lambda: Defs.components_schemas_action
        R.action = lambda: Defs.components_schemas_action
    class components_schemas_attach_server_to_network_request:
        """#/components/schemas/attach_server_to_network_request"""
        class R:
            required = ['network']
            title = 'AttachToNetworkRequest'
            type = 'object'
            description = 'Request for POST https://api.hetzner.cloud/v1/servers/{id}/actions/attach_to_network'
            _attrs = ['alias_ips', 'ip', 'network']
            alias_ips = {'example': ['10.0.1.2'], 'items': {'type': 'string'}, 'type': 'array', 'descr': 'Additional IPs to be assigned to this Server'}
            ip = {'example': '10.0.1.1', 'type': 'string', 'descr': 'IP to request to be assigned to this Server; if you do not provide this then you will be auto assigned an IP address'}
            network = {'example': 4711, 'type': 'integer', 'descr': 'ID of an existing network to attach the Server to'}
        R.alias_ips = ['10.0.1.2']
        R.ip = '10.0.1.1'
        R.network = 4711
    class components_schemas_attach_server_to_network_response:
        """#/components/schemas/attach_server_to_network_response"""
        class R:
            required = ['action']
            title = 'ActionResponse'
            type = 'object'
            description = 'Response to POST https://api.hetzner.cloud/v1/servers/{id}/actions/attach_to_network'
            _attrs = ['action']
            action = lambda: Defs.components_schemas_action
        R.action = lambda: Defs.components_schemas_action
    class components_schemas_attach_volume_to_server_request:
        """#/components/schemas/attach_volume_to_server_request"""
        class R:
            required = ['server']
            title = 'AttachVolumeRequest'
            type = 'object'
            description = 'Request for POST https://api.hetzner.cloud/v1/volumes/{id}/actions/attach'
            _attrs = ['automount', 'server']
            automount = {'example': False, 'type': 'boolean', 'descr': 'Auto-mount the Volume after attaching it'}
            server = {'example': 43, 'type': 'integer', 'descr': 'ID of the Server the Volume will be attached to'}
        R.automount = True
        R.server = 43
    class components_schemas_attach_volume_to_server_response:
        """#/components/schemas/attach_volume_to_server_response"""
        class R:
            required = ['action']
            title = 'ActionResponse'
            type = 'object'
            description = 'Response to POST https://api.hetzner.cloud/v1/volumes/{id}/actions/attach'
            _attrs = ['action']
            action = lambda: Defs.components_schemas_action
        R.action = lambda: Defs.components_schemas_action
    class components_schemas_certificate:
        """#/components/schemas/certificate"""
        class R:
            required = ['id', 'name', 'labels', 'certificate', 'created', 'not_valid_before', 'not_valid_after', 'domain_names', 'fingerprint', 'used_by']
            title = 'Certificate'
            type = 'object'
            description = 'TLS/SSL Certificates prove the identity of a Server and are used to encrypt client traffic.'
            _attrs = ['certificate', 'created', 'domain_names', 'fingerprint', 'id', 'labels', 'name', 'not_valid_after', 'not_valid_before', 'status', 'type', 'used_by']
            certificate = {'example': '-----BEGIN CERTIFICATE-----\n...', 'nullable': True, 'type': 'string', 'descr': 'Certificate and chain in PEM format, in order so that each record directly certifies the one preceding'}
            created = {'example': '2016-01-30T23:55:00+00:00', 'type': 'string', 'descr': 'Point in time when the Resource was created (in ISO-8601 format)'}
            domain_names = {'example': ['example.com', 'webmail.example.com', 'www.example.com'], 'items': {'type': 'string'}, 'type': 'array', 'descr': 'Domains and subdomains covered by the Certificate'}
            fingerprint = {'example': '03:c7:55:9b:2a:d1:04:17:09:f6:d0:7f:18:34:63:d4:3e:5f', 'nullable': True, 'type': 'string', 'descr': 'SHA256 fingerprint of the Certificate'}
            id = {'example': 42, 'type': 'integer', 'descr': 'ID of the Resource'}
            labels = lambda: Defs.components_schemas_labels
            name = {'example': 'my-resource', 'type': 'string', 'descr': 'Name of the Resource. Must be unique per Project.'}
            not_valid_after = {'example': '2019-07-08T09:59:59+00:00', 'nullable': True, 'type': 'string', 'descr': 'Point in time when the Certificate stops being valid (in ISO-8601 format)'}
            not_valid_before = {'example': '2019-01-08T10:00:00+00:00', 'nullable': True, 'type': 'string', 'descr': 'Point in time when the Certificate becomes valid (in ISO-8601 format)'}
            code = {'type': 'string'}
            message = {'type': 'string'}
            error = {'example': None, 'nullable': True, 'properties': {'code': {'type': 'string'}, 'message': {'type': 'string'}}, 'type': 'object', 'descr': 'If issuance or renewal reports `failed`, this property contains information about what happened'}
            issuance = {'enum': ['completed', 'failed', 'pending'], 'example': 'valid', 'type': 'string', 'descr': 'Status of the issuance process of the Certificate'}
            renewal = {'enum': ['failed', 'pending', 'scheduled', 'unavailable'], 'example': 'scheduled', 'type': 'string', 'descr': 'Status of the renewal process of the Certificate.'}
            status = {'nullable': True, 'properties': {'error': {'description': 'If issuance or renewal reports `failed`, this property contains information about what happened', 'example': None, 'nullable': True, 'properties': {'code': {'type': 'string'}, 'message': {'type': 'string'}}, 'type': 'object'}, 'issuance': {'description': 'Status of the issuance process of the Certificate', 'enum': ['completed', 'failed', 'pending'], 'example': 'valid', 'type': 'string'}, 'renewal': {'description': 'Status of the renewal process of the Certificate.', 'enum': ['failed', 'pending', 'scheduled', 'unavailable'], 'example': 'scheduled', 'type': 'string'}}, 'type': 'object', 'descr': 'Current status of a type `managed` Certificate, always *null* for type `uploaded` Certificates'}
            type = {'enum': ['managed', 'uploaded'], 'example': 'uploaded', 'type': 'string', 'descr': 'Type of the Certificate'}
            used_by = {'items': lambda: Defs.components_schemas_resource, 'type': 'array', 'descr': 'Resources currently using the Certificate'}
        R.certificate = '-----BEGIN CERTIFICATE-----\n...'
        R.created = '2016-01-30T23:55:00+00:00'
        R.domain_names = ['example.com', 'webmail.example.com', 'www.example.com']
        R.fingerprint = '03:c7:55:9b:2a:d1:04:17:09:f6:d0:7f:18:34:63:d4:3e:5f'
        R.id = id
        R.labels = lambda: Defs.components_schemas_labels
        R.name = 'my-resource'
        R.not_valid_after = '2019-07-08T09:59:59+00:00'
        R.not_valid_before = '2019-01-08T10:00:00+00:00'
        R.status = dict(error = dict(code = str_dflt, message = str_dflt), issuance = 'valid', renewal = 'scheduled')
        R.type = 'uploaded'
        R.used_by = [lambda: Defs.components_schemas_resource]
    class components_schemas_change_algorithm_request:
        """#/components/schemas/change_algorithm_request"""
        class R:
            dollar_ref = lambda: Defs.components_schemas_load_balancer_algorithm
    class components_schemas_change_algorithm_response:
        """#/components/schemas/change_algorithm_response"""
        class R:
            required = ['action']
            title = 'ActionResponse'
            type = 'object'
            description = 'Response to POST https://api.hetzner.cloud/v1/load_balancers/{id}/actions/change_algorithm'
            _attrs = ['action']
            action = lambda: Defs.components_schemas_action
        R.action = lambda: Defs.components_schemas_action
    class components_schemas_change_alias_ips_of_network_request:
        """#/components/schemas/change_alias_ips_of_network_request"""
        class R:
            required = ['network', 'alias_ips']
            type = 'object'
            description = 'Request for POST https://api.hetzner.cloud/v1/servers/{id}/actions/change_alias_ips'
            _attrs = ['alias_ips', 'network']
            alias_ips = {'example': ['10.0.1.2'], 'items': {'type': 'string'}, 'type': 'array', 'descr': 'New alias IPs to set for this Server'}
            network = {'example': 4711, 'type': 'integer', 'descr': 'ID of an existing Network already attached to the Server'}
        R.alias_ips = ['10.0.1.2']
        R.network = 4711
    class components_schemas_change_alias_ips_of_network_response:
        """#/components/schemas/change_alias_ips_of_network_response"""
        class R:
            required = ['action']
            title = 'ActionResponse'
            type = 'object'
            description = 'Response to POST https://api.hetzner.cloud/v1/servers/{id}/actions/change_alias_ips'
            _attrs = ['action']
            action = lambda: Defs.components_schemas_action
        R.action = lambda: Defs.components_schemas_action
    class components_schemas_change_floating_ip_protection_request:
        """#/components/schemas/change_floating_ip_protection_request"""
        class R:
            title = 'ChangeProtectionRequest'
            type = 'object'
            description = 'Request for POST https://api.hetzner.cloud/v1/floating_ips/{id}/actions/change_protection'
            _attrs = ['delete']
            delete = {'example': True, 'type': 'boolean', 'descr': 'If true, prevents the Floating IP from being deleted'}
        R.delete = True
    class components_schemas_change_floating_ip_protection_response:
        """#/components/schemas/change_floating_ip_protection_response"""
        class R:
            required = ['action']
            title = 'ActionResponse'
            type = 'object'
            description = 'Response to POST https://api.hetzner.cloud/v1/floating_ips/{id}/actions/change_protection'
            _attrs = ['action']
            action = lambda: Defs.components_schemas_action
        R.action = lambda: Defs.components_schemas_action
    class components_schemas_change_image_protection_request:
        """#/components/schemas/change_image_protection_request"""
        class R:
            type = 'object'
            description = 'Request for POST https://api.hetzner.cloud/v1/images/{id}/actions/change_protection'
            _attrs = ['delete']
            delete = {'example': True, 'type': 'boolean', 'descr': 'If true, prevents the snapshot from being deleted'}
        R.delete = True
    class components_schemas_change_image_protection_response:
        """#/components/schemas/change_image_protection_response"""
        class R:
            required = ['action']
            title = 'ActionResponse'
            type = 'object'
            description = 'Response to POST https://api.hetzner.cloud/v1/images/{id}/actions/change_protection'
            _attrs = ['action']
            action = lambda: Defs.components_schemas_action
        R.action = lambda: Defs.components_schemas_action
    class components_schemas_change_ip_range_of_network_request:
        """#/components/schemas/change_ip_range_of_network_request"""
        class R:
            required = ['ip_range']
            title = 'ChangeIPRangeRequest'
            type = 'object'
            description = 'Request for POST https://api.hetzner.cloud/v1/networks/{id}/actions/change_ip_range'
            _attrs = ['ip_range']
            ip_range = {'example': '10.0.0.0/12', 'type': 'string', 'descr': 'The new prefix for the whole Network'}
        R.ip_range = '10.0.0.0/12'
    class components_schemas_change_ip_range_of_network_response:
        """#/components/schemas/change_ip_range_of_network_response"""
        class R:
            required = ['action']
            title = 'ActionResponse'
            type = 'object'
            description = 'Response to POST https://api.hetzner.cloud/v1/networks/{id}/actions/change_ip_range'
            _attrs = ['action']
            action = lambda: Defs.components_schemas_action
        R.action = lambda: Defs.components_schemas_action
    class components_schemas_change_load_balancer_protection_request:
        """#/components/schemas/change_load_balancer_protection_request"""
        class R:
            type = 'object'
            description = 'Request for POST https://api.hetzner.cloud/v1/load_balancers/{id}/actions/change_protection'
            _attrs = ['delete']
            delete = {'example': True, 'type': 'boolean', 'descr': 'If true, prevents the Load Balancer from being deleted'}
        R.delete = True
    class components_schemas_change_load_balancer_protection_response:
        """#/components/schemas/change_load_balancer_protection_response"""
        class R:
            required = ['action']
            title = 'ActionResponse'
            type = 'object'
            description = 'Response to POST https://api.hetzner.cloud/v1/load_balancers/{id}/actions/change_protection'
            _attrs = ['action']
            action = lambda: Defs.components_schemas_action
        R.action = lambda: Defs.components_schemas_action
    class components_schemas_change_network_protection_request:
        """#/components/schemas/change_network_protection_request"""
        class R:
            title = 'ChangeProtectionRequest'
            type = 'object'
            description = 'Request for POST https://api.hetzner.cloud/v1/networks/{id}/actions/change_protection'
            _attrs = ['delete']
            delete = {'example': True, 'type': 'boolean', 'descr': 'If true, prevents the Network from being deleted'}
        R.delete = True
    class components_schemas_change_network_protection_response:
        """#/components/schemas/change_network_protection_response"""
        class R:
            required = ['action']
            title = 'ActionResponse'
            type = 'object'
            description = 'Response to POST https://api.hetzner.cloud/v1/networks/{id}/actions/change_protection'
            _attrs = ['action']
            action = lambda: Defs.components_schemas_action
        R.action = lambda: Defs.components_schemas_action
    class components_schemas_change_primary_ip_protection_request:
        """#/components/schemas/change_primary_ip_protection_request"""
        class R:
            title = 'ChangeProtectionRequest'
            type = 'object'
            description = 'Request for POST https://api.hetzner.cloud/v1/primary_ips/{id}/actions/change_protection'
            _attrs = ['delete']
            delete = {'example': True, 'type': 'boolean', 'descr': 'If true, prevents the Primary IP from being deleted'}
        R.delete = True
    class components_schemas_change_primary_ip_protection_response:
        """#/components/schemas/change_primary_ip_protection_response"""
        class R:
            required = ['action']
            title = 'ActionResponse'
            type = 'object'
            description = 'Response to POST https://api.hetzner.cloud/v1/primary_ips/{id}/actions/change_protection'
            _attrs = ['action']
            action = lambda: Defs.components_schemas_action
        R.action = lambda: Defs.components_schemas_action
    class components_schemas_change_reverse_dns_entry_for_floating_ip_request:
        """#/components/schemas/change_reverse_dns_entry_for_floating_ip_request"""
        class R:
            required = ['ip', 'dns_ptr']
            title = 'ChangeDNSPTRRequest'
            type = 'object'
            description = 'Request for POST https://api.hetzner.cloud/v1/floating_ips/{id}/actions/change_dns_ptr'
            _attrs = ['dns_ptr', 'ip']
            dns_ptr = {'example': 'server02.example.com', 'nullable': True, 'type': 'string', 'descr': 'Hostname to set as a reverse DNS PTR entry, will reset to original default value if `null`'}
            ip = {'example': '1.2.3.4', 'type': 'string', 'descr': 'IP address for which to set the reverse DNS entry'}
        R.dns_ptr = 'server02.example.com'
        R.ip = '1.2.3.4'
    class components_schemas_change_reverse_dns_entry_for_floating_ip_response:
        """#/components/schemas/change_reverse_dns_entry_for_floating_ip_response"""
        class R:
            required = ['action']
            title = 'ActionResponse'
            type = 'object'
            description = 'Response to POST https://api.hetzner.cloud/v1/floating_ips/{id}/actions/change_dns_ptr'
            _attrs = ['action']
            action = lambda: Defs.components_schemas_action
        R.action = lambda: Defs.components_schemas_action
    class components_schemas_change_reverse_dns_entry_for_primary_ip_request:
        """#/components/schemas/change_reverse_dns_entry_for_primary_ip_request"""
        class R:
            required = ['ip', 'dns_ptr']
            title = 'ChangeDNSPTRRequest'
            type = 'object'
            description = 'Request for POST https://api.hetzner.cloud/v1/primary_ips/{id}/actions/change_dns_ptr'
            _attrs = ['dns_ptr', 'ip']
            dns_ptr = {'example': 'server02.example.com', 'nullable': True, 'type': 'string', 'descr': 'Hostname to set as a reverse DNS PTR entry, will reset to original default value if `null`'}
            ip = {'example': '1.2.3.4', 'type': 'string', 'descr': 'IP address for which to set the reverse DNS entry'}
        R.dns_ptr = 'server02.example.com'
        R.ip = '1.2.3.4'
    class components_schemas_change_reverse_dns_entry_for_primary_ip_response:
        """#/components/schemas/change_reverse_dns_entry_for_primary_ip_response"""
        class R:
            required = ['action']
            title = 'ActionResponse'
            type = 'object'
            description = 'Response to POST https://api.hetzner.cloud/v1/primary_ips/{id}/actions/change_dns_ptr'
            _attrs = ['action']
            action = lambda: Defs.components_schemas_action
        R.action = lambda: Defs.components_schemas_action
    class components_schemas_change_reverse_dns_entry_for_this_load_balancer_request:
        """#/components/schemas/change_reverse_dns_entry_for_this_load_balancer_request"""
        class R:
            required = ['ip', 'dns_ptr']
            title = 'ChangeLoadbalancerDnsPtrRequest'
            type = 'object'
            description = 'Request for POST https://api.hetzner.cloud/v1/load_balancers/{id}/actions/change_dns_ptr'
            _attrs = ['dns_ptr', 'ip']
            dns_ptr = {'example': 'lb1.example.com', 'nullable': True, 'type': 'string', 'descr': 'Hostname to set as a reverse DNS PTR entry'}
            ip = {'example': '1.2.3.4', 'type': 'string', 'descr': 'Public IP address for which the reverse DNS entry should be set'}
        R.dns_ptr = 'lb1.example.com'
        R.ip = '1.2.3.4'
    class components_schemas_change_reverse_dns_entry_for_this_load_balancer_response:
        """#/components/schemas/change_reverse_dns_entry_for_this_load_balancer_response"""
        class R:
            required = ['action']
            title = 'ActionResponse'
            type = 'object'
            description = 'Response to POST https://api.hetzner.cloud/v1/load_balancers/{id}/actions/change_dns_ptr'
            _attrs = ['action']
            action = lambda: Defs.components_schemas_action
        R.action = lambda: Defs.components_schemas_action
    class components_schemas_change_reverse_dns_entry_for_this_server_request:
        """#/components/schemas/change_reverse_dns_entry_for_this_server_request"""
        class R:
            required = ['ip', 'dns_ptr']
            type = 'object'
            description = 'Request for POST https://api.hetzner.cloud/v1/servers/{id}/actions/change_dns_ptr'
            _attrs = ['dns_ptr', 'ip']
            dns_ptr = {'example': 'server01.example.com', 'nullable': True, 'type': 'string', 'descr': 'Hostname to set as a reverse DNS PTR entry, reset to original value if `null`'}
            ip = {'example': '1.2.3.4', 'type': 'string', 'descr': 'Primary IP address for which the reverse DNS entry should be set'}
        R.dns_ptr = 'server01.example.com'
        R.ip = '1.2.3.4'
    class components_schemas_change_reverse_dns_entry_for_this_server_response:
        """#/components/schemas/change_reverse_dns_entry_for_this_server_response"""
        class R:
            required = ['action']
            title = 'ActionResponse'
            type = 'object'
            description = 'Response to POST https://api.hetzner.cloud/v1/servers/{id}/actions/change_dns_ptr'
            _attrs = ['action']
            action = lambda: Defs.components_schemas_action
        R.action = lambda: Defs.components_schemas_action
    class components_schemas_change_server_protection_request:
        """#/components/schemas/change_server_protection_request"""
        class R:
            type = 'object'
            description = 'Request for POST https://api.hetzner.cloud/v1/servers/{id}/actions/change_protection'
            _attrs = ['delete', 'rebuild']
            delete = {'example': True, 'type': 'boolean', 'descr': 'If true, prevents the Server from being deleted (currently delete and rebuild attribute needs to have the same value)'}
            rebuild = {'example': True, 'type': 'boolean', 'descr': 'If true, prevents the Server from being rebuilt (currently delete and rebuild attribute needs to have the same value)'}
        R.delete = True
        R.rebuild = True
    class components_schemas_change_server_protection_response:
        """#/components/schemas/change_server_protection_response"""
        class R:
            required = ['action']
            title = 'ActionResponse'
            type = 'object'
            description = 'Response to POST https://api.hetzner.cloud/v1/servers/{id}/actions/change_protection'
            _attrs = ['action']
            action = lambda: Defs.components_schemas_action
        R.action = lambda: Defs.components_schemas_action
    class components_schemas_change_type_of_load_balancer_request:
        """#/components/schemas/change_type_of_load_balancer_request"""
        class R:
            required = ['load_balancer_type']
            title = 'ChangeTypeRequest'
            type = 'object'
            description = 'Request for POST https://api.hetzner.cloud/v1/load_balancers/{id}/actions/change_type'
            _attrs = ['load_balancer_type']
            load_balancer_type = {'example': 'lb21', 'type': 'string', 'descr': 'ID or name of Load Balancer type the Load Balancer should migrate to'}
        R.load_balancer_type = 'lb21'
    class components_schemas_change_type_of_load_balancer_response:
        """#/components/schemas/change_type_of_load_balancer_response"""
        class R:
            required = ['action']
            title = 'ActionResponse'
            type = 'object'
            description = 'Response to POST https://api.hetzner.cloud/v1/load_balancers/{id}/actions/change_type'
            _attrs = ['action']
            action = lambda: Defs.components_schemas_action
        R.action = lambda: Defs.components_schemas_action
    class components_schemas_change_type_of_server_request:
        """#/components/schemas/change_type_of_server_request"""
        class R:
            required = ['upgrade_disk', 'server_type']
            type = 'object'
            description = 'Request for POST https://api.hetzner.cloud/v1/servers/{id}/actions/change_type'
            _attrs = ['server_type', 'upgrade_disk']
            server_type = {'example': 'cx11', 'type': 'string', 'descr': 'ID or name of Server type the Server should migrate to'}
            upgrade_disk = {'example': True, 'type': 'boolean', 'descr': 'If false, do not upgrade the disk (this allows downgrading the Server type later)'}
        R.server_type = 'cx11'
        R.upgrade_disk = True
    class components_schemas_change_type_of_server_response:
        """#/components/schemas/change_type_of_server_response"""
        class R:
            required = ['action']
            title = 'ActionResponse'
            type = 'object'
            description = 'Response to POST https://api.hetzner.cloud/v1/servers/{id}/actions/change_type'
            _attrs = ['action']
            action = lambda: Defs.components_schemas_action
        R.action = lambda: Defs.components_schemas_action
    class components_schemas_change_volume_protection_request:
        """#/components/schemas/change_volume_protection_request"""
        class R:
            type = 'object'
            description = 'Request for POST https://api.hetzner.cloud/v1/volumes/{id}/actions/change_protection'
            _attrs = ['delete']
            delete = {'example': True, 'type': 'boolean', 'descr': 'If true, prevents the Volume from being deleted'}
        R.delete = True
    class components_schemas_change_volume_protection_response:
        """#/components/schemas/change_volume_protection_response"""
        class R:
            required = ['action']
            title = 'ActionResponse'
            type = 'object'
            description = 'Response to POST https://api.hetzner.cloud/v1/volumes/{id}/actions/change_protection'
            _attrs = ['action']
            action = lambda: Defs.components_schemas_action
        R.action = lambda: Defs.components_schemas_action
    class components_schemas_create_certificate_request:
        """#/components/schemas/create_certificate_request"""
        class R:
            required = ['name']
            title = 'CreateCertificateRequest'
            type = 'object'
            description = 'Request for POST https://api.hetzner.cloud/v1/certificates'
            _attrs = ['certificate', 'domain_names', 'labels', 'name', 'private_key', 'type']
            certificate = {'example': '-----BEGIN CERTIFICATE-----\n...', 'type': 'string', 'descr': 'Certificate and chain in PEM format, in order so that each record directly certifies the one preceding. Required for type `uploaded` Certificates.'}
            domain_names = {'example': None, 'items': {'type': 'string'}, 'type': 'array', 'descr': "Domains and subdomains that should be contained in the Certificate issued by *Let's Encrypt*. Required for type `managed` Certificates."}
            labels = lambda: Defs.components_schemas_labels
            name = {'example': 'my website cert', 'type': 'string', 'descr': 'Name of the Certificate'}
            private_key = {'example': '-----BEGIN PRIVATE KEY-----\n...', 'type': 'string', 'descr': 'Certificate key in PEM format. Required for type `uploaded` Certificates.'}
            type = {'enum': ['managed', 'uploaded'], 'example': 'uploaded', 'type': 'string', 'descr': "Choose between uploading a Certificate in PEM format or requesting a managed *Let's Encrypt* Certificate. If omitted defaults to `uploaded`."}
        R.certificate = '-----BEGIN CERTIFICATE-----\n...'
        R.domain_names = [str_dflt]
        R.labels = lambda: Defs.components_schemas_labels
        R.name = 'my website cert'
        R.private_key = '-----BEGIN PRIVATE KEY-----\n...'
        R.type = 'uploaded'
    class components_schemas_create_certificate_response:
        """#/components/schemas/create_certificate_response"""
        class R:
            required = ['certificate']
            title = 'CreateCertificateResponse'
            type = 'object'
            description = 'Response to POST https://api.hetzner.cloud/v1/certificates'
            _attrs = ['action', 'certificate']
            action = lambda: Defs.components_schemas_action_optional
            certificate = lambda: Defs.components_schemas_certificate
        R.action = lambda: Defs.components_schemas_action_optional
        R.certificate = lambda: Defs.components_schemas_certificate
    class components_schemas_create_firewall_request:
        """#/components/schemas/create_firewall_request"""
        class R:
            required = ['name']
            title = 'CreateFirewallRequest'
            type = 'object'
            description = 'Request for POST https://api.hetzner.cloud/v1/firewalls'
            _attrs = ['apply_to', 'labels', 'name', 'rules']
            apply_to = {'items': lambda: Defs.components_schemas_firewall_resource_with_required_type, 'type': 'array', 'descr': 'Resources the Firewall should be applied to after creation'}
            labels = lambda: Defs.components_schemas_labels
            name = {'example': 'Corporate Intranet Protection', 'type': 'string', 'descr': 'Name of the Firewall'}
            rules = {'example': [{'direction': 'in', 'port': '80', 'protocol': 'tcp', 'source_ips': ['28.239.13.1/32', '28.239.14.0/24', 'ff21:1eac:9a3b:ee58:5ca:990c:8bc9:c03b/128']}], 'items': lambda: Defs.components_schemas_rule, 'type': 'array', 'descr': 'Array of rules'}
        R.apply_to = [lambda: Defs.components_schemas_firewall_resource_with_required_type]
        R.labels = lambda: Defs.components_schemas_labels
        R.name = 'Corporate Intranet Protection'
        R.rules = [{'direction': 'in', 'port': '80', 'protocol': 'tcp', 'source_ips': ['28.239.13.1/32', '28.239.14.0/24', 'ff21:1eac:9a3b:ee58:5ca:990c:8bc9:c03b/128']}]
    class components_schemas_create_firewall_response:
        """#/components/schemas/create_firewall_response"""
        class R:
            title = 'CreateFirewallResponse'
            type = 'object'
            description = 'Response to POST https://api.hetzner.cloud/v1/firewalls'
            _attrs = ['actions', 'firewall']
            actions = {'example': [{'command': 'set_firewall_rules', 'error': {'code': 'action_failed', 'message': 'Action failed'}, 'finished': '2016-01-30T23:56:00+00:00', 'id': 13, 'progress': 100, 'resources': [{'id': 38, 'type': 'firewall'}], 'started': '2016-01-30T23:55:00+00:00', 'status': 'success'}, {'command': 'apply_firewall', 'error': {'code': 'action_failed', 'message': 'Action failed'}, 'finished': '2016-01-30T23:56:00+00:00', 'id': 14, 'progress': 100, 'resources': [{'id': 42, 'type': 'server'}, {'id': 38, 'type': 'firewall'}], 'started': '2016-01-30T23:55:00+00:00', 'status': 'success'}], 'items': lambda: Defs.components_schemas_action, 'type': 'array'}
            firewall = lambda: Defs.components_schemas_firewall
        R.actions = [{'command': 'set_firewall_rules', 'error': {'code': 'action_failed', 'message': 'Action failed'}, 'finished': '2016-01-30T23:56:00+00:00', 'id': 13, 'progress': 100, 'resources': [{'id': 38, 'type': 'firewall'}], 'started': '2016-01-30T23:55:00+00:00', 'status': 'success'}, {'command': 'apply_firewall', 'error': {'code': 'action_failed', 'message': 'Action failed'}, 'finished': '2016-01-30T23:56:00+00:00', 'id': 14, 'progress': 100, 'resources': [{'id': 42, 'type': 'server'}, {'id': 38, 'type': 'firewall'}], 'started': '2016-01-30T23:55:00+00:00', 'status': 'success'}]
        R.firewall = lambda: Defs.components_schemas_firewall
    class components_schemas_create_floating_ip_request:
        """#/components/schemas/create_floating_ip_request"""
        class R:
            required = ['type']
            title = 'CreateFloatingIPRequest'
            type = 'object'
            description = 'Request for POST https://api.hetzner.cloud/v1/floating_ips'
            _attrs = ['description', 'home_location', 'labels', 'name', 'server', 'type']
            description = {'example': 'Web Frontend', 'type': 'string'}
            home_location = {'example': 'fsn1', 'type': 'string', 'descr': 'Home Location (routing is optimized for that Location). Only optional if Server argument is passed.'}
            labels = lambda: Defs.components_schemas_labels
            name = {'example': 'Web Frontend', 'type': 'string'}
            server = {'example': 42, 'type': 'integer', 'descr': 'Server to assign the Floating IP to'}
            type = lambda: Defs.components_schemas_ip_type
        R.description = 'Web Frontend'
        R.home_location = 'fsn1'
        R.labels = lambda: Defs.components_schemas_labels
        R.name = 'Web Frontend'
        R.server = 42
        R.type = lambda: Defs.components_schemas_ip_type
    class components_schemas_create_floating_ip_response:
        """#/components/schemas/create_floating_ip_response"""
        class R:
            required = ['floating_ip']
            type = 'object'
            description = 'Response to POST https://api.hetzner.cloud/v1/floating_ips'
            _attrs = ['action', 'floating_ip']
            action = lambda: Defs.components_schemas_action
            floating_ip = lambda: Defs.components_schemas_floating_ip
        R.action = lambda: Defs.components_schemas_action
        R.floating_ip = lambda: Defs.components_schemas_floating_ip
    class components_schemas_create_image_from_server_request:
        """#/components/schemas/create_image_from_server_request"""
        class R:
            title = 'CreateImageRequest'
            type = 'object'
            description = 'Request for POST https://api.hetzner.cloud/v1/servers/{id}/actions/create_image'
            _attrs = ['description', 'labels', 'type']
            description = {'example': 'my image', 'type': 'string', 'descr': 'Description of the Image, will be auto-generated if not set'}
            labels = lambda: Defs.components_schemas_labels
            type = {'enum': ['backup', 'snapshot'], 'example': 'snapshot', 'type': 'string', 'descr': 'Type of Image to create (default: `snapshot`)'}
        R.description = 'my image'
        R.labels = lambda: Defs.components_schemas_labels
        R.type = 'snapshot'
    class components_schemas_create_image_from_server_response:
        """#/components/schemas/create_image_from_server_response"""
        class R:
            type = 'object'
            description = 'Response to POST https://api.hetzner.cloud/v1/servers/{id}/actions/create_image'
            _attrs = ['action', 'image']
            action = lambda: Defs.components_schemas_action
            image = lambda: Defs.components_schemas_image
        R.action = lambda: Defs.components_schemas_action
        R.image = lambda: Defs.components_schemas_image
    class components_schemas_create_load_balancer_request:
        """#/components/schemas/create_load_balancer_request"""
        class R:
            required = ['name', 'load_balancer_type', 'algorithm']
            title = 'CreateLoadBalancerRequest'
            type = 'object'
            description = 'Request for POST https://api.hetzner.cloud/v1/load_balancers'
            _attrs = ['algorithm', 'labels', 'load_balancer_type', 'location', 'name', 'network', 'network_zone', 'public_interface', 'services', 'targets']
            algorithm = lambda: Defs.components_schemas_load_balancer_algorithm
            labels = lambda: Defs.components_schemas_labels
            load_balancer_type = {'example': 'lb11', 'type': 'string', 'descr': 'ID or name of the Load Balancer type this Load Balancer should be created with'}
            location = {'type': 'string', 'descr': 'ID or name of Location to create Load Balancer in'}
            name = {'example': 'Web Frontend', 'type': 'string', 'descr': 'Name of the Load Balancer'}
            network = {'example': 123, 'type': 'integer', 'descr': 'ID of the network the Load Balancer should be attached to on creation'}
            network_zone = {'example': 'eu-central', 'type': 'string', 'descr': 'Name of network zone'}
            public_interface = {'example': True, 'type': 'boolean', 'descr': 'Enable or disable the public interface of the Load Balancer'}
            services = {'items': lambda: Defs.components_schemas_load_balancer_service, 'type': 'array', 'descr': 'Array of services'}
            targets = {'items': lambda: Defs.components_schemas_target, 'type': 'array', 'descr': 'Array of targets'}
        R.algorithm = lambda: Defs.components_schemas_load_balancer_algorithm
        R.labels = lambda: Defs.components_schemas_labels
        R.load_balancer_type = 'lb11'
        R.location = str_dflt
        R.name = 'Web Frontend'
        R.network = 123
        R.network_zone = 'eu-central'
        R.public_interface = True
        R.services = [lambda: Defs.components_schemas_load_balancer_service]
        R.targets = [lambda: Defs.components_schemas_target]
    class components_schemas_create_load_balancer_response:
        """#/components/schemas/create_load_balancer_response"""
        class R:
            required = ['load_balancer', 'action']
            type = 'object'
            description = 'Response to POST https://api.hetzner.cloud/v1/load_balancers'
            _attrs = ['action', 'load_balancer']
            action = lambda: Defs.components_schemas_action
            load_balancer = lambda: Defs.components_schemas_load_balancer
        R.action = lambda: Defs.components_schemas_action
        R.load_balancer = lambda: Defs.components_schemas_load_balancer
    class components_schemas_create_network_request:
        """#/components/schemas/create_network_request"""
        class R:
            required = ['name', 'ip_range']
            title = 'CreateNetworkRequest'
            type = 'object'
            description = 'Request for POST https://api.hetzner.cloud/v1/networks'
            _attrs = ['ip_range', 'labels', 'name', 'routes', 'subnets']
            ip_range = {'example': '10.0.0.0/16', 'type': 'string', 'descr': 'IP range of the whole network which must span all included subnets. Must be one of the private IPv4 ranges of RFC1918. Minimum network size is /24. We highly recommend that you pick a larger network with a /16 netmask.'}
            labels = lambda: Defs.components_schemas_labels
            name = {'example': 'mynet', 'type': 'string', 'descr': 'Name of the network'}
            routes = {'items': lambda: Defs.components_schemas_route, 'type': 'array', 'descr': 'Array of routes set in this network. The destination of the route must be one of the private IPv4 ranges of RFC1918. The gateway must be a subnet/IP of the ip_range of the network object. The destination must not overlap with an existing ip_range in any subnets or with any destinations in other routes or with the first IP of the networks ip_range or with 172.31.1.1. The gateway cannot be the first IP of the networks ip_range and also cannot be 172.31.1.1.'}
            subnets = {'items': lambda: Defs.components_schemas_subnet, 'type': 'array', 'descr': 'Array of subnets allocated.'}
        R.ip_range = '10.0.0.0/16'
        R.labels = lambda: Defs.components_schemas_labels
        R.name = 'mynet'
        R.routes = [lambda: Defs.components_schemas_route]
        R.subnets = [lambda: Defs.components_schemas_subnet]
    class components_schemas_create_network_response:
        """#/components/schemas/create_network_response"""
        class R:
            type = 'object'
            description = 'Response to POST https://api.hetzner.cloud/v1/networks'
            _attrs = ['network']
            network = lambda: Defs.components_schemas_network
        R.network = lambda: Defs.components_schemas_network
    class components_schemas_create_placementgroup_request:
        """#/components/schemas/create_placementgroup_request"""
        class R:
            required = ['name', 'type']
            title = 'CreatePlacementGroupRequest'
            type = 'object'
            description = 'Request for POST https://api.hetzner.cloud/v1/placement_groups'
            _attrs = ['labels', 'name', 'type']
            labels = lambda: Defs.components_schemas_labels
            name = {'example': 'my Placement Group', 'type': 'string', 'descr': 'Name of the PlacementGroup'}
            type = {'enum': ['spread'], 'example': 'spread', 'type': 'string', 'descr': 'Define the Placement Group Type.'}
        R.labels = lambda: Defs.components_schemas_labels
        R.name = 'my Placement Group'
        R.type = 'spread'
    class components_schemas_create_placementgroup_response:
        """#/components/schemas/create_placementgroup_response"""
        class R:
            required = ['placement_group']
            title = 'CreatePlacementGroupResponse'
            type = 'object'
            description = 'Response to POST https://api.hetzner.cloud/v1/placement_groups'
            _attrs = ['action', 'placement_group']
            action = lambda: Defs.components_schemas_action_optional
            created = {'example': '2016-01-30T23:55:00+00:00', 'type': 'string', 'descr': 'Point in time when the Resource was created (in ISO-8601 format)'}
            id = {'example': 42, 'type': 'integer', 'descr': 'ID of the Resource'}
            labels = lambda: Defs.components_schemas_labels
            name = {'example': 'my-resource', 'type': 'string', 'descr': 'Name of the Resource. Must be unique per Project.'}
            servers = {'example': [42], 'items': {'type': 'integer'}, 'type': 'array', 'descr': 'Array of IDs of Servers that are part of this Placement Group'}
            type = {'enum': ['spread'], 'example': 'spread', 'type': 'string', 'descr': 'Type of the Placement Group'}
            placement_group = {'properties': {'created': {'description': 'Point in time when the Resource was created (in ISO-8601 format)', 'example': '2016-01-30T23:55:00+00:00', 'type': 'string'}, 'id': {'description': 'ID of the Resource', 'example': 42, 'type': 'integer'}, 'labels': lambda: Defs.components_schemas_labels, 'name': {'description': 'Name of the Resource. Must be unique per Project.', 'example': 'my-resource', 'type': 'string'}, 'servers': {'description': 'Array of IDs of Servers that are part of this Placement Group', 'example': [42], 'items': {'type': 'integer'}, 'type': 'array'}, 'type': {'description': 'Type of the Placement Group', 'enum': ['spread'], 'example': 'spread', 'type': 'string'}}, 'required': ['id', 'name', 'labels', 'type', 'created', 'servers'], 'title': 'PlacementGroup', 'type': 'object'}
        R.action = lambda: Defs.components_schemas_action_optional
        R.placement_group = dict(created = '2016-01-30T23:55:00+00:00', id = id, labels = lambda: Defs.components_schemas_labels, name = 'my-resource', servers = [42], type = 'spread')
    class components_schemas_create_primary_ip_request:
        """#/components/schemas/create_primary_ip_request"""
        class R:
            required = ['name', 'type', 'assignee_type']
            title = 'CreatePrimaryIPRequest'
            type = 'object'
            description = 'Request for POST https://api.hetzner.cloud/v1/primary_ips'
            _attrs = ['assignee_id', 'assignee_type', 'auto_delete', 'datacenter', 'labels', 'name', 'type']
            assignee_id = {'example': 17, 'type': 'integer', 'descr': 'ID of the resource the Primary IP should be assigned to. Omitted if it should not be assigned.'}
            assignee_type = {'enum': ['server'], 'example': 'server', 'type': 'string', 'descr': 'Resource type the Primary IP can be assigned to'}
            auto_delete = {'example': False, 'type': 'boolean', 'descr': 'Delete the Primary IP when the Server it is assigned to is deleted. If omitted defaults to `false`.'}
            datacenter = {'example': 'fsn1-dc8', 'type': 'string', 'descr': 'ID or name of Datacenter the Primary IP will be bound to. Needs to be omitted if `assignee_id` is passed.'}
            labels = lambda: Defs.components_schemas_labels
            name = {'example': 'my-ip', 'type': 'string'}
            type = lambda: Defs.components_schemas_ip_type
        R.assignee_id = 17
        R.assignee_type = 'server'
        R.auto_delete = True
        R.datacenter = 'fsn1-dc8'
        R.labels = lambda: Defs.components_schemas_labels
        R.name = 'my-ip'
        R.type = lambda: Defs.components_schemas_ip_type
    class components_schemas_create_primary_ip_response:
        """#/components/schemas/create_primary_ip_response"""
        class R:
            required = ['primary_ip']
            title = 'CreatePrimaryIPResponse'
            type = 'object'
            description = 'Response to POST https://api.hetzner.cloud/v1/primary_ips'
            _attrs = ['action', 'primary_ip']
            action = lambda: Defs.components_schemas_action
            assignee_id = {'example': 17, 'nullable': True, 'type': 'integer', 'descr': 'ID of the resource the Primary IP is assigned to, null if it is not assigned at all'}
            assignee_type = {'enum': ['server'], 'type': 'string', 'descr': 'Resource type the Primary IP can be assigned to'}
            auto_delete = {'example': True, 'type': 'boolean', 'descr': 'Delete this Primary IP when the resource it is assigned to is deleted'}
            blocked = {'example': False, 'type': 'boolean', 'descr': 'Whether the IP is blocked'}
            created = {'example': '2016-01-30T23:55:00+00:00', 'type': 'string', 'descr': 'Point in time when the Resource was created (in ISO-8601 format)'}
            datacenter = lambda: Defs.components_schemas_datacenter
            dns_ptr = {'items': lambda: Defs.components_schemas_dns_ptr, 'type': 'array', 'descr': 'Array of reverse DNS entries'}
            id = {'example': 42, 'type': 'integer', 'descr': 'ID of the Resource'}
            ip = {'example': '131.232.99.1', 'type': 'string', 'descr': 'IP address'}
            labels = lambda: Defs.components_schemas_labels
            name = {'example': 'my-resource', 'type': 'string', 'descr': 'Name of the Resource. Must be unique per Project.'}
            protection = lambda: Defs.components_schemas_protection
            type = lambda: Defs.components_schemas_ip_type
            primary_ip = {'properties': {'assignee_id': {'description': 'ID of the resource the Primary IP is assigned to, null if it is not assigned at all', 'example': 17, 'nullable': True, 'type': 'integer'}, 'assignee_type': {'description': 'Resource type the Primary IP can be assigned to', 'enum': ['server'], 'type': 'string'}, 'auto_delete': {'description': 'Delete this Primary IP when the resource it is assigned to is deleted', 'example': True, 'type': 'boolean'}, 'blocked': {'description': 'Whether the IP is blocked', 'example': False, 'type': 'boolean'}, 'created': {'description': 'Point in time when the Resource was created (in ISO-8601 format)', 'example': '2016-01-30T23:55:00+00:00', 'type': 'string'}, 'datacenter': lambda: Defs.components_schemas_datacenter, 'dns_ptr': {'description': 'Array of reverse DNS entries', 'items': lambda: Defs.components_schemas_dns_ptr, 'type': 'array'}, 'id': {'description': 'ID of the Resource', 'example': 42, 'type': 'integer'}, 'ip': {'description': 'IP address', 'example': '131.232.99.1', 'type': 'string'}, 'labels': lambda: Defs.components_schemas_labels, 'name': {'description': 'Name of the Resource. Must be unique per Project.', 'example': 'my-resource', 'type': 'string'}, 'protection': lambda: Defs.components_schemas_protection, 'type': lambda: Defs.components_schemas_ip_type}, 'required': ['id', 'name', 'labels', 'created', 'blocked', 'datacenter', 'ip', 'dns_ptr', 'protection', 'type', 'auto_delete', 'assignee_type', 'assignee_id'], 'title': 'PrimaryIP', 'type': 'object'}
        R.action = lambda: Defs.components_schemas_action
        R.primary_ip = dict(assignee_id = 17, assignee_type = 'server', auto_delete = True, blocked = True, created = '2016-01-30T23:55:00+00:00', datacenter = lambda: Defs.components_schemas_datacenter, dns_ptr = [lambda: Defs.components_schemas_dns_ptr], id = id, ip = '131.232.99.1', labels = lambda: Defs.components_schemas_labels, name = 'my-resource', protection = lambda: Defs.components_schemas_protection, type = lambda: Defs.components_schemas_ip_type)
    class components_schemas_create_server_request:
        """#/components/schemas/create_server_request"""
        class R:
            required = ['name', 'server_type', 'image']
            title = 'CreateServerRequest'
            type = 'object'
            description = 'Request for POST https://api.hetzner.cloud/v1/servers'
            _attrs = ['automount', 'datacenter', 'firewalls', 'image', 'labels', 'location', 'name', 'networks', 'placement_group', 'public_net', 'server_type', 'ssh_keys', 'start_after_create', 'user_data', 'volumes']
            automount = {'example': False, 'type': 'boolean', 'descr': 'Auto-mount Volumes after attach'}
            datacenter = {'example': 'nbg1-dc3', 'type': 'string', 'descr': 'ID or name of Datacenter to create Server in (must not be used together with location)'}
            firewall = {'type': 'integer', 'descr': 'ID of the Firewall'}
            firewalls = {'example': [{'firewall': 38}], 'items': {'properties': {'firewall': {'description': 'ID of the Firewall', 'type': 'integer'}}, 'type': 'object', 'required': ['firewall'], 'title': 'CreateServerRequestFirewalls'}, 'type': 'array', 'descr': "Firewalls which should be applied on the Server's public network interface at creation time"}
            image = {'example': 'ubuntu-20.04', 'type': 'string', 'descr': 'ID or name of the Image the Server is created from'}
            labels = lambda: Defs.components_schemas_labels
            location = {'example': 'nbg1', 'type': 'string', 'descr': 'ID or name of Location to create Server in (must not be used together with datacenter)'}
            name = {'example': 'my-server', 'type': 'string', 'descr': 'Name of the Server to create (must be unique per Project and a valid hostname as per RFC 1123)'}
            networks = {'example': [456], 'items': {'type': 'integer'}, 'type': 'array', 'descr': 'Network IDs which should be attached to the Server private network interface at the creation time'}
            placement_group = {'example': 1, 'type': 'integer', 'descr': 'ID of the Placement Group the server should be in'}
            enable_ipv4 = {'type': 'boolean', 'descr': 'Attach an IPv4 on the public NIC. If false, no IPv4 address will be attached. Defaults to true.'}
            enable_ipv6 = {'type': 'boolean', 'descr': 'Attach an IPv6 on the public NIC. If false, no IPv6 address will be attached. Defaults to true.'}
            ipv4 = {'nullable': True, 'type': 'integer', 'descr': 'ID of the ipv4 Primary IP to use. If omitted and enable_ipv4 is true, a new ipv4 Primary IP will automatically be created.'}
            ipv6 = {'nullable': True, 'type': 'integer', 'descr': 'ID of the ipv6 Primary IP to use. If omitted and enable_ipv6 is true, a new ipv6 Primary IP will automatically be created.'}
            public_net = {'properties': {'enable_ipv4': {'description': 'Attach an IPv4 on the public NIC. If false, no IPv4 address will be attached. Defaults to true.', 'type': 'boolean'}, 'enable_ipv6': {'description': 'Attach an IPv6 on the public NIC. If false, no IPv6 address will be attached. Defaults to true.', 'type': 'boolean'}, 'ipv4': {'description': 'ID of the ipv4 Primary IP to use. If omitted and enable_ipv4 is true, a new ipv4 Primary IP will automatically be created.', 'nullable': True, 'type': 'integer'}, 'ipv6': {'description': 'ID of the ipv6 Primary IP to use. If omitted and enable_ipv6 is true, a new ipv6 Primary IP will automatically be created.', 'nullable': True, 'type': 'integer'}}, 'type': 'object', 'descr': 'Public Network options'}
            server_type = {'example': 'cx11', 'type': 'string', 'descr': 'ID or name of the Server type this Server should be created with'}
            ssh_keys = {'example': ['my-ssh-key'], 'items': {'type': 'string'}, 'type': 'array', 'descr': 'SSH key IDs (`integer`) or names (`string`) which should be injected into the Server at creation time'}
            start_after_create = {'example': True, 'type': 'boolean', 'descr': 'Start Server right after creation. Defaults to true.'}
            user_data = {'example': '#cloud-config\nruncmd:\n- [touch, /root/cloud-init-worked]\n', 'type': 'string', 'descr': 'Cloud-Init user data to use during Server creation. This field is limited to 32KiB.'}
            volumes = {'example': [123], 'items': {'type': 'integer'}, 'type': 'array', 'descr': 'Volume IDs which should be attached to the Server at the creation time. Volumes must be in the same Location.'}
        R.automount = True
        R.datacenter = 'nbg1-dc3'
        R.firewalls = [{'firewall': 38}]
        R.image = 'ubuntu-20.04'
        R.labels = lambda: Defs.components_schemas_labels
        R.location = 'nbg1'
        R.name = 'my-server'
        R.networks = [456]
        R.placement_group = 1
        R.public_net = dict(enable_ipv4 = True, enable_ipv6 = True, ipv4 = 0, ipv6 = 0)
        R.server_type = 'cx11'
        R.ssh_keys = ['my-ssh-key']
        R.start_after_create = True
        R.user_data = '#cloud-config\nruncmd:\n- [touch, /root/cloud-init-worked]\n'
        R.volumes = [123]
    class components_schemas_create_server_response:
        """#/components/schemas/create_server_response"""
        class R:
            required = ['server', 'action', 'next_actions', 'root_password']
            title = 'CreateServerResponse'
            type = 'object'
            description = 'Response to POST https://api.hetzner.cloud/v1/servers'
            _attrs = ['action', 'next_actions', 'root_password', 'server']
            action = lambda: Defs.components_schemas_action
            next_actions = {'items': lambda: Defs.components_schemas_action, 'type': 'array'}
            root_password = {'example': 'YItygq1v3GYjjMomLaKc', 'nullable': True, 'type': 'string', 'descr': 'Root password when no SSH keys have been specified'}
            server = lambda: Defs.components_schemas_server
        R.action = lambda: Defs.components_schemas_action
        R.next_actions = [lambda: Defs.components_schemas_action]
        R.root_password = 'YItygq1v3GYjjMomLaKc'
        R.server = lambda: Defs.components_schemas_server
    class components_schemas_create_ssh_key_request:
        """#/components/schemas/create_ssh_key_request"""
        class R:
            required = ['name', 'public_key']
            type = 'object'
            description = 'Request for POST https://api.hetzner.cloud/v1/ssh_keys'
            _attrs = ['labels', 'name', 'public_key']
            labels = lambda: Defs.components_schemas_labels
            name = {'example': 'My ssh key', 'type': 'string', 'descr': 'Name of the SSH key'}
            public_key = {'example': 'ssh-rsa AAAjjk76kgf...Xt', 'type': 'string', 'descr': 'Public key'}
        R.labels = lambda: Defs.components_schemas_labels
        R.name = 'My ssh key'
        R.public_key = 'ssh-rsa AAAjjk76kgf...Xt'
    class components_schemas_create_ssh_key_response:
        """#/components/schemas/create_ssh_key_response"""
        class R:
            required = ['ssh_key']
            type = 'object'
            description = 'Response to POST https://api.hetzner.cloud/v1/ssh_keys'
            _attrs = ['ssh_key']
            ssh_key = lambda: Defs.components_schemas_ssh_key
        R.ssh_key = lambda: Defs.components_schemas_ssh_key
    class components_schemas_create_volume_request:
        """#/components/schemas/create_volume_request"""
        class R:
            required = ['size', 'name']
            title = 'CreateVolumeRequest'
            type = 'object'
            description = 'Request for POST https://api.hetzner.cloud/v1/volumes'
            _attrs = ['automount', 'format', 'labels', 'location', 'name', 'server', 'size']
            automount = {'example': False, 'type': 'boolean', 'descr': 'Auto-mount Volume after attach. `server` must be provided.'}
            format = {'example': 'xfs', 'type': 'string', 'descr': 'Format Volume after creation. One of: `xfs`, `ext4`'}
            labels = lambda: Defs.components_schemas_labels
            location = {'example': 'nbg1', 'type': 'string', 'descr': 'Location to create the Volume in (can be omitted if Server is specified)'}
            name = {'example': 'databases-storage', 'type': 'string', 'descr': 'Name of the volume'}
            server = {'type': 'integer', 'descr': "Server to which to attach the Volume once it's created (Volume will be created in the same Location as the server)"}
            size = {'example': 42, 'type': 'integer', 'descr': 'Size of the Volume in GB'}
        R.automount = True
        R.format = 'xfs'
        R.labels = lambda: Defs.components_schemas_labels
        R.location = 'nbg1'
        R.name = 'databases-storage'
        R.server = 0
        R.size = 42
    class components_schemas_create_volume_response:
        """#/components/schemas/create_volume_response"""
        class R:
            required = ['volume', 'action', 'next_actions']
            type = 'object'
            description = 'Response to POST https://api.hetzner.cloud/v1/volumes'
            _attrs = ['action', 'next_actions', 'volume']
            action = lambda: Defs.components_schemas_action
            next_actions = {'items': lambda: Defs.components_schemas_action, 'type': 'array'}
            volume = lambda: Defs.components_schemas_volume
        R.action = lambda: Defs.components_schemas_action
        R.next_actions = [lambda: Defs.components_schemas_action]
        R.volume = lambda: Defs.components_schemas_volume
    class components_schemas_created_from:
        """#/components/schemas/created_from"""
        class R:
            description = 'Information about the Server the Image was created from'
            nullable = True
            required = ['id', 'name']
            type = 'object'
            _attrs = ['id', 'name']
            id = {'example': 1, 'type': 'integer', 'descr': 'ID of the Server the Image was created from'}
            name = {'example': 'Server', 'type': 'string', 'descr': 'Server name at the time the Image was created'}
        R.id = id
        R.name = 'Server'
    class components_schemas_datacenter:
        """#/components/schemas/datacenter"""
        class R:
            required = ['id', 'name', 'description', 'location', 'server_types']
            type = 'object'
            description = 'Datacenter this Primary IP is located at | Datacenter this Resource is located at'
            _attrs = ['description', 'id', 'location', 'name', 'server_types']
            description = {'example': 'Falkenstein DC Park 8', 'type': 'string', 'descr': 'Description of the Datacenter'}
            id = {'example': 42, 'type': 'integer', 'descr': 'ID of the Resource'}
            location = lambda: Defs.components_schemas_location
            name = {'example': 'fsn1-dc8', 'type': 'string', 'descr': 'Unique identifier of the Datacenter'}
            available = {'example': [1, 2, 3], 'items': {'type': 'integer'}, 'type': 'array', 'descr': 'IDs of Server types that are supported and for which the Datacenter has enough resources left'}
            available_for_migration = {'example': [1, 2, 3], 'items': {'type': 'integer'}, 'type': 'array', 'descr': 'IDs of Server types that are supported and for which the Datacenter has enough resources left'}
            supported = {'example': [1, 2, 3], 'items': {'type': 'integer'}, 'type': 'array', 'descr': 'IDs of Server types that are supported in the Datacenter'}
            server_types = {'properties': {'available': {'description': 'IDs of Server types that are supported and for which the Datacenter has enough resources left', 'example': [1, 2, 3], 'items': {'type': 'integer'}, 'type': 'array'}, 'available_for_migration': {'description': 'IDs of Server types that are supported and for which the Datacenter has enough resources left', 'example': [1, 2, 3], 'items': {'type': 'integer'}, 'type': 'array'}, 'supported': {'description': 'IDs of Server types that are supported in the Datacenter', 'example': [1, 2, 3], 'items': {'type': 'integer'}, 'type': 'array'}}, 'required': ['supported', 'available', 'available_for_migration'], 'type': 'object', 'descr': 'The Server types the Datacenter can handle'}
        R.description = 'Falkenstein DC Park 8'
        R.id = id
        R.location = lambda: Defs.components_schemas_location
        R.name = 'fsn1-dc8'
        R.server_types = dict(available = [1, 2, 3], available_for_migration = [1, 2, 3], supported = [1, 2, 3])
    class components_schemas_delete_route_from_network_request:
        """#/components/schemas/delete_route_from_network_request"""
        class R:
            dollar_ref = lambda: Defs.components_schemas_route
    class components_schemas_delete_route_from_network_response:
        """#/components/schemas/delete_route_from_network_response"""
        class R:
            required = ['action']
            title = 'ActionResponse'
            type = 'object'
            description = 'Response to POST https://api.hetzner.cloud/v1/networks/{id}/actions/delete_route'
            _attrs = ['action']
            action = lambda: Defs.components_schemas_action
        R.action = lambda: Defs.components_schemas_action
    class components_schemas_delete_server_response:
        """#/components/schemas/delete_server_response"""
        class R:
            type = 'object'
            description = 'Response to DELETE https://api.hetzner.cloud/v1/servers/{id}'
            _attrs = ['action']
            action = lambda: Defs.components_schemas_action
        R.action = lambda: Defs.components_schemas_action
    class components_schemas_delete_service_request:
        """#/components/schemas/delete_service_request"""
        class R:
            required = ['listen_port']
            type = 'object'
            description = 'Request for POST https://api.hetzner.cloud/v1/load_balancers/{id}/actions/delete_service'
            _attrs = ['listen_port']
            listen_port = {'example': 4711, 'type': 'integer', 'descr': 'The listen port of the service you want to delete'}
        R.listen_port = 4711
    class components_schemas_delete_service_response:
        """#/components/schemas/delete_service_response"""
        class R:
            required = ['action']
            title = 'ActionResponse'
            type = 'object'
            description = 'Response to POST https://api.hetzner.cloud/v1/load_balancers/{id}/actions/delete_service'
            _attrs = ['action']
            action = lambda: Defs.components_schemas_action
        R.action = lambda: Defs.components_schemas_action
    class components_schemas_delete_subnet_from_network_request:
        """#/components/schemas/delete_subnet_from_network_request"""
        class R:
            required = ['ip_range']
            title = 'DeleteSubnetRequest'
            type = 'object'
            description = 'Request for POST https://api.hetzner.cloud/v1/networks/{id}/actions/delete_subnet'
            _attrs = ['ip_range']
            ip_range = {'example': '10.0.1.0/24', 'type': 'string', 'descr': 'IP range of subnet to delete'}
        R.ip_range = '10.0.1.0/24'
    class components_schemas_delete_subnet_from_network_response:
        """#/components/schemas/delete_subnet_from_network_response"""
        class R:
            required = ['action']
            title = 'ActionResponse'
            type = 'object'
            description = 'Response to POST https://api.hetzner.cloud/v1/networks/{id}/actions/delete_subnet'
            _attrs = ['action']
            action = lambda: Defs.components_schemas_action
        R.action = lambda: Defs.components_schemas_action
    class components_schemas_detach_iso_from_server_response:
        """#/components/schemas/detach_iso_from_server_response"""
        class R:
            required = ['action']
            title = 'ActionResponse'
            type = 'object'
            description = 'Response to POST https://api.hetzner.cloud/v1/servers/{id}/actions/detach_iso'
            _attrs = ['action']
            action = lambda: Defs.components_schemas_action
        R.action = lambda: Defs.components_schemas_action
    class components_schemas_detach_load_balancer_from_network_request:
        """#/components/schemas/detach_load_balancer_from_network_request"""
        class R:
            required = ['network']
            type = 'object'
            description = 'Request for POST https://api.hetzner.cloud/v1/load_balancers/{id}/actions/detach_from_network'
            _attrs = ['network']
            network = {'example': 4711, 'type': 'integer', 'descr': 'ID of an existing network to detach the Load Balancer from'}
        R.network = 4711
    class components_schemas_detach_load_balancer_from_network_response:
        """#/components/schemas/detach_load_balancer_from_network_response"""
        class R:
            required = ['action']
            title = 'ActionResponse'
            type = 'object'
            description = 'Response to POST https://api.hetzner.cloud/v1/load_balancers/{id}/actions/detach_from_network'
            _attrs = ['action']
            action = lambda: Defs.components_schemas_action
        R.action = lambda: Defs.components_schemas_action
    class components_schemas_detach_server_from_network_request:
        """#/components/schemas/detach_server_from_network_request"""
        class R:
            required = ['network']
            title = 'DetachFromNetworkRequest'
            type = 'object'
            description = 'Request for POST https://api.hetzner.cloud/v1/servers/{id}/actions/detach_from_network'
            _attrs = ['network']
            network = {'example': 4711, 'type': 'integer', 'descr': 'ID of an existing network to detach the Server from'}
        R.network = 4711
    class components_schemas_detach_server_from_network_response:
        """#/components/schemas/detach_server_from_network_response"""
        class R:
            required = ['action']
            title = 'ActionResponse'
            type = 'object'
            description = 'Response to POST https://api.hetzner.cloud/v1/servers/{id}/actions/detach_from_network'
            _attrs = ['action']
            action = lambda: Defs.components_schemas_action
        R.action = lambda: Defs.components_schemas_action
    class components_schemas_detach_volume_response:
        """#/components/schemas/detach_volume_response"""
        class R:
            required = ['action']
            title = 'ActionResponse'
            type = 'object'
            description = 'Response to POST https://api.hetzner.cloud/v1/volumes/{id}/actions/detach'
            _attrs = ['action']
            action = lambda: Defs.components_schemas_action
        R.action = lambda: Defs.components_schemas_action
    class components_schemas_disable_backups_for_server_response:
        """#/components/schemas/disable_backups_for_server_response"""
        class R:
            required = ['action']
            title = 'ActionResponse'
            type = 'object'
            description = 'Response to POST https://api.hetzner.cloud/v1/servers/{id}/actions/disable_backup'
            _attrs = ['action']
            action = lambda: Defs.components_schemas_action
        R.action = lambda: Defs.components_schemas_action
    class components_schemas_disable_public_interface_of_load_balancer_response:
        """#/components/schemas/disable_public_interface_of_load_balancer_response"""
        class R:
            required = ['action']
            title = 'ActionResponse'
            type = 'object'
            description = 'Response to POST https://api.hetzner.cloud/v1/load_balancers/{id}/actions/disable_public_interface'
            _attrs = ['action']
            action = lambda: Defs.components_schemas_action
        R.action = lambda: Defs.components_schemas_action
    class components_schemas_disable_rescue_mode_for_server_response:
        """#/components/schemas/disable_rescue_mode_for_server_response"""
        class R:
            required = ['action']
            title = 'ActionResponse'
            type = 'object'
            description = 'Response to POST https://api.hetzner.cloud/v1/servers/{id}/actions/disable_rescue'
            _attrs = ['action']
            action = lambda: Defs.components_schemas_action
        R.action = lambda: Defs.components_schemas_action
    class components_schemas_dns_ptr:
        """#/components/schemas/dns_ptr"""
        class R:
            required = ['ip', 'dns_ptr']
            type = 'object'
            _attrs = ['dns_ptr', 'ip']
            dns_ptr = {'example': 'server.example.com', 'type': 'string', 'descr': 'DNS pointer for the specific IP address'}
            ip = {'example': '2001:db8::1', 'type': 'string', 'descr': 'Single IPv4 or IPv6 address | Single IPv6 address of this Server for which the reverse DNS entry has been set up'}
        R.dns_ptr = 'server.example.com'
        R.ip = '2001:db8::1'
    class components_schemas_enable_and_configure_backups_for_server_response:
        """#/components/schemas/enable_and_configure_backups_for_server_response"""
        class R:
            required = ['action']
            title = 'ActionResponse'
            type = 'object'
            description = 'Response to POST https://api.hetzner.cloud/v1/servers/{id}/actions/enable_backup'
            _attrs = ['action']
            action = lambda: Defs.components_schemas_action
        R.action = lambda: Defs.components_schemas_action
    class components_schemas_enable_public_interface_of_load_balancer_response:
        """#/components/schemas/enable_public_interface_of_load_balancer_response"""
        class R:
            required = ['action']
            title = 'ActionResponse'
            type = 'object'
            description = 'Response to POST https://api.hetzner.cloud/v1/load_balancers/{id}/actions/enable_public_interface'
            _attrs = ['action']
            action = lambda: Defs.components_schemas_action
        R.action = lambda: Defs.components_schemas_action
    class components_schemas_enable_rescue_mode_for_server_request:
        """#/components/schemas/enable_rescue_mode_for_server_request"""
        class R:
            type = 'object'
            description = 'Request for POST https://api.hetzner.cloud/v1/servers/{id}/actions/enable_rescue'
            _attrs = ['ssh_keys', 'type']
            ssh_keys = {'example': [2323], 'items': {'type': 'integer'}, 'type': 'array', 'descr': 'Array of SSH key IDs which should be injected into the rescue system.'}
            type = {'enum': ['linux32', 'linux64'], 'type': 'string', 'descr': 'Type of rescue system to boot (default: `linux64`)'}
        R.ssh_keys = [2323]
        R.type = 'linux32'
    class components_schemas_enable_rescue_mode_for_server_response:
        """#/components/schemas/enable_rescue_mode_for_server_response"""
        class R:
            type = 'object'
            description = 'Response to POST https://api.hetzner.cloud/v1/servers/{id}/actions/enable_rescue'
            _attrs = ['action', 'root_password']
            action = lambda: Defs.components_schemas_action
            root_password = {'example': 'zCWbFhnu950dUTko5f40', 'type': 'string', 'descr': 'Password that will be set for this Server once the Action succeeds'}
        R.action = lambda: Defs.components_schemas_action
        R.root_password = 'zCWbFhnu950dUTko5f40'
    class components_schemas_error:
        """#/components/schemas/error"""
        class R:
            description = 'Error message for the Action if error occurred, otherwise null'
            nullable = True
            required = ['code', 'message']
            type = 'object'
            _attrs = ['code', 'message']
            code = {'example': 'action_failed', 'type': 'string', 'descr': 'Fixed machine readable code'}
            message = {'example': 'Action failed', 'type': 'string', 'descr': 'Humanized error message'}
        R.code = 'action_failed'
        R.message = 'Action failed'
    class components_schemas_firewall:
        """#/components/schemas/firewall"""
        class R:
            required = ['id', 'name', 'created', 'rules', 'applied_to']
            title = 'Firewall'
            type = 'object'
            description = 'Firewalls can limit the network access to or from your resources.'
            _attrs = ['applied_to', 'created', 'id', 'labels', 'name', 'rules']
            applied_to = {'items': lambda: Defs.components_schemas_firewall_resource_id, 'type': 'array'}
            created = {'example': '2016-01-30T23:55:00+00:00', 'type': 'string', 'descr': 'Point in time when the Resource was created (in ISO-8601 format)'}
            id = {'example': 42, 'type': 'integer', 'descr': 'ID of the Resource'}
            labels = lambda: Defs.components_schemas_labels
            name = {'example': 'my-resource', 'type': 'string', 'descr': 'Name of the Resource. Must be unique per Project.'}
            rules = {'items': lambda: Defs.components_schemas_rule, 'type': 'array'}
        R.applied_to = [lambda: Defs.components_schemas_firewall_resource_id]
        R.created = '2016-01-30T23:55:00+00:00'
        R.id = id
        R.labels = lambda: Defs.components_schemas_labels
        R.name = 'my-resource'
        R.rules = [lambda: Defs.components_schemas_rule]
    class components_schemas_firewall_resource:
        """#/components/schemas/firewall_resource"""
        class R:
            title = 'FirewallApplyToResources'
            type = 'object'
            description = 'Resource a Firewall should be applied to.'
            _attrs = ['label_selector', 'server', 'type']
            label_selector = lambda: Defs.components_schemas_label_selector
            server = lambda: Defs.components_schemas_resource_id
            type = {'enum': ['label_selector', 'server'], 'type': 'string', 'descr': 'Type of the resource'}
        R.label_selector = lambda: Defs.components_schemas_label_selector
        R.server = lambda: Defs.components_schemas_resource_id
        R.type = 'label_selector'
    class components_schemas_firewall_resource_id:
        """#/components/schemas/firewall_resource_id"""
        class R:
            required = ['type']
            type = 'object'
            description = 'Resource a Firewall should be applied to.'
            _attrs = ['applied_to_resources', 'label_selector', 'server', 'type']
            server = lambda: Defs.components_schemas_resource_id
            type = {'enum': ['server'], 'example': 'server', 'type': 'string', 'descr': 'Type of resource referenced'}
            applied_to_resources = {'items': {'properties': {'server': lambda: Defs.components_schemas_resource_id, 'type': {'description': 'Type of resource referenced', 'enum': ['server'], 'example': 'server', 'type': 'string'}}, 'type': 'object', 'title': 'FirewallResourceIdAppliedToResources'}, 'type': 'array'}
            label_selector = lambda: Defs.components_schemas_label_selector
            server = lambda: Defs.components_schemas_resource_id
            type = {'enum': ['label_selector', 'server'], 'example': 'server', 'type': 'string', 'descr': 'Type of resource referenced'}
        R.applied_to_resources = [dict(server = lambda: Defs.components_schemas_resource_id, type = 'server')]
        R.label_selector = lambda: Defs.components_schemas_label_selector
        R.server = lambda: Defs.components_schemas_resource_id
        R.type = 'server'
    class components_schemas_firewall_resource_with_required_type:
        """#/components/schemas/firewall_resource_with_required_type"""
        class R:
            required = ['type']
            type = 'object'
            description = 'Resource a Firewall should be applied to.'
            _attrs = ['label_selector', 'server', 'type']
            label_selector = lambda: Defs.components_schemas_label_selector
            server = lambda: Defs.components_schemas_resource_id
            type = {'enum': ['label_selector', 'server'], 'type': 'string', 'descr': 'Type of the resource'}
        R.label_selector = lambda: Defs.components_schemas_label_selector
        R.server = lambda: Defs.components_schemas_resource_id
        R.type = 'label_selector'
    class components_schemas_floating_ip:
        """#/components/schemas/floating_ip"""
        class R:
            required = ['id', 'name', 'description', 'ip', 'type', 'server', 'dns_ptr', 'home_location', 'blocked', 'protection', 'labels', 'created']
            type = 'object'
            _attrs = ['blocked', 'created', 'description', 'dns_ptr', 'home_location', 'id', 'ip', 'labels', 'name', 'protection', 'server', 'type']
            blocked = {'example': False, 'type': 'boolean', 'descr': 'Whether the IP is blocked'}
            created = {'example': '2016-01-30T23:55:00+00:00', 'type': 'string', 'descr': 'Point in time when the Resource was created (in ISO-8601 format)'}
            description = {'example': 'this describes my resource', 'nullable': True, 'type': 'string', 'descr': 'Description of the Resource'}
            dns_ptr = {'items': lambda: Defs.components_schemas_dns_ptr, 'type': 'array', 'descr': 'Array of reverse DNS entries'}
            home_location = lambda: Defs.components_schemas_location
            id = {'example': 42, 'type': 'integer', 'descr': 'ID of the Resource'}
            ip = {'example': '131.232.99.1', 'type': 'string', 'descr': 'IP address'}
            labels = lambda: Defs.components_schemas_labels
            name = {'example': 'my-resource', 'type': 'string', 'descr': 'Name of the Resource. Must be unique per Project.'}
            protection = lambda: Defs.components_schemas_protection
            server = {'example': 42, 'nullable': True, 'type': 'integer', 'descr': 'ID of the Server the Floating IP is assigned to, null if it is not assigned at all'}
            type = lambda: Defs.components_schemas_ip_type
        R.blocked = True
        R.created = '2016-01-30T23:55:00+00:00'
        R.description = 'this describes my resource'
        R.dns_ptr = [lambda: Defs.components_schemas_dns_ptr]
        R.home_location = lambda: Defs.components_schemas_location
        R.id = id
        R.ip = '131.232.99.1'
        R.labels = lambda: Defs.components_schemas_labels
        R.name = 'my-resource'
        R.protection = lambda: Defs.components_schemas_protection
        R.server = 42
        R.type = lambda: Defs.components_schemas_ip_type
    class components_schemas_get_action_for_certificate_response:
        """#/components/schemas/get_action_for_certificate_response"""
        class R:
            required = ['action']
            title = 'ActionResponse'
            type = 'object'
            description = 'Response to GET https://api.hetzner.cloud/v1/certificates/{id}/actions/{action_id}'
            _attrs = ['action']
            action = lambda: Defs.components_schemas_action
        R.action = lambda: Defs.components_schemas_action
    class components_schemas_get_action_for_firewall_response:
        """#/components/schemas/get_action_for_firewall_response"""
        class R:
            required = ['action']
            title = 'ActionResponse'
            type = 'object'
            description = 'Response to GET https://api.hetzner.cloud/v1/firewalls/{id}/actions/{action_id}'
            _attrs = ['action']
            action = lambda: Defs.components_schemas_action
        R.action = lambda: Defs.components_schemas_action
    class components_schemas_get_action_for_floating_ip_response:
        """#/components/schemas/get_action_for_floating_ip_response"""
        class R:
            required = ['action']
            title = 'ActionResponse'
            type = 'object'
            description = 'Response to GET https://api.hetzner.cloud/v1/floating_ips/{id}/actions/{action_id}'
            _attrs = ['action']
            action = lambda: Defs.components_schemas_action
        R.action = lambda: Defs.components_schemas_action
    class components_schemas_get_action_for_image_response:
        """#/components/schemas/get_action_for_image_response"""
        class R:
            required = ['action']
            title = 'ActionResponse'
            type = 'object'
            description = 'Response to GET https://api.hetzner.cloud/v1/images/{id}/actions/{action_id}'
            _attrs = ['action']
            action = lambda: Defs.components_schemas_action
        R.action = lambda: Defs.components_schemas_action
    class components_schemas_get_action_for_load_balancer_response:
        """#/components/schemas/get_action_for_load_balancer_response"""
        class R:
            required = ['action']
            title = 'ActionResponse'
            type = 'object'
            description = 'Response to GET https://api.hetzner.cloud/v1/load_balancers/{id}/actions/{action_id}'
            _attrs = ['action']
            action = lambda: Defs.components_schemas_action
        R.action = lambda: Defs.components_schemas_action
    class components_schemas_get_action_for_network_response:
        """#/components/schemas/get_action_for_network_response"""
        class R:
            required = ['action']
            title = 'ActionResponse'
            type = 'object'
            description = 'Response to GET https://api.hetzner.cloud/v1/networks/{id}/actions/{action_id}'
            _attrs = ['action']
            action = lambda: Defs.components_schemas_action
        R.action = lambda: Defs.components_schemas_action
    class components_schemas_get_action_for_server_response:
        """#/components/schemas/get_action_for_server_response"""
        class R:
            required = ['action']
            title = 'ActionResponse'
            type = 'object'
            description = 'Response to GET https://api.hetzner.cloud/v1/servers/{id}/actions/{action_id}'
            _attrs = ['action']
            action = lambda: Defs.components_schemas_action
        R.action = lambda: Defs.components_schemas_action
    class components_schemas_get_action_for_volume_response:
        """#/components/schemas/get_action_for_volume_response"""
        class R:
            required = ['action']
            title = 'ActionResponse'
            type = 'object'
            description = 'Response to GET https://api.hetzner.cloud/v1/volumes/{id}/actions/{action_id}'
            _attrs = ['action']
            action = lambda: Defs.components_schemas_action
        R.action = lambda: Defs.components_schemas_action
    class components_schemas_get_action_response:
        """#/components/schemas/get_action_response"""
        class R:
            required = ['action']
            title = 'ActionResponse'
            type = 'object'
            description = 'Response to GET https://api.hetzner.cloud/v1/actions/{id}'
            _attrs = ['action']
            action = lambda: Defs.components_schemas_action
        R.action = lambda: Defs.components_schemas_action
    class components_schemas_get_certificate_response:
        """#/components/schemas/get_certificate_response"""
        class R:
            required = ['certificate']
            title = 'CertificateResponse'
            type = 'object'
            description = 'Response to GET https://api.hetzner.cloud/v1/certificates/{id}'
            _attrs = ['certificate']
            certificate = lambda: Defs.components_schemas_certificate
        R.certificate = lambda: Defs.components_schemas_certificate
    class components_schemas_get_datacenter_response:
        """#/components/schemas/get_datacenter_response"""
        class R:
            required = ['datacenter']
            type = 'object'
            description = 'Response to GET https://api.hetzner.cloud/v1/datacenters/{id}'
            _attrs = ['datacenter']
            datacenter = lambda: Defs.components_schemas_datacenter
        R.datacenter = lambda: Defs.components_schemas_datacenter
    class components_schemas_get_firewall_response:
        """#/components/schemas/get_firewall_response"""
        class R:
            required = ['firewall']
            title = 'FirewallResponse'
            type = 'object'
            description = 'Response to GET https://api.hetzner.cloud/v1/firewalls/{id}'
            _attrs = ['firewall']
            firewall = lambda: Defs.components_schemas_firewall
        R.firewall = lambda: Defs.components_schemas_firewall
    class components_schemas_get_floating_ip_response:
        """#/components/schemas/get_floating_ip_response"""
        class R:
            required = ['floating_ip']
            type = 'object'
            description = 'Response to GET https://api.hetzner.cloud/v1/floating_ips/{id}'
            _attrs = ['floating_ip']
            floating_ip = lambda: Defs.components_schemas_floating_ip
        R.floating_ip = lambda: Defs.components_schemas_floating_ip
    class components_schemas_get_image_response:
        """#/components/schemas/get_image_response"""
        class R:
            type = 'object'
            description = 'Response to GET https://api.hetzner.cloud/v1/images/{id}'
            _attrs = ['image']
            image = lambda: Defs.components_schemas_image
        R.image = lambda: Defs.components_schemas_image
    class components_schemas_get_iso_response:
        """#/components/schemas/get_iso_response"""
        class R:
            required = ['iso']
            type = 'object'
            description = 'Response to GET https://api.hetzner.cloud/v1/isos/{id}'
            _attrs = ['iso']
            iso = lambda: Defs.components_schemas_iso
        R.iso = lambda: Defs.components_schemas_iso
    class components_schemas_get_load_balancer_response:
        """#/components/schemas/get_load_balancer_response"""
        class R:
            required = ['load_balancer']
            type = 'object'
            description = 'Response to GET https://api.hetzner.cloud/v1/load_balancers/{id}'
            _attrs = ['load_balancer']
            load_balancer = lambda: Defs.components_schemas_load_balancer
        R.load_balancer = lambda: Defs.components_schemas_load_balancer
    class components_schemas_get_load_balancer_type_response:
        """#/components/schemas/get_load_balancer_type_response"""
        class R:
            type = 'object'
            description = 'Response to GET https://api.hetzner.cloud/v1/load_balancer_types/{id}'
            _attrs = ['load_balancer_type']
            load_balancer_type = lambda: Defs.components_schemas_load_balancer_type
        R.load_balancer_type = lambda: Defs.components_schemas_load_balancer_type
    class components_schemas_get_location_response:
        """#/components/schemas/get_location_response"""
        class R:
            required = ['location']
            type = 'object'
            description = 'Response to GET https://api.hetzner.cloud/v1/locations/{id}'
            _attrs = ['location']
            location = lambda: Defs.components_schemas_location
        R.location = lambda: Defs.components_schemas_location
    class components_schemas_get_metrics_for_loadbalancer_response:
        """#/components/schemas/get_metrics_for_loadbalancer_response"""
        class R:
            required = ['metrics']
            type = 'object'
            description = 'Response to GET https://api.hetzner.cloud/v1/load_balancers/{id}/metrics'
            _attrs = ['metrics']
            metrics = lambda: Defs.components_schemas_metrics
        R.metrics = lambda: Defs.components_schemas_metrics
    class components_schemas_get_metrics_for_server_response:
        """#/components/schemas/get_metrics_for_server_response"""
        class R:
            required = ['metrics']
            type = 'object'
            description = 'Response to GET https://api.hetzner.cloud/v1/servers/{id}/metrics'
            _attrs = ['metrics']
            metrics = lambda: Defs.components_schemas_metrics
        R.metrics = lambda: Defs.components_schemas_metrics
    class components_schemas_get_network_response:
        """#/components/schemas/get_network_response"""
        class R:
            type = 'object'
            description = 'Response to GET https://api.hetzner.cloud/v1/networks/{id}'
            _attrs = ['network']
            network = lambda: Defs.components_schemas_network
        R.network = lambda: Defs.components_schemas_network
    class components_schemas_get_placementgroup_response:
        """#/components/schemas/get_placementgroup_response"""
        class R:
            required = ['placement_group']
            title = 'PlacementGroupResponse'
            type = 'object'
            description = 'Response to GET https://api.hetzner.cloud/v1/placement_groups/{id}'
            _attrs = ['placement_group']
            created = {'example': '2016-01-30T23:55:00+00:00', 'type': 'string', 'descr': 'Point in time when the Resource was created (in ISO-8601 format)'}
            id = {'example': 42, 'type': 'integer', 'descr': 'ID of the Resource'}
            labels = lambda: Defs.components_schemas_labels
            name = {'example': 'my-resource', 'type': 'string', 'descr': 'Name of the Resource. Must be unique per Project.'}
            servers = {'example': [42], 'items': {'type': 'integer'}, 'type': 'array', 'descr': 'Array of IDs of Servers that are part of this Placement Group'}
            type = {'enum': ['spread'], 'example': 'spread', 'type': 'string', 'descr': 'Type of the Placement Group'}
            placement_group = {'properties': {'created': {'description': 'Point in time when the Resource was created (in ISO-8601 format)', 'example': '2016-01-30T23:55:00+00:00', 'type': 'string'}, 'id': {'description': 'ID of the Resource', 'example': 42, 'type': 'integer'}, 'labels': lambda: Defs.components_schemas_labels, 'name': {'description': 'Name of the Resource. Must be unique per Project.', 'example': 'my-resource', 'type': 'string'}, 'servers': {'description': 'Array of IDs of Servers that are part of this Placement Group', 'example': [42], 'items': {'type': 'integer'}, 'type': 'array'}, 'type': {'description': 'Type of the Placement Group', 'enum': ['spread'], 'example': 'spread', 'type': 'string'}}, 'required': ['id', 'name', 'labels', 'type', 'created', 'servers'], 'title': 'PlacementGroup', 'type': 'object'}
        R.placement_group = dict(created = '2016-01-30T23:55:00+00:00', id = id, labels = lambda: Defs.components_schemas_labels, name = 'my-resource', servers = [42], type = 'spread')
    class components_schemas_get_primary_ip_response:
        """#/components/schemas/get_primary_ip_response"""
        class R:
            required = ['primary_ip']
            title = 'PrimaryIPResponse'
            type = 'object'
            description = 'Response to GET https://api.hetzner.cloud/v1/primary_ips/{id}'
            _attrs = ['primary_ip']
            assignee_id = {'example': 17, 'nullable': True, 'type': 'integer', 'descr': 'ID of the resource the Primary IP is assigned to, null if it is not assigned at all'}
            assignee_type = {'enum': ['server'], 'type': 'string', 'descr': 'Resource type the Primary IP can be assigned to'}
            auto_delete = {'example': True, 'type': 'boolean', 'descr': 'Delete this Primary IP when the resource it is assigned to is deleted'}
            blocked = {'example': False, 'type': 'boolean', 'descr': 'Whether the IP is blocked'}
            created = {'example': '2016-01-30T23:55:00+00:00', 'type': 'string', 'descr': 'Point in time when the Resource was created (in ISO-8601 format)'}
            datacenter = lambda: Defs.components_schemas_datacenter
            dns_ptr = {'items': lambda: Defs.components_schemas_dns_ptr, 'type': 'array', 'descr': 'Array of reverse DNS entries'}
            id = {'example': 42, 'type': 'integer', 'descr': 'ID of the Resource'}
            ip = {'example': '131.232.99.1', 'type': 'string', 'descr': 'IP address'}
            labels = lambda: Defs.components_schemas_labels
            name = {'example': 'my-resource', 'type': 'string', 'descr': 'Name of the Resource. Must be unique per Project.'}
            protection = lambda: Defs.components_schemas_protection
            type = lambda: Defs.components_schemas_ip_type
            primary_ip = {'properties': {'assignee_id': {'description': 'ID of the resource the Primary IP is assigned to, null if it is not assigned at all', 'example': 17, 'nullable': True, 'type': 'integer'}, 'assignee_type': {'description': 'Resource type the Primary IP can be assigned to', 'enum': ['server'], 'type': 'string'}, 'auto_delete': {'description': 'Delete this Primary IP when the resource it is assigned to is deleted', 'example': True, 'type': 'boolean'}, 'blocked': {'description': 'Whether the IP is blocked', 'example': False, 'type': 'boolean'}, 'created': {'description': 'Point in time when the Resource was created (in ISO-8601 format)', 'example': '2016-01-30T23:55:00+00:00', 'type': 'string'}, 'datacenter': lambda: Defs.components_schemas_datacenter, 'dns_ptr': {'description': 'Array of reverse DNS entries', 'items': lambda: Defs.components_schemas_dns_ptr, 'type': 'array'}, 'id': {'description': 'ID of the Resource', 'example': 42, 'type': 'integer'}, 'ip': {'description': 'IP address', 'example': '131.232.99.1', 'type': 'string'}, 'labels': lambda: Defs.components_schemas_labels, 'name': {'description': 'Name of the Resource. Must be unique per Project.', 'example': 'my-resource', 'type': 'string'}, 'protection': lambda: Defs.components_schemas_protection, 'type': lambda: Defs.components_schemas_ip_type}, 'required': ['id', 'name', 'labels', 'created', 'blocked', 'datacenter', 'ip', 'dns_ptr', 'protection', 'type', 'auto_delete', 'assignee_type', 'assignee_id'], 'title': 'PrimaryIP', 'type': 'object'}
        R.primary_ip = dict(assignee_id = 17, assignee_type = 'server', auto_delete = True, blocked = True, created = '2016-01-30T23:55:00+00:00', datacenter = lambda: Defs.components_schemas_datacenter, dns_ptr = [lambda: Defs.components_schemas_dns_ptr], id = id, ip = '131.232.99.1', labels = lambda: Defs.components_schemas_labels, name = 'my-resource', protection = lambda: Defs.components_schemas_protection, type = lambda: Defs.components_schemas_ip_type)
    class components_schemas_get_server_response:
        """#/components/schemas/get_server_response"""
        class R:
            type = 'object'
            description = 'Response to GET https://api.hetzner.cloud/v1/servers/{id}'
            _attrs = ['server']
            server = lambda: Defs.components_schemas_server
        R.server = lambda: Defs.components_schemas_server
    class components_schemas_get_server_type_response:
        """#/components/schemas/get_server_type_response"""
        class R:
            required = ['server_type']
            type = 'object'
            description = 'Response to GET https://api.hetzner.cloud/v1/server_types/{id}'
            _attrs = ['server_type']
            server_type = lambda: Defs.components_schemas_server_type
        R.server_type = lambda: Defs.components_schemas_server_type
    class components_schemas_get_ssh_key_response:
        """#/components/schemas/get_ssh_key_response"""
        class R:
            required = ['ssh_key']
            type = 'object'
            description = 'Response to GET https://api.hetzner.cloud/v1/ssh_keys/{id}'
            _attrs = ['ssh_key']
            ssh_key = lambda: Defs.components_schemas_ssh_key
        R.ssh_key = lambda: Defs.components_schemas_ssh_key
    class components_schemas_get_volume_response:
        """#/components/schemas/get_volume_response"""
        class R:
            required = ['volume']
            type = 'object'
            description = 'Response to GET https://api.hetzner.cloud/v1/volumes/{id}'
            _attrs = ['volume']
            volume = lambda: Defs.components_schemas_volume
        R.volume = lambda: Defs.components_schemas_volume
    class components_schemas_health_status:
        """#/components/schemas/health_status"""
        class R:
            type = 'object'
            _attrs = ['listen_port', 'status']
            listen_port = {'example': 443, 'type': 'integer'}
            status = {'enum': ['healthy', 'unhealthy', 'unknown'], 'example': 'healthy', 'type': 'string'}
        R.listen_port = 443
        R.status = 'healthy'
    class components_schemas_http:
        """#/components/schemas/http"""
        class R:
            description = 'Configuration option for protocols http and https'
            title = 'LoadBalancerServiceHTTP'
            type = 'object'
            _attrs = ['certificates', 'cookie_lifetime', 'cookie_name', 'redirect_http', 'sticky_sessions']
            certificates = {'example': [897], 'items': {'type': 'integer'}, 'type': 'array', 'descr': 'IDs of the Certificates to use for TLS/SSL termination by the Load Balancer; empty for TLS/SSL passthrough or if `protocol` is "http"'}
            cookie_lifetime = {'example': 300, 'type': 'integer', 'descr': 'Lifetime of the cookie used for sticky sessions'}
            cookie_name = {'example': 'HCLBSTICKY', 'type': 'string', 'descr': 'Name of the cookie used for sticky sessions'}
            redirect_http = {'example': True, 'type': 'boolean', 'descr': 'Redirect HTTP requests to HTTPS. Only available if protocol is "https". Default `false`'}
            sticky_sessions = {'example': True, 'type': 'boolean', 'descr': 'Use sticky sessions. Only available if protocol is "http" or "https". Default `false`'}
        R.certificates = [897]
        R.cookie_lifetime = 300
        R.cookie_name = 'HCLBSTICKY'
        R.redirect_http = True
        R.sticky_sessions = True
    class components_schemas_image:
        """#/components/schemas/image"""
        class R:
            required = ['id', 'type', 'status', 'name', 'description', 'image_size', 'disk_size', 'created', 'created_from', 'bound_to', 'os_flavor', 'os_version', 'protection', 'deprecated', 'deleted', 'labels']
            type = 'object'
            _attrs = ['bound_to', 'created', 'created_from', 'deleted', 'deprecated', 'description', 'disk_size', 'id', 'image_size', 'labels', 'name', 'os_flavor', 'os_version', 'protection', 'rapid_deploy', 'status', 'type']
            bound_to = {'example': None, 'nullable': True, 'type': 'integer', 'descr': 'ID of Server the Image is bound to. Only set for Images of type `backup`.'}
            created = {'example': '2016-01-30T23:55:00+00:00', 'type': 'string', 'descr': 'Point in time when the Resource was created (in ISO-8601 format)'}
            created_from = lambda: Defs.components_schemas_created_from
            deleted = {'example': None, 'nullable': True, 'type': 'string', 'descr': 'Point in time where the Image was deleted (in ISO-8601 format)'}
            deprecated = {'example': '2018-02-28T00:00:00+00:00', 'nullable': True, 'type': 'string', 'descr': 'Point in time when the Image is considered to be deprecated (in ISO-8601 format)'}
            description = {'example': 'Ubuntu 20.04 Standard 64 bit', 'type': 'string', 'descr': 'Description of the Image'}
            disk_size = {'example': 10, 'type': 'number', 'descr': 'Size of the disk contained in the Image in GB'}
            id = {'example': 42, 'type': 'integer', 'descr': 'ID of the Resource'}
            image_size = {'example': 2.3, 'nullable': True, 'type': 'number', 'descr': 'Size of the Image file in our storage in GB. For snapshot Images this is the value relevant for calculating costs for the Image.'}
            labels = lambda: Defs.components_schemas_labels
            name = {'example': 'ubuntu-20.04', 'nullable': True, 'type': 'string', 'descr': 'Unique identifier of the Image. This value is only set for system Images.'}
            os_flavor = {'enum': ['centos', 'debian', 'fedora', 'rocky', 'ubuntu', 'unknown'], 'example': 'ubuntu', 'type': 'string', 'descr': 'Flavor of operating system contained in the Image'}
            os_version = {'example': '20.04', 'nullable': True, 'type': 'string', 'descr': 'Operating system version'}
            protection = lambda: Defs.components_schemas_protection
            rapid_deploy = {'example': False, 'type': 'boolean', 'descr': 'Indicates that rapid deploy of the Image is available'}
            status = {'enum': ['available', 'creating', 'unavailable'], 'type': 'string', 'descr': "Whether the Image can be used or if it's still being created or unavailable"}
            type = {'enum': ['app', 'backup', 'snapshot', 'system', 'temporary'], 'example': 'snapshot', 'type': 'string', 'descr': 'Type of the Image'}
        R.bound_to = 0
        R.created = '2016-01-30T23:55:00+00:00'
        R.created_from = lambda: Defs.components_schemas_created_from
        R.deleted = str_dflt
        R.deprecated = '2018-02-28T00:00:00+00:00'
        R.description = 'Ubuntu 20.04 Standard 64 bit'
        R.disk_size = 10
        R.id = id
        R.image_size = 2.3
        R.labels = lambda: Defs.components_schemas_labels
        R.name = 'ubuntu-20.04'
        R.os_flavor = 'ubuntu'
        R.os_version = '20.04'
        R.protection = lambda: Defs.components_schemas_protection
        R.rapid_deploy = True
        R.status = 'available'
        R.type = 'snapshot'
    class components_schemas_image_optional:
        """#/components/schemas/image_optional"""
        class R:
            nullable = True
            required = ['id', 'type', 'status', 'name', 'description', 'image_size', 'disk_size', 'created', 'created_from', 'bound_to', 'os_flavor', 'os_version', 'protection', 'deprecated', 'deleted', 'labels']
            type = 'object'
            _attrs = ['bound_to', 'created', 'created_from', 'deleted', 'deprecated', 'description', 'disk_size', 'id', 'image_size', 'labels', 'name', 'os_flavor', 'os_version', 'protection', 'rapid_deploy', 'status', 'type']
            bound_to = {'example': None, 'nullable': True, 'type': 'integer', 'descr': 'ID of Server the Image is bound to. Only set for Images of type `backup`.'}
            created = {'example': '2016-01-30T23:55:00+00:00', 'type': 'string', 'descr': 'Point in time when the Resource was created (in ISO-8601 format)'}
            created_from = lambda: Defs.components_schemas_created_from
            deleted = {'example': None, 'nullable': True, 'type': 'string', 'descr': 'Point in time where the Image was deleted (in ISO-8601 format)'}
            deprecated = {'example': '2018-02-28T00:00:00+00:00', 'nullable': True, 'type': 'string', 'descr': 'Point in time when the Image is considered to be deprecated (in ISO-8601 format)'}
            description = {'example': 'Ubuntu 20.04 Standard 64 bit', 'type': 'string', 'descr': 'Description of the Image'}
            disk_size = {'example': 10, 'type': 'number', 'descr': 'Size of the disk contained in the Image in GB'}
            id = {'example': 42, 'type': 'integer', 'descr': 'ID of the Resource'}
            image_size = {'example': 2.3, 'nullable': True, 'type': 'number', 'descr': 'Size of the Image file in our storage in GB. For snapshot Images this is the value relevant for calculating costs for the Image.'}
            labels = lambda: Defs.components_schemas_labels
            name = {'example': 'ubuntu-20.04', 'nullable': True, 'type': 'string', 'descr': 'Unique identifier of the Image. This value is only set for system Images.'}
            os_flavor = {'enum': ['centos', 'debian', 'fedora', 'rocky', 'ubuntu', 'unknown'], 'example': 'ubuntu', 'type': 'string', 'descr': 'Flavor of operating system contained in the Image'}
            os_version = {'example': '20.04', 'nullable': True, 'type': 'string', 'descr': 'Operating system version'}
            protection = lambda: Defs.components_schemas_protection
            rapid_deploy = {'example': False, 'type': 'boolean', 'descr': 'Indicates that rapid deploy of the Image is available'}
            status = {'enum': ['available', 'creating', 'unavailable'], 'type': 'string', 'descr': "Whether the Image can be used or if it's still being created or unavailable"}
            type = {'enum': ['app', 'backup', 'snapshot', 'system', 'temporary'], 'example': 'snapshot', 'type': 'string', 'descr': 'Type of the Image'}
        R.bound_to = 0
        R.created = '2016-01-30T23:55:00+00:00'
        R.created_from = lambda: Defs.components_schemas_created_from
        R.deleted = str_dflt
        R.deprecated = '2018-02-28T00:00:00+00:00'
        R.description = 'Ubuntu 20.04 Standard 64 bit'
        R.disk_size = 10
        R.id = id
        R.image_size = 2.3
        R.labels = lambda: Defs.components_schemas_labels
        R.name = 'ubuntu-20.04'
        R.os_flavor = 'ubuntu'
        R.os_version = '20.04'
        R.protection = lambda: Defs.components_schemas_protection
        R.rapid_deploy = True
        R.status = 'available'
        R.type = 'snapshot'
    class components_schemas_ip_type:
        """#/components/schemas/ip_type"""
        class R:
            _attrs = ['__val__']
            __val__ = {'enum': ['ipv4', 'ipv6'], 'type': 'string', 'descr': 'The type of the IP'}
        R.__val__ = 'ipv4'
    class components_schemas_ipv4:
        """#/components/schemas/ipv4"""
        class R:
            description = 'IP address (v4) and its reverse DNS entry of this Server'
            nullable = True
            required = ['ip', 'blocked', 'dns_ptr']
            type = 'object'
            _attrs = ['blocked', 'dns_ptr', 'id', 'ip']
            blocked = {'example': False, 'type': 'boolean', 'descr': 'If the IP is blocked by our anti abuse dept'}
            dns_ptr = {'example': 'server01.example.com', 'type': 'string', 'descr': 'Reverse DNS PTR entry for the IPv4 addresses of this Server'}
            id = {'example': 42, 'type': 'integer', 'descr': 'ID of the Resource'}
            ip = {'example': '1.2.3.4', 'type': 'string', 'descr': 'IP address (v4) of this Server'}
        R.blocked = True
        R.dns_ptr = 'server01.example.com'
        R.id = id
        R.ip = '1.2.3.4'
    class components_schemas_ipv6:
        """#/components/schemas/ipv6"""
        class R:
            description = 'IPv6 network assigned to this Server and its reverse DNS entry'
            nullable = True
            required = ['ip', 'blocked', 'dns_ptr']
            type = 'object'
            _attrs = ['blocked', 'dns_ptr', 'id', 'ip']
            blocked = {'example': False, 'type': 'boolean', 'descr': 'If the IP is blocked by our anti abuse dept'}
            dns_ptr = {'items': lambda: Defs.components_schemas_dns_ptr, 'nullable': True, 'type': 'array', 'descr': 'Reverse DNS PTR entries for the IPv6 addresses of this Server, `null` by default'}
            id = {'example': 42, 'type': 'integer', 'descr': 'ID of the Resource'}
            ip = {'example': '2001:db8::/64', 'type': 'string', 'descr': 'IP address (v6) of this Server'}
        R.blocked = True
        R.dns_ptr = [lambda: Defs.components_schemas_dns_ptr]
        R.id = id
        R.ip = '2001:db8::/64'
    class components_schemas_iso:
        """#/components/schemas/iso"""
        class R:
            required = ['id', 'name', 'description', 'type', 'deprecated']
            type = 'object'
            _attrs = ['deprecated', 'description', 'id', 'name', 'type']
            deprecated = {'example': '2018-02-28T00:00:00+00:00', 'nullable': True, 'type': 'string', 'descr': 'ISO 8601 timestamp of deprecation, null if ISO is still available. After the deprecation time it will no longer be possible to attach the ISO to Servers.'}
            description = {'example': 'FreeBSD 11.0 x64', 'type': 'string', 'descr': 'Description of the ISO'}
            id = {'example': 42, 'type': 'integer', 'descr': 'ID of the Resource'}
            name = {'example': 'FreeBSD-11.0-RELEASE-amd64-dvd1', 'nullable': True, 'type': 'string', 'descr': 'Unique identifier of the ISO. Only set for public ISOs'}
            type = {'enum': ['private', 'public'], 'type': 'string', 'descr': 'Type of the ISO'}
        R.deprecated = '2018-02-28T00:00:00+00:00'
        R.description = 'FreeBSD 11.0 x64'
        R.id = id
        R.name = 'FreeBSD-11.0-RELEASE-amd64-dvd1'
        R.type = 'private'
    class components_schemas_iso_optional:
        """#/components/schemas/iso_optional"""
        class R:
            description = 'ISO Image that is attached to this Server. Null if no ISO is attached.'
            nullable = True
            required = ['id', 'name', 'description', 'type', 'deprecated']
            type = 'object'
            _attrs = ['deprecated', 'description', 'id', 'name', 'type']
            deprecated = {'example': '2018-02-28T00:00:00+00:00', 'nullable': True, 'type': 'string', 'descr': 'ISO 8601 timestamp of deprecation, null if ISO is still available. After the deprecation time it will no longer be possible to attach the ISO to Servers.'}
            description = {'example': 'FreeBSD 11.0 x64', 'type': 'string', 'descr': 'Description of the ISO'}
            id = {'example': 42, 'type': 'integer', 'descr': 'ID of the Resource'}
            name = {'example': 'FreeBSD-11.0-RELEASE-amd64-dvd1', 'nullable': True, 'type': 'string', 'descr': 'Unique identifier of the ISO. Only set for public ISOs'}
            type = {'enum': ['private', 'public'], 'type': 'string', 'descr': 'Type of the ISO'}
        R.deprecated = '2018-02-28T00:00:00+00:00'
        R.description = 'FreeBSD 11.0 x64'
        R.id = id
        R.name = 'FreeBSD-11.0-RELEASE-amd64-dvd1'
        R.type = 'private'
    class components_schemas_label_selector:
        """#/components/schemas/label_selector"""
        class R:
            required = ['selector']
            type = 'object'
            description = 'Configuration for type LabelSelector, required if type is `label_selector`'
            _attrs = ['selector']
            selector = {'example': 'env=prod', 'type': 'string', 'descr': 'Label selector'}
        R.selector = 'env=prod'
    class components_schemas_labels:
        """#/components/schemas/labels"""
        class R:
            _attrs = ['__val__']
            __val__ = {'additionalProperties': {'type': 'string', 'pattern': '^(()|[a-z0-9A-Z]|([a-z0-9A-Z][a-z0-9A-Z\\._-]{0,61}[a-z0-9A-Z]))$'}, 'type': 'object', 'descr': 'User-defined labels (key-value pairs)'}
        R.__val__ = {}
    class components_schemas_list_actions_for_certificate_response:
        """#/components/schemas/list_actions_for_certificate_response"""
        class R:
            required = ['actions']
            title = 'ActionsResponse'
            type = 'object'
            description = 'Response to GET https://api.hetzner.cloud/v1/certificates/{id}/actions'
            _attrs = ['actions', 'meta']
            actions = {'items': lambda: Defs.components_schemas_action, 'type': 'array'}
            meta = lambda: Defs.components_schemas_meta
        R.actions = [lambda: Defs.components_schemas_action]
        R.meta = lambda: Defs.components_schemas_meta
    class components_schemas_list_actions_for_firewall_response:
        """#/components/schemas/list_actions_for_firewall_response"""
        class R:
            required = ['actions']
            title = 'ActionsResponse'
            type = 'object'
            description = 'Response to GET https://api.hetzner.cloud/v1/firewalls/{id}/actions'
            _attrs = ['actions', 'meta']
            actions = {'items': lambda: Defs.components_schemas_action, 'type': 'array'}
            meta = lambda: Defs.components_schemas_meta
        R.actions = [lambda: Defs.components_schemas_action]
        R.meta = lambda: Defs.components_schemas_meta
    class components_schemas_list_actions_for_floating_ip_response:
        """#/components/schemas/list_actions_for_floating_ip_response"""
        class R:
            required = ['actions']
            type = 'object'
            description = 'Response to GET https://api.hetzner.cloud/v1/floating_ips/{id}/actions'
            _attrs = ['actions', 'meta']
            actions = {'items': lambda: Defs.components_schemas_action, 'type': 'array'}
            meta = lambda: Defs.components_schemas_meta
        R.actions = [lambda: Defs.components_schemas_action]
        R.meta = lambda: Defs.components_schemas_meta
    class components_schemas_list_actions_for_image_response:
        """#/components/schemas/list_actions_for_image_response"""
        class R:
            required = ['actions']
            title = 'ActionsResponse'
            type = 'object'
            description = 'Response to GET https://api.hetzner.cloud/v1/images/{id}/actions'
            _attrs = ['actions', 'meta']
            actions = {'items': lambda: Defs.components_schemas_action, 'type': 'array'}
            meta = lambda: Defs.components_schemas_meta
        R.actions = [lambda: Defs.components_schemas_action]
        R.meta = lambda: Defs.components_schemas_meta
    class components_schemas_list_actions_for_load_balancer_response:
        """#/components/schemas/list_actions_for_load_balancer_response"""
        class R:
            required = ['actions']
            title = 'ActionsResponse'
            type = 'object'
            description = 'Response to GET https://api.hetzner.cloud/v1/load_balancers/{id}/actions'
            _attrs = ['actions', 'meta']
            actions = {'items': lambda: Defs.components_schemas_action, 'type': 'array'}
            meta = lambda: Defs.components_schemas_meta
        R.actions = [lambda: Defs.components_schemas_action]
        R.meta = lambda: Defs.components_schemas_meta
    class components_schemas_list_actions_for_network_response:
        """#/components/schemas/list_actions_for_network_response"""
        class R:
            required = ['actions']
            title = 'ActionsResponse'
            type = 'object'
            description = 'Response to GET https://api.hetzner.cloud/v1/networks/{id}/actions'
            _attrs = ['actions', 'meta']
            actions = {'items': lambda: Defs.components_schemas_action, 'type': 'array'}
            meta = lambda: Defs.components_schemas_meta
        R.actions = [lambda: Defs.components_schemas_action]
        R.meta = lambda: Defs.components_schemas_meta
    class components_schemas_list_actions_for_server_response:
        """#/components/schemas/list_actions_for_server_response"""
        class R:
            required = ['actions']
            title = 'ActionsResponse'
            type = 'object'
            description = 'Response to GET https://api.hetzner.cloud/v1/servers/{id}/actions'
            _attrs = ['actions', 'meta']
            actions = {'items': lambda: Defs.components_schemas_action, 'type': 'array'}
            meta = lambda: Defs.components_schemas_meta
        R.actions = [lambda: Defs.components_schemas_action]
        R.meta = lambda: Defs.components_schemas_meta
    class components_schemas_list_actions_for_volume_response:
        """#/components/schemas/list_actions_for_volume_response"""
        class R:
            required = ['actions']
            title = 'ActionsResponse'
            type = 'object'
            description = 'Response to GET https://api.hetzner.cloud/v1/volumes/{id}/actions'
            _attrs = ['actions', 'meta']
            actions = {'items': lambda: Defs.components_schemas_action, 'type': 'array'}
            meta = lambda: Defs.components_schemas_meta
        R.actions = [lambda: Defs.components_schemas_action]
        R.meta = lambda: Defs.components_schemas_meta
    class components_schemas_list_actions_response:
        """#/components/schemas/list_actions_response"""
        class R:
            required = ['actions']
            title = 'ActionsResponse'
            type = 'object'
            description = 'Response to GET https://api.hetzner.cloud/v1/actions'
            _attrs = ['actions', 'meta']
            actions = {'items': lambda: Defs.components_schemas_action, 'type': 'array'}
            meta = lambda: Defs.components_schemas_meta
        R.actions = [lambda: Defs.components_schemas_action]
        R.meta = lambda: Defs.components_schemas_meta
    class components_schemas_list_certificates_response:
        """#/components/schemas/list_certificates_response"""
        class R:
            required = ['certificates']
            title = 'CertificatesResponse'
            type = 'object'
            description = 'Response to GET https://api.hetzner.cloud/v1/certificates'
            _attrs = ['certificates', 'meta']
            certificates = {'items': lambda: Defs.components_schemas_certificate, 'type': 'array'}
            meta = lambda: Defs.components_schemas_meta
        R.certificates = [lambda: Defs.components_schemas_certificate]
        R.meta = lambda: Defs.components_schemas_meta
    class components_schemas_list_datacenters_response:
        """#/components/schemas/list_datacenters_response"""
        class R:
            required = ['datacenters', 'recommendation']
            type = 'object'
            description = 'Response to GET https://api.hetzner.cloud/v1/datacenters'
            _attrs = ['datacenters', 'recommendation']
            datacenters = {'items': lambda: Defs.components_schemas_datacenter, 'type': 'array'}
            recommendation = {'example': 1, 'type': 'integer', 'descr': 'The Datacenter which is recommended to be used to create new Servers.'}
        R.datacenters = [lambda: Defs.components_schemas_datacenter]
        R.recommendation = 1
    class components_schemas_list_firewalls_response:
        """#/components/schemas/list_firewalls_response"""
        class R:
            required = ['firewalls']
            title = 'FirewallsResponse'
            type = 'object'
            description = 'Response to GET https://api.hetzner.cloud/v1/firewalls'
            _attrs = ['firewalls', 'meta']
            firewalls = {'items': lambda: Defs.components_schemas_firewall, 'type': 'array'}
            meta = lambda: Defs.components_schemas_meta
        R.firewalls = [lambda: Defs.components_schemas_firewall]
        R.meta = lambda: Defs.components_schemas_meta
    class components_schemas_list_floating_ips_response:
        """#/components/schemas/list_floating_ips_response"""
        class R:
            required = ['floating_ips']
            type = 'object'
            description = 'Response to GET https://api.hetzner.cloud/v1/floating_ips'
            _attrs = ['floating_ips', 'meta']
            floating_ips = {'items': lambda: Defs.components_schemas_floating_ip, 'type': 'array'}
            meta = lambda: Defs.components_schemas_meta
        R.floating_ips = [lambda: Defs.components_schemas_floating_ip]
        R.meta = lambda: Defs.components_schemas_meta
    class components_schemas_list_images_response:
        """#/components/schemas/list_images_response"""
        class R:
            required = ['images']
            type = 'object'
            description = 'Response to GET https://api.hetzner.cloud/v1/images'
            _attrs = ['images', 'meta']
            images = {'items': lambda: Defs.components_schemas_image, 'type': 'array'}
            meta = lambda: Defs.components_schemas_meta
        R.images = [lambda: Defs.components_schemas_image]
        R.meta = lambda: Defs.components_schemas_meta
    class components_schemas_list_isos_response:
        """#/components/schemas/list_isos_response"""
        class R:
            required = ['isos']
            type = 'object'
            description = 'Response to GET https://api.hetzner.cloud/v1/isos'
            _attrs = ['isos', 'meta']
            isos = {'items': lambda: Defs.components_schemas_iso, 'type': 'array'}
            meta = lambda: Defs.components_schemas_meta
        R.isos = [lambda: Defs.components_schemas_iso]
        R.meta = lambda: Defs.components_schemas_meta
    class components_schemas_list_load_balancer_types_response:
        """#/components/schemas/list_load_balancer_types_response"""
        class R:
            required = ['load_balancer_types']
            type = 'object'
            description = 'Response to GET https://api.hetzner.cloud/v1/load_balancer_types'
            _attrs = ['load_balancer_types', 'meta']
            load_balancer_types = {'items': lambda: Defs.components_schemas_load_balancer_type, 'type': 'array'}
            meta = lambda: Defs.components_schemas_meta
        R.load_balancer_types = [lambda: Defs.components_schemas_load_balancer_type]
        R.meta = lambda: Defs.components_schemas_meta
    class components_schemas_list_load_balancers_response:
        """#/components/schemas/list_load_balancers_response"""
        class R:
            required = ['load_balancers']
            type = 'object'
            description = 'Response to GET https://api.hetzner.cloud/v1/load_balancers'
            _attrs = ['load_balancers', 'meta']
            load_balancers = {'items': lambda: Defs.components_schemas_load_balancer, 'type': 'array'}
            meta = lambda: Defs.components_schemas_meta
        R.load_balancers = [lambda: Defs.components_schemas_load_balancer]
        R.meta = lambda: Defs.components_schemas_meta
    class components_schemas_list_locations_response:
        """#/components/schemas/list_locations_response"""
        class R:
            required = ['locations']
            type = 'object'
            description = 'Response to GET https://api.hetzner.cloud/v1/locations'
            _attrs = ['locations', 'meta']
            locations = {'items': lambda: Defs.components_schemas_location, 'type': 'array'}
            meta = lambda: Defs.components_schemas_meta
        R.locations = [lambda: Defs.components_schemas_location]
        R.meta = lambda: Defs.components_schemas_meta
    class components_schemas_list_networks_response:
        """#/components/schemas/list_networks_response"""
        class R:
            required = ['networks']
            type = 'object'
            description = 'Response to GET https://api.hetzner.cloud/v1/networks'
            _attrs = ['meta', 'networks']
            meta = lambda: Defs.components_schemas_meta
            networks = {'items': lambda: Defs.components_schemas_network, 'type': 'array'}
        R.meta = lambda: Defs.components_schemas_meta
        R.networks = [lambda: Defs.components_schemas_network]
    class components_schemas_list_placementgroups_response:
        """#/components/schemas/list_placementgroups_response"""
        class R:
            required = ['placement_groups']
            title = 'PlacementGroupsResponse'
            type = 'object'
            description = 'Response to GET https://api.hetzner.cloud/v1/placement_groups'
            _attrs = ['meta', 'placement_groups']
            meta = lambda: Defs.components_schemas_meta
            created = {'example': '2016-01-30T23:55:00+00:00', 'type': 'string', 'descr': 'Point in time when the Resource was created (in ISO-8601 format)'}
            id = {'example': 42, 'type': 'integer', 'descr': 'ID of the Resource'}
            labels = lambda: Defs.components_schemas_labels
            name = {'example': 'my-resource', 'type': 'string', 'descr': 'Name of the Resource. Must be unique per Project.'}
            servers = {'example': [42], 'items': {'type': 'integer'}, 'type': 'array', 'descr': 'Array of IDs of Servers that are part of this Placement Group'}
            type = {'enum': ['spread'], 'example': 'spread', 'type': 'string', 'descr': 'Type of the Placement Group'}
            placement_groups = {'items': {'properties': {'created': {'description': 'Point in time when the Resource was created (in ISO-8601 format)', 'example': '2016-01-30T23:55:00+00:00', 'type': 'string'}, 'id': {'description': 'ID of the Resource', 'example': 42, 'type': 'integer'}, 'labels': lambda: Defs.components_schemas_labels, 'name': {'description': 'Name of the Resource. Must be unique per Project.', 'example': 'my-resource', 'type': 'string'}, 'servers': {'description': 'Array of IDs of Servers that are part of this Placement Group', 'example': [42], 'items': {'type': 'integer'}, 'type': 'array'}, 'type': {'description': 'Type of the Placement Group', 'enum': ['spread'], 'example': 'spread', 'type': 'string'}}, 'required': ['id', 'name', 'labels', 'type', 'created', 'servers'], 'title': 'PlacementGroup', 'type': 'object'}, 'type': 'array'}
        R.meta = lambda: Defs.components_schemas_meta
        R.placement_groups = [dict(created = '2016-01-30T23:55:00+00:00', id = id, labels = lambda: Defs.components_schemas_labels, name = 'my-resource', servers = [42], type = 'spread')]
    class components_schemas_list_prices_response:
        """#/components/schemas/list_prices_response"""
        class R:
            required = ['pricing']
            type = 'object'
            description = 'Response to GET https://api.hetzner.cloud/v1/pricing'
            _attrs = ['pricing']
            currency = {'example': 'EUR', 'type': 'string', 'descr': 'Currency the returned prices are expressed in, coded according to ISO 4217'}
            price_monthly = lambda: Defs.components_schemas_price
            floating_ip = {'properties': {'price_monthly': lambda: Defs.components_schemas_price}, 'required': ['price_monthly'], 'type': 'object', 'descr': 'The cost of one Floating IP per month'}
            prices = {'items': lambda: Defs.components_schemas_price_per_time_monthly, 'type': 'array', 'descr': 'Floating IP type costs per Location'}
            type = lambda: Defs.components_schemas_ip_type
            floating_ips = {'items': {'properties': {'prices': {'description': 'Floating IP type costs per Location', 'items': lambda: Defs.components_schemas_price_per_time_monthly, 'type': 'array'}, 'type': lambda: Defs.components_schemas_ip_type}, 'required': ['type', 'prices'], 'type': 'object', 'title': 'ListPricesResponsePricingFloatingIps'}, 'type': 'array', 'descr': 'Costs of Floating IPs types per Location and type'}
            price_per_gb_month = lambda: Defs.components_schemas_price
            image = {'properties': {'price_per_gb_month': lambda: Defs.components_schemas_price}, 'required': ['price_per_gb_month'], 'type': 'object', 'descr': 'The cost of Image per GB/month'}
            id = {'example': 1, 'type': 'integer', 'descr': 'ID of the Load Balancer type the price is for'}
            name = {'example': 'lb11', 'type': 'string', 'descr': 'Name of the Load Balancer type the price is for'}
            prices = {'items': lambda: Defs.components_schemas_price_per_time, 'type': 'array', 'descr': 'Load Balancer type costs per Location'}
            load_balancer_types = {'items': {'properties': {'id': {'description': 'ID of the Load Balancer type the price is for', 'example': 1, 'type': 'integer'}, 'name': {'description': 'Name of the Load Balancer type the price is for', 'example': 'lb11', 'type': 'string'}, 'prices': {'description': 'Load Balancer type costs per Location', 'items': lambda: Defs.components_schemas_price_per_time, 'type': 'array'}}, 'required': ['id', 'name', 'prices'], 'type': 'object', 'title': 'ListPricesResponsePricingLoadBalancerTypes'}, 'type': 'array', 'descr': 'Costs of Load Balancer types per Location and type'}
            prices = {'items': lambda: Defs.components_schemas_price_per_time, 'type': 'array', 'descr': 'Primary IP type costs per Location'}
            type = lambda: Defs.components_schemas_ip_type
            primary_ips = {'items': {'properties': {'prices': {'description': 'Primary IP type costs per Location', 'items': lambda: Defs.components_schemas_price_per_time, 'type': 'array'}, 'type': lambda: Defs.components_schemas_ip_type}, 'required': ['type', 'prices'], 'type': 'object', 'title': 'ListPricesResponsePricingPrimaryIps'}, 'type': 'array', 'descr': 'Costs of Primary IPs types per Location'}
            percentage = {'example': '20.0000000000', 'type': 'string', 'descr': 'Percentage by how much the base price will increase'}
            server_backup = {'properties': {'percentage': {'description': 'Percentage by how much the base price will increase', 'example': '20.0000000000', 'type': 'string'}}, 'required': ['percentage'], 'type': 'object', 'descr': 'Will increase base Server costs by specific percentage'}
            id = {'example': 4, 'type': 'integer', 'descr': 'ID of the Server type the price is for'}
            name = {'example': 'cx11', 'type': 'string', 'descr': 'Name of the Server type the price is for'}
            prices = {'items': lambda: Defs.components_schemas_price_per_time, 'type': 'array', 'descr': 'Server type costs per Location'}
            server_types = {'items': {'properties': {'id': {'description': 'ID of the Server type the price is for', 'example': 4, 'type': 'integer'}, 'name': {'description': 'Name of the Server type the price is for', 'example': 'cx11', 'type': 'string'}, 'prices': {'description': 'Server type costs per Location', 'items': lambda: Defs.components_schemas_price_per_time, 'type': 'array'}}, 'required': ['id', 'name', 'prices'], 'type': 'object', 'title': 'ListPricesResponsePricingServerTypes'}, 'type': 'array', 'descr': 'Costs of Server types per Location and type'}
            price_per_tb = lambda: Defs.components_schemas_price
            traffic = {'properties': {'price_per_tb': lambda: Defs.components_schemas_price}, 'required': ['price_per_tb'], 'type': 'object', 'descr': 'The cost of additional traffic per TB'}
            vat_rate = {'example': '19.000000', 'type': 'string', 'descr': 'The VAT rate used for calculating prices with VAT'}
            price_per_gb_month = lambda: Defs.components_schemas_price
            volume = {'properties': {'price_per_gb_month': lambda: Defs.components_schemas_price}, 'required': ['price_per_gb_month'], 'type': 'object', 'descr': 'The cost of Volume per GB/month'}
            pricing = {'additionalProperties': False, 'properties': {'currency': {'description': 'Currency the returned prices are expressed in, coded according to ISO 4217', 'example': 'EUR', 'type': 'string'}, 'floating_ip': {'description': 'The cost of one Floating IP per month', 'properties': {'price_monthly': lambda: Defs.components_schemas_price}, 'required': ['price_monthly'], 'type': 'object'}, 'floating_ips': {'description': 'Costs of Floating IPs types per Location and type', 'items': {'properties': {'prices': {'description': 'Floating IP type costs per Location', 'items': lambda: Defs.components_schemas_price_per_time_monthly, 'type': 'array'}, 'type': lambda: Defs.components_schemas_ip_type}, 'required': ['type', 'prices'], 'type': 'object', 'title': 'ListPricesResponsePricingFloatingIps'}, 'type': 'array'}, 'image': {'description': 'The cost of Image per GB/month', 'properties': {'price_per_gb_month': lambda: Defs.components_schemas_price}, 'required': ['price_per_gb_month'], 'type': 'object'}, 'load_balancer_types': {'description': 'Costs of Load Balancer types per Location and type', 'items': {'properties': {'id': {'description': 'ID of the Load Balancer type the price is for', 'example': 1, 'type': 'integer'}, 'name': {'description': 'Name of the Load Balancer type the price is for', 'example': 'lb11', 'type': 'string'}, 'prices': {'description': 'Load Balancer type costs per Location', 'items': lambda: Defs.components_schemas_price_per_time, 'type': 'array'}}, 'required': ['id', 'name', 'prices'], 'type': 'object', 'title': 'ListPricesResponsePricingLoadBalancerTypes'}, 'type': 'array'}, 'primary_ips': {'description': 'Costs of Primary IPs types per Location', 'items': {'properties': {'prices': {'description': 'Primary IP type costs per Location', 'items': lambda: Defs.components_schemas_price_per_time, 'type': 'array'}, 'type': lambda: Defs.components_schemas_ip_type}, 'required': ['type', 'prices'], 'type': 'object', 'title': 'ListPricesResponsePricingPrimaryIps'}, 'type': 'array'}, 'server_backup': {'description': 'Will increase base Server costs by specific percentage', 'properties': {'percentage': {'description': 'Percentage by how much the base price will increase', 'example': '20.0000000000', 'type': 'string'}}, 'required': ['percentage'], 'type': 'object'}, 'server_types': {'description': 'Costs of Server types per Location and type', 'items': {'properties': {'id': {'description': 'ID of the Server type the price is for', 'example': 4, 'type': 'integer'}, 'name': {'description': 'Name of the Server type the price is for', 'example': 'cx11', 'type': 'string'}, 'prices': {'description': 'Server type costs per Location', 'items': lambda: Defs.components_schemas_price_per_time, 'type': 'array'}}, 'required': ['id', 'name', 'prices'], 'type': 'object', 'title': 'ListPricesResponsePricingServerTypes'}, 'type': 'array'}, 'traffic': {'description': 'The cost of additional traffic per TB', 'properties': {'price_per_tb': lambda: Defs.components_schemas_price}, 'required': ['price_per_tb'], 'type': 'object'}, 'vat_rate': {'description': 'The VAT rate used for calculating prices with VAT', 'example': '19.000000', 'type': 'string'}, 'volume': {'description': 'The cost of Volume per GB/month', 'properties': {'price_per_gb_month': lambda: Defs.components_schemas_price}, 'required': ['price_per_gb_month'], 'type': 'object'}}, 'required': ['currency', 'vat_rate', 'image', 'floating_ip', 'floating_ips', 'traffic', 'server_backup', 'volume', 'server_types', 'load_balancer_types', 'primary_ips'], 'type': 'object'}
        R.pricing = dict(currency = 'EUR', floating_ip = dict(price_monthly = lambda: Defs.components_schemas_price), floating_ips = [dict(prices = [lambda: Defs.components_schemas_price_per_time_monthly], type = lambda: Defs.components_schemas_ip_type)], image = dict(price_per_gb_month = lambda: Defs.components_schemas_price), load_balancer_types = [dict(id = id, name = 'lb11', prices = [lambda: Defs.components_schemas_price_per_time])], primary_ips = [dict(prices = [lambda: Defs.components_schemas_price_per_time], type = lambda: Defs.components_schemas_ip_type)], server_backup = dict(percentage = '20.0000000000'), server_types = [dict(id = id, name = 'cx11', prices = [lambda: Defs.components_schemas_price_per_time])], traffic = dict(price_per_tb = lambda: Defs.components_schemas_price), vat_rate = '19.000000', volume = dict(price_per_gb_month = lambda: Defs.components_schemas_price))
    class components_schemas_list_primary_ips_response:
        """#/components/schemas/list_primary_ips_response"""
        class R:
            required = ['primary_ips']
            title = 'PrimaryIPsResponse'
            type = 'object'
            description = 'Response to GET https://api.hetzner.cloud/v1/primary_ips'
            _attrs = ['meta', 'primary_ips']
            meta = lambda: Defs.components_schemas_meta
            assignee_id = {'example': 17, 'nullable': True, 'type': 'integer', 'descr': 'ID of the resource the Primary IP is assigned to, null if it is not assigned at all'}
            assignee_type = {'enum': ['server'], 'type': 'string', 'descr': 'Resource type the Primary IP can be assigned to'}
            auto_delete = {'example': True, 'type': 'boolean', 'descr': 'Delete this Primary IP when the resource it is assigned to is deleted'}
            blocked = {'example': False, 'type': 'boolean', 'descr': 'Whether the IP is blocked'}
            created = {'example': '2016-01-30T23:55:00+00:00', 'type': 'string', 'descr': 'Point in time when the Resource was created (in ISO-8601 format)'}
            datacenter = lambda: Defs.components_schemas_datacenter
            dns_ptr = {'items': lambda: Defs.components_schemas_dns_ptr, 'type': 'array', 'descr': 'Array of reverse DNS entries'}
            id = {'example': 42, 'type': 'integer', 'descr': 'ID of the Resource'}
            ip = {'example': '131.232.99.1', 'type': 'string', 'descr': 'IP address'}
            labels = lambda: Defs.components_schemas_labels
            name = {'example': 'my-resource', 'type': 'string', 'descr': 'Name of the Resource. Must be unique per Project.'}
            protection = lambda: Defs.components_schemas_protection
            type = lambda: Defs.components_schemas_ip_type
            primary_ips = {'items': {'properties': {'assignee_id': {'description': 'ID of the resource the Primary IP is assigned to, null if it is not assigned at all', 'example': 17, 'nullable': True, 'type': 'integer'}, 'assignee_type': {'description': 'Resource type the Primary IP can be assigned to', 'enum': ['server'], 'type': 'string'}, 'auto_delete': {'description': 'Delete this Primary IP when the resource it is assigned to is deleted', 'example': True, 'type': 'boolean'}, 'blocked': {'description': 'Whether the IP is blocked', 'example': False, 'type': 'boolean'}, 'created': {'description': 'Point in time when the Resource was created (in ISO-8601 format)', 'example': '2016-01-30T23:55:00+00:00', 'type': 'string'}, 'datacenter': lambda: Defs.components_schemas_datacenter, 'dns_ptr': {'description': 'Array of reverse DNS entries', 'items': lambda: Defs.components_schemas_dns_ptr, 'type': 'array'}, 'id': {'description': 'ID of the Resource', 'example': 42, 'type': 'integer'}, 'ip': {'description': 'IP address', 'example': '131.232.99.1', 'type': 'string'}, 'labels': lambda: Defs.components_schemas_labels, 'name': {'description': 'Name of the Resource. Must be unique per Project.', 'example': 'my-resource', 'type': 'string'}, 'protection': lambda: Defs.components_schemas_protection, 'type': lambda: Defs.components_schemas_ip_type}, 'required': ['id', 'name', 'labels', 'created', 'blocked', 'datacenter', 'ip', 'dns_ptr', 'protection', 'type', 'auto_delete', 'assignee_type', 'assignee_id'], 'title': 'PrimaryIP', 'type': 'object'}, 'type': 'array'}
        R.meta = lambda: Defs.components_schemas_meta
        R.primary_ips = [dict(assignee_id = 17, assignee_type = 'server', auto_delete = True, blocked = True, created = '2016-01-30T23:55:00+00:00', datacenter = lambda: Defs.components_schemas_datacenter, dns_ptr = [lambda: Defs.components_schemas_dns_ptr], id = id, ip = '131.232.99.1', labels = lambda: Defs.components_schemas_labels, name = 'my-resource', protection = lambda: Defs.components_schemas_protection, type = lambda: Defs.components_schemas_ip_type)]
    class components_schemas_list_server_types_response:
        """#/components/schemas/list_server_types_response"""
        class R:
            required = ['server_types']
            type = 'object'
            description = 'Response to GET https://api.hetzner.cloud/v1/server_types'
            _attrs = ['server_types', 'meta']
            server_types = {'items': lambda: Defs.components_schemas_server_type, 'type': 'array'}
            meta = lambda: Defs.components_schemas_meta
        R.server_types = [lambda: Defs.components_schemas_server_type]
        R.meta = lambda: Defs.components_schemas_meta
    class components_schemas_list_servers_response:
        """#/components/schemas/list_servers_response"""
        class R:
            required = ['servers']
            type = 'object'
            description = 'Response to GET https://api.hetzner.cloud/v1/servers'
            _attrs = ['meta', 'servers']
            meta = lambda: Defs.components_schemas_meta
            servers = {'items': lambda: Defs.components_schemas_server, 'type': 'array'}
        R.meta = lambda: Defs.components_schemas_meta
        R.servers = [lambda: Defs.components_schemas_server]
    class components_schemas_list_ssh_keys_response:
        """#/components/schemas/list_ssh_keys_response"""
        class R:
            required = ['ssh_keys']
            type = 'object'
            description = 'Response to GET https://api.hetzner.cloud/v1/ssh_keys'
            _attrs = ['meta', 'ssh_keys']
            meta = lambda: Defs.components_schemas_meta
            ssh_keys = {'items': lambda: Defs.components_schemas_ssh_key, 'type': 'array'}
        R.meta = lambda: Defs.components_schemas_meta
        R.ssh_keys = [lambda: Defs.components_schemas_ssh_key]
    class components_schemas_list_volumes_response:
        """#/components/schemas/list_volumes_response"""
        class R:
            required = ['volumes']
            type = 'object'
            description = 'Response to GET https://api.hetzner.cloud/v1/volumes'
            _attrs = ['meta', 'volumes']
            meta = lambda: Defs.components_schemas_meta
            volumes = {'items': lambda: Defs.components_schemas_volume, 'type': 'array'}
        R.meta = lambda: Defs.components_schemas_meta
        R.volumes = [lambda: Defs.components_schemas_volume]
    class components_schemas_load_balancer:
        """#/components/schemas/load_balancer"""
        class R:
            required = ['id', 'name', 'public_net', 'private_net', 'location', 'load_balancer_type', 'protection', 'labels', 'created', 'services', 'targets', 'algorithm', 'outgoing_traffic', 'ingoing_traffic', 'included_traffic']
            type = 'object'
            _attrs = ['algorithm', 'created', 'id', 'included_traffic', 'ingoing_traffic', 'labels', 'load_balancer_type', 'location', 'name', 'outgoing_traffic', 'private_net', 'protection', 'public_net', 'services', 'targets']
            algorithm = lambda: Defs.components_schemas_load_balancer_algorithm
            created = {'example': '2016-01-30T23:55:00+00:00', 'type': 'string', 'descr': 'Point in time when the Resource was created (in ISO-8601 format)'}
            id = {'example': 42, 'type': 'integer', 'descr': 'ID of the Resource'}
            included_traffic = {'example': 10000, 'type': 'integer', 'format': 'int64', 'descr': 'Free Traffic for the current billing period in bytes'}
            ingoing_traffic = {'nullable': True, 'type': 'integer', 'format': 'int64', 'descr': 'Inbound Traffic for the current billing period in bytes'}
            labels = lambda: Defs.components_schemas_labels
            load_balancer_type = lambda: Defs.components_schemas_load_balancer_type
            location = lambda: Defs.components_schemas_location
            name = {'example': 'my-resource', 'type': 'string', 'descr': 'Name of the Resource. Must be unique per Project.'}
            outgoing_traffic = {'nullable': True, 'type': 'integer', 'format': 'int64', 'descr': 'Outbound Traffic for the current billing period in bytes'}
            private_net = {'items': lambda: Defs.components_schemas_load_balancer_private_net, 'type': 'array', 'descr': 'Private networks information'}
            protection = lambda: Defs.components_schemas_protection
            public_net = lambda: Defs.components_schemas_load_balancer_public_net
            services = {'items': lambda: Defs.components_schemas_load_balancer_service, 'type': 'array', 'descr': 'List of services that belong to this Load Balancer'}
            targets = {'items': lambda: Defs.components_schemas_target, 'type': 'array', 'descr': 'List of targets that belong to this Load Balancer'}
        R.algorithm = lambda: Defs.components_schemas_load_balancer_algorithm
        R.created = '2016-01-30T23:55:00+00:00'
        R.id = id
        R.included_traffic = 10000
        R.ingoing_traffic = 0
        R.labels = lambda: Defs.components_schemas_labels
        R.load_balancer_type = lambda: Defs.components_schemas_load_balancer_type
        R.location = lambda: Defs.components_schemas_location
        R.name = 'my-resource'
        R.outgoing_traffic = 0
        R.private_net = [lambda: Defs.components_schemas_load_balancer_private_net]
        R.protection = lambda: Defs.components_schemas_protection
        R.public_net = lambda: Defs.components_schemas_load_balancer_public_net
        R.services = [lambda: Defs.components_schemas_load_balancer_service]
        R.targets = [lambda: Defs.components_schemas_target]
    class components_schemas_load_balancer_algorithm:
        """#/components/schemas/load_balancer_algorithm"""
        class R:
            description = 'Algorithm of the Load Balancer | Request for POST https://api.hetzner.cloud/v1/load_balancers/{id}/actions/change_algorithm'
            required = ['type']
            type = 'object'
            _attrs = ['type']
            type = {'enum': ['least_connections', 'round_robin'], 'type': 'string', 'descr': 'Type of the algorithm | Algorithm of the Load Balancer'}
        R.type = 'least_connections'
    class components_schemas_load_balancer_private_net:
        """#/components/schemas/load_balancer_private_net"""
        class R:
            type = 'object'
            _attrs = ['ip', 'network']
            ip = {'example': '10.0.0.2', 'type': 'string'}
            network = {'example': 4711, 'type': 'integer'}
        R.ip = '10.0.0.2'
        R.network = 4711
    class components_schemas_load_balancer_public_net:
        """#/components/schemas/load_balancer_public_net"""
        class R:
            description = 'Public network information'
            required = ['enabled', 'ipv4', 'ipv6']
            type = 'object'
            _attrs = ['enabled', 'ipv4', 'ipv6']
            enabled = {'type': 'boolean', 'descr': 'Public Interface enabled or not'}
            dns_ptr = {'example': 'lb1.example.com', 'nullable': True, 'type': 'string', 'descr': 'Reverse DNS PTR entry for the IPv4 address of this Load Balancer'}
            ip = {'example': '1.2.3.4', 'nullable': True, 'type': 'string', 'descr': 'IP address (v4) of this Load Balancer'}
            ipv4 = {'properties': {'dns_ptr': {'description': 'Reverse DNS PTR entry for the IPv4 address of this Load Balancer', 'example': 'lb1.example.com', 'nullable': True, 'type': 'string'}, 'ip': {'description': 'IP address (v4) of this Load Balancer', 'example': '1.2.3.4', 'nullable': True, 'type': 'string'}}, 'type': 'object', 'descr': 'IP address (v4)'}
            dns_ptr = {'example': 'lb1.example.com', 'nullable': True, 'type': 'string', 'descr': 'Reverse DNS PTR entry for the IPv6 address of this Load Balancer'}
            ip = {'example': '2001:db8::1', 'nullable': True, 'type': 'string', 'descr': 'IP address (v6) of this Load Balancer'}
            ipv6 = {'properties': {'dns_ptr': {'description': 'Reverse DNS PTR entry for the IPv6 address of this Load Balancer', 'example': 'lb1.example.com', 'nullable': True, 'type': 'string'}, 'ip': {'description': 'IP address (v6) of this Load Balancer', 'example': '2001:db8::1', 'nullable': True, 'type': 'string'}}, 'type': 'object', 'descr': 'IP address (v6)'}
        R.enabled = True
        R.ipv4 = dict(dns_ptr = 'lb1.example.com', ip = '1.2.3.4')
        R.ipv6 = dict(dns_ptr = 'lb1.example.com', ip = '2001:db8::1')
    class components_schemas_load_balancer_service:
        """#/components/schemas/load_balancer_service"""
        class R:
            required = ['protocol', 'listen_port', 'destination_port', 'proxyprotocol', 'health_check']
            title = 'LoadBalancerService'
            type = 'object'
            description = 'A service for a Load Balancer.'
            _attrs = ['destination_port', 'health_check', 'http', 'listen_port', 'protocol', 'proxyprotocol']
            destination_port = {'example': 80, 'type': 'integer', 'descr': 'Port the Load Balancer will balance to'}
            domain = {'example': 'example.com', 'nullable': True, 'type': 'string', 'descr': 'Host header to send in the HTTP request. May not contain spaces, percent or backslash symbols. Can be null, in that case no host header is sent.'}
            path = {'example': '/', 'type': 'string', 'descr': 'HTTP path to use for health checks. May not contain literal spaces, use percent-encoding instead.'}
            response = {'example': '{"status": "ok"}', 'type': 'string', 'descr': 'String that must be contained in HTTP response in order to pass the health check'}
            status_codes = {'example': ['2??', '3??'], 'items': {'type': 'string'}, 'type': 'array', 'descr': 'List of returned HTTP status codes in order to pass the health check. Supports the wildcards `?` for exactly one character and `*` for multiple ones. The default is to pass the health check for any status code between 2?? and 3??.'}
            tls = {'example': False, 'type': 'boolean', 'descr': 'Use HTTPS for health check'}
            http = {'additionalProperties': False, 'properties': {'domain': {'description': 'Host header to send in the HTTP request. May not contain spaces, percent or backslash symbols. Can be null, in that case no host header is sent.', 'example': 'example.com', 'nullable': True, 'type': 'string'}, 'path': {'description': 'HTTP path to use for health checks. May not contain literal spaces, use percent-encoding instead.', 'example': '/', 'type': 'string'}, 'response': {'description': 'String that must be contained in HTTP response in order to pass the health check', 'example': '{"status": "ok"}', 'type': 'string'}, 'status_codes': {'description': 'List of returned HTTP status codes in order to pass the health check. Supports the wildcards `?` for exactly one character and `*` for multiple ones. The default is to pass the health check for any status code between 2?? and 3??.', 'example': ['2??', '3??'], 'items': {'type': 'string'}, 'type': 'array'}, 'tls': {'description': 'Use HTTPS for health check', 'example': False, 'type': 'boolean'}}, 'required': ['domain', 'path'], 'type': 'object', 'descr': 'Additional configuration for protocol http'}
            interval = {'example': 15, 'type': 'integer', 'descr': 'Time interval in seconds health checks are performed'}
            port = {'example': 4711, 'type': 'integer', 'descr': 'Port the health check will be performed on'}
            protocol = {'enum': ['http', 'tcp'], 'example': 'http', 'type': 'string', 'descr': 'Type of the health check'}
            retries = {'example': 3, 'type': 'integer', 'descr': 'Unsuccessful retries needed until a target is considered unhealthy; an unhealthy target needs the same number of successful retries to become healthy again'}
            timeout = {'example': 10, 'type': 'integer', 'descr': 'Time in seconds after an attempt is considered a timeout'}
            health_check = {'additionalProperties': False, 'properties': {'http': {'additionalProperties': False, 'description': 'Additional configuration for protocol http', 'properties': {'domain': {'description': 'Host header to send in the HTTP request. May not contain spaces, percent or backslash symbols. Can be null, in that case no host header is sent.', 'example': 'example.com', 'nullable': True, 'type': 'string'}, 'path': {'description': 'HTTP path to use for health checks. May not contain literal spaces, use percent-encoding instead.', 'example': '/', 'type': 'string'}, 'response': {'description': 'String that must be contained in HTTP response in order to pass the health check', 'example': '{"status": "ok"}', 'type': 'string'}, 'status_codes': {'description': 'List of returned HTTP status codes in order to pass the health check. Supports the wildcards `?` for exactly one character and `*` for multiple ones. The default is to pass the health check for any status code between 2?? and 3??.', 'example': ['2??', '3??'], 'items': {'type': 'string'}, 'type': 'array'}, 'tls': {'description': 'Use HTTPS for health check', 'example': False, 'type': 'boolean'}}, 'required': ['domain', 'path'], 'type': 'object'}, 'interval': {'description': 'Time interval in seconds health checks are performed', 'example': 15, 'type': 'integer'}, 'port': {'description': 'Port the health check will be performed on', 'example': 4711, 'type': 'integer'}, 'protocol': {'description': 'Type of the health check', 'enum': ['http', 'tcp'], 'example': 'http', 'type': 'string'}, 'retries': {'description': 'Unsuccessful retries needed until a target is considered unhealthy; an unhealthy target needs the same number of successful retries to become healthy again', 'example': 3, 'type': 'integer'}, 'timeout': {'description': 'Time in seconds after an attempt is considered a timeout', 'example': 10, 'type': 'integer'}}, 'required': ['protocol', 'port', 'interval', 'timeout', 'retries'], 'title': 'LoadBalancerServiceHealthCheck', 'type': 'object', 'descr': 'Service health check'}
            http = lambda: Defs.components_schemas_http
            listen_port = {'example': 443, 'type': 'integer', 'descr': 'Port the Load Balancer listens on'}
            protocol = {'enum': ['http', 'https', 'tcp'], 'example': 'https', 'type': 'string', 'descr': 'Protocol of the Load Balancer'}
            proxyprotocol = {'example': False, 'type': 'boolean', 'descr': 'Is Proxyprotocol enabled or not'}
        R.destination_port = 80
        R.health_check = dict(http = dict(domain = 'example.com', path = '/', response = '{"status": "ok"}', status_codes = ['2??', '3??'], tls = True), interval = 15, port = 4711, protocol = 'http', retries = 3, timeout = 10)
        R.http = lambda: Defs.components_schemas_http
        R.listen_port = 443
        R.protocol = 'https'
        R.proxyprotocol = True
    class components_schemas_load_balancer_type:
        """#/components/schemas/load_balancer_type"""
        class R:
            required = ['id', 'name', 'description', 'max_connections', 'max_services', 'max_targets', 'max_assigned_certificates', 'deprecated', 'prices']
            type = 'object'
            _attrs = ['deprecated', 'description', 'id', 'max_assigned_certificates', 'max_connections', 'max_services', 'max_targets', 'name', 'prices']
            deprecated = {'example': '2016-01-30T23:50:00+00:00', 'nullable': True, 'type': 'string', 'descr': 'Point in time when the Load Balancer type is deprecated (in ISO-8601 format)'}
            description = {'example': 'LB11', 'type': 'string', 'descr': 'Description of the Load Balancer type'}
            id = {'example': 1, 'type': 'integer', 'descr': 'ID of the Load Balancer type'}
            max_assigned_certificates = {'example': 10, 'type': 'integer', 'descr': 'Number of SSL Certificates that can be assigned to a single Load Balancer'}
            max_connections = {'example': 20000, 'type': 'integer', 'descr': 'Number of maximum simultaneous open connections'}
            max_services = {'example': 5, 'type': 'integer', 'descr': 'Number of services a Load Balancer of this type can have'}
            max_targets = {'example': 25, 'type': 'integer', 'descr': 'Number of targets a single Load Balancer can have'}
            name = {'example': 'lb11', 'type': 'string', 'descr': 'Unique identifier of the Load Balancer type'}
            prices = {'items': lambda: Defs.components_schemas_price_per_time, 'type': 'array', 'descr': 'Prices in different network zones'}
        R.deprecated = '2016-01-30T23:50:00+00:00'
        R.description = 'LB11'
        R.id = id
        R.max_assigned_certificates = 10
        R.max_connections = 20000
        R.max_services = 5
        R.max_targets = 25
        R.name = 'lb11'
        R.prices = [lambda: Defs.components_schemas_price_per_time]
    class components_schemas_location:
        """#/components/schemas/location"""
        class R:
            required = ['id', 'name', 'description', 'country', 'city', 'latitude', 'longitude', 'network_zone']
            type = 'object'
            description = 'Location the Floating IP was created in. Routing is optimized for this Location. | Location of the Volume. Volume can only be attached to Servers in the same Location.'
            _attrs = ['city', 'country', 'description', 'id', 'latitude', 'longitude', 'name', 'network_zone']
            city = {'example': 'Falkenstein', 'type': 'string', 'descr': 'City the Location is closest to'}
            country = {'example': 'DE', 'type': 'string', 'descr': 'ISO 3166-1 alpha-2 code of the country the Location resides in'}
            description = {'example': 'Falkenstein DC Park 1', 'type': 'string', 'descr': 'Description of the Location'}
            id = {'example': 1, 'type': 'integer', 'descr': 'ID of the Location'}
            latitude = {'example': 50.47612, 'type': 'number', 'descr': 'Latitude of the city closest to the Location'}
            longitude = {'example': 12.370071, 'type': 'number', 'descr': 'Longitude of the city closest to the Location'}
            name = {'example': 'fsn1', 'type': 'string', 'descr': 'Unique identifier of the Location'}
            network_zone = {'example': 'eu-central', 'type': 'string', 'descr': 'Name of network zone this Location resides in'}
        R.city = 'Falkenstein'
        R.country = 'DE'
        R.description = 'Falkenstein DC Park 1'
        R.id = id
        R.latitude = 50.47612
        R.longitude = 12.370071
        R.name = 'fsn1'
        R.network_zone = 'eu-central'
    class components_schemas_meta:
        """#/components/schemas/meta"""
        class R:
            required = ['pagination']
            type = 'object'
            description = 'Metadata contained in the response'
            _attrs = ['pagination']
            pagination = lambda: Defs.components_schemas_pagination
        R.pagination = lambda: Defs.components_schemas_pagination
    class components_schemas_metrics:
        """#/components/schemas/metrics"""
        class R:
            required = ['start', 'end', 'step', 'time_series']
            type = 'object'
            description = 'You must specify the type of metric to get: open_connections, requests_per_second or bandwidth. You can also specify more than one type by comma separation, e.g. requests_per_second,bandwidth. Depending on the type you will get different time series data.'
            _attrs = ['end', 'start', 'step', 'time_series']
            end = {'example': '2017-01-01T23:00:00+00:00', 'type': 'string', 'descr': 'End of period of metrics reported (in ISO-8601 format)'}
            start = {'example': '2017-01-01T00:00:00+00:00', 'type': 'string', 'descr': 'Start of period of metrics reported (in ISO-8601 format)'}
            step = {'example': 60, 'type': 'integer', 'descr': 'Resolution of results in seconds.'}
            time_series = {'additionalProperties': {'properties': {'values': {'description': 'Metrics Timestamps with values', 'items': {'items': {'oneOf': [{'type': 'number'}, {'type': 'string'}], 'title': 'MetricsTimeSeriesValue'}, 'type': 'array'}, 'type': 'array'}}, 'required': ['values'], 'type': 'object'}, 'example': {'name_of_timeseries': {'values': [[1435781470.622, '42'], [1435781471.622, '43']]}}, 'type': 'object', 'title': 'MetricsTimeSeries', 'descr': 'Hash with timeseries information, containing the name of timeseries as key'}
        R.end = '2017-01-01T23:00:00+00:00'
        R.start = '2017-01-01T00:00:00+00:00'
        R.step = 60
        R.time_series = {'name_of_timeseries': {'values': [[1435781470.622, '42'], [1435781471.622, '43']]}},
    class components_schemas_network:
        """#/components/schemas/network"""
        class R:
            required = ['id', 'name', 'ip_range', 'subnets', 'routes', 'servers', 'protection', 'labels', 'created']
            type = 'object'
            _attrs = ['created', 'id', 'ip_range', 'labels', 'load_balancers', 'name', 'protection', 'routes', 'servers', 'subnets']
            created = {'example': '2016-01-30T23:50:00+00:00', 'type': 'string', 'descr': 'Point in time when the Network was created (in ISO-8601 format)'}
            id = {'example': 4711, 'type': 'integer', 'descr': 'ID of the Network'}
            ip_range = {'example': '10.0.0.0/16', 'type': 'string', 'descr': 'IPv4 prefix of the whole Network'}
            labels = lambda: Defs.components_schemas_labels
            load_balancers = {'example': [42], 'items': {'type': 'integer'}, 'type': 'array', 'descr': 'Array of IDs of Load Balancers attached to this Network'}
            name = {'example': 'mynet', 'type': 'string', 'descr': 'Name of the Network'}
            protection = lambda: Defs.components_schemas_protection
            routes = {'items': lambda: Defs.components_schemas_route, 'type': 'array', 'descr': 'Array of routes set in this Network'}
            servers = {'example': [42], 'items': {'type': 'integer'}, 'type': 'array', 'descr': 'Array of IDs of Servers attached to this Network'}
            subnets = {'items': lambda: Defs.components_schemas_subnet_with_gateway, 'type': 'array', 'descr': 'Array subnets allocated in this Network'}
        R.created = '2016-01-30T23:50:00+00:00'
        R.id = id
        R.ip_range = '10.0.0.0/16'
        R.labels = lambda: Defs.components_schemas_labels
        R.load_balancers = [42]
        R.name = 'mynet'
        R.protection = lambda: Defs.components_schemas_protection
        R.routes = [lambda: Defs.components_schemas_route]
        R.servers = [42]
        R.subnets = [lambda: Defs.components_schemas_subnet_with_gateway]
    class components_schemas_pagination:
        """#/components/schemas/pagination"""
        class R:
            required = ['page', 'per_page', 'previous_page', 'next_page', 'last_page', 'total_entries']
            type = 'object'
            description = 'Information about the current pagination. The keys previous_page, next_page, last_page, and total_entries may be null when on the first page, last page, or when the total number of entries is unknown'
            _attrs = ['last_page', 'next_page', 'page', 'per_page', 'previous_page', 'total_entries']
            last_page = {'example': 4, 'nullable': True, 'type': 'integer', 'descr': 'ID of the last page available. Can be null if the current page is the last one. | The last page number'}
            next_page = {'example': 4, 'nullable': True, 'type': 'integer', 'descr': 'ID of the next page. Can be null if the current page is the last one. | The next page number'}
            page = {'example': 3, 'type': 'integer', 'descr': 'Current page number | The current page number'}
            per_page = {'example': 25, 'type': 'integer', 'descr': 'Maximum number of items shown per page in the response | The number of entries per page'}
            previous_page = {'example': 2, 'nullable': True, 'type': 'integer', 'descr': 'ID of the previous page. Can be null if the current page is the first one. | The previous page number'}
            total_entries = {'example': 100, 'nullable': True, 'type': 'integer', 'descr': 'The total number of entries that exist in the database for this query. Nullable if unknown. | The total number of entries'}
        R.last_page = 4
        R.next_page = 4
        R.page = 3
        R.per_page = 25
        R.previous_page = 2
        R.total_entries = 100
    class components_schemas_power_off_server_response:
        """#/components/schemas/power_off_server_response"""
        class R:
            required = ['action']
            title = 'ActionResponse'
            type = 'object'
            description = 'Response to POST https://api.hetzner.cloud/v1/servers/{id}/actions/poweroff'
            _attrs = ['action']
            action = lambda: Defs.components_schemas_action
        R.action = lambda: Defs.components_schemas_action
    class components_schemas_power_on_server_response:
        """#/components/schemas/power_on_server_response"""
        class R:
            required = ['action']
            title = 'ActionResponse'
            type = 'object'
            description = 'Response to POST https://api.hetzner.cloud/v1/servers/{id}/actions/poweron'
            _attrs = ['action']
            action = lambda: Defs.components_schemas_action
        R.action = lambda: Defs.components_schemas_action
    class components_schemas_price:
        """#/components/schemas/price"""
        class R:
            description = 'Hourly costs for a Resource in this Location | Monthly costs for a Resource in this Location | Monthly costs for a Floating IP type in this Location | Hourly costs for a Load Balancer type in this network zone | Monthly costs for a Load Balancer type in this network zone | Hourly costs for a Primary IP type in this Location | Monthly costs for a Primary IP type in this Location | Hourly costs for a Server type in this Location | Monthly costs for a Server type in this Location'
            required = ['net', 'gross']
            type = 'object'
            _attrs = ['gross', 'net']
            gross = {'example': '1.1900000000000000', 'type': 'string', 'format': 'decimal', 'descr': 'Price with VAT added'}
            net = {'example': '1.0000000000', 'type': 'string', 'format': 'decimal', 'descr': 'Price without VAT'}
        R.gross = '1.1900000000000000'
        R.net = '1.0000000000'
    class components_schemas_price_per_time:
        """#/components/schemas/price_per_time"""
        class R:
            required = ['location', 'price_hourly', 'price_monthly']
            type = 'object'
            _attrs = ['location', 'price_hourly', 'price_monthly']
            location = {'example': 'fsn1', 'type': 'string', 'descr': 'Name of the Location the price is for'}
            price_hourly = lambda: Defs.components_schemas_price
            price_monthly = lambda: Defs.components_schemas_price
        R.location = 'fsn1'
        R.price_hourly = lambda: Defs.components_schemas_price
        R.price_monthly = lambda: Defs.components_schemas_price
    class components_schemas_price_per_time_monthly:
        """#/components/schemas/price_per_time_monthly"""
        class R:
            required = ['location', 'price_monthly']
            type = 'object'
            _attrs = ['location', 'price_monthly']
            location = {'example': 'fsn1', 'type': 'string', 'descr': 'Name of the Location the price is for'}
            price_monthly = lambda: Defs.components_schemas_price
        R.location = 'fsn1'
        R.price_monthly = lambda: Defs.components_schemas_price
    class components_schemas_protection:
        """#/components/schemas/protection"""
        class R:
            description = 'Protection configuration for the Resource'
            required = ['delete']
            type = 'object'
            _attrs = ['delete']
            delete = {'example': False, 'type': 'boolean', 'descr': 'If true, prevents the Resource from being deleted | If true, prevents the Network from being deleted'}
        R.delete = True
    class components_schemas_rebuild_server_from_image_request:
        """#/components/schemas/rebuild_server_from_image_request"""
        class R:
            required = ['image']
            title = 'RebuildServerRequest'
            type = 'object'
            description = 'Request for POST https://api.hetzner.cloud/v1/servers/{id}/actions/rebuild'
            _attrs = ['image']
            image = {'example': 'ubuntu-20.04', 'type': 'string', 'descr': 'ID or name of Image to rebuilt from.'}
        R.image = 'ubuntu-20.04'
    class components_schemas_rebuild_server_from_image_response:
        """#/components/schemas/rebuild_server_from_image_response"""
        class R:
            type = 'object'
            description = 'Response to POST https://api.hetzner.cloud/v1/servers/{id}/actions/rebuild'
            _attrs = ['action', 'root_password']
            action = lambda: Defs.components_schemas_action
            root_password = {'nullable': True, 'type': 'string', 'descr': 'New root password when not using SSH keys'}
        R.action = lambda: Defs.components_schemas_action
        R.root_password = str_dflt
    class components_schemas_remove_from_placement_group_response:
        """#/components/schemas/remove_from_placement_group_response"""
        class R:
            required = ['action']
            title = 'ActionResponse'
            type = 'object'
            description = 'Response to POST https://api.hetzner.cloud/v1/servers/{id}/actions/remove_from_placement_group'
            _attrs = ['action']
            action = lambda: Defs.components_schemas_action
        R.action = lambda: Defs.components_schemas_action
    class components_schemas_remove_from_resources_request:
        """#/components/schemas/remove_from_resources_request"""
        class R:
            required = ['remove_from']
            title = 'RemoveFromResourcesRequest'
            type = 'object'
            description = 'Request for POST https://api.hetzner.cloud/v1/firewalls/{id}/actions/remove_from_resources'
            _attrs = ['remove_from']
            remove_from = {'items': lambda: Defs.components_schemas_firewall_resource, 'type': 'array', 'descr': 'Resources the Firewall should be removed from'}
        R.remove_from = [lambda: Defs.components_schemas_firewall_resource]
    class components_schemas_remove_from_resources_response:
        """#/components/schemas/remove_from_resources_response"""
        class R:
            required = ['actions']
            title = 'ActionsResponse'
            type = 'object'
            description = 'Response to POST https://api.hetzner.cloud/v1/firewalls/{id}/actions/remove_from_resources'
            _attrs = ['actions', 'meta']
            actions = {'items': lambda: Defs.components_schemas_action, 'type': 'array'}
            meta = lambda: Defs.components_schemas_meta
        R.actions = [lambda: Defs.components_schemas_action]
        R.meta = lambda: Defs.components_schemas_meta
    class components_schemas_remove_target_request:
        """#/components/schemas/remove_target_request"""
        class R:
            required = ['type']
            title = 'RemoveTargetRequest'
            type = 'object'
            description = 'Request for POST https://api.hetzner.cloud/v1/load_balancers/{id}/actions/remove_target'
            _attrs = ['ip', 'label_selector', 'server', 'type']
            ip = {'example': '203.0.113.1', 'type': 'string', 'descr': 'IP of a server that belongs to the same customer (public IPv4/IPv6) or private IP in a Subnetwork type vswitch.'}
            ip = {'properties': {'ip': {'description': 'IP of a server that belongs to the same customer (public IPv4/IPv6) or private IP in a Subnetwork type vswitch.', 'example': '203.0.113.1', 'type': 'string'}}, 'required': ['ip'], 'type': 'object', 'descr': 'IP targets where the traffic should be routed through. It is only possible to use the (Public or vSwitch) IPs of Hetzner Online Root Servers belonging to the project owner. IPs belonging to other users are blocked. Additionally IPs belonging to services provided by Hetzner Cloud (Servers, Load Balancers, ...) are blocked as well.'}
            label_selector = lambda: Defs.components_schemas_label_selector
            id = {'example': 80, 'type': 'integer', 'descr': 'ID of the Server'}
            server = {'additionalProperties': False, 'properties': {'id': {'description': 'ID of the Server', 'example': 80, 'type': 'integer'}}, 'required': ['id'], 'type': 'object', 'descr': 'Configuration for type Server, required if type is `server`'}
            type = {'enum': ['ip', 'label_selector', 'server'], 'type': 'string', 'descr': 'Type of the resource'}
        R.ip = dict(ip = '203.0.113.1')
        R.label_selector = lambda: Defs.components_schemas_label_selector
        R.server = dict(id = id)
        R.type = 'ip'
    class components_schemas_remove_target_response:
        """#/components/schemas/remove_target_response"""
        class R:
            required = ['action']
            title = 'ActionResponse'
            type = 'object'
            description = 'Response to POST https://api.hetzner.cloud/v1/load_balancers/{id}/actions/remove_target'
            _attrs = ['action']
            action = lambda: Defs.components_schemas_action
        R.action = lambda: Defs.components_schemas_action
    class components_schemas_replace_certificate_request:
        """#/components/schemas/replace_certificate_request"""
        class R:
            title = 'UpdateCertificateRequest'
            type = 'object'
            description = 'Request for PUT https://api.hetzner.cloud/v1/certificates/{id}'
            _attrs = ['labels', 'name']
            labels = lambda: Defs.components_schemas_labels
            name = {'example': 'my website cert', 'type': 'string', 'descr': 'New Certificate name'}
        R.labels = lambda: Defs.components_schemas_labels
        R.name = 'my website cert'
    class components_schemas_replace_certificate_response:
        """#/components/schemas/replace_certificate_response"""
        class R:
            required = ['certificate']
            title = 'CertificateResponse'
            type = 'object'
            description = 'Response to PUT https://api.hetzner.cloud/v1/certificates/{id}'
            _attrs = ['certificate']
            certificate = lambda: Defs.components_schemas_certificate
        R.certificate = lambda: Defs.components_schemas_certificate
    class components_schemas_replace_firewall_request:
        """#/components/schemas/replace_firewall_request"""
        class R:
            title = 'UpdateFirewallRequest'
            type = 'object'
            description = 'Request for PUT https://api.hetzner.cloud/v1/firewalls/{id}'
            _attrs = ['labels', 'name']
            labels = lambda: Defs.components_schemas_labels
            name = {'example': 'new-name', 'type': 'string', 'descr': 'New Firewall name'}
        R.labels = lambda: Defs.components_schemas_labels
        R.name = 'new-name'
    class components_schemas_replace_firewall_response:
        """#/components/schemas/replace_firewall_response"""
        class R:
            required = ['firewall']
            title = 'FirewallResponse'
            type = 'object'
            description = 'Response to PUT https://api.hetzner.cloud/v1/firewalls/{id}'
            _attrs = ['firewall']
            firewall = lambda: Defs.components_schemas_firewall
        R.firewall = lambda: Defs.components_schemas_firewall
    class components_schemas_replace_floating_ip_request:
        """#/components/schemas/replace_floating_ip_request"""
        class R:
            title = 'UpdateFloatingIPRequest'
            type = 'object'
            description = 'Request for PUT https://api.hetzner.cloud/v1/floating_ips/{id}'
            _attrs = ['description', 'labels', 'name']
            description = {'example': 'Web Frontend', 'type': 'string', 'descr': 'New Description to set'}
            labels = lambda: Defs.components_schemas_labels
            name = {'example': 'Web Frontend', 'type': 'string', 'descr': 'New unique name to set'}
        R.description = 'Web Frontend'
        R.labels = lambda: Defs.components_schemas_labels
        R.name = 'Web Frontend'
    class components_schemas_replace_floating_ip_response:
        """#/components/schemas/replace_floating_ip_response"""
        class R:
            required = ['floating_ip']
            type = 'object'
            description = 'Response to PUT https://api.hetzner.cloud/v1/floating_ips/{id}'
            _attrs = ['floating_ip']
            floating_ip = lambda: Defs.components_schemas_floating_ip
        R.floating_ip = lambda: Defs.components_schemas_floating_ip
    class components_schemas_replace_image_request:
        """#/components/schemas/replace_image_request"""
        class R:
            title = 'UpdateImageRequest'
            type = 'object'
            description = 'Request for PUT https://api.hetzner.cloud/v1/images/{id}'
            _attrs = ['description', 'labels', 'type']
            description = {'example': 'My new Image description', 'type': 'string', 'descr': 'New description of Image'}
            labels = lambda: Defs.components_schemas_labels
            type = {'enum': ['snapshot'], 'type': 'string', 'descr': 'Destination Image type to convert to'}
        R.description = 'My new Image description'
        R.labels = lambda: Defs.components_schemas_labels
        R.type = 'snapshot'
    class components_schemas_replace_image_response:
        """#/components/schemas/replace_image_response"""
        class R:
            type = 'object'
            description = 'Response to PUT https://api.hetzner.cloud/v1/images/{id}'
            _attrs = ['image']
            image = lambda: Defs.components_schemas_image
        R.image = lambda: Defs.components_schemas_image
    class components_schemas_replace_load_balancer_request:
        """#/components/schemas/replace_load_balancer_request"""
        class R:
            type = 'object'
            description = 'Request for PUT https://api.hetzner.cloud/v1/load_balancers/{id}'
            _attrs = ['labels', 'name']
            labels = lambda: Defs.components_schemas_labels
            name = {'example': 'new-name', 'type': 'string', 'descr': 'New Load Balancer name'}
        R.labels = lambda: Defs.components_schemas_labels
        R.name = 'new-name'
    class components_schemas_replace_load_balancer_response:
        """#/components/schemas/replace_load_balancer_response"""
        class R:
            required = ['load_balancer']
            type = 'object'
            description = 'Response to PUT https://api.hetzner.cloud/v1/load_balancers/{id}'
            _attrs = ['load_balancer']
            load_balancer = lambda: Defs.components_schemas_load_balancer
        R.load_balancer = lambda: Defs.components_schemas_load_balancer
    class components_schemas_replace_network_request:
        """#/components/schemas/replace_network_request"""
        class R:
            title = 'UpdateNetworkRequest'
            type = 'object'
            description = 'Request for PUT https://api.hetzner.cloud/v1/networks/{id}'
            _attrs = ['labels', 'name']
            labels = lambda: Defs.components_schemas_labels
            name = {'example': 'new-name', 'type': 'string', 'descr': 'New network name'}
        R.labels = lambda: Defs.components_schemas_labels
        R.name = 'new-name'
    class components_schemas_replace_network_response:
        """#/components/schemas/replace_network_response"""
        class R:
            type = 'object'
            description = 'Response to PUT https://api.hetzner.cloud/v1/networks/{id}'
            _attrs = ['network']
            network = lambda: Defs.components_schemas_network
        R.network = lambda: Defs.components_schemas_network
    class components_schemas_replace_placementgroup_request:
        """#/components/schemas/replace_placementgroup_request"""
        class R:
            title = 'UpdatePlacementGroupRequest'
            type = 'object'
            description = 'Request for PUT https://api.hetzner.cloud/v1/placement_groups/{id}'
            _attrs = ['labels', 'name']
            labels = lambda: Defs.components_schemas_labels
            name = {'example': 'my Placement Group', 'type': 'string', 'descr': 'New PlacementGroup name'}
        R.labels = lambda: Defs.components_schemas_labels
        R.name = 'my Placement Group'
    class components_schemas_replace_placementgroup_response:
        """#/components/schemas/replace_placementgroup_response"""
        class R:
            required = ['placement_group']
            title = 'PlacementGroupResponse'
            type = 'object'
            description = 'Response to PUT https://api.hetzner.cloud/v1/placement_groups/{id}'
            _attrs = ['placement_group']
            created = {'example': '2016-01-30T23:55:00+00:00', 'type': 'string', 'descr': 'Point in time when the Resource was created (in ISO-8601 format)'}
            id = {'example': 42, 'type': 'integer', 'descr': 'ID of the Resource'}
            labels = lambda: Defs.components_schemas_labels
            name = {'example': 'my-resource', 'type': 'string', 'descr': 'Name of the Resource. Must be unique per Project.'}
            servers = {'example': [42], 'items': {'type': 'integer'}, 'type': 'array', 'descr': 'Array of IDs of Servers that are part of this Placement Group'}
            type = {'enum': ['spread'], 'example': 'spread', 'type': 'string', 'descr': 'Type of the Placement Group'}
            placement_group = {'properties': {'created': {'description': 'Point in time when the Resource was created (in ISO-8601 format)', 'example': '2016-01-30T23:55:00+00:00', 'type': 'string'}, 'id': {'description': 'ID of the Resource', 'example': 42, 'type': 'integer'}, 'labels': lambda: Defs.components_schemas_labels, 'name': {'description': 'Name of the Resource. Must be unique per Project.', 'example': 'my-resource', 'type': 'string'}, 'servers': {'description': 'Array of IDs of Servers that are part of this Placement Group', 'example': [42], 'items': {'type': 'integer'}, 'type': 'array'}, 'type': {'description': 'Type of the Placement Group', 'enum': ['spread'], 'example': 'spread', 'type': 'string'}}, 'required': ['id', 'name', 'labels', 'type', 'created', 'servers'], 'title': 'PlacementGroup', 'type': 'object'}
        R.placement_group = dict(created = '2016-01-30T23:55:00+00:00', id = id, labels = lambda: Defs.components_schemas_labels, name = 'my-resource', servers = [42], type = 'spread')
    class components_schemas_replace_primary_ip_request:
        """#/components/schemas/replace_primary_ip_request"""
        class R:
            title = 'UpdatePrimaryIPRequest'
            type = 'object'
            description = 'Request for PUT https://api.hetzner.cloud/v1/primary_ips/{id}'
            _attrs = ['auto_delete', 'labels', 'name']
            auto_delete = {'example': True, 'type': 'boolean', 'descr': 'Delete this Primary IP when the resource it is assigned to is deleted'}
            labels = lambda: Defs.components_schemas_labels
            name = {'example': 'my-ip', 'type': 'string', 'descr': 'New unique name to set'}
        R.auto_delete = True
        R.labels = lambda: Defs.components_schemas_labels
        R.name = 'my-ip'
    class components_schemas_replace_primary_ip_response:
        """#/components/schemas/replace_primary_ip_response"""
        class R:
            required = ['primary_ip']
            title = 'PrimaryIPResponse'
            type = 'object'
            description = 'Response to PUT https://api.hetzner.cloud/v1/primary_ips/{id}'
            _attrs = ['primary_ip']
            assignee_id = {'example': 17, 'nullable': True, 'type': 'integer', 'descr': 'ID of the resource the Primary IP is assigned to, null if it is not assigned at all'}
            assignee_type = {'enum': ['server'], 'type': 'string', 'descr': 'Resource type the Primary IP can be assigned to'}
            auto_delete = {'example': True, 'type': 'boolean', 'descr': 'Delete this Primary IP when the resource it is assigned to is deleted'}
            blocked = {'example': False, 'type': 'boolean', 'descr': 'Whether the IP is blocked'}
            created = {'example': '2016-01-30T23:55:00+00:00', 'type': 'string', 'descr': 'Point in time when the Resource was created (in ISO-8601 format)'}
            datacenter = lambda: Defs.components_schemas_datacenter
            dns_ptr = {'items': lambda: Defs.components_schemas_dns_ptr, 'type': 'array', 'descr': 'Array of reverse DNS entries'}
            id = {'example': 42, 'type': 'integer', 'descr': 'ID of the Resource'}
            ip = {'example': '131.232.99.1', 'type': 'string', 'descr': 'IP address'}
            labels = lambda: Defs.components_schemas_labels
            name = {'example': 'my-resource', 'type': 'string', 'descr': 'Name of the Resource. Must be unique per Project.'}
            protection = lambda: Defs.components_schemas_protection
            type = lambda: Defs.components_schemas_ip_type
            primary_ip = {'properties': {'assignee_id': {'description': 'ID of the resource the Primary IP is assigned to, null if it is not assigned at all', 'example': 17, 'nullable': True, 'type': 'integer'}, 'assignee_type': {'description': 'Resource type the Primary IP can be assigned to', 'enum': ['server'], 'type': 'string'}, 'auto_delete': {'description': 'Delete this Primary IP when the resource it is assigned to is deleted', 'example': True, 'type': 'boolean'}, 'blocked': {'description': 'Whether the IP is blocked', 'example': False, 'type': 'boolean'}, 'created': {'description': 'Point in time when the Resource was created (in ISO-8601 format)', 'example': '2016-01-30T23:55:00+00:00', 'type': 'string'}, 'datacenter': lambda: Defs.components_schemas_datacenter, 'dns_ptr': {'description': 'Array of reverse DNS entries', 'items': lambda: Defs.components_schemas_dns_ptr, 'type': 'array'}, 'id': {'description': 'ID of the Resource', 'example': 42, 'type': 'integer'}, 'ip': {'description': 'IP address', 'example': '131.232.99.1', 'type': 'string'}, 'labels': lambda: Defs.components_schemas_labels, 'name': {'description': 'Name of the Resource. Must be unique per Project.', 'example': 'my-resource', 'type': 'string'}, 'protection': lambda: Defs.components_schemas_protection, 'type': lambda: Defs.components_schemas_ip_type}, 'required': ['id', 'name', 'labels', 'created', 'blocked', 'datacenter', 'ip', 'dns_ptr', 'protection', 'type', 'auto_delete', 'assignee_type', 'assignee_id'], 'title': 'PrimaryIP', 'type': 'object'}
        R.primary_ip = dict(assignee_id = 17, assignee_type = 'server', auto_delete = True, blocked = True, created = '2016-01-30T23:55:00+00:00', datacenter = lambda: Defs.components_schemas_datacenter, dns_ptr = [lambda: Defs.components_schemas_dns_ptr], id = id, ip = '131.232.99.1', labels = lambda: Defs.components_schemas_labels, name = 'my-resource', protection = lambda: Defs.components_schemas_protection, type = lambda: Defs.components_schemas_ip_type)
    class components_schemas_replace_server_request:
        """#/components/schemas/replace_server_request"""
        class R:
            title = 'UpdateServerRequest'
            type = 'object'
            description = 'Request for PUT https://api.hetzner.cloud/v1/servers/{id}'
            _attrs = ['labels', 'name']
            labels = lambda: Defs.components_schemas_labels
            name = {'example': 'my-server', 'type': 'string', 'descr': 'New name to set'}
        R.labels = lambda: Defs.components_schemas_labels
        R.name = 'my-server'
    class components_schemas_replace_server_response:
        """#/components/schemas/replace_server_response"""
        class R:
            type = 'object'
            description = 'Response to PUT https://api.hetzner.cloud/v1/servers/{id}'
            _attrs = ['server']
            server = lambda: Defs.components_schemas_server
        R.server = lambda: Defs.components_schemas_server
    class components_schemas_replace_ssh_key_request:
        """#/components/schemas/replace_ssh_key_request"""
        class R:
            type = 'object'
            description = 'Request for PUT https://api.hetzner.cloud/v1/ssh_keys/{id}'
            _attrs = ['labels', 'name']
            labels = lambda: Defs.components_schemas_labels
            name = {'example': 'My ssh key', 'type': 'string', 'descr': 'New name Name to set'}
        R.labels = lambda: Defs.components_schemas_labels
        R.name = 'My ssh key'
    class components_schemas_replace_ssh_key_response:
        """#/components/schemas/replace_ssh_key_response"""
        class R:
            required = ['ssh_key']
            type = 'object'
            description = 'Response to PUT https://api.hetzner.cloud/v1/ssh_keys/{id}'
            _attrs = ['ssh_key']
            ssh_key = lambda: Defs.components_schemas_ssh_key
        R.ssh_key = lambda: Defs.components_schemas_ssh_key
    class components_schemas_replace_volume_request:
        """#/components/schemas/replace_volume_request"""
        class R:
            required = ['name']
            title = 'UpdateVolumeRequest'
            type = 'object'
            description = 'Request for PUT https://api.hetzner.cloud/v1/volumes/{id}'
            _attrs = ['labels', 'name']
            labels = lambda: Defs.components_schemas_labels
            name = {'example': 'database-storage', 'type': 'string', 'descr': 'New Volume name'}
        R.labels = lambda: Defs.components_schemas_labels
        R.name = 'database-storage'
    class components_schemas_replace_volume_response:
        """#/components/schemas/replace_volume_response"""
        class R:
            required = ['volume']
            type = 'object'
            description = 'Response to PUT https://api.hetzner.cloud/v1/volumes/{id}'
            _attrs = ['volume']
            volume = lambda: Defs.components_schemas_volume
        R.volume = lambda: Defs.components_schemas_volume
    class components_schemas_request_console_for_server_response:
        """#/components/schemas/request_console_for_server_response"""
        class R:
            required = ['wss_url', 'password', 'action']
            type = 'object'
            description = 'Response to POST https://api.hetzner.cloud/v1/servers/{id}/actions/request_console'
            _attrs = ['action', 'password', 'wss_url']
            action = lambda: Defs.components_schemas_action
            password = {'example': '9MQaTg2VAGI0FIpc10k3UpRXcHj2wQ6x', 'type': 'string', 'descr': 'VNC password to use for this connection (this password only works in combination with a wss_url with valid token)'}
            wss_url = {'example': 'wss://console.hetzner.cloud/?server_id=1&token=3db32d15-af2f-459c-8bf8-dee1fd05f49c', 'type': 'string', 'descr': 'URL of websocket proxy to use; this includes a token which is valid for a limited time only'}
        R.action = lambda: Defs.components_schemas_action
        R.password = '9MQaTg2VAGI0FIpc10k3UpRXcHj2wQ6x'
        R.wss_url = 'wss://console.hetzner.cloud/?server_id=1&token=3db32d15-af2f-459c-8bf8-dee1fd05f49c'
    class components_schemas_reset_root_password_of_server_response:
        """#/components/schemas/reset_root_password_of_server_response"""
        class R:
            type = 'object'
            description = 'Response to POST https://api.hetzner.cloud/v1/servers/{id}/actions/reset_password'
            _attrs = ['action', 'root_password']
            action = lambda: Defs.components_schemas_action
            root_password = {'example': 'zCWbFhnu950dUTko5f40', 'type': 'string', 'descr': 'Password that will be set for this Server once the Action succeeds'}
        R.action = lambda: Defs.components_schemas_action
        R.root_password = 'zCWbFhnu950dUTko5f40'
    class components_schemas_reset_server_response:
        """#/components/schemas/reset_server_response"""
        class R:
            required = ['action']
            title = 'ActionResponse'
            type = 'object'
            description = 'Response to POST https://api.hetzner.cloud/v1/servers/{id}/actions/reset'
            _attrs = ['action']
            action = lambda: Defs.components_schemas_action
        R.action = lambda: Defs.components_schemas_action
    class components_schemas_resize_volume_request:
        """#/components/schemas/resize_volume_request"""
        class R:
            required = ['size']
            type = 'object'
            description = 'Request for POST https://api.hetzner.cloud/v1/volumes/{id}/actions/resize'
            _attrs = ['size']
            size = {'example': 50, 'type': 'number', 'descr': 'New Volume size in GB (must be greater than current size)'}
        R.size = 50
    class components_schemas_resize_volume_response:
        """#/components/schemas/resize_volume_response"""
        class R:
            required = ['action']
            title = 'ActionResponse'
            type = 'object'
            description = 'Response to POST https://api.hetzner.cloud/v1/volumes/{id}/actions/resize'
            _attrs = ['action']
            action = lambda: Defs.components_schemas_action
        R.action = lambda: Defs.components_schemas_action
    class components_schemas_resource:
        """#/components/schemas/resource"""
        class R:
            required = ['id', 'type']
            type = 'object'
            _attrs = ['id', 'type']
            id = {'example': 42, 'type': 'integer', 'descr': 'ID of the Resource | ID of resource referenced'}
            type = {'example': 'server', 'type': 'string', 'descr': 'Type of resource referenced'}
        R.id = id
        R.type = 'server'
    class components_schemas_resource_id:
        """#/components/schemas/resource_id"""
        class R:
            required = ['id']
            type = 'object'
            description = 'ID of the Resource'
            _attrs = ['id']
            id = {'example': 42, 'type': 'integer', 'descr': 'ID of the Resource | ID of the Server'}
        R.id = id
    class components_schemas_retry_issuance_or_renewal_response:
        """#/components/schemas/retry_issuance_or_renewal_response"""
        class R:
            required = ['action']
            title = 'ActionResponse'
            type = 'object'
            description = 'Response to POST https://api.hetzner.cloud/v1/certificates/{id}/actions/retry'
            _attrs = ['action']
            action = lambda: Defs.components_schemas_action
        R.action = lambda: Defs.components_schemas_action
    class components_schemas_route:
        """#/components/schemas/route"""
        class R:
            required = ['destination', 'gateway']
            type = 'object'
            description = 'Request for POST https://api.hetzner.cloud/v1/networks/{id}/actions/add_route | Request for POST https://api.hetzner.cloud/v1/networks/{id}/actions/delete_route'
            _attrs = ['destination', 'gateway']
            destination = {'example': '10.100.1.0/24', 'type': 'string', 'descr': 'Destination network or host of this route. Must not overlap with an existing ip_range in any subnets or with any destinations in other routes or with the first IP of the networks ip_range or with 172.31.1.1. Must be one of the private IPv4 ranges of RFC1918.'}
            gateway = {'example': '10.0.1.1', 'type': 'string', 'descr': 'Gateway for the route. Cannot be the first IP of the networks ip_range and also cannot be 172.31.1.1 as this IP is being used as a gateway for the public network interface of Servers. | Gateway for the route. Cannot be the first IP of the networks ip_range, an IP behind a vSwitch or 172.31.1.1, as this IP is being used as a gateway for the public network interface of Servers.'}
        R.destination = '10.100.1.0/24'
        R.gateway = '10.0.1.1'
    class components_schemas_rule:
        """#/components/schemas/rule"""
        class R:
            required = ['direction', 'protocol']
            title = 'Rule'
            type = 'object'
            description = 'Rule of a firewall.'
            _attrs = ['description', 'destination_ips', 'direction', 'port', 'protocol', 'source_ips']
            description = {'maxLength': 255, 'nullable': True, 'type': 'string', 'descr': 'Description of the Rule'}
            destination_ips = {'example': ['28.239.13.1/32', '28.239.14.0/24', 'ff21:1eac:9a3b:ee58:5ca:990c:8bc9:c03b/128'], 'items': {'type': 'string'}, 'type': 'array', 'descr': 'List of permitted IPv4/IPv6 addresses in CIDR notation. Use `0.0.0.0/0` to allow all IPv4 addresses and `::/0` to allow all IPv6 addresses. You can specify 100 CIDRs at most.'}
            direction = {'enum': ['in', 'out'], 'type': 'string', 'descr': 'Select traffic direction on which rule should be applied. Use `source_ips` for direction `in` and `destination_ips` for direction `out`.'}
            port = {'example': '80', 'type': 'string', 'descr': 'Port or port range to which traffic will be allowed, only applicable for protocols TCP and UDP. A port range can be specified by separating two ports with a dash, e.g `1024-5000`.'}
            protocol = {'enum': ['esp', 'gre', 'icmp', 'tcp', 'udp'], 'type': 'string', 'descr': 'Type of traffic to allow'}
            source_ips = {'example': ['28.239.13.1/32', '28.239.14.0/24', 'ff21:1eac:9a3b:ee58:5ca:990c:8bc9:c03b/128'], 'items': {'type': 'string'}, 'type': 'array', 'descr': 'List of permitted IPv4/IPv6 addresses in CIDR notation. Use `0.0.0.0/0` to allow all IPv4 addresses and `::/0` to allow all IPv6 addresses. You can specify 100 CIDRs at most.'}
        R.description = str_dflt
        R.destination_ips = ['28.239.13.1/32', '28.239.14.0/24', 'ff21:1eac:9a3b:ee58:5ca:990c:8bc9:c03b/128']
        R.direction = 'in'
        R.port = '80'
        R.protocol = 'esp'
        R.source_ips = ['28.239.13.1/32', '28.239.14.0/24', 'ff21:1eac:9a3b:ee58:5ca:990c:8bc9:c03b/128']
    class components_schemas_selected_target:
        """#/components/schemas/selected_target"""
        class R:
            type = 'object'
            _attrs = ['health_status', 'server', 'type', 'use_private_ip']
            health_status = {'items': lambda: Defs.components_schemas_health_status, 'type': 'array'}
            server = lambda: Defs.components_schemas_resource_id
            type = {'example': 'server', 'type': 'string'}
            use_private_ip = {'example': False, 'type': 'boolean'}
        R.health_status = [lambda: Defs.components_schemas_health_status]
        R.server = lambda: Defs.components_schemas_resource_id
        R.type = 'server'
        R.use_private_ip = True
    class components_schemas_server:
        """#/components/schemas/server"""
        class R:
            required = ['id', 'name', 'status', 'created', 'public_net', 'private_net', 'server_type', 'datacenter', 'image', 'iso', 'rescue_enabled', 'locked', 'backup_window', 'outgoing_traffic', 'ingoing_traffic', 'included_traffic', 'protection', 'labels', 'primary_disk_size']
            type = 'object'
            description = 'Servers are virtual machines that can be provisioned.'
            _attrs = ['backup_window', 'created', 'datacenter', 'id', 'image', 'included_traffic', 'ingoing_traffic', 'iso', 'labels', 'load_balancers', 'locked', 'name', 'outgoing_traffic', 'placement_group', 'primary_disk_size', 'private_net', 'protection', 'public_net', 'rescue_enabled', 'server_type', 'status', 'volumes']
            backup_window = {'example': '22-02', 'nullable': True, 'type': 'string', 'descr': 'Time window (UTC) in which the backup will run, or null if the backups are not enabled'}
            created = {'example': '2016-01-30T23:55:00+00:00', 'type': 'string', 'descr': 'Point in time when the Resource was created (in ISO-8601 format)'}
            datacenter = lambda: Defs.components_schemas_datacenter
            id = {'example': 42, 'type': 'integer', 'descr': 'ID of the Resource'}
            image = lambda: Defs.components_schemas_image_optional
            included_traffic = {'example': 654321, 'nullable': True, 'type': 'integer', 'format': 'int64', 'descr': 'Free Traffic for the current billing period in bytes'}
            ingoing_traffic = {'example': 123456, 'nullable': True, 'type': 'integer', 'format': 'int64', 'descr': 'Inbound Traffic for the current billing period in bytes'}
            iso = lambda: Defs.components_schemas_iso_optional
            labels = lambda: Defs.components_schemas_labels
            load_balancers = {'items': {'type': 'integer'}, 'type': 'array'}
            locked = {'example': False, 'type': 'boolean', 'descr': 'True if Server has been locked and is not available to user'}
            name = {'example': 'my-resource', 'type': 'string', 'descr': 'Name of the Server (must be unique per Project and a valid hostname as per RFC 1123)'}
            outgoing_traffic = {'example': 123456, 'nullable': True, 'type': 'integer', 'format': 'int64', 'descr': 'Outbound Traffic for the current billing period in bytes'}
            created = {'example': '2016-01-30T23:55:00+00:00', 'type': 'string', 'descr': 'Point in time when the Resource was created (in ISO-8601 format)'}
            id = {'example': 42, 'type': 'integer', 'descr': 'ID of the Resource'}
            labels = lambda: Defs.components_schemas_labels
            name = {'example': 'my-resource', 'type': 'string', 'descr': 'Name of the Resource. Must be unique per Project.'}
            servers = {'example': [42], 'items': {'type': 'integer'}, 'type': 'array', 'descr': 'Array of IDs of Servers that are part of this Placement Group'}
            type = {'enum': ['spread'], 'example': 'spread', 'type': 'string', 'descr': 'Type of the Placement Group'}
            placement_group = {'nullable': True, 'properties': {'created': {'description': 'Point in time when the Resource was created (in ISO-8601 format)', 'example': '2016-01-30T23:55:00+00:00', 'type': 'string'}, 'id': {'description': 'ID of the Resource', 'example': 42, 'type': 'integer'}, 'labels': lambda: Defs.components_schemas_labels, 'name': {'description': 'Name of the Resource. Must be unique per Project.', 'example': 'my-resource', 'type': 'string'}, 'servers': {'description': 'Array of IDs of Servers that are part of this Placement Group', 'example': [42], 'items': {'type': 'integer'}, 'type': 'array'}, 'type': {'description': 'Type of the Placement Group', 'enum': ['spread'], 'example': 'spread', 'type': 'string'}}, 'required': ['id', 'name', 'labels', 'type', 'created', 'servers'], 'title': 'PlacementGroupNullable', 'type': 'object'}
            primary_disk_size = {'example': 50, 'type': 'integer', 'descr': 'Size of the primary Disk'}
            private_net = {'items': lambda: Defs.components_schemas_server_private_net, 'type': 'array', 'descr': 'Private networks information'}
            protection = lambda: Defs.components_schemas_server_protection
            public_net = lambda: Defs.components_schemas_server_public_net
            rescue_enabled = {'example': False, 'type': 'boolean', 'descr': 'True if rescue mode is enabled. Server will then boot into rescue system on next reboot'}
            server_type = lambda: Defs.components_schemas_server_type
            status = {'enum': ['deleting', 'initializing', 'migrating', 'off', 'rebuilding', 'running', 'starting', 'stopping', 'unknown'], 'type': 'string', 'descr': 'Status of the Server'}
            volumes = {'items': {'type': 'integer'}, 'type': 'array', 'descr': 'IDs of Volumes assigned to this Server'}
        R.backup_window = '22-02'
        R.created = '2016-01-30T23:55:00+00:00'
        R.datacenter = lambda: Defs.components_schemas_datacenter
        R.id = id
        R.image = lambda: Defs.components_schemas_image_optional
        R.included_traffic = 654321
        R.ingoing_traffic = 123456
        R.iso = lambda: Defs.components_schemas_iso_optional
        R.labels = lambda: Defs.components_schemas_labels
        R.load_balancers = [0]
        R.locked = True
        R.name = 'my-resource'
        R.outgoing_traffic = 123456
        R.placement_group = dict(created = '2016-01-30T23:55:00+00:00', id = id, labels = lambda: Defs.components_schemas_labels, name = 'my-resource', servers = [42], type = 'spread')
        R.primary_disk_size = 50
        R.private_net = [lambda: Defs.components_schemas_server_private_net]
        R.protection = lambda: Defs.components_schemas_server_protection
        R.public_net = lambda: Defs.components_schemas_server_public_net
        R.rescue_enabled = True
        R.server_type = lambda: Defs.components_schemas_server_type
        R.status = 'deleting'
        R.volumes = [0]
    class components_schemas_server_private_net:
        """#/components/schemas/server_private_net"""
        class R:
            type = 'object'
            _attrs = ['alias_ips', 'ip', 'mac_address', 'network']
            alias_ips = {'items': {'type': 'string'}, 'type': 'array'}
            ip = {'example': '10.0.0.2', 'type': 'string'}
            mac_address = {'example': '86:00:ff:2a:7d:e1', 'type': 'string'}
            network = {'example': 4711, 'type': 'integer'}
        R.alias_ips = [str_dflt]
        R.ip = '10.0.0.2'
        R.mac_address = '86:00:ff:2a:7d:e1'
        R.network = 4711
    class components_schemas_server_protection:
        """#/components/schemas/server_protection"""
        class R:
            description = 'Protection configuration for the Server'
            required = ['delete', 'rebuild']
            type = 'object'
            _attrs = ['delete', 'rebuild']
            delete = {'example': False, 'type': 'boolean', 'descr': 'If true, prevents the Server from being deleted'}
            rebuild = {'example': False, 'type': 'boolean', 'descr': 'If true, prevents the Server from being rebuilt'}
        R.delete = True
        R.rebuild = True
    class components_schemas_server_public_net:
        """#/components/schemas/server_public_net"""
        class R:
            description = 'Public network information. The Server"s IPv4 address can be found in `public_net->ipv4->ip`'
            required = ['ipv4', 'ipv6', 'floating_ips']
            type = 'object'
            _attrs = ['firewalls', 'floating_ips', 'ipv4', 'ipv6']
            id = {'example': 42, 'type': 'integer', 'descr': 'ID of the Resource'}
            status = {'enum': ['applied', 'pending'], 'example': 'applied', 'type': 'string', 'descr': 'Status of the Firewall on the Server'}
            firewalls = {'items': {'properties': {'id': {'description': 'ID of the Resource', 'example': 42, 'type': 'integer'}, 'status': {'description': 'Status of the Firewall on the Server', 'enum': ['applied', 'pending'], 'example': 'applied', 'type': 'string'}}, 'title': 'ServerPublicNetFirewall', 'type': 'object'}, 'type': 'array', 'descr': 'Firewalls applied to the public network interface of this Server'}
            floating_ips = {'example': [478], 'items': {'type': 'integer'}, 'type': 'array', 'descr': 'IDs of Floating IPs assigned to this Server'}
            ipv4 = lambda: Defs.components_schemas_ipv4
            ipv6 = lambda: Defs.components_schemas_ipv6
        R.firewalls = [dict(id = id, status = 'applied')]
        R.floating_ips = [478]
        R.ipv4 = lambda: Defs.components_schemas_ipv4
        R.ipv6 = lambda: Defs.components_schemas_ipv6
    class components_schemas_server_type:
        """#/components/schemas/server_type"""
        class R:
            required = ['id', 'name', 'description', 'cores', 'memory', 'disk', 'deprecated', 'prices', 'storage_type', 'cpu_type']
            type = 'object'
            description = 'Type of Server - determines how much ram, disk and cpu a Server has'
            _attrs = ['cores', 'cpu_type', 'deprecated', 'description', 'disk', 'id', 'memory', 'name', 'prices', 'storage_type']
            cores = {'example': 1, 'type': 'integer', 'descr': 'Number of cpu cores a Server of this type will have'}
            cpu_type = {'enum': ['dedicated', 'shared'], 'type': 'string', 'descr': 'Type of cpu'}
            deprecated = {'example': False, 'type': 'boolean', 'nullable': True, 'descr': 'True if Server type is deprecated'}
            description = {'example': 'CX11', 'type': 'string', 'descr': 'Description of the Server type'}
            disk = {'example': 24, 'type': 'number', 'descr': 'Disk size a Server of this type will have in GB'}
            id = {'example': 1, 'type': 'integer', 'descr': 'ID of the Server type'}
            memory = {'example': 1, 'type': 'number', 'descr': 'Memory a Server of this type will have in GB'}
            name = {'example': 'cx11', 'type': 'string', 'descr': 'Unique identifier of the Server type'}
            prices = {'items': lambda: Defs.components_schemas_price_per_time, 'type': 'array', 'descr': 'Prices in different Locations'}
            storage_type = {'enum': ['local', 'network'], 'type': 'string', 'descr': 'Type of Server boot drive. Local has higher speed. Network has better availability.'}
        R.cores = 1
        R.cpu_type = 'dedicated'
        R.deprecated = True
        R.description = 'CX11'
        R.disk = 24
        R.id = id
        R.memory = 1
        R.name = 'cx11'
        R.prices = [lambda: Defs.components_schemas_price_per_time]
        R.storage_type = 'local'
    class components_schemas_set_rules_request:
        """#/components/schemas/set_rules_request"""
        class R:
            required = ['rules']
            title = 'SetRulesRequest'
            type = 'object'
            description = 'Request for POST https://api.hetzner.cloud/v1/firewalls/{id}/actions/set_rules'
            _attrs = ['rules']
            rules = {'items': lambda: Defs.components_schemas_rule, 'maxItems': 50, 'type': 'array', 'descr': 'Array of rules'}
        R.rules = [lambda: Defs.components_schemas_rule]
    class components_schemas_set_rules_response:
        """#/components/schemas/set_rules_response"""
        class R:
            required = ['actions']
            title = 'ActionsResponse'
            type = 'object'
            description = 'Response to POST https://api.hetzner.cloud/v1/firewalls/{id}/actions/set_rules'
            _attrs = ['actions', 'meta']
            actions = {'items': lambda: Defs.components_schemas_action, 'type': 'array'}
            meta = lambda: Defs.components_schemas_meta
        R.actions = [lambda: Defs.components_schemas_action]
        R.meta = lambda: Defs.components_schemas_meta
    class components_schemas_shutdown_server_response:
        """#/components/schemas/shutdown_server_response"""
        class R:
            required = ['action']
            title = 'ActionResponse'
            type = 'object'
            description = 'Response to POST https://api.hetzner.cloud/v1/servers/{id}/actions/shutdown'
            _attrs = ['action']
            action = lambda: Defs.components_schemas_action
        R.action = lambda: Defs.components_schemas_action
    class components_schemas_soft_reboot_server_response:
        """#/components/schemas/soft_reboot_server_response"""
        class R:
            required = ['action']
            title = 'ActionResponse'
            type = 'object'
            description = 'Response to POST https://api.hetzner.cloud/v1/servers/{id}/actions/reboot'
            _attrs = ['action']
            action = lambda: Defs.components_schemas_action
        R.action = lambda: Defs.components_schemas_action
    class components_schemas_ssh_key:
        """#/components/schemas/ssh_key"""
        class R:
            required = ['id', 'name', 'fingerprint', 'public_key', 'labels', 'created']
            type = 'object'
            description = 'SSH keys are public keys you provide to the cloud system. They can be injected into Servers at creation time. We highly recommend that you use keys instead of passwords to manage your Servers.'
            _attrs = ['created', 'fingerprint', 'id', 'labels', 'name', 'public_key']
            created = {'example': '2016-01-30T23:55:00+00:00', 'type': 'string', 'descr': 'Point in time when the Resource was created (in ISO-8601 format)'}
            fingerprint = {'example': 'b7:2f:30:a0:2f:6c:58:6c:21:04:58:61:ba:06:3b:2f', 'type': 'string', 'descr': 'Fingerprint of public key'}
            id = {'example': 42, 'type': 'integer', 'descr': 'ID of the Resource'}
            labels = lambda: Defs.components_schemas_labels
            name = {'example': 'my-resource', 'type': 'string', 'descr': 'Name of the Resource. Must be unique per Project.'}
            public_key = {'example': 'ssh-rsa AAAjjk76kgf...Xt', 'type': 'string', 'descr': 'Public key'}
        R.created = '2016-01-30T23:55:00+00:00'
        R.fingerprint = 'b7:2f:30:a0:2f:6c:58:6c:21:04:58:61:ba:06:3b:2f'
        R.id = id
        R.labels = lambda: Defs.components_schemas_labels
        R.name = 'my-resource'
        R.public_key = 'ssh-rsa AAAjjk76kgf...Xt'
    class components_schemas_subnet:
        """#/components/schemas/subnet"""
        class R:
            required = ['type', 'network_zone']
            title = 'AddSubnetRequest'
            type = 'object'
            description = 'Subnets divide the ip_range from the parent Network object into multiple Subnetworks that you can use for different specific purposes.'
            _attrs = ['ip_range', 'network_zone', 'type', 'vswitch_id']
            ip_range = {'example': '10.0.1.0/24', 'type': 'string', 'descr': 'Range to allocate IPs from. Must be a Subnet of the ip_range of the parent network object and must not overlap with any other subnets or with any destinations in routes. If the Subnet is of type vSwitch, it also can not overlap with any gateway in routes. Minimum Network size is /30. We suggest that you pick a bigger Network with a /24 netmask.'}
            network_zone = {'example': 'eu-central', 'type': 'string', 'descr': 'Name of Network zone. The Location object contains the `network_zone` property each Location belongs to.'}
            type = {'enum': ['cloud', 'server', 'vswitch'], 'type': 'string', 'descr': 'Type of Subnetwork'}
            vswitch_id = {'example': 1000, 'type': 'integer', 'descr': 'ID of the robot vSwitch. Must be supplied if the subnet is of type vswitch.'}
        R.ip_range = '10.0.1.0/24'
        R.network_zone = 'eu-central'
        R.type = 'cloud'
        R.vswitch_id = 1000
    class components_schemas_subnet_with_gateway:
        """#/components/schemas/subnet_with_gateway"""
        class R:
            required = ['type', 'network_zone', 'gateway']
            type = 'object'
            _attrs = ['gateway', 'ip_range', 'network_zone', 'type']
            gateway = {'example': '10.0.0.1', 'type': 'string', 'descr': 'Gateway for Servers attached to this subnet. For subnets of type Server this is always the first IP of the network IP range.'}
            ip_range = {'example': '10.0.1.0/24', 'type': 'string', 'descr': 'Range to allocate IPs from. Must be a Subnet of the ip_range of the parent network object and must not overlap with any other subnets or with any destinations in routes. Minimum Network size is /30. We suggest that you pick a bigger Network with a /24 netmask.'}
            network_zone = {'example': 'eu-central', 'type': 'string', 'descr': 'Name of Network zone. The Location object contains the `network_zone` property each Location belongs to.'}
            type = {'enum': ['cloud', 'server', 'vswitch'], 'type': 'string', 'descr': 'Type of Subnetwork'}
        R.gateway = '10.0.0.1'
        R.ip_range = '10.0.1.0/24'
        R.network_zone = 'eu-central'
        R.type = 'cloud'
    class components_schemas_target:
        """#/components/schemas/target"""
        class R:
            required = ['type']
            title = 'LoadBalancerTarget'
            type = 'object'
            description = 'A target for a load balancer'
            _attrs = ['health_status', 'ip', 'label_selector', 'server', 'targets', 'type', 'use_private_ip']
            health_status = {'items': lambda: Defs.components_schemas_health_status, 'type': 'array', 'descr': 'List of health statuses of the services on this target'}
            ip = {'example': '203.0.113.1', 'type': 'string', 'descr': 'IP of a server that belongs to the same customer (public IPv4/IPv6) or private IP in a Subnetwork type vswitch.'}
            ip = {'properties': {'ip': {'description': 'IP of a server that belongs to the same customer (public IPv4/IPv6) or private IP in a Subnetwork type vswitch.', 'example': '203.0.113.1', 'type': 'string'}}, 'required': ['ip'], 'type': 'object', 'descr': 'IP targets where the traffic should be routed through. It is only possible to use the (Public or vSwitch) IPs of Hetzner Online Root Servers belonging to the project owner. IPs belonging to other users are blocked. Additionally IPs belonging to services provided by Hetzner Cloud (Servers, Load Balancers, ...) are blocked as well.'}
            label_selector = lambda: Defs.components_schemas_label_selector
            server = lambda: Defs.components_schemas_resource_id
            targets = {'items': lambda: Defs.components_schemas_selected_target, 'type': 'array', 'descr': 'List of selected targets'}
            type = {'enum': ['ip', 'label_selector', 'server'], 'type': 'string', 'descr': 'Type of the resource'}
            use_private_ip = {'type': 'boolean', 'descr': 'Use the private network IP instead of the public IP. Default value is false.'}
        R.health_status = [lambda: Defs.components_schemas_health_status]
        R.ip = dict(ip = '203.0.113.1')
        R.label_selector = lambda: Defs.components_schemas_label_selector
        R.server = lambda: Defs.components_schemas_resource_id
        R.targets = [lambda: Defs.components_schemas_selected_target]
        R.type = 'ip'
        R.use_private_ip = True
    class components_schemas_unassign_floating_ip_response:
        """#/components/schemas/unassign_floating_ip_response"""
        class R:
            required = ['action']
            title = 'ActionResponse'
            type = 'object'
            description = 'Response to POST https://api.hetzner.cloud/v1/floating_ips/{id}/actions/unassign'
            _attrs = ['action']
            action = lambda: Defs.components_schemas_action
        R.action = lambda: Defs.components_schemas_action
    class components_schemas_unassign_primary_ip_from_resource_response:
        """#/components/schemas/unassign_primary_ip_from_resource_response"""
        class R:
            required = ['action']
            title = 'ActionResponse'
            type = 'object'
            description = 'Response to POST https://api.hetzner.cloud/v1/primary_ips/{id}/actions/unassign'
            _attrs = ['action']
            action = lambda: Defs.components_schemas_action
        R.action = lambda: Defs.components_schemas_action
    class components_schemas_update_service_request:
        """#/components/schemas/update_service_request"""
        class R:
            dollar_ref = lambda: Defs.components_schemas_load_balancer_service
    class components_schemas_update_service_response:
        """#/components/schemas/update_service_response"""
        class R:
            required = ['action']
            title = 'ActionResponse'
            type = 'object'
            description = 'Response to POST https://api.hetzner.cloud/v1/load_balancers/{id}/actions/update_service'
            _attrs = ['action']
            action = lambda: Defs.components_schemas_action
        R.action = lambda: Defs.components_schemas_action
    class components_schemas_volume:
        """#/components/schemas/volume"""
        class R:
            required = ['id', 'created', 'name', 'server', 'location', 'size', 'linux_device', 'protection', 'labels', 'status', 'format']
            type = 'object'
            description = 'A Volume is a highly-available, scalable, and SSD-based block storage for Servers. Pricing for Volumes depends on the Volume size and Location, not the actual used storage. Please see [Hetzner Wiki](https://wiki.hetzner.de/index.php/CloudServer/en#Volumes) for more details about Volumes.'
            _attrs = ['created', 'format', 'id', 'labels', 'linux_device', 'location', 'name', 'protection', 'server', 'size', 'status']
            created = {'example': '2016-01-30T23:55:00+00:00', 'type': 'string', 'descr': 'Point in time when the Resource was created (in ISO-8601 format)'}
            format = {'example': 'xfs', 'nullable': True, 'type': 'string', 'descr': 'Filesystem of the Volume if formatted on creation, null if not formatted on creation'}
            id = {'example': 42, 'type': 'integer', 'descr': 'ID of the Resource'}
            labels = lambda: Defs.components_schemas_labels
            linux_device = {'example': '/dev/disk/by-id/scsi-0HC_Volume_4711', 'type': 'string', 'descr': 'Device path on the file system for the Volume'}
            location = lambda: Defs.components_schemas_location
            name = {'example': 'my-resource', 'type': 'string', 'descr': 'Name of the Resource. Must be unique per Project.'}
            protection = lambda: Defs.components_schemas_protection
            server = {'example': 12, 'nullable': True, 'type': 'integer', 'descr': 'ID of the Server the Volume is attached to, null if it is not attached at all'}
            size = {'example': 42, 'type': 'number', 'descr': 'Size in GB of the Volume'}
            status = {'enum': ['available', 'creating'], 'example': 'available', 'type': 'string', 'descr': 'Current status of the Volume'}
        R.created = '2016-01-30T23:55:00+00:00'
        R.format = 'xfs'
        R.id = id
        R.labels = lambda: Defs.components_schemas_labels
        R.linux_device = '/dev/disk/by-id/scsi-0HC_Volume_4711'
        R.location = lambda: Defs.components_schemas_location
        R.name = 'my-resource'
        R.protection = lambda: Defs.components_schemas_protection
        R.server = 12
        R.size = 42
        R.status = 'available'

class actions:
    pth = "/actions"

    class get:
        """Returns all Action objects. You can `sort` the results by using the sort URI parameter, and filter them with the `status` parameter. Get all Actions"""
        class R:
            _query = ['id', 'sort', 'status', 'page', 'per_page'];
            _ = {'responses': {'200': {'content': {'application/json': {'schema': Defs.components_schemas_list_actions_response}}, 'description': 'The `actions` key contains a list of Actions'}}, 'tags': ['actions'], 'operationId': 'list_actions'}
            id = {'type': 'integer'}
            sort = {'enum': ['id', 'id:asc', 'id:desc', 'command', 'command:asc', 'command:desc', 'status', 'status:asc', 'status:desc', 'progress', 'progress:asc', 'progress:desc', 'started', 'started:asc', 'started:desc', 'finished', 'finished:asc', 'finished:desc'], 'title': 'ParameterSort', 'type': 'string'}
            status = {'enum': ['running', 'success', 'error'], 'title': 'ParameterStatus', 'type': 'string'}
            page = {'type': 'integer', 'minimum': 1}
            per_page = {'type': 'integer', 'minimum': 1, 'maximum': 50}
        R.id = id
        R.sort = 'id'
        R.status = 'running'
        R.page = 0
        R.per_page = 0

class actions___id_:
    pth = "/actions/{id}"

    class get:
        """Returns a specific Action object. Get an Action"""
        class R:
            _path = ['id'];
            _ = {'responses': {'200': {'content': {'application/json': {'schema': Defs.components_schemas_get_action_response}}, 'description': 'The `action` key in the reply has this structure'}}, 'tags': ['actions'], 'operationId': 'get_action'}
            id = {'type': 'integer'}
        R.id = id

class certificates:
    pth = "/certificates"

    class get:
        """Returns all Certificate objects. Get all Certificates"""
        class R:
            _query = ['sort', 'name', 'label_selector', 'type', 'page', 'per_page'];
            _ = {'responses': {'200': {'content': {'application/json': {'example': {'certificates': [{'certificate': '-----BEGIN CERTIFICATE-----\n...', 'created': '2019-01-08T12:10:00+00:00', 'domain_names': ['example.com', 'webmail.example.com', 'www.example.com'], 'fingerprint': '03:c7:55:9b:2a:d1:04:17:09:f6:d0:7f:18:34:63:d4:3e:5f', 'id': 897, 'labels': {'env': 'dev'}, 'name': 'my website cert', 'not_valid_after': '2019-07-08T09:59:59+00:00', 'not_valid_before': '2019-01-08T10:00:00+00:00', 'status': None, 'type': 'uploaded', 'used_by': [{'id': 4711, 'type': 'load_balancer'}]}]}, 'schema': Defs.components_schemas_list_certificates_response}}, 'description': 'The `certificates` key contains an array of Certificate objects'}}, 'tags': ['certificates'], 'operationId': 'list_certificates'}
            sort = {'enum': ['id', 'id:asc', 'id:desc', 'name', 'name:asc', 'name:desc', 'created', 'created:asc', 'created:desc'], 'type': 'string'}
            name = {'type': 'string'}
            label_selector = {'type': 'string'}
            type = {'enum': ['uploaded', 'managed'], 'title': 'ParameterType', 'type': 'string'}
            page = {'type': 'integer', 'minimum': 1}
            per_page = {'type': 'integer', 'minimum': 1, 'maximum': 50}
        R.sort = 'id'
        R.name = str_dflt
        R.label_selector = str_dflt
        R.type = 'uploaded'
        R.page = 0
        R.per_page = 0

    class post:
        """Creates a new Certificate.

The default type **uploaded** allows for uploading your existing `certificate` and `private_key` in PEM format. You have to monitor its expiration date and handle renewal yourself.

In contrast, type **managed** requests a new Certificate from *Let's Encrypt* for the specified `domain_names`. Only domains managed by *Hetzner DNS* are supported. We handle renewal and timely alert the project owner via email if problems occur.

For type `managed` Certificates the `action` key of the response contains the Action that allows for tracking the issuance process. For type `uploaded` Certificates the `action` is always null.
 Create a Certificate"""
        class R:
            _body = ['body'];
            _ = {'requestBody': {'content': {}}, 'responses': {'201': {'content': {'application/json': {'examples': {'managed': {'summary': 'Response when creating a type `managed` Certificate', 'value': {'action': {'command': 'create_certificate', 'error': {'code': 'action_failed', 'message': 'Action failed'}, 'finished': None, 'id': 13, 'progress': 0, 'resources': [{'id': 879, 'type': 'certificate'}], 'started': '2019-01-08T12:10:00+00:00', 'status': 'running'}, 'certificate': {'certificate': None, 'created': '2019-01-08T12:10:00+00:00', 'domain_names': ['example.com', 'webmail.example.com', 'www.example.com'], 'fingerprint': None, 'id': 897, 'labels': {'env': 'dev'}, 'name': 'my website cert', 'not_valid_after': None, 'not_valid_before': None, 'status': {'error': None, 'issuance': 'pending', 'renewal': 'unavailable'}, 'type': 'managed', 'used_by': [{'id': 4711, 'type': 'load_balancer'}]}}}, 'uploaded': {'summary': 'Response when creating a type `uploaded` Certificate', 'value': {'action': None, 'certificate': {'certificate': '-----BEGIN CERTIFICATE-----\n...', 'created': '2019-01-08T12:10:00+00:00', 'domain_names': ['example.com', 'webmail.example.com', 'www.example.com'], 'fingerprint': '03:c7:55:9b:2a:d1:04:17:09:f6:d0:7f:18:34:63:d4:3e:5f', 'id': 897, 'labels': {'env': 'dev'}, 'name': 'my website cert', 'not_valid_after': '2019-07-08T09:59:59+00:00', 'not_valid_before': '2019-01-08T10:00:00+00:00', 'status': None, 'type': 'uploaded', 'used_by': [{'id': 4711, 'type': 'load_balancer'}]}}}}, 'schema': Defs.components_schemas_create_certificate_response}}, 'description': 'The `certificate` key contains the Certificate that was just created. For type `managed` Certificates the `action` key contains the Action that allows for tracking the issuance process. For type `uploaded` Certificates the `action` is always null.'}}, 'tags': ['certificates'], 'operationId': 'create_certificate', 'mime': 'application/json'}
            body = Defs.components_schemas_create_certificate_request
        R.body = Defs.components_schemas_create_certificate_request

class certificates___id_:
    pth = "/certificates/{id}"

    class delete:
        """Deletes a Certificate. Delete a Certificate"""
        class R:
            _path = ['id'];
            _ = {'responses': {'204': {'description': 'Certificate deleted'}}, 'tags': ['certificates'], 'operationId': 'delete_certificate'}
            id = {'type': 'integer'}
        R.id = id

    class get:
        """Gets a specific Certificate object. Get a Certificate"""
        class R:
            _path = ['id'];
            _ = {'responses': {'200': {'content': {'application/json': {'example': {'certificate': {'certificate': '-----BEGIN CERTIFICATE-----\n...', 'created': '2019-01-08T12:10:00+00:00', 'domain_names': ['example.com', 'webmail.example.com', 'www.example.com'], 'fingerprint': '03:c7:55:9b:2a:d1:04:17:09:f6:d0:7f:18:34:63:d4:3e:5f', 'id': 897, 'labels': {'env': 'dev'}, 'name': 'my website cert', 'not_valid_after': '2019-07-08T09:59:59+00:00', 'not_valid_before': '2019-01-08T10:00:00+00:00', 'status': None, 'type': 'uploaded', 'used_by': [{'id': 4711, 'type': 'load_balancer'}]}}, 'schema': Defs.components_schemas_get_certificate_response}}, 'description': 'The `certificate` key contains a Certificate object'}}, 'tags': ['certificates'], 'operationId': 'get_certificate'}
            id = {'type': 'integer'}
        R.id = id

    class put:
        """Updates the Certificate properties.

Note that when updating labels, the Certificate’s current set of labels will be replaced with the labels provided in the request body. So, for example, if you want to add a new label, you have to provide all existing labels plus the new label in the request body.

Note: if the Certificate object changes during the request, the response will be a “conflict” error.
 Update a Certificate"""
        class R:
            _path = ['id']; _body = ['body'];
            _ = {'requestBody': {'content': {}}, 'responses': {'200': {'content': {'application/json': {'example': {'certificate': {'certificate': '-----BEGIN CERTIFICATE-----\n...', 'created': '2019-01-08T12:10:00+00:00', 'domain_names': ['example.com', 'webmail.example.com', 'www.example.com'], 'fingerprint': '03:c7:55:9b:2a:d1:04:17:09:f6:d0:7f:18:34:63:d4:3e:5f', 'id': 897, 'labels': {'labelkey': 'value'}, 'name': 'my website cert', 'not_valid_after': '2019-07-08T09:59:59+00:00', 'not_valid_before': '2019-01-08T10:00:00+00:00', 'status': None, 'type': 'uploaded', 'used_by': [{'id': 4711, 'type': 'load_balancer'}]}}, 'schema': Defs.components_schemas_replace_certificate_response}}, 'description': 'The `certificate` key contains the Certificate that was just updated'}}, 'tags': ['certificates'], 'operationId': 'replace_certificate', 'mime': 'application/json'}
            id = {'type': 'integer'}
            body = Defs.components_schemas_replace_certificate_request
        R.id = id
        R.body = Defs.components_schemas_replace_certificate_request

class certificates___id___actions:
    pth = "/certificates/{id}/actions"

    class get:
        """Returns all Action objects for a Certificate. You can sort the results by using the `sort` URI parameter, and filter them with the `status` parameter.

Only type `managed` Certificates can have Actions. For type `uploaded` Certificates the `actions` key will always contain an empty array.
 Get all Actions for a Certificate"""
        class R:
            _query = ['sort', 'status', 'page', 'per_page']; _path = ['id'];
            _ = {'responses': {'200': {'content': {'application/json': {'example': {'actions': [{'command': 'issue_certificate', 'error': {'code': 'action_failed', 'message': 'Action failed'}, 'finished': '2021-01-30T23:57:00+00:00', 'id': 14, 'progress': 100, 'resources': [{'id': 896, 'type': 'certificate'}], 'started': '2021-01-30T23:55:00+00:00', 'status': 'success'}]}, 'schema': Defs.components_schemas_list_actions_for_certificate_response}}, 'description': 'The `actions` key contains a list of Actions'}}, 'tags': ['certificates'], 'operationId': 'list_actions_for_certificate'}
            id = {'type': 'integer'}
            sort = {'enum': ['id', 'id:asc', 'id:desc', 'command', 'command:asc', 'command:desc', 'status', 'status:asc', 'status:desc', 'progress', 'progress:asc', 'progress:desc', 'started', 'started:asc', 'started:desc', 'finished', 'finished:asc', 'finished:desc'], 'title': 'ParameterSort', 'type': 'string'}
            status = {'enum': ['running', 'success', 'error'], 'title': 'ParameterStatus', 'type': 'string'}
            page = {'type': 'integer', 'minimum': 1}
            per_page = {'type': 'integer', 'minimum': 1, 'maximum': 50}
        R.id = id
        R.sort = 'id'
        R.status = 'running'
        R.page = 0
        R.per_page = 0

class certificates___id___actions___action_id_:
    pth = "/certificates/{id}/actions/{action_id}"

    class get:
        """Returns a specific Action for a Certificate. Only type `managed` Certificates have Actions. Get an Action for a Certificate"""
        class R:
            _path = ['id', 'action_id'];
            _ = {'responses': {'200': {'content': {'application/json': {'example': {'action': {'command': 'issue_certificate', 'error': {'code': 'action_failed', 'message': 'Action failed'}, 'finished': '2021-01-30T23:57:00+00:00', 'id': 14, 'progress': 100, 'resources': [{'id': 896, 'type': 'certificate'}], 'started': '2021-01-30T23:55:00+00:00', 'status': 'success'}}, 'schema': Defs.components_schemas_get_action_for_certificate_response}}, 'description': 'The `action` key contains the Certificate Action'}}, 'tags': ['certificates'], 'operationId': 'get_action_for_certificate'}
            id = {'type': 'integer'}
            action_id = {'type': 'integer'}
        R.id = id
        R.action_id = action_id

class certificates___id___actions__retry:
    pth = "/certificates/{id}/actions/retry"

    class post:
        """Retry a failed Certificate issuance or renewal.

Only applicable if the type of the Certificate is `managed` and the issuance or renewal status is `failed`.

#### Call specific error codes

| Code                                                    | Description                                                               |
|---------------------------------------------------------|---------------------------------------------------------------------------|
| `caa_record_does_not_allow_ca`                          | CAA record does not allow certificate authority                           |
| `ca_dns_validation_failed`                              | Certificate Authority: DNS validation failed                              |
| `ca_too_many_authorizations_failed_recently`            | Certificate Authority: Too many authorizations failed recently            |
| `ca_too_many_certificates_issued_for_registered_domain` | Certificate Authority: Too many certificates issued for registered domain |
| `ca_too_many_duplicate_certificates`                    | Certificate Authority: Too many duplicate certificates                    |
| `could_not_verify_domain_delegated_to_zone`             | Could not verify domain delegated to zone                                 |
| `dns_zone_not_found`                                    | DNS zone not found                                                        |
| `dns_zone_is_secondary_zone`                            | DNS zone is a secondary zone                                              |
 Retry Issuance or Renewal"""
        class R:
            _path = ['id'];
            _ = {'responses': {'201': {'content': {'application/json': {'example': {'action': {'command': 'issue_certificate', 'error': {'code': 'action_failed', 'message': 'Action failed'}, 'finished': '2021-01-30T23:57:00+00:00', 'id': 14, 'progress': 100, 'resources': [{'id': 896, 'type': 'certificate'}], 'started': '2021-01-30T23:55:00+00:00', 'status': 'success'}}, 'schema': Defs.components_schemas_retry_issuance_or_renewal_response}}, 'description': 'The `action` key contains the resulting Action'}}, 'tags': ['certificates'], 'operationId': 'retry_issuance_or_renewal'}
            id = {'type': 'integer'}
        R.id = id

class datacenters:
    pth = "/datacenters"

    class get:
        """Returns all Datacenter objects. Get all Datacenters"""
        class R:
            _query = ['name'];
            _ = {'responses': {'200': {'content': {'application/json': {'schema': Defs.components_schemas_list_datacenters_response}}, 'description': 'The reply contains the `datacenters` and `recommendation` keys'}}, 'tags': ['datacenters'], 'operationId': 'list_datacenters'}
            name = {'type': 'string'}
        R.name = str_dflt

class datacenters___id_:
    pth = "/datacenters/{id}"

    class get:
        """Returns a specific Datacenter object. Get a Datacenter"""
        class R:
            _path = ['id'];
            _ = {'responses': {'200': {'content': {'application/json': {'schema': Defs.components_schemas_get_datacenter_response}}, 'description': 'The `datacenter` key in the reply contains a Datacenter object with this structure'}}, 'tags': ['datacenters'], 'operationId': 'get_datacenter'}
            id = {'type': 'integer'}
        R.id = id

class firewalls:
    pth = "/firewalls"

    class get:
        """Returns all Firewall objects. Get all Firewalls"""
        class R:
            _query = ['sort', 'name', 'label_selector', 'page', 'per_page'];
            _ = {'responses': {'200': {'content': {'application/json': {'schema': Defs.components_schemas_list_firewalls_response}}, 'description': 'The `firewalls` key contains an array of Firewall objects'}}, 'tags': ['firewalls'], 'operationId': 'list_firewalls'}
            sort = {'enum': ['id', 'id:asc', 'id:desc', 'name', 'name:asc', 'name:desc', 'created', 'created:asc', 'created:desc'], 'type': 'string'}
            name = {'type': 'string'}
            label_selector = {'type': 'string'}
            page = {'type': 'integer', 'minimum': 1}
            per_page = {'type': 'integer', 'minimum': 1, 'maximum': 50}
        R.sort = 'id'
        R.name = str_dflt
        R.label_selector = str_dflt
        R.page = 0
        R.per_page = 0

    class post:
        """Creates a new Firewall.

#### Call specific error codes

| Code                          | Description                                                   |
|------------------------------ |-------------------------------------------------------------- |
| `server_already_added`        | Server added more than one time to resource                   |
| `incompatible_network_type`   | The Network type is incompatible for the given resource       |
| `firewall_resource_not_found` | The resource the Firewall should be attached to was not found |
 Create a Firewall"""
        class R:
            _body = ['body'];
            _ = {'requestBody': {'content': {}}, 'responses': {'201': {'content': {'application/json': {'schema': Defs.components_schemas_create_firewall_response}}, 'description': 'The `firewall` key contains the Firewall that was just created'}}, 'tags': ['firewalls'], 'operationId': 'create_firewall', 'mime': 'application/json'}
            body = Defs.components_schemas_create_firewall_request
        R.body = Defs.components_schemas_create_firewall_request

class firewalls___id_:
    pth = "/firewalls/{id}"

    class delete:
        """Deletes a Firewall.

#### Call specific error codes

| Code                 | Description                               |
|--------------------- |-------------------------------------------|
| `resource_in_use`    | Firewall must not be in use to be deleted |
 Delete a Firewall"""
        class R:
            _path = ['id'];
            _ = {'responses': {'204': {'description': 'Firewall deleted'}}, 'tags': ['firewalls'], 'operationId': 'delete_firewall'}
            id = {'type': 'integer'}
        R.id = id

    class get:
        """Gets a specific Firewall object. Get a Firewall"""
        class R:
            _path = ['id'];
            _ = {'responses': {'200': {'content': {'application/json': {'schema': Defs.components_schemas_get_firewall_response}}, 'description': 'The `firewall` key contains a Firewall object'}}, 'tags': ['firewalls'], 'operationId': 'get_firewall'}
            id = {'type': 'integer'}
        R.id = id

    class put:
        """Updates the Firewall.

Note that when updating labels, the Firewall's current set of labels will be replaced with the labels provided in the request body. So, for example, if you want to add a new label, you have to provide all existing labels plus the new label in the request body.

Note: if the Firewall object changes during the request, the response will be a “conflict” error.
 Update a Firewall"""
        class R:
            _path = ['id']; _body = ['body'];
            _ = {'requestBody': {'content': {}}, 'responses': {'200': {'content': {'application/json': {'schema': Defs.components_schemas_replace_firewall_response}}, 'description': 'The `firewall` key contains the Firewall that was just updated'}}, 'tags': ['firewalls'], 'operationId': 'replace_firewall', 'mime': 'application/json'}
            id = {'type': 'integer'}
            body = Defs.components_schemas_replace_firewall_request
        R.id = id
        R.body = Defs.components_schemas_replace_firewall_request

class firewalls___id___actions:
    pth = "/firewalls/{id}/actions"

    class get:
        """Returns all Action objects for a Firewall. You can sort the results by using the `sort` URI parameter, and filter them with the `status` parameter. Get all Actions for a Firewall"""
        class R:
            _query = ['sort', 'status', 'page', 'per_page']; _path = ['id'];
            _ = {'responses': {'200': {'content': {'application/json': {'example': {'actions': [{'command': 'set_firewall_rules', 'error': {'code': 'action_failed', 'message': 'Action failed'}, 'finished': '2016-01-30T23:56:00+00:00', 'id': 13, 'progress': 100, 'resources': [{'id': 38, 'type': 'firewall'}], 'started': '2016-01-30T23:55:00+00:00', 'status': 'success'}]}, 'schema': Defs.components_schemas_list_actions_for_firewall_response}}, 'description': 'The `actions` key contains a list of Actions'}}, 'tags': ['firewalls'], 'operationId': 'list_actions_for_firewall'}
            id = {'type': 'integer'}
            sort = {'enum': ['id', 'id:asc', 'id:desc', 'command', 'command:asc', 'command:desc', 'status', 'status:asc', 'status:desc', 'progress', 'progress:asc', 'progress:desc', 'started', 'started:asc', 'started:desc', 'finished', 'finished:asc', 'finished:desc'], 'title': 'ParameterSort', 'type': 'string'}
            status = {'enum': ['running', 'success', 'error'], 'title': 'ParameterStatus', 'type': 'string'}
            page = {'type': 'integer', 'minimum': 1}
            per_page = {'type': 'integer', 'minimum': 1, 'maximum': 50}
        R.id = id
        R.sort = 'id'
        R.status = 'running'
        R.page = 0
        R.per_page = 0

class firewalls___id___actions___action_id_:
    pth = "/firewalls/{id}/actions/{action_id}"

    class get:
        """Returns a specific Action for a Firewall. Get an Action for a Firewall"""
        class R:
            _path = ['id', 'action_id'];
            _ = {'responses': {'200': {'content': {'application/json': {'example': {'action': {'command': 'set_firewall_rules', 'error': {'code': 'action_failed', 'message': 'Action failed'}, 'finished': '2016-01-30T23:56:00+00:00', 'id': 13, 'progress': 100, 'resources': [{'id': 38, 'type': 'firewall'}], 'started': '2016-01-30T23:55:00+00:00', 'status': 'success'}}, 'schema': Defs.components_schemas_get_action_for_firewall_response}}, 'description': 'The `action` key contains the Firewall Action'}}, 'tags': ['firewalls'], 'operationId': 'get_action_for_firewall'}
            id = {'type': 'integer'}
            action_id = {'type': 'integer'}
        R.id = id
        R.action_id = action_id

class firewalls___id___actions__apply_to_resources:
    pth = "/firewalls/{id}/actions/apply_to_resources"

    class post:
        """Applies one Firewall to multiple resources.

Currently servers (public network interface) and label selectors are supported.

#### Call specific error codes

| Code                          | Description                                                   |
|-------------------------------|---------------------------------------------------------------|
| `firewall_already_applied`    | Firewall was already applied on resource                      |
| `incompatible_network_type`   | The Network type is incompatible for the given resource       |
| `firewall_resource_not_found` | The resource the Firewall should be attached to was not found |
 Apply to Resources"""
        class R:
            _path = ['id']; _body = ['body'];
            _ = {'requestBody': {'content': {}}, 'responses': {'201': {'content': {'application/json': {'example': {'actions': [{'command': 'apply_firewall', 'error': {'code': 'action_failed', 'message': 'Action failed'}, 'finished': '2016-01-30T23:56:00+00:00', 'id': 14, 'progress': 100, 'resources': [{'id': 42, 'type': 'server'}, {'id': 38, 'type': 'firewall'}], 'started': '2016-01-30T23:55:00+00:00', 'status': 'success'}]}, 'schema': Defs.components_schemas_apply_to_resources_response}}, 'description': 'The `actions` key contains multiple `apply_firewall` Actions'}}, 'tags': ['firewalls'], 'operationId': 'apply_to_resources', 'mime': 'application/json'}
            id = {'type': 'integer'}
            body = Defs.components_schemas_apply_to_resources_request
        R.id = id
        R.body = Defs.components_schemas_apply_to_resources_request

class firewalls___id___actions__remove_from_resources:
    pth = "/firewalls/{id}/actions/remove_from_resources"

    class post:
        """Removes one Firewall from multiple resources.

Currently only Servers (and their public network interfaces) are supported.

#### Call specific error codes

| Code                                  | Description                                                            |
|---------------------------------------|------------------------------------------------------------------------|
| `firewall_already_removed`            | Firewall was already removed from the resource                         |
| `firewall_resource_not_found`         | The resource the Firewall should be attached to was not found          |
| `firewall_managed_by_label_selector`  | Firewall was applied via label selector and cannot be removed manually |
 Remove from Resources"""
        class R:
            _path = ['id']; _body = ['body'];
            _ = {'requestBody': {'content': {}}, 'responses': {'201': {'content': {'application/json': {'example': {'actions': [{'command': 'remove_firewall', 'error': {'code': 'action_failed', 'message': 'Action failed'}, 'finished': '2016-01-30T23:56:00+00:00', 'id': 14, 'progress': 100, 'resources': [{'id': 42, 'type': 'server'}, {'id': 38, 'type': 'firewall'}], 'started': '2016-01-30T23:55:00+00:00', 'status': 'success'}]}, 'schema': Defs.components_schemas_remove_from_resources_response}}, 'description': 'The `actions` key contains multiple `remove_firewall` Actions'}}, 'tags': ['firewalls'], 'operationId': 'remove_from_resources', 'mime': 'application/json'}
            id = {'type': 'integer'}
            body = Defs.components_schemas_remove_from_resources_request
        R.id = id
        R.body = Defs.components_schemas_remove_from_resources_request

class firewalls___id___actions__set_rules:
    pth = "/firewalls/{id}/actions/set_rules"

    class post:
        """Sets the rules of a Firewall.

All existing rules will be overwritten. Pass an empty `rules` array to remove all rules.
The maximum amount of rules that can be defined is 50.

#### Call specific error codes

| Code                          | Description                                                   |
|-------------------------------|---------------------------------------------------------------|
| `firewall_resource_not_found` | The resource the Firewall should be attached to was not found |
 Set Rules"""
        class R:
            _path = ['id']; _body = ['body'];
            _ = {'requestBody': {'content': {}}, 'responses': {'201': {'content': {'application/json': {'example': {'actions': [{'command': 'set_firewall_rules', 'error': {'code': 'action_failed', 'message': 'Action failed'}, 'finished': '2016-01-30T23:56:00+00:00', 'id': 13, 'progress': 100, 'resources': [{'id': 38, 'type': 'firewall'}], 'started': '2016-01-30T23:55:00+00:00', 'status': 'success'}, {'command': 'apply_firewall', 'error': {'code': 'action_failed', 'message': 'Action failed'}, 'finished': '2016-01-30T23:56:00+00:00', 'id': 14, 'progress': 100, 'resources': [{'id': 38, 'type': 'firewall'}, {'id': 42, 'type': 'server'}], 'started': '2016-01-30T23:55:00+00:00', 'status': 'success'}]}, 'schema': Defs.components_schemas_set_rules_response}}, 'description': 'The `action` key contains one `set_firewall_rules` Action plus one `apply_firewall` Action per resource where the Firewall is active'}}, 'tags': ['firewalls'], 'operationId': 'set_rules', 'mime': 'application/json'}
            id = {'type': 'integer'}
            body = Defs.components_schemas_set_rules_request
        R.id = id
        R.body = Defs.components_schemas_set_rules_request

class floating_ips:
    pth = "/floating_ips"

    class get:
        """Returns all Floating IP objects. Get all Floating IPs"""
        class R:
            _query = ['name', 'label_selector', 'sort', 'page', 'per_page'];
            _ = {'responses': {'200': {'content': {'application/json': {'schema': Defs.components_schemas_list_floating_ips_response}}, 'description': 'The `floating_ips` key in the reply contains an array of Floating IP objects with this structure'}}, 'tags': ['floating_ips'], 'operationId': 'list_floating_ips'}
            name = {'type': 'string'}
            label_selector = {'type': 'string'}
            sort = {'enum': ['id', 'id:asc', 'id:desc', 'created', 'created:asc', 'created:desc'], 'type': 'string'}
            page = {'type': 'integer', 'minimum': 1}
            per_page = {'type': 'integer', 'minimum': 1, 'maximum': 50}
        R.name = str_dflt
        R.label_selector = str_dflt
        R.sort = 'id'
        R.page = 0
        R.per_page = 0

    class post:
        """Creates a new Floating IP assigned to a Server. If you want to create a Floating IP that is not bound to a Server, you need to provide the `home_location` key instead of `server`. This can be either the ID or the name of the Location this IP shall be created in. Note that a Floating IP can be assigned to a Server in any Location later on. For optimal routing it is advised to use the Floating IP in the same Location it was created in. Create a Floating IP"""
        class R:
            _body = ['body'];
            _ = {'requestBody': {'content': {}, 'description': 'The `type` argument is required while `home_location` and `server` are mutually exclusive.'}, 'responses': {'201': {'content': {'application/json': {'example': {'action': {'command': 'create_floating_ip', 'error': {'code': 'action_failed', 'message': 'Action failed'}, 'finished': None, 'id': 13, 'progress': 0, 'resources': [{'id': 42, 'type': 'server'}], 'started': '2016-01-30T23:50:00+00:00', 'status': 'running'}, 'floating_ip': {'blocked': False, 'created': '2016-01-30T23:50:00+00:00', 'description': 'Web Frontend', 'dns_ptr': [{'dns_ptr': 'server.example.com', 'ip': '2001:db8::1'}], 'home_location': {'city': 'Falkenstein', 'country': 'DE', 'description': 'Falkenstein DC Park 1', 'id': 1, 'latitude': 50.47612, 'longitude': 12.370071, 'name': 'fsn1', 'network_zone': 'eu-central'}, 'id': 4711, 'ip': '131.232.99.1', 'labels': {'env': 'dev'}, 'name': 'Web Frontend', 'protection': {'delete': False}, 'server': 42, 'type': 'ipv4'}}, 'schema': Defs.components_schemas_create_floating_ip_response}}, 'description': 'The `floating_ip` key in the reply contains the object that was just created'}}, 'tags': ['floating_ips'], 'operationId': 'create_floating_ip', 'mime': 'application/json'}
            body = Defs.components_schemas_create_floating_ip_request
        R.body = Defs.components_schemas_create_floating_ip_request

class floating_ips___id_:
    pth = "/floating_ips/{id}"

    class delete:
        """Deletes a Floating IP. If it is currently assigned to a Server it will automatically get unassigned. Delete a Floating IP"""
        class R:
            _path = ['id'];
            _ = {'responses': {'204': {'description': 'Floating IP deleted'}}, 'tags': ['floating_ips'], 'operationId': 'delete_floating_ip'}
            id = {'type': 'integer'}
        R.id = id

    class get:
        """Returns a specific Floating IP object. Get a Floating IP"""
        class R:
            _path = ['id'];
            _ = {'responses': {'200': {'content': {'application/json': {'schema': Defs.components_schemas_get_floating_ip_response}}, 'description': 'The `floating_ip` key in the reply contains a Floating IP object with this structure'}}, 'tags': ['floating_ips'], 'operationId': 'get_floating_ip'}
            id = {'type': 'integer'}
        R.id = id

    class put:
        """Updates the description or labels of a Floating IP.
Also note that when updating labels, the Floating IP’s current set of labels will be replaced with the labels provided in the request body. So, for example, if you want to add a new label, you have to provide all existing labels plus the new label in the request body. Update a Floating IP"""
        class R:
            _path = ['id']; _body = ['body'];
            _ = {'requestBody': {'content': {}}, 'responses': {'200': {'content': {'application/json': {'example': {'floating_ip': {'blocked': False, 'created': '2016-01-30T23:50:00+00:00', 'description': 'Web Frontend', 'dns_ptr': [{'dns_ptr': 'server.example.com', 'ip': '2001:db8::1'}], 'home_location': {'city': 'Falkenstein', 'country': 'DE', 'description': 'Falkenstein DC Park 1', 'id': 1, 'latitude': 50.47612, 'longitude': 12.370071, 'name': 'fsn1', 'network_zone': 'eu-central'}, 'id': 4711, 'ip': '131.232.99.1', 'labels': {'labelkey': 'value'}, 'name': 'Web Frontend', 'protection': {'delete': False}, 'server': 42, 'type': 'ipv4'}}, 'schema': Defs.components_schemas_replace_floating_ip_response}}, 'description': 'The `floating_ip` key in the reply contains the modified Floating IP object with the new description'}}, 'tags': ['floating_ips'], 'operationId': 'replace_floating_ip', 'mime': 'application/json'}
            id = {'type': 'integer'}
            body = Defs.components_schemas_replace_floating_ip_request
        R.id = id
        R.body = Defs.components_schemas_replace_floating_ip_request

class floating_ips___id___actions:
    pth = "/floating_ips/{id}/actions"

    class get:
        """Returns all Action objects for a Floating IP. You can sort the results by using the `sort` URI parameter, and filter them with the `status` parameter. Get all Actions for a Floating IP"""
        class R:
            _query = ['sort', 'status', 'page', 'per_page']; _path = ['id'];
            _ = {'responses': {'200': {'content': {'application/json': {'example': {'actions': [{'command': 'assign_floating_ip', 'error': {'code': 'action_failed', 'message': 'Action failed'}, 'finished': '2016-01-30T23:56:00+00:00', 'id': 13, 'progress': 100, 'resources': [{'id': 4711, 'type': 'server'}, {'id': 4712, 'type': 'floating_ip'}], 'started': '2016-01-30T23:55:00+00:00', 'status': 'success'}]}, 'schema': Defs.components_schemas_list_actions_for_floating_ip_response}}, 'description': 'The `actions` key contains a list of Actions'}}, 'tags': ['floating_ips'], 'operationId': 'list_actions_for_floating_ip'}
            id = {'type': 'integer'}
            sort = {'enum': ['id', 'id:asc', 'id:desc', 'command', 'command:asc', 'command:desc', 'status', 'status:asc', 'status:desc', 'progress', 'progress:asc', 'progress:desc', 'started', 'started:asc', 'started:desc', 'finished', 'finished:asc', 'finished:desc'], 'title': 'ParameterSort', 'type': 'string'}
            status = {'enum': ['running', 'success', 'error'], 'title': 'ParameterStatus', 'type': 'string'}
            page = {'type': 'integer', 'minimum': 1}
            per_page = {'type': 'integer', 'minimum': 1, 'maximum': 50}
        R.id = id
        R.sort = 'id'
        R.status = 'running'
        R.page = 0
        R.per_page = 0

class floating_ips___id___actions___action_id_:
    pth = "/floating_ips/{id}/actions/{action_id}"

    class get:
        """Returns a specific Action object for a Floating IP. Get an Action for a Floating IP"""
        class R:
            _path = ['id', 'action_id'];
            _ = {'responses': {'200': {'content': {'application/json': {'example': {'action': {'command': 'assign_floating_ip', 'error': {'code': 'action_failed', 'message': 'Action failed'}, 'finished': '2016-01-30T23:56:00+00:00', 'id': 13, 'progress': 100, 'resources': [{'id': 42, 'type': 'server'}, {'id': 4711, 'type': 'floating_ip'}], 'started': '2016-01-30T23:55:00+00:00', 'status': 'success'}}, 'schema': Defs.components_schemas_get_action_for_floating_ip_response}}, 'description': 'The `action` key in the reply has this structure'}}, 'tags': ['floating_ips'], 'operationId': 'get_action_for_floating_ip'}
            id = {'type': 'integer'}
            action_id = {'type': 'integer'}
        R.id = id
        R.action_id = action_id

class floating_ips___id___actions__assign:
    pth = "/floating_ips/{id}/actions/assign"

    class post:
        """Assigns a Floating IP to a Server. Assign a Floating IP to a Server"""
        class R:
            _path = ['id']; _body = ['body'];
            _ = {'requestBody': {'content': {}}, 'responses': {'201': {'content': {'application/json': {'example': {'action': {'command': 'assign_floating_ip', 'error': {'code': 'action_failed', 'message': 'Action failed'}, 'finished': '2016-01-30T23:56:00+00:00', 'id': 13, 'progress': 100, 'resources': [{'id': 42, 'type': 'server'}, {'id': 4711, 'type': 'floating_ip'}], 'started': '2016-01-30T23:55:00+00:00', 'status': 'success'}}, 'schema': Defs.components_schemas_assign_floating_ip_to_server_response}}, 'description': 'The `action` key contains the `assign` Action'}}, 'tags': ['floating_ips'], 'operationId': 'assign_floating_ip_to_server', 'mime': 'application/json'}
            id = {'type': 'integer'}
            body = Defs.components_schemas_assign_floating_ip_to_server_request
        R.id = id
        R.body = Defs.components_schemas_assign_floating_ip_to_server_request

class floating_ips___id___actions__change_dns_ptr:
    pth = "/floating_ips/{id}/actions/change_dns_ptr"

    class post:
        """Changes the hostname that will appear when getting the hostname belonging to this Floating IP. Change reverse DNS entry for a Floating IP"""
        class R:
            _path = ['id']; _body = ['body'];
            _ = {'requestBody': {'content': {}, 'description': 'Select the IP address for which to change the DNS entry by passing `ip`. For a Floating IP of type `ipv4` this must exactly match the IP address of the Floating IP. For a Floating IP of type `ipv6` this must be a single IP within the IPv6 /64 range that belongs to this Floating IP.\n\nThe target hostname is set by passing `dns_ptr`.\n'}, 'responses': {'201': {'content': {'application/json': {'example': {'action': {'command': 'change_dns_ptr', 'error': {'code': 'action_failed', 'message': 'Action failed'}, 'finished': '2016-01-30T23:56:00+00:00', 'id': 13, 'progress': 100, 'resources': [{'id': 4711, 'type': 'floating_ip'}], 'started': '2016-01-30T23:55:00+00:00', 'status': 'success'}}, 'schema': Defs.components_schemas_change_reverse_dns_entry_for_floating_ip_response}}, 'description': 'The `action` key contains the `change_dns_ptr` Action'}}, 'tags': ['floating_ips'], 'operationId': 'change_reverse_dns_entry_for_floating_ip', 'mime': 'application/json'}
            id = {'type': 'integer'}
            body = Defs.components_schemas_change_reverse_dns_entry_for_floating_ip_request
        R.id = id
        R.body = Defs.components_schemas_change_reverse_dns_entry_for_floating_ip_request

class floating_ips___id___actions__change_protection:
    pth = "/floating_ips/{id}/actions/change_protection"

    class post:
        """Changes the protection configuration of the Floating IP. Change Floating IP Protection"""
        class R:
            _path = ['id']; _body = ['body'];
            _ = {'requestBody': {'content': {}}, 'responses': {'201': {'content': {'application/json': {'example': {'action': {'command': 'change_protection', 'error': {'code': 'action_failed', 'message': 'Action failed'}, 'finished': '2016-01-30T23:56:00+00:00', 'id': 13, 'progress': 100, 'resources': [{'id': 4711, 'type': 'floating_ip'}], 'started': '2016-01-30T23:55:00+00:00', 'status': 'success'}}, 'schema': Defs.components_schemas_change_floating_ip_protection_response}}, 'description': 'The `action` key contains the `change_protection` Action'}}, 'tags': ['floating_ips'], 'operationId': 'change_floating_ip_protection', 'mime': 'application/json'}
            id = {'type': 'integer'}
            body = Defs.components_schemas_change_floating_ip_protection_request
        R.id = id
        R.body = Defs.components_schemas_change_floating_ip_protection_request

class floating_ips___id___actions__unassign:
    pth = "/floating_ips/{id}/actions/unassign"

    class post:
        """Unassigns a Floating IP, resulting in it being unreachable. You may assign it to a Server again at a later time. Unassign a Floating IP"""
        class R:
            _path = ['id'];
            _ = {'responses': {'201': {'content': {'application/json': {'example': {'action': {'command': 'unassign_floating_ip', 'error': {'code': 'action_failed', 'message': 'Action failed'}, 'finished': '2016-01-30T23:56:00+00:00', 'id': 13, 'progress': 100, 'resources': [{'id': 42, 'type': 'server'}, {'id': 4711, 'type': 'floating_ip'}], 'started': '2016-01-30T23:55:00+00:00', 'status': 'success'}}, 'schema': Defs.components_schemas_unassign_floating_ip_response}}, 'description': 'The `action` key contains the `unassign` Action'}}, 'tags': ['floating_ips'], 'operationId': 'unassign_floating_ip'}
            id = {'type': 'integer'}
        R.id = id

class images:
    pth = "/images"

    class get:
        """Returns all Image objects. You can select specific Image types only and sort the results by using URI parameters. Get all Images"""
        class R:
            _query = ['sort', 'type', 'status', 'bound_to', 'include_deprecated', 'name', 'label_selector', 'page', 'per_page'];
            _ = {'responses': {'200': {'content': {'application/json': {'schema': Defs.components_schemas_list_images_response}}, 'description': 'The `images` key in the reply contains an array of Image objects with this structure'}}, 'tags': ['images'], 'operationId': 'list_images'}
            sort = {'enum': ['id', 'id:asc', 'id:desc', 'name', 'name:asc', 'name:desc', 'created', 'created:asc', 'created:desc'], 'type': 'string'}
            type = {'enum': ['system', 'snapshot', 'backup', 'app'], 'type': 'string'}
            status = {'enum': ['available', 'creating'], 'type': 'string'}
            bound_to = {'type': 'string'}
            include_deprecated = {'type': 'boolean'}
            name = {'type': 'string'}
            label_selector = {'type': 'string'}
            page = {'type': 'integer', 'minimum': 1}
            per_page = {'type': 'integer', 'minimum': 1, 'maximum': 50}
        R.sort = 'id'
        R.type = 'system'
        R.status = 'available'
        R.bound_to = str_dflt
        R.include_deprecated = True
        R.name = str_dflt
        R.label_selector = str_dflt
        R.page = 0
        R.per_page = 0

class images___id_:
    pth = "/images/{id}"

    class delete:
        """Deletes an Image. Only Images of type `snapshot` and `backup` can be deleted. Delete an Image"""
        class R:
            _path = ['id'];
            _ = {'responses': {'204': {'description': 'Image deleted'}}, 'tags': ['images'], 'operationId': 'delete_image'}
            id = {'type': 'integer'}
        R.id = id

    class get:
        """Returns a specific Image object. Get an Image"""
        class R:
            _path = ['id'];
            _ = {'responses': {'200': {'content': {'application/json': {'schema': Defs.components_schemas_get_image_response}}, 'description': 'The `image` key in the reply contains an Image object with this structure'}}, 'tags': ['images'], 'operationId': 'get_image'}
            id = {'type': 'integer'}
        R.id = id

    class put:
        """Updates the Image. You may change the description, convert a Backup Image to a Snapshot Image or change the Image labels. Only Images of type `snapshot` and `backup` can be updated.

Note that when updating labels, the current set of labels will be replaced with the labels provided in the request body. So, for example, if you want to add a new label, you have to provide all existing labels plus the new label in the request body.
 Update an Image"""
        class R:
            _path = ['id']; _body = ['body'];
            _ = {'requestBody': {'content': {}}, 'responses': {'200': {'content': {'application/json': {'example': {'image': {'bound_to': None, 'build_id': 'c313fe40383af26094a5a92026054320ab55abc7', 'created': '2016-01-30T23:50:00+00:00', 'created_from': {'id': 1, 'name': 'Server'}, 'deleted': None, 'deprecated': '2018-02-28T00:00:00+00:00', 'description': 'My new Image description', 'disk_size': 10, 'id': 4711, 'image_size': 2.3, 'labels': {'labelkey': 'value'}, 'name': None, 'os_flavor': 'ubuntu', 'os_version': '20.04', 'protection': {'delete': False}, 'rapid_deploy': False, 'status': 'available', 'type': 'snapshot'}}, 'schema': Defs.components_schemas_replace_image_response}}, 'description': 'The image key in the reply contains the modified Image object'}}, 'tags': ['images'], 'operationId': 'replace_image', 'mime': 'application/json'}
            id = {'type': 'integer'}
            body = Defs.components_schemas_replace_image_request
        R.id = id
        R.body = Defs.components_schemas_replace_image_request

class images___id___actions:
    pth = "/images/{id}/actions"

    class get:
        """Returns all Action objects for an Image. You can sort the results by using the `sort` URI parameter, and filter them with the `status` parameter. Get all Actions for an Image"""
        class R:
            _query = ['sort', 'status', 'page', 'per_page']; _path = ['id'];
            _ = {'responses': {'200': {'content': {'application/json': {'example': {'actions': [{'command': 'change_protection', 'error': {'code': 'action_failed', 'message': 'Action failed'}, 'finished': '2016-01-30T23:56:00+00:00', 'id': 13, 'progress': 100, 'resources': [{'id': 4711, 'type': 'image'}], 'started': '2016-01-30T23:55:00+00:00', 'status': 'success'}]}, 'schema': Defs.components_schemas_list_actions_for_image_response}}, 'description': 'The `actions` key contains a list of Actions'}}, 'tags': ['images'], 'operationId': 'list_actions_for_image'}
            id = {'type': 'integer'}
            sort = {'enum': ['id', 'id:asc', 'id:desc', 'command', 'command:asc', 'command:desc', 'status', 'status:asc', 'status:desc', 'progress', 'progress:asc', 'progress:desc', 'started', 'started:asc', 'started:desc', 'finished', 'finished:asc', 'finished:desc'], 'title': 'ParameterSort', 'type': 'string'}
            status = {'enum': ['running', 'success', 'error'], 'title': 'ParameterStatus', 'type': 'string'}
            page = {'type': 'integer', 'minimum': 1}
            per_page = {'type': 'integer', 'minimum': 1, 'maximum': 50}
        R.id = id
        R.sort = 'id'
        R.status = 'running'
        R.page = 0
        R.per_page = 0

class images___id___actions___action_id_:
    pth = "/images/{id}/actions/{action_id}"

    class get:
        """Returns a specific Action for an Image. Get an Action for an Image"""
        class R:
            _path = ['id', 'action_id'];
            _ = {'responses': {'200': {'content': {'application/json': {'example': {'action': {'command': 'change_protection', 'error': {'code': 'action_failed', 'message': 'Action failed'}, 'finished': '2016-01-30T23:56:00+00:00', 'id': 13, 'progress': 100, 'resources': [{'id': 4711, 'type': 'image'}], 'started': '2016-01-30T23:55:00+00:00', 'status': 'success'}}, 'schema': Defs.components_schemas_get_action_for_image_response}}, 'description': 'The `action` key contains the Image Action'}}, 'tags': ['images'], 'operationId': 'get_action_for_image'}
            id = {'type': 'integer'}
            action_id = {'type': 'integer'}
        R.id = id
        R.action_id = action_id

class images___id___actions__change_protection:
    pth = "/images/{id}/actions/change_protection"

    class post:
        """Changes the protection configuration of the Image. Can only be used on snapshots. Change Image Protection"""
        class R:
            _path = ['id']; _body = ['body'];
            _ = {'requestBody': {'content': {}}, 'responses': {'201': {'content': {'application/json': {'example': {'action': {'command': 'change_protection', 'error': {'code': 'action_failed', 'message': 'Action failed'}, 'finished': '2016-01-30T23:56:00+00:00', 'id': 13, 'progress': 100, 'resources': [{'id': 4711, 'type': 'image'}], 'started': '2016-01-30T23:55:00+00:00', 'status': 'success'}}, 'schema': Defs.components_schemas_change_image_protection_response}}, 'description': 'The `action` key contains the `change_protection` Action'}}, 'tags': ['images'], 'operationId': 'change_image_protection', 'mime': 'application/json'}
            id = {'type': 'integer'}
            body = Defs.components_schemas_change_image_protection_request
        R.id = id
        R.body = Defs.components_schemas_change_image_protection_request

class isos:
    pth = "/isos"

    class get:
        """Returns all available ISO objects. Get all ISOs"""
        class R:
            _query = ['name', 'page', 'per_page'];
            _ = {'responses': {'200': {'content': {'application/json': {'schema': Defs.components_schemas_list_isos_response}}, 'description': 'The `isos` key in the reply contains an array of iso objects with this structure'}}, 'tags': ['isos'], 'operationId': 'list_isos'}
            name = {'type': 'string'}
            page = {'type': 'integer', 'minimum': 1}
            per_page = {'type': 'integer', 'minimum': 1, 'maximum': 50}
        R.name = str_dflt
        R.page = 0
        R.per_page = 0

class isos___id_:
    pth = "/isos/{id}"

    class get:
        """Returns a specific ISO object. Get an ISO"""
        class R:
            _path = ['id'];
            _ = {'responses': {'200': {'content': {'application/json': {'schema': Defs.components_schemas_get_iso_response}}, 'description': 'The `iso` key in the reply contains an array of ISO objects with this structure'}}, 'tags': ['isos'], 'operationId': 'get_iso'}
            id = {'type': 'integer'}
        R.id = id

class load_balancer_types:
    pth = "/load_balancer_types"

    class get:
        """Gets all Load Balancer type objects. Get all Load Balancer Types"""
        class R:
            _query = ['name', 'page', 'per_page'];
            _ = {'responses': {'200': {'content': {'application/json': {'schema': Defs.components_schemas_list_load_balancer_types_response}}, 'description': 'The `load_balancer_types` key in the reply contains an array of Load Balancer type objects with this structure'}}, 'tags': ['load_balancer_types'], 'operationId': 'list_load_balancer_types'}
            name = {'type': 'string'}
            page = {'type': 'integer', 'minimum': 1}
            per_page = {'type': 'integer', 'minimum': 1, 'maximum': 50}
        R.name = str_dflt
        R.page = 0
        R.per_page = 0

class load_balancer_types___id_:
    pth = "/load_balancer_types/{id}"

    class get:
        """Gets a specific Load Balancer type object. Get a Load Balancer Type"""
        class R:
            _path = ['id'];
            _ = {'responses': {'200': {'content': {'application/json': {'schema': Defs.components_schemas_get_load_balancer_type_response}}, 'description': 'The `load_balancer_type` key in the reply contains a Load Balancer type object with this structure'}}, 'tags': ['load_balancer_types'], 'operationId': 'get_load_balancer_type'}
            id = {'type': 'integer'}
        R.id = id

class load_balancers:
    pth = "/load_balancers"

    class get:
        """Gets all existing Load Balancers that you have available. Get all Load Balancers"""
        class R:
            _query = ['sort', 'name', 'label_selector', 'page', 'per_page'];
            _ = {'responses': {'200': {'content': {'application/json': {'schema': Defs.components_schemas_list_load_balancers_response}}, 'description': 'The `load_balancers` key contains a list of Load Balancers'}}, 'tags': ['load_balancers'], 'operationId': 'list_load_balancers'}
            sort = {'enum': ['id', 'id:asc', 'id:desc', 'name', 'name:asc', 'name:desc', 'created', 'created:asc', 'created:desc'], 'type': 'string'}
            name = {'type': 'string'}
            label_selector = {'type': 'string'}
            page = {'type': 'integer', 'minimum': 1}
            per_page = {'type': 'integer', 'minimum': 1, 'maximum': 50}
        R.sort = 'id'
        R.name = str_dflt
        R.label_selector = str_dflt
        R.page = 0
        R.per_page = 0

    class post:
        """Creates a Load Balancer.

#### Call specific error codes

| Code                                    | Description                                                                                           |
|-----------------------------------------|-------------------------------------------------------------------------------------------------------|
| `cloud_resource_ip_not_allowed`         | The IP you are trying to add as a target belongs to a Hetzner Cloud resource                          |
| `ip_not_owned`                          | The IP is not owned by the owner of the project of the Load Balancer                                  |
| `load_balancer_not_attached_to_network` | The Load Balancer is not attached to a network                                                        |
| `robot_unavailable`                     | Robot was not available. The caller may retry the operation after a short delay.                      |
| `server_not_attached_to_network`        | The server you are trying to add as a target is not attached to the same network as the Load Balancer |
| `source_port_already_used`              | The source port you are trying to add is already in use                                               |
| `target_already_defined`                | The Load Balancer target you are trying to define is already defined                                  |
 Create a Load Balancer"""
        class R:
            _body = ['body'];
            _ = {'requestBody': {'content': {}}, 'responses': {'201': {'content': {'application/json': {'example': {'action': {'command': 'create_load_balancer', 'error': {'code': 'action_failed', 'message': 'Action failed'}, 'finished': '2016-01-30T23:56:00+00:00', 'id': 13, 'progress': 100, 'resources': [{'id': 4711, 'type': 'load_balancer'}], 'started': '2016-01-30T23:55:00+00:00', 'status': 'success'}, 'load_balancer': {'algorithm': {'type': 'round_robin'}, 'created': '2016-01-30T23:50:00+00:00', 'id': 4711, 'included_traffic': 654321, 'ingoing_traffic': 123456, 'labels': {'env': 'dev'}, 'load_balancer_type': {'deprecated': '2016-01-30T23:50:00+00:00', 'description': 'LB11', 'id': 1, 'max_assigned_certificates': 10, 'max_connections': 20000, 'max_services': 5, 'max_targets': 25, 'name': 'lb11', 'prices': [{'location': 'fsn1', 'price_hourly': {'gross': '1.1900000000000000', 'net': '1.0000000000'}, 'price_monthly': {'gross': '1.1900000000000000', 'net': '1.0000000000'}}]}, 'location': {'city': 'Falkenstein', 'country': 'DE', 'description': 'Falkenstein DC Park 1', 'id': 1, 'latitude': 50.47612, 'longitude': 12.370071, 'name': 'fsn1', 'network_zone': 'eu-central'}, 'name': 'Web Frontend', 'outgoing_traffic': 123456, 'private_net': [{'ip': '10.0.0.2', 'network': 4711}], 'protection': {'delete': False}, 'public_net': {'enabled': False, 'ipv4': {'ip': '1.2.3.4'}, 'ipv6': {'ip': '2001:db8::1'}}, 'services': [{'destination_port': 80, 'health_check': {'http': {'domain': 'example.com', 'path': '/', 'response': '{"status": "ok"}', 'status_codes': ['2??,3??'], 'tls': False}, 'interval': 15, 'port': 4711, 'protocol': 'http', 'retries': 3, 'timeout': 10}, 'http': {'certificates': [897], 'cookie_lifetime': 300, 'cookie_name': 'HCLBSTICKY', 'redirect_http': True, 'sticky_sessions': True}, 'listen_port': 443, 'protocol': 'http', 'proxyprotocol': False}], 'targets': [{'health_status': [{'listen_port': 443, 'status': 'healthy'}], 'server': {'id': 80}, 'targets': [{'health_status': [{'listen_port': 443, 'status': 'healthy'}], 'label_selector': None, 'server': {'id': 80}, 'type': 'server', 'use_private_ip': True}], 'type': 'server', 'use_private_ip': True}]}}, 'schema': Defs.components_schemas_create_load_balancer_response}}, 'description': 'The `load_balancer` key contains the Load Balancer that was just created'}}, 'tags': ['load_balancers'], 'operationId': 'create_load_balancer', 'mime': 'application/json'}
            body = Defs.components_schemas_create_load_balancer_request
        R.body = Defs.components_schemas_create_load_balancer_request

class load_balancers___id_:
    pth = "/load_balancers/{id}"

    class delete:
        """Deletes a Load Balancer. Delete a Load Balancer"""
        class R:
            _path = ['id'];
            _ = {'responses': {'204': {'description': 'Load Balancer deleted'}}, 'tags': ['load_balancers'], 'operationId': 'delete_load_balancer'}
            id = {'type': 'integer'}
        R.id = id

    class get:
        """Gets a specific Load Balancer object. Get a Load Balancer"""
        class R:
            _path = ['id'];
            _ = {'responses': {'200': {'content': {'application/json': {'schema': Defs.components_schemas_get_load_balancer_response}}, 'description': 'The `load_balancer` key contains the Load Balancer'}}, 'tags': ['load_balancers'], 'operationId': 'get_load_balancer'}
            id = {'type': 'integer'}
        R.id = id

    class put:
        """Updates a Load Balancer. You can update a Load Balancer’s name and a Load Balancer’s labels.

Note that when updating labels, the Load Balancer’s current set of labels will be replaced with the labels provided in the request body. So, for example, if you want to add a new label, you have to provide all existing labels plus the new label in the request body.

Note: if the Load Balancer object changes during the request, the response will be a “conflict” error.
 Update a Load Balancer"""
        class R:
            _path = ['id']; _body = ['body'];
            _ = {'requestBody': {'content': {}}, 'responses': {'200': {'content': {'application/json': {'example': {'load_balancer': {'algorithm': {'type': 'round_robin'}, 'created': '2016-01-30T23:50:00+00:00', 'id': 4711, 'included_traffic': 654321, 'ingoing_traffic': 123456, 'labels': {'labelkey': 'value'}, 'load_balancer_type': {'deprecated': '2016-01-30T23:50:00+00:00', 'description': 'LB11', 'id': 1, 'max_assigned_certificates': 10, 'max_connections': 20000, 'max_services': 5, 'max_targets': 25, 'name': 'lb11', 'prices': [{'location': 'fsn1', 'price_hourly': {'gross': '1.1900000000000000', 'net': '1.0000000000'}, 'price_monthly': {'gross': '1.1900000000000000', 'net': '1.0000000000'}}]}, 'location': {'city': 'Falkenstein', 'country': 'DE', 'description': 'Falkenstein DC Park 1', 'id': 1, 'latitude': 50.47612, 'longitude': 12.370071, 'name': 'fsn1', 'network_zone': 'eu-central'}, 'name': 'new-name', 'outgoing_traffic': 123456, 'private_net': [{'ip': '10.0.0.2', 'network': 4711}], 'protection': {'delete': False}, 'public_net': {'enabled': False, 'ipv4': {'ip': '1.2.3.4'}, 'ipv6': {'ip': '2001:db8::1'}}, 'services': [{'destination_port': 80, 'health_check': {'http': {'domain': 'example.com', 'path': '/', 'response': '{"status": "ok"}', 'status_codes': ['2??,3??'], 'tls': False}, 'interval': 15, 'port': 4711, 'protocol': 'http', 'retries': 3, 'timeout': 10}, 'http': {'certificates': [897], 'cookie_lifetime': 300, 'cookie_name': 'HCLBSTICKY', 'redirect_http': True, 'sticky_sessions': True}, 'listen_port': 443, 'protocol': 'http', 'proxyprotocol': False}], 'targets': [{'health_status': [{'listen_port': 443, 'status': 'healthy'}], 'ip': {'ip': '203.0.113.1'}, 'label_selector': {'selector': 'env=prod'}, 'server': {'id': 80}, 'targets': [{'health_status': [{'listen_port': 443, 'status': 'healthy'}], 'label_selector': None, 'server': {'id': 80}, 'type': 'server', 'use_private_ip': True}], 'type': 'server', 'use_private_ip': True}]}}, 'schema': Defs.components_schemas_replace_load_balancer_response}}, 'description': 'The `load_balancer` key contains the updated Load Balancer'}}, 'tags': ['load_balancers'], 'operationId': 'replace_load_balancer', 'mime': 'application/json'}
            id = {'type': 'integer'}
            body = Defs.components_schemas_replace_load_balancer_request
        R.id = id
        R.body = Defs.components_schemas_replace_load_balancer_request

class load_balancers___id___actions:
    pth = "/load_balancers/{id}/actions"

    class get:
        """Returns all Action objects for a Load Balancer. You can sort the results by using the `sort` URI parameter, and filter them with the `status` parameter. Get all Actions for a Load Balancer"""
        class R:
            _query = ['sort', 'status', 'page', 'per_page']; _path = ['id'];
            _ = {'responses': {'200': {'content': {'application/json': {'example': {'actions': [{'command': 'add_service', 'error': {'code': 'action_failed', 'message': 'Action failed'}, 'finished': '2016-01-30T23:56:00+00:00', 'id': 13, 'progress': 100, 'resources': [{'id': 4711, 'type': 'load_balancer'}], 'started': '2016-01-30T23:55:00+00:00', 'status': 'success'}]}, 'schema': Defs.components_schemas_list_actions_for_load_balancer_response}}, 'description': 'The `actions` key contains a list of Actions'}}, 'tags': ['load_balancers'], 'operationId': 'list_actions_for_load_balancer'}
            id = {'type': 'integer'}
            sort = {'enum': ['id', 'id:asc', 'id:desc', 'command', 'command:asc', 'command:desc', 'status', 'status:asc', 'status:desc', 'progress', 'progress:asc', 'progress:desc', 'started', 'started:asc', 'started:desc', 'finished', 'finished:asc', 'finished:desc'], 'title': 'ParameterSort', 'type': 'string'}
            status = {'enum': ['running', 'success', 'error'], 'title': 'ParameterStatus', 'type': 'string'}
            page = {'type': 'integer', 'minimum': 1}
            per_page = {'type': 'integer', 'minimum': 1, 'maximum': 50}
        R.id = id
        R.sort = 'id'
        R.status = 'running'
        R.page = 0
        R.per_page = 0

class load_balancers___id___actions___action_id_:
    pth = "/load_balancers/{id}/actions/{action_id}"

    class get:
        """Returns a specific Action for a Load Balancer. Get an Action for a Load Balancer"""
        class R:
            _path = ['id', 'action_id'];
            _ = {'responses': {'200': {'content': {'application/json': {'example': {'action': {'command': 'change_protection', 'error': {'code': 'action_failed', 'message': 'Action failed'}, 'finished': '2016-01-30T23:56:00+00:00', 'id': 13, 'progress': 100, 'resources': [{'id': 4711, 'type': 'load_balancer'}], 'started': '2016-01-30T23:55:00+00:00', 'status': 'success'}}, 'schema': Defs.components_schemas_get_action_for_load_balancer_response}}, 'description': 'The `action` key contains the Load Balancer Action'}}, 'tags': ['load_balancers'], 'operationId': 'get_action_for_load_balancer'}
            id = {'type': 'integer'}
            action_id = {'type': 'integer'}
        R.id = id
        R.action_id = action_id

class load_balancers___id___actions__add_service:
    pth = "/load_balancers/{id}/actions/add_service"

    class post:
        """Adds a service to a Load Balancer.

#### Call specific error codes

| Code                       | Description                                             |
|----------------------------|---------------------------------------------------------|
| `source_port_already_used` | The source port you are trying to add is already in use |
 Add Service"""
        class R:
            _path = ['id']; _body = ['body'];
            _ = {'requestBody': {'content': {}}, 'responses': {'201': {'content': {'application/json': {'example': {'action': {'command': 'add_service', 'error': {'code': 'action_failed', 'message': 'Action failed'}, 'finished': '2016-01-30T23:56:00+00:00', 'id': 13, 'progress': 100, 'resources': [{'id': 4711, 'type': 'load_balancer'}], 'started': '2016-01-30T23:55:00+00:00', 'status': 'success'}}, 'schema': Defs.components_schemas_add_service_response}}, 'description': 'The `action` key contains the `add_service` Action'}}, 'tags': ['load_balancers'], 'operationId': 'add_service', 'mime': 'application/json'}
            id = {'type': 'integer'}
            body = Defs.components_schemas_add_service_request
        R.id = id
        R.body = Defs.components_schemas_add_service_request

class load_balancers___id___actions__add_target:
    pth = "/load_balancers/{id}/actions/add_target"

    class post:
        """Adds a target to a Load Balancer.

#### Call specific error codes

| Code                                    | Description                                                                                           |
|-----------------------------------------|-------------------------------------------------------------------------------------------------------|
| `cloud_resource_ip_not_allowed`         | The IP you are trying to add as a target belongs to a Hetzner Cloud resource                          |
| `ip_not_owned`                          | The IP you are trying to add as a target is not owned by the Project owner                            |
| `load_balancer_not_attached_to_network` | The Load Balancer is not attached to a network                                                        |
| `robot_unavailable`                     | Robot was not available. The caller may retry the operation after a short delay.                      |
| `server_not_attached_to_network`        | The server you are trying to add as a target is not attached to the same network as the Load Balancer |
| `target_already_defined`                | The Load Balancer target you are trying to define is already defined                                  |
 Add Target"""
        class R:
            _path = ['id']; _body = ['body'];
            _ = {'requestBody': {'content': {}}, 'responses': {'201': {'content': {'application/json': {'example': {'action': {'command': 'add_target', 'error': {'code': 'action_failed', 'message': 'Action failed'}, 'finished': '2016-01-30T23:56:00+00:00', 'id': 13, 'progress': 100, 'resources': [{'id': 4711, 'type': 'load_balancer'}], 'started': '2016-01-30T23:55:00+00:00', 'status': 'success'}}, 'schema': Defs.components_schemas_add_target_response}}, 'description': 'The `action` key contains the `add_target` Action'}}, 'tags': ['load_balancers'], 'operationId': 'add_target', 'mime': 'application/json'}
            id = {'type': 'integer'}
            body = Defs.components_schemas_add_target_request
        R.id = id
        R.body = Defs.components_schemas_add_target_request

class load_balancers___id___actions__attach_to_network:
    pth = "/load_balancers/{id}/actions/attach_to_network"

    class post:
        """Attach a Load Balancer to a Network.

**Call specific error codes**

| Code                             | Description                                                           |
|----------------------------------|-----------------------------------------------------------------------|
| `load_balancer_already_attached` | The Load Balancer is already attached to a network                    |
| `ip_not_available`               | The provided Network IP is not available                              |
| `no_subnet_available`            | No Subnet or IP is available for the Load Balancer within the network |
 Attach a Load Balancer to a Network"""
        class R:
            _path = ['id']; _body = ['body'];
            _ = {'requestBody': {'content': {}}, 'responses': {'201': {'content': {'application/json': {'example': {'action': {'command': 'attach_to_network', 'error': {'code': 'action_failed', 'message': 'Action failed'}, 'finished': '2016-01-30T23:56:00+00:00', 'id': 13, 'progress': 100, 'resources': [{'id': 4711, 'type': 'load_balancer'}], 'started': '2016-01-30T23:55:00+00:00', 'status': 'success'}}, 'schema': Defs.components_schemas_attach_load_balancer_to_network_response}}, 'description': 'The `action` key contains the `attach_to_network` Action'}}, 'tags': ['load_balancers'], 'operationId': 'attach_load_balancer_to_network', 'mime': 'application/json'}
            id = {'type': 'integer'}
            body = Defs.components_schemas_attach_load_balancer_to_network_request
        R.id = id
        R.body = Defs.components_schemas_attach_load_balancer_to_network_request

class load_balancers___id___actions__change_algorithm:
    pth = "/load_balancers/{id}/actions/change_algorithm"

    class post:
        """Change the algorithm that determines to which target new requests are sent. Change Algorithm"""
        class R:
            _path = ['id']; _body = ['body'];
            _ = {'requestBody': {'content': {}}, 'responses': {'201': {'content': {'application/json': {'example': {'action': {'command': 'change_algorithm', 'error': {'code': 'action_failed', 'message': 'Action failed'}, 'finished': '2016-01-30T23:56:00+00:00', 'id': 13, 'progress': 100, 'resources': [{'id': 4711, 'type': 'load_balancer'}], 'started': '2016-01-30T23:55:00+00:00', 'status': 'success'}}, 'schema': Defs.components_schemas_change_algorithm_response}}, 'description': 'The `action` key contains the `change_algorithm` Action'}}, 'tags': ['load_balancers'], 'operationId': 'change_algorithm', 'mime': 'application/json'}
            id = {'type': 'integer'}
            body = Defs.components_schemas_change_algorithm_request
        R.id = id
        R.body = Defs.components_schemas_change_algorithm_request

class load_balancers___id___actions__change_dns_ptr:
    pth = "/load_balancers/{id}/actions/change_dns_ptr"

    class post:
        """Changes the hostname that will appear when getting the hostname belonging to the public IPs (IPv4 and IPv6) of this Load Balancer.

Floating IPs assigned to the Server are not affected by this.
 Change reverse DNS entry for this Load Balancer"""
        class R:
            _path = ['id']; _body = ['body'];
            _ = {'requestBody': {'content': {}, 'description': 'Select the IP address for which to change the DNS entry by passing `ip`. It can be either IPv4 or IPv6. The target hostname is set by passing `dns_ptr`.'}, 'responses': {'201': {'content': {'application/json': {'example': {'action': {'command': 'change_dns_ptr', 'error': {'code': 'action_failed', 'message': 'Action failed'}, 'finished': None, 'id': 13, 'progress': 0, 'resources': [{'id': 42, 'type': 'load_balancer'}], 'started': '2016-01-30T23:50:00+00:00', 'status': 'running'}}, 'schema': Defs.components_schemas_change_reverse_dns_entry_for_this_load_balancer_response}}, 'description': 'The `action` key in the reply contains an Action object with this structure'}}, 'tags': ['load_balancers'], 'operationId': 'change_reverse_dns_entry_for_this_load_balancer', 'mime': 'application/json'}
            id = {'type': 'integer'}
            body = Defs.components_schemas_change_reverse_dns_entry_for_this_load_balancer_request
        R.id = id
        R.body = Defs.components_schemas_change_reverse_dns_entry_for_this_load_balancer_request

class load_balancers___id___actions__change_protection:
    pth = "/load_balancers/{id}/actions/change_protection"

    class post:
        """Changes the protection configuration of a Load Balancer. Change Load Balancer Protection"""
        class R:
            _path = ['id']; _body = ['body'];
            _ = {'requestBody': {'content': {}}, 'responses': {'201': {'content': {'application/json': {'example': {'action': {'command': 'change_protection', 'error': {'code': 'action_failed', 'message': 'Action failed'}, 'finished': '2016-01-30T23:56:00+00:00', 'id': 13, 'progress': 100, 'resources': [{'id': 4711, 'type': 'load_balancer'}], 'started': '2016-01-30T23:55:00+00:00', 'status': 'success'}}, 'schema': Defs.components_schemas_change_load_balancer_protection_response}}, 'description': 'The `action` key contains the `change_protection` Action'}}, 'tags': ['load_balancers'], 'operationId': 'change_load_balancer_protection', 'mime': 'application/json'}
            id = {'type': 'integer'}
            body = Defs.components_schemas_change_load_balancer_protection_request
        R.id = id
        R.body = Defs.components_schemas_change_load_balancer_protection_request

class load_balancers___id___actions__change_type:
    pth = "/load_balancers/{id}/actions/change_type"

    class post:
        """Changes the type (Max Services, Max Targets and Max Connections) of a Load Balancer.

**Call specific error codes**

| Code                         | Description                                                     |
|------------------------------|-----------------------------------------------------------------|
| `invalid_load_balancer_type` | The Load Balancer type does not fit for the given Load Balancer |
 Change the Type of a Load Balancer"""
        class R:
            _path = ['id']; _body = ['body'];
            _ = {'requestBody': {'content': {}}, 'responses': {'201': {'content': {'application/json': {'example': {'action': {'command': 'change_load_balancer_type', 'error': {'code': 'action_failed', 'message': 'Action failed'}, 'finished': None, 'id': 13, 'progress': 0, 'resources': [{'id': 42, 'type': 'server'}], 'started': '2016-01-30T23:50:00+00:00', 'status': 'running'}}, 'schema': Defs.components_schemas_change_type_of_load_balancer_response}}, 'description': 'The `action` key contains the `change_load_balancer_type` Action'}}, 'tags': ['load_balancers'], 'operationId': 'change_type_of_load_balancer', 'mime': 'application/json'}
            id = {'type': 'integer'}
            body = Defs.components_schemas_change_type_of_load_balancer_request
        R.id = id
        R.body = Defs.components_schemas_change_type_of_load_balancer_request

class load_balancers___id___actions__delete_service:
    pth = "/load_balancers/{id}/actions/delete_service"

    class post:
        """Delete a service of a Load Balancer. Delete Service"""
        class R:
            _path = ['id']; _body = ['body'];
            _ = {'requestBody': {'content': {}}, 'responses': {'201': {'content': {'application/json': {'example': {'action': {'command': 'delete_service', 'error': {'code': 'action_failed', 'message': 'Action failed'}, 'finished': '2016-01-30T23:56:00+00:00', 'id': 13, 'progress': 100, 'resources': [{'id': 4711, 'type': 'load_balancer'}], 'started': '2016-01-30T23:55:00+00:00', 'status': 'success'}}, 'schema': Defs.components_schemas_delete_service_response}}, 'description': 'The `action` key contains the `delete_service` Action'}}, 'tags': ['load_balancers'], 'operationId': 'delete_service', 'mime': 'application/json'}
            id = {'type': 'integer'}
            body = Defs.components_schemas_delete_service_request
        R.id = id
        R.body = Defs.components_schemas_delete_service_request

class load_balancers___id___actions__detach_from_network:
    pth = "/load_balancers/{id}/actions/detach_from_network"

    class post:
        """Detaches a Load Balancer from a network. Detach a Load Balancer from a Network"""
        class R:
            _path = ['id']; _body = ['body'];
            _ = {'requestBody': {'content': {}}, 'responses': {'201': {'content': {'application/json': {'example': {'action': {'command': 'detach_from_network', 'error': {'code': 'action_failed', 'message': 'Action failed'}, 'finished': None, 'id': 13, 'progress': 0, 'resources': [{'id': 42, 'type': 'server'}, {'id': 4711, 'type': 'network'}], 'started': '2016-01-30T23:50:00+00:00', 'status': 'running'}}, 'schema': Defs.components_schemas_detach_load_balancer_from_network_response}}, 'description': 'The `action` key contains the `detach_from_network` Action'}}, 'tags': ['load_balancers'], 'operationId': 'detach_load_balancer_from_network', 'mime': 'application/json'}
            id = {'type': 'integer'}
            body = Defs.components_schemas_detach_load_balancer_from_network_request
        R.id = id
        R.body = Defs.components_schemas_detach_load_balancer_from_network_request

class load_balancers___id___actions__disable_public_interface:
    pth = "/load_balancers/{id}/actions/disable_public_interface"

    class post:
        """Disable the public interface of a Load Balancer. The Load Balancer will be not accessible from the internet via its public IPs.

#### Call specific error codes

| Code                                      | Description                                                                    |
|-------------------------------------------|--------------------------------------------------------------------------------|
| `load_balancer_not_attached_to_network`   |  The Load Balancer is not attached to a network                                |
| `targets_without_use_private_ip`          | The Load Balancer has targets that use the public IP instead of the private IP |
 Disable the public interface of a Load Balancer"""
        class R:
            _path = ['id'];
            _ = {'responses': {'201': {'content': {'application/json': {'example': {'action': {'command': 'disable_public_interface', 'error': {'code': 'action_failed', 'message': 'Action failed'}, 'finished': None, 'id': 13, 'progress': 0, 'resources': [{'id': 42, 'type': 'server'}, {'id': 4711, 'type': 'network'}], 'started': '2016-01-30T23:50:00+00:00', 'status': 'running'}}, 'schema': Defs.components_schemas_disable_public_interface_of_load_balancer_response}}, 'description': 'The `action` key contains the `disable_public_interface` Action'}}, 'tags': ['load_balancers'], 'operationId': 'disable_public_interface_of_load_balancer'}
            id = {'type': 'integer'}
        R.id = id

class load_balancers___id___actions__enable_public_interface:
    pth = "/load_balancers/{id}/actions/enable_public_interface"

    class post:
        """Enable the public interface of a Load Balancer. The Load Balancer will be accessible from the internet via its public IPs. Enable the public interface of a Load Balancer"""
        class R:
            _path = ['id'];
            _ = {'responses': {'201': {'content': {'application/json': {'example': {'action': {'command': 'enable_public_interface', 'error': {'code': 'action_failed', 'message': 'Action failed'}, 'finished': None, 'id': 13, 'progress': 0, 'resources': [{'id': 42, 'type': 'server'}, {'id': 4711, 'type': 'network'}], 'started': '2016-01-30T23:50:00+00:00', 'status': 'running'}}, 'schema': Defs.components_schemas_enable_public_interface_of_load_balancer_response}}, 'description': 'The `action` key contains the `enable_public_interface` Action'}}, 'tags': ['load_balancers'], 'operationId': 'enable_public_interface_of_load_balancer'}
            id = {'type': 'integer'}
        R.id = id

class load_balancers___id___actions__remove_target:
    pth = "/load_balancers/{id}/actions/remove_target"

    class post:
        """Removes a target from a Load Balancer. Remove Target"""
        class R:
            _path = ['id']; _body = ['body'];
            _ = {'requestBody': {'content': {}}, 'responses': {'201': {'content': {'application/json': {'example': {'action': {'command': 'remove_target', 'error': {'code': 'action_failed', 'message': 'Action failed'}, 'finished': '2016-01-30T23:56:00+00:00', 'id': 13, 'progress': 100, 'resources': [{'id': 4711, 'type': 'load_balancer'}], 'started': '2016-01-30T23:55:00+00:00', 'status': 'success'}}, 'schema': Defs.components_schemas_remove_target_response}}, 'description': 'The `action` key contains the `remove_target` Action'}}, 'tags': ['load_balancers'], 'operationId': 'remove_target', 'mime': 'application/json'}
            id = {'type': 'integer'}
            body = Defs.components_schemas_remove_target_request
        R.id = id
        R.body = Defs.components_schemas_remove_target_request

class load_balancers___id___actions__update_service:
    pth = "/load_balancers/{id}/actions/update_service"

    class post:
        """Updates a Load Balancer Service.

#### Call specific error codes

| Code                       | Description                                             |
|----------------------------|---------------------------------------------------------|
| `source_port_already_used` | The source port you are trying to add is already in use |
 Update Service"""
        class R:
            _path = ['id']; _body = ['body'];
            _ = {'requestBody': {'content': {}}, 'responses': {'201': {'content': {'application/json': {'example': {'action': {'command': 'update_service', 'error': {'code': 'action_failed', 'message': 'Action failed'}, 'finished': '2016-01-30T23:56:00+00:00', 'id': 13, 'progress': 100, 'resources': [{'id': 4711, 'type': 'load_balancer'}], 'started': '2016-01-30T23:55:00+00:00', 'status': 'success'}}, 'schema': Defs.components_schemas_update_service_response}}, 'description': 'The `action` key contains the `update_service` Action'}}, 'tags': ['load_balancers'], 'operationId': 'update_service', 'mime': 'application/json'}
            id = {'type': 'integer'}
            body = Defs.components_schemas_update_service_request
        R.id = id
        R.body = Defs.components_schemas_update_service_request

class load_balancers___id___metrics:
    pth = "/load_balancers/{id}/metrics"

    class get:
        """You must specify the type of metric to get: `open_connections`, `connections_per_second`, `requests_per_second` or `bandwidth`. You can also specify more than one type by comma separation, e.g. `requests_per_second,bandwidth`.

Depending on the type you will get different time series data:

|Type | Timeseries | Unit | Description |
|---- |------------|------|-------------|
| open_connections | open_connections | number | Open connections |
| connections_per_second | connections_per_second | connections/s | Connections per second |
| requests_per_second | requests_per_second | requests/s | Requests per second |
| bandwidth | bandwidth.in | bytes/s | Ingress bandwidth |
|| bandwidth.out | bytes/s | Egress bandwidth |

Metrics are available for the last 30 days only.

If you do not provide the step argument we will automatically adjust it so that 200 samples are returned.

We limit the number of samples to a maximum of 500 and will adjust the step parameter accordingly.
 Get Metrics for a LoadBalancer"""
        class R:
            _query = ['type', 'start', 'end', 'step']; _path = ['id'];
            _ = {'responses': {'200': {'content': {'application/json': {'schema': Defs.components_schemas_get_metrics_for_loadbalancer_response}}, 'description': 'The `metrics` key in the reply contains a metrics object with this structure'}}, 'tags': ['load_balancers'], 'operationId': 'get_metrics_for_loadbalancer'}
            id = {'type': 'integer'}
            type = {'enum': ['open_connections', 'connections_per_second', 'requests_per_second', 'bandwidth'], 'type': 'string'}
            start = {'type': 'string'}
            end = {'type': 'string'}
            step = {'type': 'string'}
        R.id = id
        R.type = 'open_connections'
        R.start = str_dflt
        R.end = str_dflt
        R.step = str_dflt

class locations:
    pth = "/locations"

    class get:
        """Returns all Location objects. Get all Locations"""
        class R:
            _query = ['name', 'page', 'per_page'];
            _ = {'responses': {'200': {'content': {'application/json': {'schema': Defs.components_schemas_list_locations_response}}, 'description': 'The `locations` key in the reply contains an array of Location objects with this structure'}}, 'tags': ['locations'], 'operationId': 'list_locations'}
            name = {'type': 'string'}
            page = {'type': 'integer', 'minimum': 1}
            per_page = {'type': 'integer', 'minimum': 1, 'maximum': 50}
        R.name = str_dflt
        R.page = 0
        R.per_page = 0

class locations___id_:
    pth = "/locations/{id}"

    class get:
        """Returns a specific Location object. Get a Location"""
        class R:
            _path = ['id'];
            _ = {'responses': {'200': {'content': {'application/json': {'schema': Defs.components_schemas_get_location_response}}, 'description': 'The `location` key in the reply contains a Location object with this structure'}}, 'tags': ['locations'], 'operationId': 'get_location'}
            id = {'type': 'integer'}
        R.id = id

class networks:
    pth = "/networks"

    class get:
        """Gets all existing networks that you have available. Get all Networks"""
        class R:
            _query = ['name', 'label_selector', 'page', 'per_page'];
            _ = {'responses': {'200': {'content': {'application/json': {'schema': Defs.components_schemas_list_networks_response}}, 'description': 'The `networks` key contains a list of networks'}}, 'tags': ['networks'], 'operationId': 'list_networks'}
            name = {'type': 'string'}
            label_selector = {'type': 'string'}
            page = {'type': 'integer', 'minimum': 1}
            per_page = {'type': 'integer', 'minimum': 1, 'maximum': 50}
        R.name = str_dflt
        R.label_selector = str_dflt
        R.page = 0
        R.per_page = 0

    class post:
        """Creates a network with the specified `ip_range`.

You may specify one or more `subnets`. You can also add more Subnets later by using the [add subnet action](https://docs.hetzner.cloud/#network-actions-add-a-subnet-to-a-network). If you do not specify an `ip_range` in the subnet we will automatically pick the first available /24 range for you.

You may specify one or more routes in `routes`. You can also add more routes later by using the [add route action](https://docs.hetzner.cloud/#network-actions-add-a-route-to-a-network).
 Create a Network"""
        class R:
            _body = ['body'];
            _ = {'requestBody': {'content': {}}, 'responses': {'201': {'content': {'application/json': {'schema': Defs.components_schemas_create_network_response}}, 'description': 'The `network` key contains the network that was just created'}}, 'tags': ['networks'], 'operationId': 'create_network', 'mime': 'application/json'}
            body = Defs.components_schemas_create_network_request
        R.body = Defs.components_schemas_create_network_request

class networks___id_:
    pth = "/networks/{id}"

    class delete:
        """Deletes a network. If there are Servers attached they will be detached in the background.

Note: if the network object changes during the request, the response will be a “conflict” error.
 Delete a Network"""
        class R:
            _path = ['id'];
            _ = {'responses': {'204': {'description': 'Network deleted'}}, 'tags': ['networks'], 'operationId': 'delete_network'}
            id = {'type': 'integer'}
        R.id = id

    class get:
        """Gets a specific network object. Get a Network"""
        class R:
            _path = ['id'];
            _ = {'responses': {'200': {'content': {'application/json': {'schema': Defs.components_schemas_get_network_response}}, 'description': 'The `network` key contains the network'}}, 'tags': ['networks'], 'operationId': 'get_network'}
            id = {'type': 'integer'}
        R.id = id

    class put:
        """Updates the network properties.

Note that when updating labels, the network’s current set of labels will be replaced with the labels provided in the request body. So, for example, if you want to add a new label, you have to provide all existing labels plus the new label in the request body.

Note: if the network object changes during the request, the response will be a “conflict” error.
 Update a Network"""
        class R:
            _path = ['id']; _body = ['body'];
            _ = {'requestBody': {'content': {}}, 'responses': {'200': {'content': {'application/json': {'example': {'network': {'created': '2016-01-30T23:50:00+00:00', 'id': 4711, 'ip_range': '10.0.0.0/16', 'labels': {'labelkey': 'value'}, 'load_balancers': [42], 'name': 'new-name', 'protection': {'delete': False}, 'routes': [{'destination': '10.100.1.0/24', 'gateway': '10.0.1.1'}], 'servers': [42], 'subnets': [{'gateway': '10.0.0.1', 'ip_range': '10.0.1.0/24', 'network_zone': 'eu-central', 'type': 'cloud'}]}}, 'schema': Defs.components_schemas_replace_network_response}}, 'description': 'The `network` key contains the updated network'}}, 'tags': ['networks'], 'operationId': 'replace_network', 'mime': 'application/json'}
            id = {'type': 'integer'}
            body = Defs.components_schemas_replace_network_request
        R.id = id
        R.body = Defs.components_schemas_replace_network_request

class networks___id___actions:
    pth = "/networks/{id}/actions"

    class get:
        """Returns all Action objects for a Network. You can sort the results by using the `sort` URI parameter, and filter them with the `status` parameter. Get all Actions for a Network"""
        class R:
            _query = ['sort', 'status', 'page', 'per_page']; _path = ['id'];
            _ = {'responses': {'200': {'content': {'application/json': {'example': {'actions': [{'command': 'add_subnet', 'error': {'code': 'action_failed', 'message': 'Action failed'}, 'finished': '2016-01-30T23:56:00+00:00', 'id': 13, 'progress': 100, 'resources': [{'id': 42, 'type': 'server'}], 'started': '2016-01-30T23:55:00+00:00', 'status': 'success'}]}, 'schema': Defs.components_schemas_list_actions_for_network_response}}, 'description': 'The `actions` key contains a list of Actions'}}, 'tags': ['networks'], 'operationId': 'list_actions_for_network'}
            id = {'type': 'integer'}
            sort = {'enum': ['id', 'id:asc', 'id:desc', 'command', 'command:asc', 'command:desc', 'status', 'status:asc', 'status:desc', 'progress', 'progress:asc', 'progress:desc', 'started', 'started:asc', 'started:desc', 'finished', 'finished:asc', 'finished:desc'], 'title': 'ParameterSort', 'type': 'string'}
            status = {'enum': ['running', 'success', 'error'], 'title': 'ParameterStatus', 'type': 'string'}
            page = {'type': 'integer', 'minimum': 1}
            per_page = {'type': 'integer', 'minimum': 1, 'maximum': 50}
        R.id = id
        R.sort = 'id'
        R.status = 'running'
        R.page = 0
        R.per_page = 0

class networks___id___actions___action_id_:
    pth = "/networks/{id}/actions/{action_id}"

    class get:
        """Returns a specific Action for a Network. Get an Action for a Network"""
        class R:
            _path = ['id', 'action_id'];
            _ = {'responses': {'200': {'content': {'application/json': {'example': {'action': {'command': 'add_subnet', 'error': {'code': 'action_failed', 'message': 'Action failed'}, 'finished': '2016-01-30T23:56:00+00:00', 'id': 13, 'progress': 100, 'resources': [{'id': 4711, 'type': 'network'}], 'started': '2016-01-30T23:55:00+00:00', 'status': 'success'}}, 'schema': Defs.components_schemas_get_action_for_network_response}}, 'description': 'The `action` key contains the Network Action'}}, 'tags': ['networks'], 'operationId': 'get_action_for_network'}
            id = {'type': 'integer'}
            action_id = {'type': 'integer'}
        R.id = id
        R.action_id = action_id

class networks___id___actions__add_route:
    pth = "/networks/{id}/actions/add_route"

    class post:
        """Adds a route entry to a Network.

Note: if the Network object changes during the request, the response will be a “conflict” error.
 Add a route to a Network"""
        class R:
            _path = ['id']; _body = ['body'];
            _ = {'requestBody': {'content': {}}, 'responses': {'201': {'content': {'application/json': {'example': {'action': {'command': 'add_route', 'error': {'code': 'action_failed', 'message': 'Action failed'}, 'finished': None, 'id': 13, 'progress': 0, 'resources': [{'id': 4711, 'type': 'network'}], 'started': '2016-01-30T23:50:00+00:00', 'status': 'running'}}, 'schema': Defs.components_schemas_add_route_to_network_response}}, 'description': 'The `action` key contains the `add_route` Action'}}, 'tags': ['networks'], 'operationId': 'add_route_to_network', 'mime': 'application/json'}
            id = {'type': 'integer'}
            body = Defs.components_schemas_add_route_to_network_request
        R.id = id
        R.body = Defs.components_schemas_add_route_to_network_request

class networks___id___actions__add_subnet:
    pth = "/networks/{id}/actions/add_subnet"

    class post:
        """Adds a new subnet object to the Network. If you do not specify an `ip_range` for the subnet we will automatically pick the first available /24 range for you if possible.

Note: if the parent Network object changes during the request, the response will be a “conflict” error.
 Add a subnet to a Network"""
        class R:
            _path = ['id']; _body = ['body'];
            _ = {'requestBody': {'content': {}}, 'responses': {'201': {'content': {'application/json': {'example': {'action': {'command': 'add_subnet', 'error': {'code': 'action_failed', 'message': 'Action failed'}, 'finished': None, 'id': 13, 'progress': 0, 'resources': [{'id': 4711, 'type': 'network'}], 'started': '2016-01-30T23:50:00+00:00', 'status': 'running'}}, 'schema': Defs.components_schemas_add_subnet_to_network_response}}, 'description': 'The `action` key contains the `add_subnet` Action'}}, 'tags': ['networks'], 'operationId': 'add_subnet_to_network', 'mime': 'application/json'}
            id = {'type': 'integer'}
            body = Defs.components_schemas_add_subnet_to_network_request
        R.id = id
        R.body = Defs.components_schemas_add_subnet_to_network_request

class networks___id___actions__change_ip_range:
    pth = "/networks/{id}/actions/change_ip_range"

    class post:
        """Changes the IP range of a Network. IP ranges can only be extended and never shrunk. You can only add IPs at the end of an existing IP range. This means that the IP part of your existing range must stay the same and you can only change its netmask.

For example if you have a range `10.0.0.0/16` you want to extend then your new range must also start with the IP `10.0.0.0`. Your CIDR netmask `/16` may change to a number that is smaller than `16` thereby increasing the IP range. So valid entries would be `10.0.0.0/15`, `10.0.0.0/14`, `10.0.0.0/13` and so on.

After changing the IP range you will have to adjust the routes on your connected Servers by either rebooting them or manually changing the routes to your private Network interface.

Note: if the Network object changes during the request, the response will be a “conflict” error.
 Change IP range of a Network"""
        class R:
            _path = ['id']; _body = ['body'];
            _ = {'requestBody': {'content': {}}, 'responses': {'201': {'content': {'application/json': {'example': {'action': {'command': 'change_ip_range', 'error': {'code': 'action_failed', 'message': 'Action failed'}, 'finished': '2016-01-30T23:56:00+00:00', 'id': 13, 'progress': 100, 'resources': [{'id': 4711, 'type': 'network'}], 'started': '2016-01-30T23:55:00+00:00', 'status': 'success'}}, 'schema': Defs.components_schemas_change_ip_range_of_network_response}}, 'description': 'The `action` key contains the `change_ip_range` Action'}}, 'tags': ['networks'], 'operationId': 'change_ip_range_of_network', 'mime': 'application/json'}
            id = {'type': 'integer'}
            body = Defs.components_schemas_change_ip_range_of_network_request
        R.id = id
        R.body = Defs.components_schemas_change_ip_range_of_network_request

class networks___id___actions__change_protection:
    pth = "/networks/{id}/actions/change_protection"

    class post:
        """Changes the protection configuration of a Network.

Note: if the Network object changes during the request, the response will be a “conflict” error.
 Change Network Protection"""
        class R:
            _path = ['id']; _body = ['body'];
            _ = {'requestBody': {'content': {}}, 'responses': {'201': {'content': {'application/json': {'example': {'action': {'command': 'change_protection', 'error': {'code': 'action_failed', 'message': 'Action failed'}, 'finished': '2016-01-30T23:56:00+00:00', 'id': 13, 'progress': 100, 'resources': [{'id': 4711, 'type': 'network'}], 'started': '2016-01-30T23:55:00+00:00', 'status': 'success'}}, 'schema': Defs.components_schemas_change_network_protection_response}}, 'description': 'The `action` key contains the `change_protection` Action'}}, 'tags': ['networks'], 'operationId': 'change_network_protection', 'mime': 'application/json'}
            id = {'type': 'integer'}
            body = Defs.components_schemas_change_network_protection_request
        R.id = id
        R.body = Defs.components_schemas_change_network_protection_request

class networks___id___actions__delete_route:
    pth = "/networks/{id}/actions/delete_route"

    class post:
        """Delete a route entry from a Network.

Note: if the Network object changes during the request, the response will be a “conflict” error.
 Delete a route from a Network"""
        class R:
            _path = ['id']; _body = ['body'];
            _ = {'requestBody': {'content': {}}, 'responses': {'201': {'content': {'application/json': {'example': {'action': {'command': 'delete_route', 'error': {'code': 'action_failed', 'message': 'Action failed'}, 'finished': None, 'id': 13, 'progress': 0, 'resources': [{'id': 4711, 'type': 'network'}], 'started': '2016-01-30T23:50:00+00:00', 'status': 'running'}}, 'schema': Defs.components_schemas_delete_route_from_network_response}}, 'description': 'The `action` key contains the `delete_route` Action'}}, 'tags': ['networks'], 'operationId': 'delete_route_from_network', 'mime': 'application/json'}
            id = {'type': 'integer'}
            body = Defs.components_schemas_delete_route_from_network_request
        R.id = id
        R.body = Defs.components_schemas_delete_route_from_network_request

class networks___id___actions__delete_subnet:
    pth = "/networks/{id}/actions/delete_subnet"

    class post:
        """Deletes a single subnet entry from a Network. You cannot delete subnets which still have Servers attached. If you have Servers attached you first need to detach all Servers that use IPs from this subnet before you can delete the subnet.

Note: if the Network object changes during the request, the response will be a “conflict” error.
 Delete a subnet from a Network"""
        class R:
            _path = ['id']; _body = ['body'];
            _ = {'requestBody': {'content': {}}, 'responses': {'201': {'content': {'application/json': {'example': {'action': {'command': 'delete_subnet', 'error': {'code': 'action_failed', 'message': 'Action failed'}, 'finished': None, 'id': 13, 'progress': 0, 'resources': [{'id': 4711, 'type': 'network'}], 'started': '2016-01-30T23:50:00+00:00', 'status': 'running'}}, 'schema': Defs.components_schemas_delete_subnet_from_network_response}}, 'description': 'The `action` key contains the `delete_subnet` Action'}}, 'tags': ['networks'], 'operationId': 'delete_subnet_from_network', 'mime': 'application/json'}
            id = {'type': 'integer'}
            body = Defs.components_schemas_delete_subnet_from_network_request
        R.id = id
        R.body = Defs.components_schemas_delete_subnet_from_network_request

class placement_groups:
    pth = "/placement_groups"

    class get:
        """Returns all PlacementGroup objects. Get all PlacementGroups"""
        class R:
            _query = ['sort', 'name', 'label_selector', 'type', 'page', 'per_page'];
            _ = {'responses': {'200': {'content': {'application/json': {'example': {'placement_groups': [{'created': '2019-01-08T12:10:00+00:00', 'id': 897, 'labels': {'key': 'value'}, 'name': 'my Placement Group', 'servers': [4711, 4712], 'type': 'spread'}]}, 'schema': Defs.components_schemas_list_placementgroups_response}}, 'description': 'The `placement_groups` key contains an array of PlacementGroup objects'}}, 'tags': ['placement_groups'], 'operationId': 'list_placementgroups'}
            sort = {'enum': ['id', 'id:asc', 'id:desc', 'name', 'name:asc', 'name:desc', 'created', 'created:asc', 'created:desc'], 'type': 'string'}
            name = {'type': 'string'}
            label_selector = {'type': 'string'}
            type = {'enum': ['spread'], 'title': 'ParameterType', 'type': 'string'}
            page = {'type': 'integer', 'minimum': 1}
            per_page = {'type': 'integer', 'minimum': 1, 'maximum': 50}
        R.sort = 'id'
        R.name = str_dflt
        R.label_selector = str_dflt
        R.type = 'spread'
        R.page = 0
        R.per_page = 0

    class post:
        """Creates a new PlacementGroup.
 Create a PlacementGroup"""
        class R:
            _body = ['body'];
            _ = {'requestBody': {'content': {}}, 'responses': {'201': {'content': {'application/json': {'examples': {'spread': {'summary': 'Response when creating a type `spread` PlacementGroup', 'value': {'placement_group': {'created': '2019-01-08T12:10:00+00:00', 'id': 897, 'labels': {'key': 'value'}, 'name': 'my Placement Group', 'servers': [], 'type': 'spread'}}}}, 'schema': Defs.components_schemas_create_placementgroup_response}}, 'description': 'The `PlacementGroup` key contains the PlacementGroup that was just created.'}}, 'tags': ['placement_groups'], 'operationId': 'create_placementgroup', 'mime': 'application/json'}
            body = Defs.components_schemas_create_placementgroup_request
        R.body = Defs.components_schemas_create_placementgroup_request

class placement_groups___id_:
    pth = "/placement_groups/{id}"

    class delete:
        """Deletes a PlacementGroup. Delete a PlacementGroup"""
        class R:
            _path = ['id'];
            _ = {'responses': {'204': {'description': 'PlacementGroup deleted'}}, 'tags': ['placement_groups'], 'operationId': 'delete_placementgroup'}
            id = {'type': 'integer'}
        R.id = id

    class get:
        """Gets a specific PlacementGroup object. Get a PlacementGroup"""
        class R:
            _path = ['id'];
            _ = {'responses': {'200': {'content': {'application/json': {'example': {'placement_group': {'created': '2019-01-08T12:10:00+00:00', 'id': 897, 'labels': {'key': 'value'}, 'name': 'my Placement Group', 'servers': [4711, 4712], 'type': 'spread'}}, 'schema': Defs.components_schemas_get_placementgroup_response}}, 'description': 'The `placement_group` key contains a PlacementGroup object'}}, 'tags': ['placement_groups'], 'operationId': 'get_placementgroup'}
            id = {'type': 'integer'}
        R.id = id

    class put:
        """Updates the PlacementGroup properties.

Note that when updating labels, the PlacementGroup’s current set of labels will be replaced with the labels provided in the request body. So, for example, if you want to add a new label, you have to provide all existing labels plus the new label in the request body.

Note: if the PlacementGroup object changes during the request, the response will be a “conflict” error.
 Update a PlacementGroup"""
        class R:
            _path = ['id']; _body = ['body'];
            _ = {'requestBody': {'content': {}}, 'responses': {'200': {'content': {'application/json': {'example': {'placement_group': {'created': '2019-01-08T12:10:00+00:00', 'id': 897, 'labels': {'key': 'value'}, 'name': 'my Placement Group', 'servers': [4711, 4712], 'type': 'spread'}}, 'schema': Defs.components_schemas_replace_placementgroup_response}}, 'description': 'The `certificate` key contains the PlacementGroup that was just updated'}}, 'tags': ['placement_groups'], 'operationId': 'replace_placementgroup', 'mime': 'application/json'}
            id = {'type': 'integer'}
            body = Defs.components_schemas_replace_placementgroup_request
        R.id = id
        R.body = Defs.components_schemas_replace_placementgroup_request

class pricing:
    pth = "/pricing"

    class get:
        """Returns prices for all resources available on the platform. VAT and currency of the Project owner are used for calculations.

Both net and gross prices are included in the response.
 Get all prices"""
        class R:
            _ = {'responses': {'200': {'content': {'application/json': {'schema': Defs.components_schemas_list_prices_response}}, 'description': 'The `pricing` key in the reply contains an pricing object with this structure'}}, 'tags': ['pricing'], 'operationId': 'list_prices'}

class primary_ips:
    pth = "/primary_ips"

    class get:
        """Returns all Primary IP objects. Get all Primary IPs"""
        class R:
            _query = ['name', 'label_selector', 'ip', 'sort', 'page', 'per_page'];
            _ = {'responses': {'200': {'content': {'application/json': {'schema': Defs.components_schemas_list_primary_ips_response}}, 'description': 'The `primary_ips` key contains an array of Primary IP objects'}}, 'tags': ['primary_ips'], 'operationId': 'list_primary_ips'}
            name = {'type': 'string'}
            label_selector = {'type': 'string'}
            ip = {'type': 'string'}
            sort = {'enum': ['id', 'id:asc', 'id:desc', 'created', 'created:asc', 'created:desc'], 'type': 'string'}
            page = {'type': 'integer', 'minimum': 1}
            per_page = {'type': 'integer', 'minimum': 1, 'maximum': 50}
        R.name = str_dflt
        R.label_selector = str_dflt
        R.ip = str_dflt
        R.sort = 'id'
        R.page = 0
        R.per_page = 0

    class post:
        """Creates a new Primary IP, optionally assigned to a Server.

If you want to create a Primary IP that is not assigned to a Server, you need to provide the `datacenter` key instead of `assignee_id`. This can be either the ID or the name of the Datacenter this Primary IP shall be created in.

Note that a Primary IP can only be assigned to a Server in the same Datacenter later on.

#### Call specific error codes

| Code                          | Description                                                   |
|------------------------------ |-------------------------------------------------------------- |
| `server_not_stopped`          | The specified server is running, but needs to be powered off  |
| `server_has_ipv4`             | The server already has an ipv4 address                        |
| `server_has_ipv6`             | The server already has an ipv6 address                        |
 Create a Primary IP"""
        class R:
            _body = ['body'];
            _ = {'requestBody': {'content': {}, 'description': 'The `type` argument is required while `datacenter` and `assignee_id` are mutually exclusive.'}, 'responses': {'201': {'content': {'application/json': {'example': {'action': {'command': 'create_primary_ip', 'error': {'code': 'action_failed', 'message': 'Action failed'}, 'finished': None, 'id': 13, 'progress': 0, 'resources': [{'id': 17, 'type': 'server'}], 'started': '2016-01-30T23:50:00+00:00', 'status': 'running'}, 'primary_ip': {'assignee_id': 17, 'assignee_type': 'server', 'auto_delete': True, 'blocked': False, 'created': '2016-01-30T23:50:00+00:00', 'datacenter': {'description': 'Falkenstein DC Park 8', 'id': 42, 'location': {'city': 'Falkenstein', 'country': 'DE', 'description': 'Falkenstein DC Park 1', 'id': 1, 'latitude': 50.47612, 'longitude': 12.370071, 'name': 'fsn1', 'network_zone': 'eu-central'}, 'name': 'fsn1-dc8', 'server_types': {'available': [1, 2, 3], 'available_for_migration': [1, 2, 3], 'supported': [1, 2, 3]}}, 'dns_ptr': [{'dns_ptr': 'server.example.com', 'ip': '2001:db8::1'}], 'id': 42, 'ip': '131.232.99.1', 'labels': {'labelkey': 'value'}, 'name': 'my-ip', 'protection': {'delete': False}, 'type': 'ipv4'}}, 'schema': Defs.components_schemas_create_primary_ip_response}}, 'description': 'The `primary_ip` key contains the Primary IP that was just created'}}, 'tags': ['primary_ips'], 'operationId': 'create_primary_ip', 'mime': 'application/json'}
            body = Defs.components_schemas_create_primary_ip_request
        R.body = Defs.components_schemas_create_primary_ip_request

class primary_ips___id_:
    pth = "/primary_ips/{id}"

    class delete:
        """Deletes a Primary IP.

The Primary IP may be assigned to a Server. In this case it is unassigned automatically. The Server must be powered off (status `off`) in order for this operation to succeed.
 Delete a Primary IP"""
        class R:
            _path = ['id'];
            _ = {'responses': {'204': {'description': 'Primary IP deleted'}}, 'tags': ['primary_ips'], 'operationId': 'delete_primary_ip'}
            id = {'type': 'integer'}
        R.id = id

    class get:
        """Returns a specific Primary IP object. Get a Primary IP"""
        class R:
            _path = ['id'];
            _ = {'responses': {'200': {'content': {'application/json': {'schema': Defs.components_schemas_get_primary_ip_response}}, 'description': 'The `primary_ip` key contains a Primary IP object'}}, 'tags': ['primary_ips'], 'operationId': 'get_primary_ip'}
            id = {'type': 'integer'}
        R.id = id

    class put:
        """Updates the Primary IP.

Note that when updating labels, the Primary IP's current set of labels will be replaced with the labels provided in the request body. So, for example, if you want to add a new label, you have to provide all existing labels plus the new label in the request body.

If the Primary IP object changes during the request, the response will be a “conflict” error.
 Update a Primary IP"""
        class R:
            _path = ['id']; _body = ['body'];
            _ = {'requestBody': {'content': {}}, 'responses': {'200': {'content': {'application/json': {'schema': Defs.components_schemas_replace_primary_ip_response}}, 'description': 'The `primary_ip` key contains the Primary IP that was just updated'}}, 'tags': ['primary_ips'], 'operationId': 'replace_primary_ip', 'mime': 'application/json'}
            id = {'type': 'integer'}
            body = Defs.components_schemas_replace_primary_ip_request
        R.id = id
        R.body = Defs.components_schemas_replace_primary_ip_request

class primary_ips___id___actions__assign:
    pth = "/primary_ips/{id}/actions/assign"

    class post:
        """Assigns a Primary IP to a Server.

A Server can only have one Primary IP of type `ipv4` and one of type `ipv6` assigned. If you need more IPs use Floating IPs.

The Server must be powered off (status `off`) in order for this operation to succeed.

#### Call specific error codes

| Code                          | Description                                                   |
|------------------------------ |-------------------------------------------------------------- |
| `server_not_stopped`          | The server is running, but needs to be powered off            |
| `primary_ip_already_assigned` | Primary ip is already assigned to a different server          |
| `server_has_ipv4`             | The server already has an ipv4 address                        |
| `server_has_ipv6`             | The server already has an ipv6 address                        |
 Assign a Primary IP to a resource"""
        class R:
            _path = ['id']; _body = ['body'];
            _ = {'requestBody': {'content': {}}, 'responses': {'201': {'content': {'application/json': {'example': {'action': {'command': 'assign_primary_ip', 'error': {'code': 'action_failed', 'message': 'Action failed'}, 'finished': None, 'id': 13, 'progress': 0, 'resources': [{'id': 42, 'type': 'server'}, {'id': 4711, 'type': 'primary_ip'}], 'started': '2016-01-30T23:50:00+00:00', 'status': 'running'}}, 'schema': Defs.components_schemas_assign_primary_ip_to_resource_response}}, 'description': 'The `action` key in the reply contains an Action object with this structure'}}, 'tags': ['primary_ips'], 'operationId': 'assign_primary_ip_to_resource', 'mime': 'application/json'}
            id = {'type': 'integer'}
            body = Defs.components_schemas_assign_primary_ip_to_resource_request
        R.id = id
        R.body = Defs.components_schemas_assign_primary_ip_to_resource_request

class primary_ips___id___actions__change_dns_ptr:
    pth = "/primary_ips/{id}/actions/change_dns_ptr"

    class post:
        """Changes the hostname that will appear when getting the hostname belonging to this Primary IP. Change reverse DNS entry for a Primary IP"""
        class R:
            _path = ['id']; _body = ['body'];
            _ = {'requestBody': {'content': {}, 'description': 'Select the IP address for which to change the DNS entry by passing `ip`. For a Primary IP of type `ipv4` this must exactly match the IP address of the Primary IP. For a Primary IP of type `ipv6` this must be a single IP within the IPv6 /64 range that belongs to this Primary IP.\n\nThe target hostname is set by passing `dns_ptr`.\n'}, 'responses': {'201': {'content': {'application/json': {'example': {'action': {'command': 'change_dns_ptr', 'error': {'code': 'action_failed', 'message': 'Action failed'}, 'finished': '2016-01-30T23:56:00+00:00', 'id': 13, 'progress': 100, 'resources': [{'id': 4711, 'type': 'primary_ip'}], 'started': '2016-01-30T23:55:00+00:00', 'status': 'success'}}, 'schema': Defs.components_schemas_change_reverse_dns_entry_for_primary_ip_response}}, 'description': 'The `action` key contains the `change_dns_ptr` Action'}}, 'tags': ['primary_ips'], 'operationId': 'change_reverse_dns_entry_for_primary_ip', 'mime': 'application/json'}
            id = {'type': 'integer'}
            body = Defs.components_schemas_change_reverse_dns_entry_for_primary_ip_request
        R.id = id
        R.body = Defs.components_schemas_change_reverse_dns_entry_for_primary_ip_request

class primary_ips___id___actions__change_protection:
    pth = "/primary_ips/{id}/actions/change_protection"

    class post:
        """Changes the protection configuration of a Primary IP.

A Primary IP can only be delete protected if its `auto_delete` property is set to `false`.
 Change Primary IP Protection"""
        class R:
            _path = ['id']; _body = ['body'];
            _ = {'requestBody': {'content': {}}, 'responses': {'201': {'content': {'application/json': {'example': {'action': {'command': 'change_protection', 'error': {'code': 'action_failed', 'message': 'Action failed'}, 'finished': '2016-01-30T23:56:00+00:00', 'id': 13, 'progress': 100, 'resources': [{'id': 4711, 'type': 'primary_ip'}], 'started': '2016-01-30T23:55:00+00:00', 'status': 'success'}}, 'schema': Defs.components_schemas_change_primary_ip_protection_response}}, 'description': 'The `action` key contains the `change_protection` Action'}}, 'tags': ['primary_ips'], 'operationId': 'change_primary_ip_protection', 'mime': 'application/json'}
            id = {'type': 'integer'}
            body = Defs.components_schemas_change_primary_ip_protection_request
        R.id = id
        R.body = Defs.components_schemas_change_primary_ip_protection_request

class primary_ips___id___actions__unassign:
    pth = "/primary_ips/{id}/actions/unassign"

    class post:
        """Unassigns a Primary IP from a Server.

The Server must be powered off (status `off`) in order for this operation to succeed.

Note that only Servers that have at least one network interface (public or private) attached can be powered on.

#### Call specific error codes

| Code                              | Description                                                   |
|---------------------------------- |-------------------------------------------------------------- |
| `server_not_stopped`              | The server is running, but needs to be powered off            |
| `server_is_load_balancer_target`  | The server ipv4 address is a loadbalancer target              |
 Unassign a Primary IP from a resource"""
        class R:
            _path = ['id'];
            _ = {'responses': {'201': {'content': {'application/json': {'example': {'action': {'command': 'unassign_primary_ip', 'error': {'code': 'action_failed', 'message': 'Action failed'}, 'finished': None, 'id': 13, 'progress': 0, 'resources': [{'id': 42, 'type': 'server'}, {'id': 4711, 'type': 'primary_ip'}], 'started': '2016-01-30T23:50:00+00:00', 'status': 'running'}}, 'schema': Defs.components_schemas_unassign_primary_ip_from_resource_response}}, 'description': 'The `action` key in the reply contains an Action object with this structure'}}, 'tags': ['primary_ips'], 'operationId': 'unassign_primary_ip_from_resource'}
            id = {'type': 'integer'}
        R.id = id

class server_types:
    pth = "/server_types"

    class get:
        """Gets all Server type objects. Get all Server Types"""
        class R:
            _query = ['name', 'page', 'per_page'];
            _ = {'responses': {'200': {'content': {'application/json': {'schema': Defs.components_schemas_list_server_types_response}}, 'description': 'The `server_types` key in the reply contains an array of Server type objects with this structure'}}, 'tags': ['server_types'], 'operationId': 'list_server_types'}
            name = {'type': 'string'}
            page = {'type': 'integer', 'minimum': 1}
            per_page = {'type': 'integer', 'minimum': 1, 'maximum': 50}
        R.name = str_dflt
        R.page = 0
        R.per_page = 0

class server_types___id_:
    pth = "/server_types/{id}"

    class get:
        """Gets a specific Server type object. Get a Server Type"""
        class R:
            _path = ['id'];
            _ = {'responses': {'200': {'content': {'application/json': {'schema': Defs.components_schemas_get_server_type_response}}, 'description': 'The `server_type` key in the reply contains a Server type object with this structure'}}, 'tags': ['server_types'], 'operationId': 'get_server_type'}
            id = {'type': 'integer'}
        R.id = id

class servers:
    pth = "/servers"

    class get:
        """Returns all existing Server objects Get all Servers"""
        class R:
            _query = ['name', 'label_selector', 'sort', 'status', 'page', 'per_page'];
            _ = {'responses': {'200': {'content': {'application/json': {'schema': Defs.components_schemas_list_servers_response}}, 'description': 'A paged array of servers', 'headers': {'x-next': {'description': 'A link to the next page of responses', 'schema': {'type': 'string'}}}}}, 'tags': ['servers'], 'operationId': 'list_servers'}
            name = {'type': 'string'}
            label_selector = {'type': 'string'}
            sort = {'enum': ['id', 'id:asc', 'id:desc', 'name', 'name:asc', 'name:desc', 'created', 'created:asc', 'created:desc'], 'type': 'string'}
            status = {'enum': ['initializing', 'starting', 'running', 'stopping', 'off', 'deleting', 'rebuilding', 'migrating', 'unknown'], 'type': 'string'}
            page = {'type': 'integer', 'minimum': 1}
            per_page = {'type': 'integer', 'minimum': 1, 'maximum': 50}
        R.name = str_dflt
        R.label_selector = str_dflt
        R.sort = 'id'
        R.status = 'initializing'
        R.page = 0
        R.per_page = 0

    class post:
        """Creates a new Server. Returns preliminary information about the Server as well as an Action that covers progress of creation. Create a Server"""
        class R:
            _body = ['body'];
            _ = {'requestBody': {'content': {}, 'description': 'Please note that Server names must be unique per Project and valid hostnames as per RFC 1123 (i.e. may only contain letters, digits, periods, and dashes).\n\nFor `server_type` you can either use the ID as listed in `/server_types` or its name.\n\nFor `image` you can either use the ID as listed in `/images` or its name.\n\nIf you want to create the Server in a Location, you must set `location` to the ID or name as listed in `/locations`. This is the recommended way. You can be even more specific by setting `datacenter` to the ID or name as listed in `/datacenters`. However directly specifying the Datacenter is discouraged since supply availability in Datacenters varies greatly and Datacenters may be out of stock for extended periods of time or not serve certain Server types at all.\n\nSome properties like `start_after_create` or `automount` will trigger Actions after the Server is created. Those Actions are listed in the `next_actions` field in the response.\n\nFor accessing your Server we strongly recommend to use SSH keys by passing the respective key IDs in `ssh_keys`. If you do not specify any `ssh_keys` we will generate a root password for you and return it in the response.\n\nPlease note that provided user-data is stored in our systems. While we take measures to protect it we highly recommend that you don’t use it to store passwords or other sensitive information.\n\n#### Call specific error codes\n\n| Code                             | Description                                                |\n|----------------------------------|------------------------------------------------------------|\n| `placement_error`                | An error during the placement occurred                     |\n| `primary_ip_assigned`            | The specified Primary IP is already assigned to a server   |\n| `primary_ip_datacenter_mismatch` | The specified Primary IP is in a different datacenter      |\n| `primary_ip_version_mismatch`    | The specified Primary IP has the wrong IP Version          |\n'}, 'responses': {'201': {'content': {'application/json': {'example': {'action': {'command': 'create_server', 'error': {'code': 'action_failed', 'message': 'Action failed'}, 'finished': None, 'id': 1, 'progress': 0, 'resources': [{'id': 42, 'type': 'server'}], 'started': '2016-01-30T23:50:00+00:00', 'status': 'running'}, 'next_actions': [{'command': 'start_server', 'error': {'code': 'action_failed', 'message': 'Action failed'}, 'finished': None, 'id': 13, 'progress': 0, 'resources': [{'id': 42, 'type': 'server'}], 'started': '2016-01-30T23:50:00+00:00', 'status': 'running'}], 'root_password': 'YItygq1v3GYjjMomLaKc', 'server': {'backup_window': '22-02', 'created': '2016-01-30T23:50:00+00:00', 'datacenter': {'description': 'Falkenstein 1 DC 8', 'id': 1, 'location': {'city': 'Falkenstein', 'country': 'DE', 'description': 'Falkenstein DC Park 1', 'id': 1, 'latitude': 50.47612, 'longitude': 12.370071, 'name': 'fsn1', 'network_zone': 'eu-central'}, 'name': 'fsn1-dc8', 'server_types': {'available': [1, 2, 3], 'available_for_migration': [1, 2, 3], 'supported': [1, 2, 3]}}, 'id': 42, 'image': {'bound_to': None, 'created': '2016-01-30T23:50:00+00:00', 'created_from': {'id': 1, 'name': 'Server'}, 'deleted': None, 'deprecated': '2018-02-28T00:00:00+00:00', 'description': 'Ubuntu 20.04 Standard 64 bit', 'disk_size': 10, 'id': 4711, 'image_size': 2.3, 'labels': {'env': 'dev'}, 'name': 'ubuntu-20.04', 'os_flavor': 'ubuntu', 'os_version': '20.04', 'protection': {'delete': False}, 'rapid_deploy': False, 'status': 'available', 'type': 'snapshot'}, 'included_traffic': 654321, 'ingoing_traffic': 123456, 'iso': {'deprecated': '2018-02-28T00:00:00+00:00', 'description': 'FreeBSD 11.0 x64', 'id': 4711, 'name': 'FreeBSD-11.0-RELEASE-amd64-dvd1', 'type': 'public'}, 'labels': {'env': 'dev'}, 'load_balancers': [], 'locked': False, 'name': 'my-server', 'outgoing_traffic': 123456, 'primary_disk_size': 50, 'private_net': [{'alias_ips': [], 'ip': '10.0.0.2', 'mac_address': '86:00:ff:2a:7d:e1', 'network': 4711}], 'protection': {'delete': False, 'rebuild': False}, 'public_net': {'firewalls': [{'id': 38, 'status': 'applied'}], 'floating_ips': [478], 'ipv4': {'blocked': False, 'dns_ptr': 'server01.example.com', 'ip': '1.2.3.4'}, 'ipv6': {'blocked': False, 'dns_ptr': [{'dns_ptr': 'server.example.com', 'ip': '2001:db8::1'}], 'ip': '2001:db8::/64'}}, 'rescue_enabled': False, 'server_type': {'cores': 1, 'cpu_type': 'shared', 'deprecated': True, 'description': 'CX11', 'disk': 25, 'id': 1, 'memory': 1, 'name': 'cx11', 'prices': [{'location': 'fsn1', 'price_hourly': {'gross': '1.1900000000000000', 'net': '1.0000000000'}, 'price_monthly': {'gross': '1.1900000000000000', 'net': '1.0000000000'}}], 'storage_type': 'local'}, 'status': 'initializing', 'volumes': []}}, 'schema': Defs.components_schemas_create_server_response}}, 'description': 'The `server` key in the reply contains a Server object with this structure'}}, 'tags': ['servers'], 'operationId': 'create_server', 'mime': 'application/json'}
            body = Defs.components_schemas_create_server_request
        R.body = Defs.components_schemas_create_server_request

class servers___id_:
    pth = "/servers/{id}"

    class delete:
        """Deletes a Server. This immediately removes the Server from your account, and it is no longer accessible. Delete a Server"""
        class R:
            _path = ['id'];
            _ = {'responses': {'200': {'content': {'application/json': {'schema': Defs.components_schemas_delete_server_response}}, 'description': 'The `action` key in the reply contains an Action object with this structure'}}, 'tags': ['servers'], 'operationId': 'delete_server'}
            id = {'type': 'integer'}
        R.id = id

    class get:
        """Returns a specific Server object. The Server must exist inside the Project Get a Server"""
        class R:
            _path = ['id'];
            _ = {'responses': {'200': {'content': {'application/json': {'schema': Defs.components_schemas_get_server_response}}, 'description': 'The `server` key in the reply contains a Server object with this structure'}}, 'tags': ['servers'], 'operationId': 'get_server'}
            id = {'type': 'integer'}
        R.id = id

    class put:
        """Updates a Server. You can update a Server’s name and a Server’s labels.
Please note that Server names must be unique per Project and valid hostnames as per RFC 1123 (i.e. may only contain letters, digits, periods, and dashes).
Also note that when updating labels, the Server’s current set of labels will be replaced with the labels provided in the request body. So, for example, if you want to add a new label, you have to provide all existing labels plus the new label in the request body. Update a Server"""
        class R:
            _path = ['id']; _body = ['body'];
            _ = {'requestBody': {'content': {}}, 'responses': {'200': {'content': {'application/json': {'schema': Defs.components_schemas_replace_server_response}}, 'description': 'The `server` key in the reply contains the updated Server'}}, 'tags': ['servers'], 'operationId': 'replace_server', 'mime': 'application/json'}
            id = {'type': 'integer'}
            body = Defs.components_schemas_replace_server_request
        R.id = id
        R.body = Defs.components_schemas_replace_server_request

class servers___id___actions:
    pth = "/servers/{id}/actions"

    class get:
        """Returns all Action objects for a Server. You can `sort` the results by using the sort URI parameter, and filter them with the `status` parameter. Get all Actions for a Server"""
        class R:
            _query = ['sort', 'status', 'page', 'per_page']; _path = ['id'];
            _ = {'responses': {'200': {'content': {'application/json': {'example': {'actions': [{'command': 'start_server', 'error': {'code': 'action_failed', 'message': 'Action failed'}, 'finished': '2016-01-30T23:56:00+00:00', 'id': 13, 'progress': 100, 'resources': [{'id': 42, 'type': 'server'}], 'started': '2016-01-30T23:55:00+00:00', 'status': 'success'}]}, 'schema': Defs.components_schemas_list_actions_for_server_response}}, 'description': 'The `actions` key contains a list of Actions'}}, 'tags': ['servers'], 'operationId': 'list_actions_for_server'}
            id = {'type': 'integer'}
            sort = {'enum': ['id', 'id:asc', 'id:desc', 'command', 'command:asc', 'command:desc', 'status', 'status:asc', 'status:desc', 'progress', 'progress:asc', 'progress:desc', 'started', 'started:asc', 'started:desc', 'finished', 'finished:asc', 'finished:desc'], 'title': 'ParameterSort', 'type': 'string'}
            status = {'enum': ['running', 'success', 'error'], 'title': 'ParameterStatus', 'type': 'string'}
            page = {'type': 'integer', 'minimum': 1}
            per_page = {'type': 'integer', 'minimum': 1, 'maximum': 50}
        R.id = id
        R.sort = 'id'
        R.status = 'running'
        R.page = 0
        R.per_page = 0

class servers___id___actions___action_id_:
    pth = "/servers/{id}/actions/{action_id}"

    class get:
        """Returns a specific Action object for a Server. Get an Action for a Server"""
        class R:
            _path = ['id', 'action_id'];
            _ = {'responses': {'200': {'content': {'application/json': {'example': {'action': {'command': 'start_server', 'error': {'code': 'action_failed', 'message': 'Action failed'}, 'finished': '2016-01-30T23:56:00+00:00', 'id': 13, 'progress': 100, 'resources': [{'id': 42, 'type': 'server'}], 'started': '2016-01-30T23:55:00+00:00', 'status': 'success'}}, 'schema': Defs.components_schemas_get_action_for_server_response}}, 'description': 'The `action` key in the reply has this structure'}}, 'tags': ['servers'], 'operationId': 'get_action_for_server'}
            id = {'type': 'integer'}
            action_id = {'type': 'integer'}
        R.id = id
        R.action_id = action_id

class servers___id___actions__add_to_placement_group:
    pth = "/servers/{id}/actions/add_to_placement_group"

    class post:
        """Adds a Server to a Placement Group.

Server must be powered off for this command to succeed.

#### Call specific error codes

| Code                          | Description                                                          |
|-------------------------------|----------------------------------------------------------------------|
| `server_not_stopped`          | The action requires a stopped server                                 |
 Add a Server to a Placement Group"""
        class R:
            _path = ['id']; _body = ['body'];
            _ = {'requestBody': {'content': {}}, 'responses': {'201': {'content': {'application/json': {'example': {'action': {'command': 'add_to_placement_group', 'error': {'code': 'action_failed', 'message': 'Action failed'}, 'finished': None, 'id': 13, 'progress': 0, 'resources': [{'id': 42, 'type': 'server'}], 'started': '2016-01-30T23:50:00+00:00', 'status': 'running'}}, 'schema': Defs.components_schemas_add_server_to_placement_group_response}}, 'description': 'The `action` key in the reply contains an Action object with this structure'}}, 'tags': ['servers'], 'operationId': 'add_server_to_placement_group', 'mime': 'application/json'}
            id = {'type': 'integer'}
            body = Defs.components_schemas_add_server_to_placement_group_request
        R.id = id
        R.body = Defs.components_schemas_add_server_to_placement_group_request

class servers___id___actions__attach_iso:
    pth = "/servers/{id}/actions/attach_iso"

    class post:
        """Attaches an ISO to a Server. The Server will immediately see it as a new disk. An already attached ISO will automatically be detached before the new ISO is attached.

Servers with attached ISOs have a modified boot order: They will try to boot from the ISO first before falling back to hard disk.
 Attach an ISO to a Server"""
        class R:
            _path = ['id']; _body = ['body'];
            _ = {'requestBody': {'content': {}}, 'responses': {'201': {'content': {'application/json': {'example': {'action': {'command': 'attach_iso', 'error': {'code': 'action_failed', 'message': 'Action failed'}, 'finished': None, 'id': 13, 'progress': 0, 'resources': [{'id': 42, 'type': 'server'}], 'started': '2016-01-30T23:50:00+00:00', 'status': 'running'}}, 'schema': Defs.components_schemas_attach_iso_to_server_response}}, 'description': 'The `action` key in the reply contains an Action object with this structure'}}, 'tags': ['servers'], 'operationId': 'attach_iso_to_server', 'mime': 'application/json'}
            id = {'type': 'integer'}
            body = Defs.components_schemas_attach_iso_to_server_request
        R.id = id
        R.body = Defs.components_schemas_attach_iso_to_server_request

class servers___id___actions__attach_to_network:
    pth = "/servers/{id}/actions/attach_to_network"

    class post:
        """Attaches a Server to a network. This will complement the fixed public Server interface by adding an additional ethernet interface to the Server which is connected to the specified network.

The Server will get an IP auto assigned from a subnet of type `server` in the same `network_zone`.

Using the `alias_ips` attribute you can also define one or more additional IPs to the Servers. Please note that you will have to configure these IPs by hand on your Server since only the primary IP will be given out by DHCP.

**Call specific error codes**

| Code                             | Description                                                           |
|----------------------------------|-----------------------------------------------------------------------|
| `server_already_attached`        | The server is already attached to the network                         |
| `ip_not_available`               | The provided Network IP is not available                              |
| `no_subnet_available`            | No Subnet or IP is available for the Server within the network        |
| `networks_overlap`               | The network IP range overlaps with one of the server networks         |
 Attach a Server to a Network"""
        class R:
            _path = ['id']; _body = ['body'];
            _ = {'requestBody': {'content': {}}, 'responses': {'201': {'content': {'application/json': {'example': {'action': {'command': 'attach_to_network', 'error': {'code': 'action_failed', 'message': 'Action failed'}, 'finished': None, 'id': 13, 'progress': 0, 'resources': [{'id': 42, 'type': 'server'}, {'id': 4711, 'type': 'network'}], 'started': '2016-01-30T23:50:00+00:00', 'status': 'running'}}, 'schema': Defs.components_schemas_attach_server_to_network_response}}, 'description': 'The `action` key in the reply contains an Action object with this structure'}}, 'tags': ['servers'], 'operationId': 'attach_server_to_network', 'mime': 'application/json'}
            id = {'type': 'integer'}
            body = Defs.components_schemas_attach_server_to_network_request
        R.id = id
        R.body = Defs.components_schemas_attach_server_to_network_request

class servers___id___actions__change_alias_ips:
    pth = "/servers/{id}/actions/change_alias_ips"

    class post:
        """Changes the alias IPs of an already attached Network. Note that the existing aliases for the specified Network will be replaced with these provided in the request body. So if you want to add an alias IP, you have to provide the existing ones from the Network plus the new alias IP in the request body. Change alias IPs of a Network"""
        class R:
            _path = ['id']; _body = ['body'];
            _ = {'requestBody': {'content': {}}, 'responses': {'201': {'content': {'application/json': {'example': {'action': {'command': 'change_alias_ips', 'error': {'code': 'action_failed', 'message': 'Action failed'}, 'finished': None, 'id': 13, 'progress': 0, 'resources': [{'id': 42, 'type': 'server'}, {'id': 4711, 'type': 'network'}], 'started': '2016-01-30T23:50:00+00:00', 'status': 'running'}}, 'schema': Defs.components_schemas_change_alias_ips_of_network_response}}, 'description': 'The `action` key in the reply contains an Action object with this structure'}}, 'tags': ['servers'], 'operationId': 'change_alias_ips_of_network', 'mime': 'application/json'}
            id = {'type': 'integer'}
            body = Defs.components_schemas_change_alias_ips_of_network_request
        R.id = id
        R.body = Defs.components_schemas_change_alias_ips_of_network_request

class servers___id___actions__change_dns_ptr:
    pth = "/servers/{id}/actions/change_dns_ptr"

    class post:
        """Changes the hostname that will appear when getting the hostname belonging to the primary IPs (IPv4 and IPv6) of this Server.

Floating IPs assigned to the Server are not affected by this.
 Change reverse DNS entry for this Server"""
        class R:
            _path = ['id']; _body = ['body'];
            _ = {'requestBody': {'content': {}, 'description': 'Select the IP address for which to change the DNS entry by passing `ip`. It can be either IPv4 or IPv6. The target hostname is set by passing `dns_ptr`.'}, 'responses': {'201': {'content': {'application/json': {'example': {'action': {'command': 'change_dns_ptr', 'error': {'code': 'action_failed', 'message': 'Action failed'}, 'finished': None, 'id': 13, 'progress': 0, 'resources': [{'id': 42, 'type': 'server'}], 'started': '2016-01-30T23:50:00+00:00', 'status': 'running'}}, 'schema': Defs.components_schemas_change_reverse_dns_entry_for_this_server_response}}, 'description': 'The `action` key in the reply contains an Action object with this structure'}}, 'tags': ['servers'], 'operationId': 'change_reverse_dns_entry_for_this_server', 'mime': 'application/json'}
            id = {'type': 'integer'}
            body = Defs.components_schemas_change_reverse_dns_entry_for_this_server_request
        R.id = id
        R.body = Defs.components_schemas_change_reverse_dns_entry_for_this_server_request

class servers___id___actions__change_protection:
    pth = "/servers/{id}/actions/change_protection"

    class post:
        """Changes the protection configuration of the Server. Change Server Protection"""
        class R:
            _path = ['id']; _body = ['body'];
            _ = {'requestBody': {'content': {}}, 'responses': {'201': {'content': {'application/json': {'example': {'action': {'command': 'change_protection', 'error': {'code': 'action_failed', 'message': 'Action failed'}, 'finished': '2016-01-30T23:56:00+00:00', 'id': 13, 'progress': 100, 'resources': [{'id': 42, 'type': 'server'}], 'started': '2016-01-30T23:55:00+00:00', 'status': 'success'}}, 'schema': Defs.components_schemas_change_server_protection_response}}, 'description': 'The `action` key in the reply contains an Action object with this structure'}}, 'tags': ['servers'], 'operationId': 'change_server_protection', 'mime': 'application/json'}
            id = {'type': 'integer'}
            body = Defs.components_schemas_change_server_protection_request
        R.id = id
        R.body = Defs.components_schemas_change_server_protection_request

class servers___id___actions__change_type:
    pth = "/servers/{id}/actions/change_type"

    class post:
        """Changes the type (Cores, RAM and disk sizes) of a Server.

Server must be powered off for this command to succeed.

This copies the content of its disk, and starts it again.

You can only migrate to Server types with the same `storage_type` and equal or bigger disks. Shrinking disks is not possible as it might destroy data.

If the disk gets upgraded, the Server type can not be downgraded any more. If you plan to downgrade the Server type, set `upgrade_disk` to `false`.

#### Call specific error codes

| Code                          | Description                                                          |
|-------------------------------|----------------------------------------------------------------------|
| `invalid_server_type`         | The server type does not fit for the given server or is deprecated   |
| `server_not_stopped`          | The action requires a stopped server                                 |
 Change the Type of a Server"""
        class R:
            _path = ['id']; _body = ['body'];
            _ = {'requestBody': {'content': {}}, 'responses': {'201': {'content': {'application/json': {'example': {'action': {'command': 'change_server_type', 'error': {'code': 'action_failed', 'message': 'Action failed'}, 'finished': None, 'id': 13, 'progress': 0, 'resources': [{'id': 42, 'type': 'server'}], 'started': '2016-01-30T23:50:00+00:00', 'status': 'running'}}, 'schema': Defs.components_schemas_change_type_of_server_response}}, 'description': 'The `action` key in the reply contains an Action object with this structure'}}, 'tags': ['servers'], 'operationId': 'change_type_of_server', 'mime': 'application/json'}
            id = {'type': 'integer'}
            body = Defs.components_schemas_change_type_of_server_request
        R.id = id
        R.body = Defs.components_schemas_change_type_of_server_request

class servers___id___actions__create_image:
    pth = "/servers/{id}/actions/create_image"

    class post:
        """Creates an Image (snapshot) from a Server by copying the contents of its disks. This creates a snapshot of the current state of the disk and copies it into an Image. If the Server is currently running you must make sure that its disk content is consistent. Otherwise, the created Image may not be readable.

To make sure disk content is consistent, we recommend to shut down the Server prior to creating an Image.

You can either create a `backup` Image that is bound to the Server and therefore will be deleted when the Server is deleted, or you can create an `snapshot` Image which is completely independent of the Server it was created from and will survive Server deletion. Backup Images are only available when the backup option is enabled for the Server. Snapshot Images are billed on a per GB basis.
 Create Image from a Server"""
        class R:
            _path = ['id']; _body = ['body'];
            _ = {'requestBody': {'content': {}}, 'responses': {'201': {'content': {'application/json': {'example': {'action': {'command': 'create_image', 'error': {'code': 'action_failed', 'message': 'Action failed'}, 'finished': '2016-01-30T23:56:00+00:00', 'id': 13, 'progress': 100, 'resources': [{'id': 42, 'type': 'server'}], 'started': '2016-01-30T23:55:00+00:00', 'status': 'success'}, 'image': {'bound_to': None, 'created': '2016-01-30T23:50:00+00:00', 'created_from': {'id': 1, 'name': 'Server'}, 'deleted': None, 'deprecated': '2018-02-28T00:00:00+00:00', 'description': 'my image', 'disk_size': 10, 'id': 4711, 'image_size': 2.3, 'labels': {'env': 'dev'}, 'name': None, 'os_flavor': 'ubuntu', 'os_version': '20.04', 'protection': {'delete': False}, 'rapid_deploy': False, 'status': 'creating', 'type': 'snapshot'}}, 'schema': Defs.components_schemas_create_image_from_server_response}}, 'description': 'The `image` key in the reply contains an the created Image, which is an object with this structure\n\nThe `action` key in the reply contains an Action object with this structure\n'}}, 'tags': ['servers'], 'operationId': 'create_image_from_server', 'mime': 'application/json'}
            id = {'type': 'integer'}
            body = Defs.components_schemas_create_image_from_server_request
        R.id = id
        R.body = Defs.components_schemas_create_image_from_server_request

class servers___id___actions__detach_from_network:
    pth = "/servers/{id}/actions/detach_from_network"

    class post:
        """Detaches a Server from a network. The interface for this network will vanish. Detach a Server from a Network"""
        class R:
            _path = ['id']; _body = ['body'];
            _ = {'requestBody': {'content': {}}, 'responses': {'201': {'content': {'application/json': {'example': {'action': {'command': 'detach_from_network', 'error': {'code': 'action_failed', 'message': 'Action failed'}, 'finished': None, 'id': 13, 'progress': 0, 'resources': [{'id': 42, 'type': 'server'}, {'id': 4711, 'type': 'network'}], 'started': '2016-01-30T23:50:00+00:00', 'status': 'running'}}, 'schema': Defs.components_schemas_detach_server_from_network_response}}, 'description': 'The `action` key in the reply contains an Action object with this structure'}}, 'tags': ['servers'], 'operationId': 'detach_server_from_network', 'mime': 'application/json'}
            id = {'type': 'integer'}
            body = Defs.components_schemas_detach_server_from_network_request
        R.id = id
        R.body = Defs.components_schemas_detach_server_from_network_request

class servers___id___actions__detach_iso:
    pth = "/servers/{id}/actions/detach_iso"

    class post:
        """Detaches an ISO from a Server. In case no ISO Image is attached to the Server, the status of the returned Action is immediately set to `success` Detach an ISO from a Server"""
        class R:
            _path = ['id'];
            _ = {'responses': {'201': {'content': {'application/json': {'example': {'action': {'command': 'detach_iso', 'error': {'code': 'action_failed', 'message': 'Action failed'}, 'finished': None, 'id': 13, 'progress': 0, 'resources': [{'id': 42, 'type': 'server'}], 'started': '2016-01-30T23:50:00+00:00', 'status': 'running'}}, 'schema': Defs.components_schemas_detach_iso_from_server_response}}, 'description': 'The `action` key in the reply contains an Action object with this structure'}}, 'tags': ['servers'], 'operationId': 'detach_iso_from_server'}
            id = {'type': 'integer'}
        R.id = id

class servers___id___actions__disable_backup:
    pth = "/servers/{id}/actions/disable_backup"

    class post:
        """Disables the automatic backup option and deletes all existing Backups for a Server. No more additional charges for backups will be made.

Caution: This immediately removes all existing backups for the Server!
 Disable Backups for a Server"""
        class R:
            _path = ['id'];
            _ = {'responses': {'201': {'content': {'application/json': {'example': {'action': {'command': 'disable_backup', 'error': {'code': 'action_failed', 'message': 'Action failed'}, 'finished': '2016-01-30T23:56:00+00:00', 'id': 13, 'progress': 100, 'resources': [{'id': 42, 'type': 'server'}], 'started': '2016-01-30T23:55:00+00:00', 'status': 'success'}}, 'schema': Defs.components_schemas_disable_backups_for_server_response}}, 'description': 'The `action` key in the reply contains an Action object with this structure'}}, 'tags': ['servers'], 'operationId': 'disable_backups_for_server'}
            id = {'type': 'integer'}
        R.id = id

class servers___id___actions__disable_rescue:
    pth = "/servers/{id}/actions/disable_rescue"

    class post:
        """Disables the Hetzner Rescue System for a Server. This makes a Server start from its disks on next reboot.

Rescue Mode is automatically disabled when you first boot into it or if you do not use it for 60 minutes.

Disabling rescue mode will not reboot your Server — you will have to do this yourself.
 Disable Rescue Mode for a Server"""
        class R:
            _path = ['id'];
            _ = {'responses': {'201': {'content': {'application/json': {'example': {'action': {'command': 'disable_rescue', 'error': {'code': 'action_failed', 'message': 'Action failed'}, 'finished': None, 'id': 13, 'progress': 0, 'resources': [{'id': 42, 'type': 'server'}], 'started': '2016-01-30T23:50:00+00:00', 'status': 'running'}}, 'schema': Defs.components_schemas_disable_rescue_mode_for_server_response}}, 'description': 'The `action` key in the reply contains an Action object with this structure'}}, 'tags': ['servers'], 'operationId': 'disable_rescue_mode_for_server'}
            id = {'type': 'integer'}
        R.id = id

class servers___id___actions__enable_backup:
    pth = "/servers/{id}/actions/enable_backup"

    class post:
        """Enables and configures the automatic daily backup option for the Server. Enabling automatic backups will increase the price of the Server by 20%. In return, you will get seven slots where Images of type backup can be stored.

Backups are automatically created daily.
 Enable and Configure Backups for a Server"""
        class R:
            _path = ['id'];
            _ = {'responses': {'201': {'content': {'application/json': {'example': {'action': {'command': 'enable_backup', 'error': {'code': 'action_failed', 'message': 'Action failed'}, 'finished': '2016-01-30T23:56:00+00:00', 'id': 13, 'progress': 100, 'resources': [{'id': 42, 'type': 'server'}], 'started': '2016-01-30T23:55:00+00:00', 'status': 'success'}}, 'schema': Defs.components_schemas_enable_and_configure_backups_for_server_response}}, 'description': 'The `action` key in the reply contains an Action object with this structure'}}, 'tags': ['servers'], 'operationId': 'enable_and_configure_backups_for_server'}
            id = {'type': 'integer'}
        R.id = id

class servers___id___actions__enable_rescue:
    pth = "/servers/{id}/actions/enable_rescue"

    class post:
        """Enable the Hetzner Rescue System for this Server. The next time a Server with enabled rescue mode boots it will start a special minimal Linux distribution designed for repair and reinstall.

In case a Server cannot boot on its own you can use this to access a Server’s disks.

Rescue Mode is automatically disabled when you first boot into it or if you do not use it for 60 minutes.

Enabling rescue mode will not [reboot](https://docs.hetzner.cloud/#server-actions-soft-reboot-a-server) your Server — you will have to do this yourself.
 Enable Rescue Mode for a Server"""
        class R:
            _path = ['id']; _body = ['body'];
            _ = {'requestBody': {'content': {}}, 'responses': {'201': {'content': {'application/json': {'example': {'action': {'command': 'enable_rescue', 'error': {'code': 'action_failed', 'message': 'Action failed'}, 'finished': '2016-01-30T23:56:00+00:00', 'id': 13, 'progress': 100, 'resources': [{'id': 42, 'type': 'server'}], 'started': '2016-01-30T23:55:00+00:00', 'status': 'success'}, 'root_password': 'zCWbFhnu950dUTko5f40'}, 'schema': Defs.components_schemas_enable_rescue_mode_for_server_response}}, 'description': 'The `root_password` key in the reply contains the root password that can be used to access the booted rescue system.\n\nThe `action` key in the reply contains an Action object with this structure\n'}}, 'tags': ['servers'], 'operationId': 'enable_rescue_mode_for_server', 'mime': 'application/json'}
            id = {'type': 'integer'}
            body = Defs.components_schemas_enable_rescue_mode_for_server_request
        R.id = id
        R.body = Defs.components_schemas_enable_rescue_mode_for_server_request

class servers___id___actions__poweroff:
    pth = "/servers/{id}/actions/poweroff"

    class post:
        """Cuts power to the Server. This forcefully stops it without giving the Server operating system time to gracefully stop. May lead to data loss, equivalent to pulling the power cord. Power off should only be used when shutdown does not work. Power off a Server"""
        class R:
            _path = ['id'];
            _ = {'responses': {'201': {'content': {'application/json': {'example': {'action': {'command': 'stop_server', 'error': {'code': 'action_failed', 'message': 'Action failed'}, 'finished': None, 'id': 13, 'progress': 0, 'resources': [{'id': 42, 'type': 'server'}], 'started': '2016-01-30T23:50:00+00:00', 'status': 'running'}}, 'schema': Defs.components_schemas_power_off_server_response}}, 'description': 'The `action` key in the reply contains an Action object with this structure'}}, 'tags': ['servers'], 'operationId': 'power_off_server'}
            id = {'type': 'integer'}
        R.id = id

class servers___id___actions__poweron:
    pth = "/servers/{id}/actions/poweron"

    class post:
        """Starts a Server by turning its power on. Power on a Server"""
        class R:
            _path = ['id'];
            _ = {'responses': {'201': {'content': {'application/json': {'example': {'action': {'command': 'start_server', 'error': {'code': 'action_failed', 'message': 'Action failed'}, 'finished': None, 'id': 13, 'progress': 0, 'resources': [{'id': 42, 'type': 'server'}], 'started': '2016-01-30T23:50:00+00:00', 'status': 'running'}}, 'schema': Defs.components_schemas_power_on_server_response}}, 'description': 'The `action` key in the reply contains an Action object with this structure'}}, 'tags': ['servers'], 'operationId': 'power_on_server'}
            id = {'type': 'integer'}
        R.id = id

class servers___id___actions__reboot:
    pth = "/servers/{id}/actions/reboot"

    class post:
        """Reboots a Server gracefully by sending an ACPI request. The Server operating system must support ACPI and react to the request, otherwise the Server will not reboot. Soft-reboot a Server"""
        class R:
            _path = ['id'];
            _ = {'responses': {'201': {'content': {'application/json': {'example': {'action': {'command': 'reboot_server', 'error': {'code': 'action_failed', 'message': 'Action failed'}, 'finished': None, 'id': 13, 'progress': 0, 'resources': [{'id': 42, 'type': 'server'}], 'started': '2016-01-30T23:50:00+00:00', 'status': 'running'}}, 'schema': Defs.components_schemas_soft_reboot_server_response}}, 'description': 'The `action` key in the reply contains an Action object with this structure'}}, 'tags': ['servers'], 'operationId': 'soft_reboot_server'}
            id = {'type': 'integer'}
        R.id = id

class servers___id___actions__rebuild:
    pth = "/servers/{id}/actions/rebuild"

    class post:
        """Rebuilds a Server overwriting its disk with the content of an Image, thereby **destroying all data** on the target Server

The Image can either be one you have created earlier (`backup` or `snapshot` Image) or it can be a completely fresh `system` Image provided by us. You can get a list of all available Images with `GET /images`.

Your Server will automatically be powered off before the rebuild command executes.
 Rebuild a Server from an Image"""
        class R:
            _path = ['id']; _body = ['body'];
            _ = {'requestBody': {'content': {}, 'description': 'To select which Image to rebuild from you can either pass an ID or a name as the `image` argument. Passing a name only works for `system` Images since the other Image types do not have a name set.'}, 'responses': {'201': {'content': {'application/json': {'example': {'action': {'command': 'rebuild_server', 'error': {'code': 'action_failed', 'message': 'Action failed'}, 'finished': None, 'id': 13, 'progress': 0, 'resources': [{'id': 42, 'type': 'server'}], 'started': '2016-01-30T23:50:00+00:00', 'status': 'running'}, 'root_password': None}, 'schema': Defs.components_schemas_rebuild_server_from_image_response}}, 'description': 'The `action` key in the reply contains an Action object with this structure'}}, 'tags': ['servers'], 'operationId': 'rebuild_server_from_image', 'mime': 'application/json'}
            id = {'type': 'integer'}
            body = Defs.components_schemas_rebuild_server_from_image_request
        R.id = id
        R.body = Defs.components_schemas_rebuild_server_from_image_request

class servers___id___actions__remove_from_placement_group:
    pth = "/servers/{id}/actions/remove_from_placement_group"

    class post:
        """Removes a Server from a Placement Group.
 Remove from Placement Group"""
        class R:
            _path = ['id'];
            _ = {'responses': {'201': {'content': {'application/json': {'example': {'action': {'command': 'remove_from_placement_group', 'error': {'code': 'action_failed', 'message': 'Action failed'}, 'finished': '2016-01-30T23:56:00+00:00', 'id': 13, 'progress': 100, 'resources': [{'id': 42, 'type': 'server'}], 'started': '2016-01-30T23:55:00+00:00', 'status': 'success'}}, 'schema': Defs.components_schemas_remove_from_placement_group_response}}, 'description': 'The `action` key in the reply contains an Action object with this structure'}}, 'tags': ['servers'], 'operationId': 'remove_from_placement_group'}
            id = {'type': 'integer'}
        R.id = id

class servers___id___actions__request_console:
    pth = "/servers/{id}/actions/request_console"

    class post:
        """Requests credentials for remote access via VNC over websocket to keyboard, monitor, and mouse for a Server. The provided URL is valid for 1 minute, after this period a new url needs to be created to connect to the Server. How long the connection is open after the initial connect is not subject to this timeout. Request Console for a Server"""
        class R:
            _path = ['id'];
            _ = {'responses': {'201': {'content': {'application/json': {'example': {'action': {'command': 'request_console', 'error': {'code': 'action_failed', 'message': 'Action failed'}, 'finished': '2016-01-30T23:56:00+00:00', 'id': 13, 'progress': 100, 'resources': [{'id': 42, 'type': 'server'}], 'started': '2016-01-30T23:55:00+00:00', 'status': 'success'}, 'password': '9MQaTg2VAGI0FIpc10k3UpRXcHj2wQ6x', 'wss_url': 'wss://console.hetzner.cloud/?server_id=1&token=3db32d15-af2f-459c-8bf8-dee1fd05f49c'}, 'schema': Defs.components_schemas_request_console_for_server_response}}, 'description': 'The `action` key in the reply contains an Action object with this structure'}}, 'tags': ['servers'], 'operationId': 'request_console_for_server'}
            id = {'type': 'integer'}
        R.id = id

class servers___id___actions__reset:
    pth = "/servers/{id}/actions/reset"

    class post:
        """Cuts power to a Server and starts it again. This forcefully stops it without giving the Server operating system time to gracefully stop. This may lead to data loss, it’s equivalent to pulling the power cord and plugging it in again. Reset should only be used when reboot does not work. Reset a Server"""
        class R:
            _path = ['id'];
            _ = {'responses': {'201': {'content': {'application/json': {'example': {'action': {'command': 'reset_server', 'error': {'code': 'action_failed', 'message': 'Action failed'}, 'finished': None, 'id': 13, 'progress': 0, 'resources': [{'id': 42, 'type': 'server'}], 'started': '2016-01-30T23:50:00+00:00', 'status': 'running'}}, 'schema': Defs.components_schemas_reset_server_response}}, 'description': 'The `action` key in the reply contains an Action object with this structure'}}, 'tags': ['servers'], 'operationId': 'reset_server'}
            id = {'type': 'integer'}
        R.id = id

class servers___id___actions__reset_password:
    pth = "/servers/{id}/actions/reset_password"

    class post:
        """Resets the root password. Only works for Linux systems that are running the qemu guest agent. Server must be powered on (status `running`) in order for this operation to succeed.

This will generate a new password for this Server and return it.

If this does not succeed you can use the rescue system to netboot the Server and manually change your Server password by hand.
 Reset root Password of a Server"""
        class R:
            _path = ['id'];
            _ = {'responses': {'201': {'content': {'application/json': {'example': {'action': {'command': 'reset_password', 'error': {'code': 'action_failed', 'message': 'Action failed'}, 'finished': None, 'id': 13, 'progress': 0, 'resources': [{'id': 42, 'type': 'server'}], 'started': '2016-01-30T23:50:00+00:00', 'status': 'running'}, 'root_password': 'zCWbFhnu950dUTko5f40'}, 'schema': Defs.components_schemas_reset_root_password_of_server_response}}, 'description': 'The `root_password` key in the reply contains the new root password that will be active if the Action succeeds.\n\nThe `action` key in the reply contains an Action object with this structure:\n'}}, 'tags': ['servers'], 'operationId': 'reset_root_password_of_server'}
            id = {'type': 'integer'}
        R.id = id

class servers___id___actions__shutdown:
    pth = "/servers/{id}/actions/shutdown"

    class post:
        """Shuts down a Server gracefully by sending an ACPI shutdown request. The Server operating system must support ACPI and react to the request, otherwise the Server will not shut down. Shutdown a Server"""
        class R:
            _path = ['id'];
            _ = {'responses': {'201': {'content': {'application/json': {'example': {'action': {'command': 'shutdown_server', 'error': {'code': 'action_failed', 'message': 'Action failed'}, 'finished': None, 'id': 13, 'progress': 0, 'resources': [{'id': 42, 'type': 'server'}], 'started': '2016-01-30T23:50:00+00:00', 'status': 'running'}}, 'schema': Defs.components_schemas_shutdown_server_response}}, 'description': 'The `action` key in the reply contains an Action object with this structure'}}, 'tags': ['servers'], 'operationId': 'shutdown_server'}
            id = {'type': 'integer'}
        R.id = id

class servers___id___metrics:
    pth = "/servers/{id}/metrics"

    class get:
        """Get Metrics for specified Server.

You must specify the type of metric to get: cpu, disk or network. You can also specify more than one type by comma separation, e.g. cpu,disk.

Depending on the type you will get different time series data

| Type    | Timeseries              | Unit      | Description                                          |
|---------|-------------------------|-----------|------------------------------------------------------|
| cpu     | cpu                     | percent   | Percent CPU usage                                    |
| disk    | disk.0.iops.read        | iop/s     | Number of read IO operations per second              |
|         | disk.0.iops.write       | iop/s     | Number of write IO operations per second             |
|         | disk.0.bandwidth.read   | bytes/s   | Bytes read per second                                |
|         | disk.0.bandwidth.write  | bytes/s   | Bytes written per second                             |
| network | network.0.pps.in        | packets/s | Public Network interface packets per second received |
|         | network.0.pps.out       | packets/s | Public Network interface packets per second sent     |
|         | network.0.bandwidth.in  | bytes/s   | Public Network interface bytes/s received            |
|         | network.0.bandwidth.out | bytes/s   | Public Network interface bytes/s sent                |

Metrics are available for the last 30 days only.

If you do not provide the step argument we will automatically adjust it so that a maximum of 200 samples are returned.

We limit the number of samples returned to a maximum of 500 and will adjust the step parameter accordingly.
 Get Metrics for a Server"""
        class R:
            _query = ['type', 'start', 'end', 'step']; _path = ['id'];
            _ = {'responses': {'200': {'content': {'application/json': {'schema': Defs.components_schemas_get_metrics_for_server_response}}, 'description': 'The `metrics` key in the reply contains a metrics object with this structure'}}, 'tags': ['servers'], 'operationId': 'get_metrics_for_server'}
            id = {'type': 'integer'}
            type = {'enum': ['cpu', 'disk', 'network'], 'type': 'string'}
            start = {'type': 'string'}
            end = {'type': 'string'}
            step = {'type': 'string'}
        R.id = id
        R.type = 'cpu'
        R.start = str_dflt
        R.end = str_dflt
        R.step = str_dflt

class ssh_keys:
    pth = "/ssh_keys"

    class get:
        """Returns all SSH key objects. Get all SSH keys"""
        class R:
            _query = ['sort', 'name', 'fingerprint', 'label_selector', 'page', 'per_page'];
            _ = {'responses': {'200': {'content': {'application/json': {'schema': Defs.components_schemas_list_ssh_keys_response}}, 'description': 'The `ssh_keys` key in the reply contains an array of SSH key objects with this structure'}}, 'tags': ['ssh_keys'], 'operationId': 'list_ssh_keys'}
            sort = {'enum': ['id', 'id:asc', 'id:desc', 'name', 'name:asc', 'name:desc'], 'type': 'string'}
            name = {'type': 'string'}
            fingerprint = {'type': 'string'}
            label_selector = {'type': 'string'}
            page = {'type': 'integer', 'minimum': 1}
            per_page = {'type': 'integer', 'minimum': 1, 'maximum': 50}
        R.sort = 'id'
        R.name = str_dflt
        R.fingerprint = str_dflt
        R.label_selector = str_dflt
        R.page = 0
        R.per_page = 0

    class post:
        """Creates a new SSH key with the given `name` and `public_key`. Once an SSH key is created, it can be used in other calls such as creating Servers. Create an SSH key"""
        class R:
            _body = ['body'];
            _ = {'requestBody': {'content': {}}, 'responses': {'201': {'content': {'application/json': {'schema': Defs.components_schemas_create_ssh_key_response}}, 'description': 'The `ssh_key` key in the reply contains the object that was just created'}}, 'tags': ['ssh_keys'], 'operationId': 'create_ssh_key', 'mime': 'application/json'}
            body = Defs.components_schemas_create_ssh_key_request
        R.body = Defs.components_schemas_create_ssh_key_request

class ssh_keys___id_:
    pth = "/ssh_keys/{id}"

    class delete:
        """Deletes an SSH key. It cannot be used anymore. Delete an SSH key"""
        class R:
            _path = ['id'];
            _ = {'responses': {'204': {'description': 'SSH key deleted'}}, 'tags': ['ssh_keys'], 'operationId': 'delete_ssh_key'}
            id = {'type': 'string'}
        R.id = id

    class get:
        """Returns a specific SSH key object. Get a SSH key"""
        class R:
            _path = ['id'];
            _ = {'responses': {'200': {'content': {'application/json': {'schema': Defs.components_schemas_get_ssh_key_response}}, 'description': 'The `ssh_key` key in the reply contains an SSH key object with this structure'}}, 'tags': ['ssh_keys'], 'operationId': 'get_ssh_key'}
            id = {'type': 'integer'}
        R.id = id

    class put:
        """Updates an SSH key. You can update an SSH key name and an SSH key labels.

Please note that when updating labels, the SSH key current set of labels will be replaced with the labels provided in the request body. So, for example, if you want to add a new label, you have to provide all existing labels plus the new label in the request body.
 Update an SSH key"""
        class R:
            _path = ['id']; _body = ['body'];
            _ = {'requestBody': {'content': {}}, 'responses': {'200': {'content': {'application/json': {'example': {'ssh_key': {'created': '2016-01-30T23:50:00+00:00', 'fingerprint': 'b7:2f:30:a0:2f:6c:58:6c:21:04:58:61:ba:06:3b:2f', 'id': 2323, 'labels': {'labelkey': 'value'}, 'name': 'My ssh key', 'public_key': 'ssh-rsa AAAjjk76kgf...Xt'}}, 'schema': Defs.components_schemas_replace_ssh_key_response}}, 'description': 'The `ssh_key` key in the reply contains the modified SSH key object with the new description'}}, 'tags': ['ssh_keys'], 'operationId': 'replace_ssh_key', 'mime': 'application/json'}
            id = {'type': 'string'}
            body = Defs.components_schemas_replace_ssh_key_request
        R.id = id
        R.body = Defs.components_schemas_replace_ssh_key_request

class volumes:
    pth = "/volumes"

    class get:
        """Gets all existing Volumes that you have available. Get all Volumes"""
        class R:
            _query = ['status', 'sort', 'name', 'label_selector', 'page', 'per_page'];
            _ = {'responses': {'200': {'content': {'application/json': {'schema': Defs.components_schemas_list_volumes_response}}, 'description': 'The `volumes` key contains a list of volumes'}}, 'tags': ['volumes'], 'operationId': 'list_volumes'}
            status = {'enum': ['available', 'creating'], 'type': 'string'}
            sort = {'enum': ['id', 'id:asc', 'id:desc', 'name', 'name:asc', 'name:desc', 'created', 'created:asc', 'created:desc'], 'type': 'string'}
            name = {'type': 'string'}
            label_selector = {'type': 'string'}
            page = {'type': 'integer', 'minimum': 1}
            per_page = {'type': 'integer', 'minimum': 1, 'maximum': 50}
        R.status = 'available'
        R.sort = 'id'
        R.name = str_dflt
        R.label_selector = str_dflt
        R.page = 0
        R.per_page = 0

    class post:
        """Creates a new Volume attached to a Server. If you want to create a Volume that is not attached to a Server, you need to provide the `location` key instead of `server`. This can be either the ID or the name of the Location this Volume will be created in. Note that a Volume can be attached to a Server only in the same Location as the Volume itself.

Specifying the Server during Volume creation will automatically attach the Volume to that Server after it has been initialized. In that case, the `next_actions` key in the response is an array which contains a single `attach_volume` action.

The minimum Volume size is 10GB and the maximum size is 10TB (10240GB).

A volume’s name can consist of alphanumeric characters, dashes, underscores, and dots, but has to start and end with an alphanumeric character. The total length is limited to 64 characters. Volume names must be unique per Project.

#### Call specific error codes

| Code                                | Description                                         |
|-------------------------------------|-----------------------------------------------------|
| `no_space_left_in_location`         | There is no volume space left in the given location |
 Create a Volume"""
        class R:
            _body = ['body'];
            _ = {'requestBody': {'content': {}}, 'responses': {'201': {'content': {'application/json': {'example': {'action': {'command': 'create_volume', 'error': {'code': 'action_failed', 'message': 'Action failed'}, 'finished': None, 'id': 13, 'progress': 0, 'resources': [{'id': 42, 'type': 'server'}, {'id': 554, 'type': 'volume'}], 'started': '2016-01-30T23:50:00+00:00', 'status': 'running'}, 'next_actions': [{'command': 'attach_volume', 'error': {'code': 'action_failed', 'message': 'Action failed'}, 'finished': None, 'id': 13, 'progress': 0, 'resources': [{'id': 42, 'type': 'server'}, {'id': 554, 'type': 'volume'}], 'started': '2016-01-30T23:50:00+00:00', 'status': 'running'}], 'volume': {'created': '2016-01-30T23:50:11+00:00', 'format': 'xfs', 'id': 4711, 'labels': {'env': 'dev'}, 'linux_device': '/dev/disk/by-id/scsi-0HC_Volume_4711', 'location': {'city': 'Falkenstein', 'country': 'DE', 'description': 'Falkenstein DC Park 1', 'id': 1, 'latitude': 50.47612, 'longitude': 12.370071, 'name': 'fsn1', 'network_zone': 'eu-central'}, 'name': 'database-storage', 'protection': {'delete': False}, 'server': 12, 'size': 42, 'status': 'available'}}, 'schema': Defs.components_schemas_create_volume_response}}, 'description': 'The `volume` key contains the Volume that was just created\n\nThe `action` key contains the Action tracking Volume creation\n'}}, 'tags': ['volumes'], 'operationId': 'create_volume', 'mime': 'application/json'}
            body = Defs.components_schemas_create_volume_request
        R.body = Defs.components_schemas_create_volume_request

class volumes___id_:
    pth = "/volumes/{id}"

    class delete:
        """Deletes a volume. All Volume data is irreversibly destroyed. The Volume must not be attached to a Server and it must not have delete protection enabled. Delete a Volume"""
        class R:
            _path = ['id'];
            _ = {'responses': {'204': {'description': 'Volume deleted'}}, 'tags': ['volumes'], 'operationId': 'delete_volume'}
            id = {'type': 'string'}
        R.id = id

    class get:
        """Gets a specific Volume object. Get a Volume"""
        class R:
            _path = ['id'];
            _ = {'responses': {'200': {'content': {'application/json': {'schema': Defs.components_schemas_get_volume_response}}, 'description': 'The `volume` key contains the volume'}}, 'tags': ['volumes'], 'operationId': 'get_volume'}
            id = {'type': 'integer'}
        R.id = id

    class put:
        """Updates the Volume properties.

Note that when updating labels, the volume’s current set of labels will be replaced with the labels provided in the request body. So, for example, if you want to add a new label, you have to provide all existing labels plus the new label in the request body.
 Update a Volume"""
        class R:
            _path = ['id']; _body = ['body'];
            _ = {'requestBody': {'content': {}}, 'responses': {'200': {'content': {'application/json': {'example': {'volume': {'created': '2016-01-30T23:50:11+00:00', 'format': 'xfs', 'id': 4711, 'labels': {'labelkey': 'value'}, 'linux_device': '/dev/disk/by-id/scsi-0HC_Volume_4711', 'location': {'city': 'Falkenstein', 'country': 'DE', 'description': 'Falkenstein DC Park 1', 'id': 1, 'latitude': 50.47612, 'longitude': 12.370071, 'name': 'fsn1', 'network_zone': 'eu-central'}, 'name': 'database-storage', 'protection': {'delete': False}, 'server': 12, 'size': 42, 'status': 'available'}}, 'schema': Defs.components_schemas_replace_volume_response}}, 'description': 'The `volume` key contains the updated volume'}}, 'tags': ['volumes'], 'operationId': 'replace_volume', 'mime': 'application/json'}
            id = {'type': 'string'}
            body = Defs.components_schemas_replace_volume_request
        R.id = id
        R.body = Defs.components_schemas_replace_volume_request

class volumes___id___actions:
    pth = "/volumes/{id}/actions"

    class get:
        """Returns all Action objects for a Volume. You can `sort` the results by using the sort URI parameter, and filter them with the `status` parameter. Get all Actions for a Volume"""
        class R:
            _query = ['sort', 'status', 'page', 'per_page']; _path = ['id'];
            _ = {'responses': {'200': {'content': {'application/json': {'example': {'actions': [{'command': 'attach_volume', 'error': {'code': 'action_failed', 'message': 'Action failed'}, 'finished': '2016-01-30T23:56:00+00:00', 'id': 13, 'progress': 100, 'resources': [{'id': 42, 'type': 'server'}, {'id': 13, 'type': 'volume'}], 'started': '2016-01-30T23:55:00+00:00', 'status': 'success'}]}, 'schema': Defs.components_schemas_list_actions_for_volume_response}}, 'description': 'The `actions` key contains a list of Actions'}}, 'tags': ['volumes'], 'operationId': 'list_actions_for_volume'}
            id = {'type': 'integer'}
            sort = {'enum': ['id', 'id:asc', 'id:desc', 'command', 'command:asc', 'command:desc', 'status', 'status:asc', 'status:desc', 'progress', 'progress:asc', 'progress:desc', 'started', 'started:asc', 'started:desc', 'finished', 'finished:asc', 'finished:desc'], 'title': 'ParameterSort', 'type': 'string'}
            status = {'enum': ['running', 'success', 'error'], 'title': 'ParameterStatus', 'type': 'string'}
            page = {'type': 'integer', 'minimum': 1}
            per_page = {'type': 'integer', 'minimum': 1, 'maximum': 50}
        R.id = id
        R.sort = 'id'
        R.status = 'running'
        R.page = 0
        R.per_page = 0

class volumes___id___actions___action_id_:
    pth = "/volumes/{id}/actions/{action_id}"

    class get:
        """Returns a specific Action for a Volume. Get an Action for a Volume"""
        class R:
            _path = ['id', 'action_id'];
            _ = {'responses': {'200': {'content': {'application/json': {'example': {'action': {'command': 'attach_volume', 'error': {'code': 'action_failed', 'message': 'Action failed'}, 'finished': '2016-01-30T23:56:00+00:00', 'id': 13, 'progress': 100, 'resources': [{'id': 42, 'type': 'server'}], 'started': '2016-01-30T23:55:00+00:00', 'status': 'success'}}, 'schema': Defs.components_schemas_get_action_for_volume_response}}, 'description': 'The `action` key contains the Volume Action'}}, 'tags': ['volumes'], 'operationId': 'get_action_for_volume'}
            id = {'type': 'integer'}
            action_id = {'type': 'integer'}
        R.id = id
        R.action_id = action_id

class volumes___id___actions__attach:
    pth = "/volumes/{id}/actions/attach"

    class post:
        """Attaches a Volume to a Server. Works only if the Server is in the same Location as the Volume. Attach Volume to a Server"""
        class R:
            _path = ['id']; _body = ['body'];
            _ = {'requestBody': {'content': {}}, 'responses': {'201': {'content': {'application/json': {'example': {'action': {'command': 'attach_volume', 'error': {'code': 'action_failed', 'message': 'Action failed'}, 'finished': None, 'id': 13, 'progress': 0, 'resources': [{'id': 43, 'type': 'server'}, {'id': 554, 'type': 'volume'}], 'started': '2016-01-30T23:50:00+00:00', 'status': 'running'}}, 'schema': Defs.components_schemas_attach_volume_to_server_response}}, 'description': 'The `action` key contains the `attach_volume` Action'}}, 'tags': ['volumes'], 'operationId': 'attach_volume_to_server', 'mime': 'application/json'}
            id = {'type': 'integer'}
            body = Defs.components_schemas_attach_volume_to_server_request
        R.id = id
        R.body = Defs.components_schemas_attach_volume_to_server_request

class volumes___id___actions__change_protection:
    pth = "/volumes/{id}/actions/change_protection"

    class post:
        """Changes the protection configuration of a Volume. Change Volume Protection"""
        class R:
            _path = ['id']; _body = ['body'];
            _ = {'requestBody': {'content': {}}, 'responses': {'201': {'content': {'application/json': {'example': {'action': {'command': 'change_protection', 'error': {'code': 'action_failed', 'message': 'Action failed'}, 'finished': '2016-01-30T23:56:00+00:00', 'id': 13, 'progress': 100, 'resources': [{'id': 42, 'type': 'server'}, {'id': 554, 'type': 'volume'}], 'started': '2016-01-30T23:55:00+00:00', 'status': 'success'}}, 'schema': Defs.components_schemas_change_volume_protection_response}}, 'description': 'The `action` key contains the `change_protection` Action'}}, 'tags': ['volumes'], 'operationId': 'change_volume_protection', 'mime': 'application/json'}
            id = {'type': 'integer'}
            body = Defs.components_schemas_change_volume_protection_request
        R.id = id
        R.body = Defs.components_schemas_change_volume_protection_request

class volumes___id___actions__detach:
    pth = "/volumes/{id}/actions/detach"

    class post:
        """Detaches a Volume from the Server it’s attached to. You may attach it to a Server again at a later time. Detach Volume"""
        class R:
            _path = ['id'];
            _ = {'responses': {'201': {'content': {'application/json': {'example': {'action': {'command': 'detach_volume', 'error': {'code': 'action_failed', 'message': 'Action failed'}, 'finished': None, 'id': 13, 'progress': 0, 'resources': [{'id': 42, 'type': 'server'}], 'started': '2016-01-30T23:50:00+00:00', 'status': 'running'}}, 'schema': Defs.components_schemas_detach_volume_response}}, 'description': 'The `action` key contains the `detach_volume` Action'}}, 'tags': ['volumes'], 'operationId': 'detach_volume'}
            id = {'type': 'integer'}
        R.id = id

class volumes___id___actions__resize:
    pth = "/volumes/{id}/actions/resize"

    class post:
        """Changes the size of a Volume. Note that downsizing a Volume is not possible. Resize Volume"""
        class R:
            _path = ['id']; _body = ['body'];
            _ = {'requestBody': {'content': {}}, 'responses': {'201': {'content': {'application/json': {'example': {'action': {'command': 'resize_volume', 'error': {'code': 'action_failed', 'message': 'Action failed'}, 'finished': None, 'id': 13, 'progress': 0, 'resources': [{'id': 554, 'type': 'volume'}], 'started': '2016-01-30T23:50:00+00:00', 'status': 'running'}}, 'schema': Defs.components_schemas_resize_volume_response}}, 'description': 'The `action` key contains the `resize_volume` Action'}}, 'tags': ['volumes'], 'operationId': 'resize_volume', 'mime': 'application/json'}
            id = {'type': 'integer'}
            body = Defs.components_schemas_resize_volume_request
        R.id = id
        R.body = Defs.components_schemas_resize_volume_request

# ─────────────── Tools ─────────────────────
import requests, json, functools, inspect, os
keyw = {'import', 'while', 'continue', 'async', 'from', 'raise', 'for', 'if', 'except', 'not'}

class Tools:
    @staticmethod
    def build_req(meth):
        data, h, q = None, API.hdrs, {}
        g = lambda o, k, d=None: getattr(o, k, d)
        c = globals()[meth.__qualname__.split('.', 1)[0]]
        R = g(meth, 'R')
        if R:
            h['Content-Type'] = m = g(R, '_mime', 'application/json')
            if not 'form' in m and not 'json' in m and g(R, 'content'):
                data = R.content
            p = {a: g(R, a) for a in g(R, '_path', ())}
            pth = c.pth.format(**p)
            for a in g(R, '_query', ()):
                v = g(R, a)
                if v is not None:
                    q[a] = g(R, a)
            b = g(R, 'body')
            if b:
                data = Tools.obj(b)
            f = g(R, '_formData')
            if f:
                data = {k: Tools.obj(g(R, k)) for k in f}
                data = data['form'] if f == ['form'] else data
        return meth.__name__, pth, q, data, h

    @staticmethod
    def obj(def_, is_=isinstance, g=getattr):
        if is_(def_, tuple):
            return def_[0]
        if callable(def_):
            if inspect.isfunction(def_):
                def_ = def_()
        if is_(def_, (float, int, bool, str)):
            return def_
        obj = Tools.obj
        if is_(def_, list):
            return [obj(def_[0])]
        dict_ = lambda d: d.get('__val__', d)
        if is_(def_, dict):
            return dict_({k: obj(v) for k, v in def_.items()})
        R = g(def_, 'R', 0)
        if R:
            return obj(R)
        l = g(def_, '_attrs', [i for i in dir(def_) if not i[0] == '_'])
        r = {k: obj(g(def_, k)) for k in l if not is_(g(def_, k), dict)}
        return dict_(r)

    @staticmethod
    def send(meth, *args):
        if args:
            meth = args[0]   # ico in line
        env = os.environ.get
        getenv = lambda v: env(v[1:], '') if (v and v[0] == '$') else v

        def repl(s):
            if isinstance(s, str):
                for k in keyw:
                    s = s.replace(f'{k}__', k)
            else:
                s = json.loads(repl(json.dumps(s)))
            return s

        try:
            methd, pth, params, data, h = Tools.build_req(meth)
            params = repl(params)
            host = f'{API.host}'
            if not '://' in host:
                host = 'https://' + host
            url = repl(f'{host}{API.base}{pth}')
            h = {k: getenv(v) for k, v in h.items()}
            kw = {'params': params, 'headers': h, 'timeout': timeout}
            if getenv(API.passw):
                kw['auth'] = (getenv(API.user), getenv(API.passw))
            if isinstance(data, (list, dict)):
                kw['data'] = repl(data)
            req = getattr(requests, methd)
            if result == 0:   # no send
                return [url, methd, kw]
            if 'json' in h.get('Content-Type') and data is not None:
                kw['data'] = json.dumps(kw['data'])
            req = req(url, **kw)
            if result == 3:
                return req   # show all
            r = {'status': req.status_code}
            try:
                r['resp'] = json.loads(req.text)
            except:
                r['resp'] = req.text
        except Exception as ex:
            r = {'Exception': str(ex)}
        if result == 2:
            r.update(dict(kw))
            r['url'] = url
        return r


    

if __name__ == '__main__':
    import sys, os
    match = '' if len(sys.argv) == 1 else sys.argv[1]
    a, result = ([1], 0) if 'testmode' in os.environ else ([0], 2)
    for m in methods():
        if callable(m) and match in m.__qualname__:
            print(f'Calling {m.__qualname__}', file=sys.stderr)
            if not a[0]:
                y = input('Ok [y/a(lways)/N/q]? ').lower()
                if y == 'q': sys.exit(0)
                if y == 'a': a[0] = 1
                if y not in {'y', 'a'}: continue
            print(json.dumps(Tools.send(m), indent=4, sort_keys=True))
    