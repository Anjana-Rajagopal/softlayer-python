"""
    SoftLayer.CLI.routes
    ~~~~~~~~~~~~~~~~~~~~~
    This is how all commands are registered with the CLI.

    :license: MIT, see LICENSE for more details.
"""

ALL_ROUTES = [
    ('shell', 'SoftLayer.shell.core:cli'),

    ('call-api', 'SoftLayer.CLI.call_api:cli'),

    ('virtual', 'SoftLayer.CLI.virt'),
    ('virtual:cancel', 'SoftLayer.CLI.virt.cancel:cli'),
    ('virtual:capture', 'SoftLayer.CLI.virt.capture:cli'),
    ('virtual:create', 'SoftLayer.CLI.virt.create:cli'),
    ('virtual:create-options', 'SoftLayer.CLI.virt.create_options:cli'),
    ('virtual:detail', 'SoftLayer.CLI.virt.detail:cli'),
    ('virtual:dns-sync', 'SoftLayer.CLI.virt.dns:cli'),
    ('virtual:edit', 'SoftLayer.CLI.virt.edit:cli'),
    ('virtual:list', 'SoftLayer.CLI.virt.list:cli'),
    ('virtual:pause', 'SoftLayer.CLI.virt.power:pause'),
    ('virtual:power-off', 'SoftLayer.CLI.virt.power:power_off'),
    ('virtual:power-on', 'SoftLayer.CLI.virt.power:power_on'),
    ('virtual:rescue', 'SoftLayer.CLI.virt.power:rescue'),
    ('virtual:resume', 'SoftLayer.CLI.virt.power:resume'),
    ('virtual:ready', 'SoftLayer.CLI.virt.ready:cli'),
    ('virtual:reboot', 'SoftLayer.CLI.virt.power:reboot'),
    ('virtual:reload', 'SoftLayer.CLI.virt.reload:cli'),
    ('virtual:upgrade', 'SoftLayer.CLI.virt.upgrade:cli'),
    ('virtual:credentials', 'SoftLayer.CLI.virt.credentials:cli'),

    ('cdn', 'SoftLayer.CLI.cdn'),
    ('cdn:detail', 'SoftLayer.CLI.cdn.detail:cli'),
    ('cdn:list', 'SoftLayer.CLI.cdn.list:cli'),
    ('cdn:load', 'SoftLayer.CLI.cdn.load:cli'),
    ('cdn:origin-add', 'SoftLayer.CLI.cdn.origin_add:cli'),
    ('cdn:origin-list', 'SoftLayer.CLI.cdn.origin_list:cli'),
    ('cdn:origin-remove', 'SoftLayer.CLI.cdn.origin_remove:cli'),
    ('cdn:purge', 'SoftLayer.CLI.cdn.purge:cli'),

    ('config', 'SoftLayer.CLI.config'),
    ('config:setup', 'SoftLayer.CLI.config.setup:cli'),
    ('config:show', 'SoftLayer.CLI.config.show:cli'),
    ('setup', 'SoftLayer.CLI.config.setup:cli'),

    ('dns', 'SoftLayer.CLI.dns'),
    ('dns:import', 'SoftLayer.CLI.dns.zone_import:cli'),
    ('dns:record-add', 'SoftLayer.CLI.dns.record_add:cli'),
    ('dns:record-edit', 'SoftLayer.CLI.dns.record_edit:cli'),
    ('dns:record-list', 'SoftLayer.CLI.dns.record_list:cli'),
    ('dns:record-remove', 'SoftLayer.CLI.dns.record_remove:cli'),
    ('dns:zone-create', 'SoftLayer.CLI.dns.zone_create:cli'),
    ('dns:zone-delete', 'SoftLayer.CLI.dns.zone_delete:cli'),
    ('dns:zone-list', 'SoftLayer.CLI.dns.zone_list:cli'),
    ('dns:zone-print', 'SoftLayer.CLI.dns.zone_print:cli'),

    ('block', 'SoftLayer.CLI.block'),
    ('block:volume-list', 'SoftLayer.CLI.block.list:cli'),
    ('block:volume-detail', 'SoftLayer.CLI.block.detail:cli'),
    ('block:volume-cancel', 'SoftLayer.CLI.block.cancel:cli'),
    ('block:volume-order', 'SoftLayer.CLI.block.order:cli'),

    ('block:snapshot-list', 'SoftLayer.CLI.block.snapshot_list:cli'),
    ('block:snapshot-delete', 'SoftLayer.CLI.block.snapshot_delete:cli'),

    ('block:access-list', 'SoftLayer.CLI.block.access_list:cli'),
    ('block:access-authorize', 'SoftLayer.CLI.block.access.authorize:cli'),
    ('block:access-revoke', 'SoftLayer.CLI.block.access.revoke:cli'),

    ('firewall', 'SoftLayer.CLI.firewall'),
    ('firewall:add', 'SoftLayer.CLI.firewall.add:cli'),
    ('firewall:cancel', 'SoftLayer.CLI.firewall.cancel:cli'),
    ('firewall:detail', 'SoftLayer.CLI.firewall.detail:cli'),
    ('firewall:edit', 'SoftLayer.CLI.firewall.edit:cli'),
    ('firewall:list', 'SoftLayer.CLI.firewall.list:cli'),

    ('globalip', 'SoftLayer.CLI.globalip'),
    ('globalip:assign', 'SoftLayer.CLI.globalip.assign:cli'),
    ('globalip:cancel', 'SoftLayer.CLI.globalip.cancel:cli'),
    ('globalip:create', 'SoftLayer.CLI.globalip.create:cli'),
    ('globalip:list', 'SoftLayer.CLI.globalip.list:cli'),
    ('globalip:unassign', 'SoftLayer.CLI.globalip.unassign:cli'),

    ('image', 'SoftLayer.CLI.image'),
    ('image:delete', 'SoftLayer.CLI.image.delete:cli'),
    ('image:detail', 'SoftLayer.CLI.image.detail:cli'),
    ('image:edit', 'SoftLayer.CLI.image.edit:cli'),
    ('image:list', 'SoftLayer.CLI.image.list:cli'),
    ('image:import', 'SoftLayer.CLI.image.import:cli'),
    ('image:export', 'SoftLayer.CLI.image.export:cli'),

    ('iscsi', 'SoftLayer.CLI.iscsi'),
    ('iscsi:cancel', 'SoftLayer.CLI.iscsi.cancel:cli'),
    ('iscsi:create', 'SoftLayer.CLI.iscsi.create:cli'),
    ('iscsi:detail', 'SoftLayer.CLI.iscsi.detail:cli'),
    ('iscsi:list', 'SoftLayer.CLI.iscsi.list:cli'),

    ('loadbal', 'SoftLayer.CLI.loadbal'),
    ('loadbal:cancel', 'SoftLayer.CLI.loadbal.cancel:cli'),
    ('loadbal:create', 'SoftLayer.CLI.loadbal.create:cli'),
    ('loadbal:create-options', 'SoftLayer.CLI.loadbal.create_options:cli'),
    ('loadbal:detail', 'SoftLayer.CLI.loadbal.detail:cli'),
    ('loadbal:group-add', 'SoftLayer.CLI.loadbal.group_add:cli'),
    ('loadbal:group-delete', 'SoftLayer.CLI.loadbal.group_delete:cli'),
    ('loadbal:group-edit', 'SoftLayer.CLI.loadbal.group_edit:cli'),
    ('loadbal:group-reset', 'SoftLayer.CLI.loadbal.group_reset:cli'),
    ('loadbal:health-checks', 'SoftLayer.CLI.loadbal.health_checks:cli'),
    ('loadbal:list', 'SoftLayer.CLI.loadbal.list:cli'),
    ('loadbal:routing-methods', 'SoftLayer.CLI.loadbal.routing_methods:cli'),
    ('loadbal:routing-types', 'SoftLayer.CLI.loadbal.routing_types:cli'),
    ('loadbal:service-add', 'SoftLayer.CLI.loadbal.service_add:cli'),
    ('loadbal:service-delete', 'SoftLayer.CLI.loadbal.service_delete:cli'),
    ('loadbal:service-edit', 'SoftLayer.CLI.loadbal.service_edit:cli'),
    ('loadbal:service-toggle', 'SoftLayer.CLI.loadbal.service_toggle:cli'),

    ('messaging', 'SoftLayer.CLI.mq'),
    ('messaging:accounts-list', 'SoftLayer.CLI.mq.accounts_list:cli'),
    ('messaging:endpoints-list', 'SoftLayer.CLI.mq.endpoints_list:cli'),
    ('messaging:ping', 'SoftLayer.CLI.mq.ping:cli'),
    ('messaging:queue-add', 'SoftLayer.CLI.mq.queue_add:cli'),
    ('messaging:queue-detail', 'SoftLayer.CLI.mq.queue_detail:cli'),
    ('messaging:queue-edit', 'SoftLayer.CLI.mq.queue_edit:cli'),
    ('messaging:queue-list', 'SoftLayer.CLI.mq.queue_list:cli'),
    ('messaging:queue-pop', 'SoftLayer.CLI.mq.queue_pop:cli'),
    ('messaging:queue-push', 'SoftLayer.CLI.mq.queue_push:cli'),
    ('messaging:queue-remove', 'SoftLayer.CLI.mq.queue_remove:cli'),
    ('messaging:topic-add', 'SoftLayer.CLI.mq.topic_add:cli'),
    ('messaging:topic-detail', 'SoftLayer.CLI.mq.topic_detail:cli'),
    ('messaging:topic-list', 'SoftLayer.CLI.mq.topic_list:cli'),
    ('messaging:topic-push', 'SoftLayer.CLI.mq.topic_push:cli'),
    ('messaging:topic-remove', 'SoftLayer.CLI.mq.topic_remove:cli'),
    ('messaging:topic-subscribe', 'SoftLayer.CLI.mq.topic_subscribe:cli'),
    ('messaging:topic-unsubscribe', 'SoftLayer.CLI.mq.topic_unsubscribe:cli'),

    ('metadata', 'SoftLayer.CLI.metadata:cli'),

    ('nas', 'SoftLayer.CLI.nas'),
    ('nas:list', 'SoftLayer.CLI.nas.list:cli'),
    ('nas:credentials', 'SoftLayer.CLI.nas.credentials:cli'),

    ('object-storage', 'SoftLayer.CLI.object_storage'),
    ('object-storage:accounts',
     'SoftLayer.CLI.object_storage.list_accounts:cli'),
    ('object-storage:endpoints',
     'SoftLayer.CLI.object_storage.list_endpoints:cli'),

    ('rwhois', 'SoftLayer.CLI.rwhois'),
    ('rwhois:edit', 'SoftLayer.CLI.rwhois.edit:cli'),
    ('rwhois:show', 'SoftLayer.CLI.rwhois.show:cli'),

    ('hardware', 'SoftLayer.CLI.hardware'),
    ('hardware:cancel', 'SoftLayer.CLI.hardware.cancel:cli'),
    ('hardware:cancel-reasons', 'SoftLayer.CLI.hardware.cancel_reasons:cli'),
    ('hardware:create', 'SoftLayer.CLI.hardware.create:cli'),
    ('hardware:create-options', 'SoftLayer.CLI.hardware.create_options:cli'),
    ('hardware:detail', 'SoftLayer.CLI.hardware.detail:cli'),
    ('hardware:edit', 'SoftLayer.CLI.hardware.edit:cli'),
    ('hardware:list', 'SoftLayer.CLI.hardware.list:cli'),
    ('hardware:power-cycle', 'SoftLayer.CLI.hardware.power:power_cycle'),
    ('hardware:power-off', 'SoftLayer.CLI.hardware.power:power_off'),
    ('hardware:power-on', 'SoftLayer.CLI.hardware.power:power_on'),
    ('hardware:reboot', 'SoftLayer.CLI.hardware.power:reboot'),
    ('hardware:reload', 'SoftLayer.CLI.hardware.reload:cli'),
    ('hardware:credentials', 'SoftLayer.CLI.hardware.credentials:cli'),
    ('hardware:update-firmware', 'SoftLayer.CLI.hardware.update_firmware:cli'),

    ('snapshot', 'SoftLayer.CLI.snapshot'),
    ('snapshot:cancel', 'SoftLayer.CLI.snapshot.cancel:cli'),
    ('snapshot:create', 'SoftLayer.CLI.snapshot.create:cli'),
    ('snapshot:create-space', 'SoftLayer.CLI.snapshot.create_space:cli'),
    ('snapshot:list', 'SoftLayer.CLI.snapshot.list:cli'),
    ('snapshot:restore-volume', 'SoftLayer.CLI.snapshot.restore_volume:cli'),

    ('sshkey', 'SoftLayer.CLI.sshkey'),
    ('sshkey:add', 'SoftLayer.CLI.sshkey.add:cli'),
    ('sshkey:remove', 'SoftLayer.CLI.sshkey.remove:cli'),
    ('sshkey:edit', 'SoftLayer.CLI.sshkey.edit:cli'),
    ('sshkey:list', 'SoftLayer.CLI.sshkey.list:cli'),
    ('sshkey:print', 'SoftLayer.CLI.sshkey.print:cli'),

    ('ssl', 'SoftLayer.CLI.ssl'),
    ('ssl:add', 'SoftLayer.CLI.ssl.add:cli'),
    ('ssl:download', 'SoftLayer.CLI.ssl.download:cli'),
    ('ssl:edit', 'SoftLayer.CLI.ssl.edit:cli'),
    ('ssl:list', 'SoftLayer.CLI.ssl.list:cli'),
    ('ssl:remove', 'SoftLayer.CLI.ssl.remove:cli'),

    ('subnet', 'SoftLayer.CLI.subnet'),
    ('subnet:cancel', 'SoftLayer.CLI.subnet.cancel:cli'),
    ('subnet:create', 'SoftLayer.CLI.subnet.create:cli'),
    ('subnet:detail', 'SoftLayer.CLI.subnet.detail:cli'),
    ('subnet:list', 'SoftLayer.CLI.subnet.list:cli'),
    ('subnet:lookup', 'SoftLayer.CLI.subnet.lookup:cli'),

    ('ticket', 'SoftLayer.CLI.ticket'),
    ('ticket:create', 'SoftLayer.CLI.ticket.create:cli'),
    ('ticket:detail', 'SoftLayer.CLI.ticket.detail:cli'),
    ('ticket:list', 'SoftLayer.CLI.ticket.list:cli'),
    ('ticket:update', 'SoftLayer.CLI.ticket.update:cli'),
    ('ticket:upload', 'SoftLayer.CLI.ticket.upload:cli'),
    ('ticket:subjects', 'SoftLayer.CLI.ticket.subjects:cli'),
    ('ticket:summary', 'SoftLayer.CLI.ticket.summary:cli'),
    ('ticket:attach', 'SoftLayer.CLI.ticket.attach:cli'),
    ('ticket:detach', 'SoftLayer.CLI.ticket.detach:cli'),

    ('vlan', 'SoftLayer.CLI.vlan'),
    ('vlan:detail', 'SoftLayer.CLI.vlan.detail:cli'),
    ('vlan:list', 'SoftLayer.CLI.vlan.list:cli'),

    ('summary', 'SoftLayer.CLI.summary:cli'),
]

ALL_ALIASES = {
    'hw': 'hardware',
    'lb': 'loadbal',
    'meta': 'metadata',
    'my': 'metadata',
    'server': 'hardware',
    'vm': 'virtual',
    'vs': 'virtual',
}
