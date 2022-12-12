#!/usr/bin/env python

# type: ignore
'''
Swagger API Tester
openapi.json

3.0.0
'''
result = 1
str_dflt = ''
timeout = 5
# -

class API:
    user, passw = '$user', '$password'
    host = 'https://api.dynu.com/v2'
    base = ''
    hdrs = {}


hostname = 'test.mydomain.com'
id = 8358362
dnsRecordId = 758426278
webRedirectId = 758426278
blacklistId = 758426278
whitelistId = 758426278

# fmt:off
methods = lambda: ( # :clear :doc :eval all :exec single :wrap p = Tools.send({})
 '🟩', dns.get,
 '🟪', dns.post,
 '🟩', dns__getroot___hostname_.get,
 '🟩', dns__record___hostname_.get,
 '🟩', dns___id_.get,
 '🟪', dns___id_.post,
 '🟥', dns___id_.delete,
 '🟩', dns___id___dnssec.get,
 '🟩', dns___id___dnssec__enable.get,
 '🟩', dns___id___dnssec__disable.get,
 '🟩', dns___id___record.get,
 '🟪', dns___id___record.post,
 '🟩', dns___id___record___dnsRecordId_.get,
 '🟪', dns___id___record___dnsRecordId_.post,
 '🟥', dns___id___record___dnsRecordId_.delete,
 '🟩', dns___id___webredirect.get,
 '🟪', dns___id___webredirect.post,
 '🟩', dns___id___webRedirect___webRedirectId_.get,
 '🟪', dns___id___webRedirect___webRedirectId_.post,
 '🟥', dns___id___webRedirect___webRedirectId_.delete,
 '🟩', dns__ipUpdateHistory.get,
 '🟩', dns__group.get,
 '🟪', dns__group.post,
 '🟪', dns__group___id_.post,
 '🟥', dns__group___id_.delete,
 '🟩', dns__limit.get,
 '🟩', dns___id___limit.get,
 '🟩', domain.get,
 '🟩', domain___id_.get,
 '🟩', domain___id___autorenewEnable.get,
 '🟩', domain___id___autorenewDisable.get,
 '🟩', domain___id___lock.get,
 '🟩', domain___id___unlock.get,
 '🟩', domain___id___nameServer.get,
 '🟥', domain___id___nameServer.delete,
 '🟩', domain___id___nameServer__add.get,
 '🟩', domain___id___nameServer__primary.get,
 '🟩', domain___id___cancel.get,
 '🟩', email.get,
 '🟩', email___id_.get,
 '🟩', email___id___deliveryQueue.get,
 '🟩', email___id___blacklist.get,
 '🟪', email___id___blacklist.post,
 '🟩', email___id___blacklist___blacklistId_.get,
 '🟪', email___id___blacklist___blacklistId_.post,
 '🟥', email___id___blacklist___blacklistId_.delete,
 '🟩', email___id___whitelist.get,
 '🟪', email___id___whitelist.post,
 '🟩', email___id___whitelist___whitelistId_.get,
 '🟪', email___id___whitelist___whitelistId_.post,
 '🟥', email___id___whitelist___whitelistId_.delete,
 '🟩', monitor__limit.get,
 '🟩', monitor.get,
 '🟪', monitor.post,
 '🟩', monitor___id_.get,
 '🟥', monitor___id_.delete,
 '🟩', monitor___id___pause.get,
 '🟩', monitor___id___unpause.get,
 '🟩', ping.get,
 '🟪', ping.post,
) 
# fmt:on


class Defs:
    class components_responses_200:
        """#/components/responses/200"""
        class R:
            description = 'Success.'
            content = {'application/json': {'schema': lambda: Defs.components_schemas_apiResponse}}
            examples = {'Success': {'statusCode': 200}}
    class components_responses_200DNSDNSSECGetById:
        """#/components/responses/200DNSDNSSECGetById"""
        class R:
            description = 'DS record for DNSSEC of a domain for DNS service.'
            content = {'application/json': {'schema': {'allOf': [lambda: Defs.components_schemas_apiResponse, lambda: Defs.components_schemas_DNS_dnsSec]}}}
            examples = {'Success': {'statusCode': 200, 'id': 568335462, 'domainName': 'example.com', 'dsRecord': 'example.com. 86400 IN DS 13534 13 2 58E0F0314C93FE095C41F2813DB1C28DE5214770F588E7BA9A71962F7DB643C4', 'digest': '58E0F0314C93FE095C41F2813DB1C28DE5214770F588E7BA9A71962F7DB643C4', 'digestType': 'Sha256', 'algorithm': 13, 'publicKey': '+1xulhSFjEGp/Y+4m8IHLACNMMFHdmQEZ6zY30ToQpmNPPkwC0Tn9y5XL1UBKr2Fs+A7ZuEV4pHEznMBT3rUWw==', 'keyTag': 13534, 'flags': 257}, 'Failure': {'exception': {'statusCode': 404, 'type': 'Request Exception', 'message': 'Invalid.'}}}
    class components_responses_200DNSDomain:
        """#/components/responses/200DNSDomain"""
        class R:
            description = 'A list of domains for DNS service.'
            content = {'application/json': {'schema': {'allOf': [lambda: Defs.components_schemas_apiResponse, {'type': 'object', 'properties': {'domains': {'type': 'array', 'items': lambda: Defs.components_schemas_DNS_domain}}}]}}}
            examples = {'default': {'statusCode': 200, 'domains': [{'id': 358362, 'name': 'workplace.mywire.org', 'unicodeName': 'workplace.mywire.org', 'token': 'yc0bia6g92p49061wko1', 'state': 'Complete', 'group': 'Office', 'ipv4Address': '207.52.45.12', 'ttl': 300, 'ipv4': True, 'ipv6': False, 'ipv4WildcardAlias': False, 'createdOn': '2012-08-09T10:20:50.52Z', 'updatedOn': '2018-07-19T13:42:08.52Z'}, {'id': 365321, 'name': 'organic.org', 'unicodeName': 'organic.org', 'token': '8q34u7mhplopq6vwpmkh', 'state': 'Complete', 'ipv4Address': '207.52.45.12', 'ipv6Address': '2001:38e4:38e4::8', 'ttl': 180, 'ipv4': True, 'ipv6': True, 'ipv4WildcardAlias': True, 'ipv6WildcardAlias': True, 'allowZoneTransfer': False, 'dnssec': True, 'createdOn': '2014-04-12T23:20:50.52Z', 'updatedOn': '2018-05-08T14:52:11.52Z'}, {'id': 428546, 'name': 'xn--witowa-g1a3lpy.pl', 'unicodeName': 'świętować.pl', 'token': 'p2nqroylqmohjrq66mks', 'state': 'Complete', 'group': 'hosting', 'ipv4Address': '105.46.76.33', 'ttl': 180, 'ipv4': True, 'ipv6': False, 'ipv4WildcardAlias': True, 'ipv6WildcardAlias': False, 'allowZoneTransfer': False, 'dnssec': False, 'createdOn': '2018-04-12T23:20:50.52Z', 'updatedOn': '2018-07-19T13:42:08.52Z'}]}}
    class components_responses_200DNSDomainGetById:
        """#/components/responses/200DNSDomainGetById"""
        class R:
            description = 'Details of a domain for DNS service.'
            content = {'application/json': {'schema': {'allOf': [lambda: Defs.components_schemas_apiResponse, lambda: Defs.components_schemas_DNS_domain]}}}
            examples = {'Success': {'statusCode': 200, 'id': 358362, 'name': 'workplace.mywire.org', 'unicodeName': 'workplace.mywire.org', 'token': 'yc0bia6g92p49061wko1', 'state': 'Complete', 'group': 'Office', 'ipv4Address': '207.52.45.12', 'ttl': 300, 'ipv4': True, 'ipv6': False, 'ipv4WildcardAlias': False, 'createdOn': '2012-08-09T10:20:50.52Z', 'updatedOn': '2018-07-19T13:42:08.52Z'}, 'Failure': {'exception': {'statusCode': 404, 'type': 'Request Exception', 'message': 'Invalid.'}}}
    class components_responses_200DNSGroup:
        """#/components/responses/200DNSGroup"""
        class R:
            description = 'A list of groups to which hosts are assigned to.'
            content = {'application/json': {'schema': {'allOf': [lambda: Defs.components_schemas_apiResponse, {'type': 'object', 'properties': {'groups': {'type': 'array', 'items': lambda: Defs.components_schemas_DNS_dnsGroup}}}]}}}
            examples = {'default': {'statusCode': 200, 'groups': [{'id': 108510696, 'domainName': 'workplace.mywire.org', 'groupName': 'work'}, {'id': 408455637, 'domainName': 'organic.org', 'groupName': 'datacenter'}, {'id': 208395892, 'domainName': 'xn--witowa-g1a3lpy.pl', 'groupName': None}, {'id': 101758524, 'domainName': 'home.mywire.org', 'groupName': None}]}}
    class components_responses_200DNSGroupGetById:
        """#/components/responses/200DNSGroupGetById"""
        class R:
            description = 'Details of the group.'
            content = {'application/json': {'schema': {'allOf': [lambda: Defs.components_schemas_apiResponse, lambda: Defs.components_schemas_DNS_dnsGroup]}}}
            examples = {'Success': {'statusCode': 200, 'id': 35836280, 'domainName': 'mydomain.com', 'groupName': 'work'}, 'Failure': {'exception': {'statusCode': 404, 'type': 'Request Exception', 'message': 'Invalid.'}}}
    class components_responses_200DNSHostnameGetGetrootByHostname:
        """#/components/responses/200DNSHostnameGetGetrootByHostname"""
        class R:
            description = 'Root domain of DNS service along with the hostname and node.'
            content = {'application/json': {'schema': {'allOf': [lambda: Defs.components_schemas_apiResponse, lambda: Defs.components_schemas_DNS_hostname]}}}
            examples = {'Success': {'statusCode': 200, 'id': 358362, 'hostname': 'secure.mydomain.com', 'domainName': 'mydomain.com', 'node': 'secure'}, 'Failure': {'exception': {'statusCode': 404, 'type': 'Request Exception', 'message': 'Invalid.'}}}
    class components_responses_200DNSIPUpdateHistory:
        """#/components/responses/200DNSIPUpdateHistory"""
        class R:
            description = 'A list of IP address updates.'
            content = {'application/json': {'schema': {'allOf': [lambda: Defs.components_schemas_apiResponse, {'type': 'object', 'properties': {'domains': {'type': 'array', 'items': lambda: Defs.components_schemas_DNS_ipUpdate}}}]}}}
            examples = {'default': {'statusCode': 200, 'ipUpdateHistory': [{'id': 108510696, 'responseId': 'QQRM636796275004079722', 'updateStatus': 'No Change', 'ipv4Address': '97.124.226.198', 'ipv6Address': '2602:61:7ce2:c600:6061:4749:3257:3de8', 'queryString': '/nic/clientupdate?group=&myipv4=97.124.226.198&myipv6=2602:0061:7ce2:c600:6061:4749:3257:3de8', 'userAgent': 'Dynu.Service 5.3.0.0', 'ssl': True, 'updatedOn': '2018-07-19T13:42:08.52Z'}, {'id': 108455637, 'responseId': 'JTBS636796202648455271', 'updateStatus': 'Good', 'ipv4Address': '97.124.226.198', 'ipv6Address': '2602:61:7ce2:c600:6061:4749:3257:3de8', 'queryString': '/nic/clientupdate?group=&myipv4=97.124.226.198&myipv6=2602:61:7ce2:c600:6061:4749:3257:3de8', 'userAgent': 'Dynu.Service 5.3.0.0', 'ssl': True, 'updatedOn': '2018-07-11T43:16:18.32Z'}, {'id': 108395892, 'responseId': 'POFT636796162019617771', 'updateStatus': 'No Change', 'ipv4Address': '207.81.26.211', 'ipv6Address': None, 'queryString': '/nic/clientupdate?group=&myipv4=207.81.26.211&ipv6=no', 'userAgent': 'Dynu.Service 5.3.0.0', 'ssl': True, 'updatedOn': '2018-07-10T18:39:48.12Z'}]}}
    class components_responses_200DNSLimit:
        """#/components/responses/200DNSLimit"""
        class R:
            description = 'Limits associated with hostnames.'
            content = {'application/json': {'schema': {'allOf': [lambda: Defs.components_schemas_apiResponse, lambda: Defs.components_schemas_DNS_limit]}}}
            examples = {'Success': {'statusCode': 200, 'activeCount': 32, 'remainingCount': 68}, 'Failure': {'statusCode': 503, 'type': 'Quota Exception', 'message': 'Failed.'}}
    class components_responses_200DNSRecord:
        """#/components/responses/200DNSRecord"""
        class R:
            description = 'A list of DNS records for DNS service.'
            content = {'application/json': {'schema': {'allOf': [lambda: Defs.components_schemas_apiResponse, {'type': 'object', 'properties': {'dnsRecords': {'type': 'array', 'items': {'anyOf': [lambda: Defs.components_schemas_DNS_dnsRecordA, lambda: Defs.components_schemas_DNS_dnsRecordAAAA, lambda: Defs.components_schemas_DNS_dnsRecordCAA, lambda: Defs.components_schemas_DNS_dnsRecordCNAME, lambda: Defs.components_schemas_DNS_dnsRecordHINFO, lambda: Defs.components_schemas_DNS_dnsRecordLOC, lambda: Defs.components_schemas_DNS_dnsRecordMX, lambda: Defs.components_schemas_DNS_dnsRecordNS, lambda: Defs.components_schemas_DNS_dnsRecordPTR, lambda: Defs.components_schemas_DNS_dnsRecordRP, lambda: Defs.components_schemas_DNS_dnsRecordSOA, lambda: Defs.components_schemas_DNS_dnsRecordSPF, lambda: Defs.components_schemas_DNS_dnsRecordSRV, lambda: Defs.components_schemas_DNS_dnsRecordSSHFP, lambda: Defs.components_schemas_DNS_dnsRecordTLSA, lambda: Defs.components_schemas_DNS_dnsRecordTXT, lambda: Defs.components_schemas_DNS_dnsRecordURI]}}}}]}}}
            examples = {'default': {'statusCode': 200, 'dnsRecords': [{'id': 35836280, 'domainId': 8246254, 'domainName': 'mydomain.com', 'nodeName': 'mail', 'hostname': 'mail.mydomain.com', 'recordType': 'A', 'ttl': 300, 'state': True, 'content': '204.25.79.214', 'updatedOn': '2018-07-19T13:42:08.52Z', 'group': 'work', 'ipv4Address': '204.25.79.214'}, {'id': 45805321, 'domainId': 8246254, 'domainName': 'mydomain.com', 'nodeName': 'www', 'hostname': 'www.mydomain.com', 'recordType': 'CNAME', 'ttl': 600, 'state': True, 'content': 'www.anotherdomain.com', 'updatedOn': '2018-07-19T13:42:08.52Z', 'host': 'www.anotherdomain.com'}]}}
    class components_responses_200DNSRecordGetById:
        """#/components/responses/200DNSRecordGetById"""
        class R:
            description = 'Details of a DNS record for DNS service.'
            content = {'application/json': {'schema': {'allOf': [lambda: Defs.components_schemas_apiResponse, {'oneOf': [lambda: Defs.components_schemas_DNS_dnsRecordA, lambda: Defs.components_schemas_DNS_dnsRecordAAAA, lambda: Defs.components_schemas_DNS_dnsRecordCAA, lambda: Defs.components_schemas_DNS_dnsRecordCNAME, lambda: Defs.components_schemas_DNS_dnsRecordHINFO, lambda: Defs.components_schemas_DNS_dnsRecordLOC, lambda: Defs.components_schemas_DNS_dnsRecordMX, lambda: Defs.components_schemas_DNS_dnsRecordNS, lambda: Defs.components_schemas_DNS_dnsRecordPTR, lambda: Defs.components_schemas_DNS_dnsRecordRP, lambda: Defs.components_schemas_DNS_dnsRecordSOA, lambda: Defs.components_schemas_DNS_dnsRecordSPF, lambda: Defs.components_schemas_DNS_dnsRecordSRV, lambda: Defs.components_schemas_DNS_dnsRecordSSHFP, lambda: Defs.components_schemas_DNS_dnsRecordTLSA, lambda: Defs.components_schemas_DNS_dnsRecordTXT, lambda: Defs.components_schemas_DNS_dnsRecordURI]}]}}}
            examples = {'Success': {'statusCode': 200, 'id': 35836280, 'domainId': 8246254, 'domainName': 'mydomain.com', 'nodeName': 'www', 'hostname': 'www.mydomain.com', 'recordType': 'A', 'ttl': 300, 'state': True, 'content': '204.25.79.214', 'updatedOn': '2018-07-19T13:42:08.52Z', 'group': 'work', 'ipv4Address': '204.25.79.214'}, 'Failure': {'exception': {'statusCode': 501, 'type': 'Argument Exception', 'message': 'Invalid.'}}}
    class components_responses_200DNSRecordLimit:
        """#/components/responses/200DNSRecordLimit"""
        class R:
            description = 'Limits associated with DNS records.'
            content = {'application/json': {'schema': {'allOf': [lambda: Defs.components_schemas_apiResponse, {'type': 'object', 'properties': {'domains': {'type': 'array', 'items': lambda: Defs.components_schemas_DNS_recordLimit}}}]}}}
            examples = {'Member': {'statusCode': 200, 'limits': [{'recordTypes': ['A', 'AAAA', 'AFSDB', 'CAA', 'CNAME', 'HINFO', 'KEY', 'LOC', 'MX', 'NS', 'NAPTR', 'PF', 'PTR', 'RP', 'SPF', 'SRV', 'SSHFP', 'TLSA', 'TXT', 'UF', 'URI'], 'activeCount': 149, 'remainingCount': 351}]}, 'NonMember': {'statusCode': 200, 'limits': [{'recordTypes': ['A', 'AAAA'], 'activeCount': 3, 'remainingCount': 1}, {'recordTypes': ['MX'], 'activeCount': 2, 'remainingCount': 2}, {'recordTypes': ['AFSDB', 'CAA', 'CNAME', 'HINFO', 'KEY', 'LOC', 'PTR', 'RP', 'SPF', 'SRV', 'SSHFP', 'TLSA', 'TXT', 'URI'], 'activeCount': 3, 'remainingCount': 1}, {'recordTypes': ['PF', 'UF'], 'activeCount': 0, 'remainingCount': 4}]}}
    class components_responses_200Domain:
        """#/components/responses/200Domain"""
        class R:
            description = 'A list of domains.'
            content = {'application/json': {'schema': {'allOf': [lambda: Defs.components_schemas_apiResponse, {'type': 'object', 'properties': {'domains': {'type': 'array', 'items': lambda: Defs.components_schemas_Domain_domain}}}]}}}
            examples = {'default': {'statusCode': 200, 'domains': [{'id': 358362, 'name': 'mydomain.com', 'unicodeName': 'mydomain.com', 'token': 'yc0bia6g92p49061wko1', 'state': 'Complete', 'autoRenew': True, 'whoisProtected': False, 'createdOn': '2014-04-12T23:20:50.52Z', 'updatedOn': '2017-07-19T13:42:08.52Z', 'expires': '2019-04-12T23:32:13.52Z'}, {'id': 365321, 'name': 'organic.org', 'unicodeName': 'organic.org', 'token': 'i6ge0g76pqa890f01vyv', 'state': 'AwaitingPayment', 'autoRenew': True, 'whoisProtected': False, 'createdOn': '2017-04-12T23:20:50.52Z', 'updatedOn': '2017-07-19T13:42:08.52Z', 'expires': None}, {'id': 428546, 'name': 'xn--witowa-g1a3lpy.pl', 'unicodeName': 'świętować.pl', 'token': '8gzd6pu5kffa8q6wo0nt', 'state': 'TransferPending', 'autoRenew': True, 'whoisProtected': False, 'createdOn': '2017-04-12T23:20:50.52Z', 'updatedOn': '2017-07-19T13:42:08.52Z', 'expires': '2019-04-12T23:32:13.52Z'}]}}
    class components_responses_200DomainGetById:
        """#/components/responses/200DomainGetById"""
        class R:
            description = 'Details of a domain.'
            content = {'application/json': {'schema': {'allOf': [lambda: Defs.components_schemas_apiResponse, lambda: Defs.components_schemas_Domain_domain]}}}
            examples = {'Success': {'statusCode': 200, 'id': 358362, 'name': 'mydomain.com', 'unicodeName': 'mydomain.com', 'state': 'Complete', 'autoRenew': True, 'whoisProtected': False, 'createdOn': '2014-04-12T23:20:50.52Z', 'updatedOn': '2017-07-19T13:42:08.52Z', 'expires': '2019-04-12T23:32:13.52Z'}, 'Failure': {'exception': {'statusCode': 404, 'type': 'Request Exception', 'message': 'Invalid.'}}}
    class components_responses_200DomainNameServer:
        """#/components/responses/200DomainNameServer"""
        class R:
            description = 'A list of name servers for a domain.'
            content = {'application/json': {'schema': {'allOf': [lambda: Defs.components_schemas_apiResponse, {'type': 'object', 'properties': {'nameServers': {'type': 'array', 'items': {'type': 'string'}}}}]}}}
            examples = {'default': {'statusCode': 200, 'domains': [{'id': 358362, 'name': 'mydomain.com', 'unicodeName': 'mydomain.com', 'state': 'Complete', 'autoRenew': True, 'whoisProtected': False, 'createdOn': '2014-04-12T23:20:50.52Z', 'updatedOn': '2017-07-19T13:42:08.52Z', 'expires': '2019-04-12T23:32:13.52Z'}, {'id': 365321, 'name': 'organic.org', 'unicodeName': 'organic.org', 'state': 'AwaitingPayment', 'autoRenew': True, 'whoisProtected': False, 'createdOn': '2017-04-12T23:20:50.52Z', 'updatedOn': '2017-07-19T13:42:08.52Z', 'expires': None}, {'id': 428546, 'name': 'xn--witowa-g1a3lpy.pl', 'unicodeName': 'świętować.pl', 'state': 'TransferPending', 'autoRenew': True, 'whoisProtected': False, 'createdOn': '2017-04-12T23:20:50.52Z', 'updatedOn': '2017-07-19T13:42:08.52Z', 'expires': '2019-04-12T23:32:13.52Z'}]}}
    class components_responses_200Email:
        """#/components/responses/200Email"""
        class R:
            description = 'A list of email services.'
            content = {'application/json': {'schema': {'allOf': [lambda: Defs.components_schemas_apiResponse, {'type': 'object', 'properties': {'monitors': {'type': 'array', 'items': {'anyOf': [lambda: Defs.components_schemas_Email_emailBackup, lambda: Defs.components_schemas_Email_emailForward, lambda: Defs.components_schemas_Email_emailFullService, lambda: Defs.components_schemas_Email_emailSMTPOutboundRelay, lambda: Defs.components_schemas_Email_emailStoreForward]}}}}]}}}
            examples = {'default': {'statusCode': 200, 'emails': [{'id': 358362, 'name': 'mydomain.com', 'unicodeName': 'mydomain.com', 'state': 'Complete', 'type': 'EmailStoreForward', 'autoRenew': True, 'antiSpam': False, 'createdOn': '2014-04-12T23:20:50.52Z', 'updatedOn': '2017-07-19T13:42:08.52Z', 'expires': '2019-04-12T23:32:13.52Z', 'etrnHost': 'mail.myemailserver.com', 'etrnPort': 2525, 'etrnConnectionSecurity': 'None', 'etrnRetryInterval': 10}, {'id': 365321, 'name': 'organic.org', 'unicodeName': 'organic.org', 'state': 'AwaitingPayment', 'type': 'EmailForward', 'autoRenew': True, 'antiSpam': False, 'createdOn': '2017-04-12T23:20:50.52Z', 'updatedOn': '2017-07-19T13:42:08.52Z', 'expires': None, 'catchAllAddress': 'user@mydomain.com', 'plusAddressing': False, 'plusAddressingCharacter': '+', 'greyListing': False}]}}
    class components_responses_200EmailBlacklist:
        """#/components/responses/200EmailBlacklist"""
        class R:
            description = 'A list of blacklist.'
            content = {'application/json': {'schema': {'allOf': [lambda: Defs.components_schemas_apiResponse, {'type': 'object', 'properties': {'blacklists': {'type': 'array', 'items': lambda: Defs.components_schemas_Email_emailBlacklist}}}]}}}
            examples = {'default': {'statusCode': 200, 'blacklists': [{'id': 32236132, 'domainId': 84257892, 'domainName': 'mydomain.com', 'type': 'EmailAddress', 'data': 'tom@externaldomain.com', 'state': True}, {'id': 32236132, 'domainId': 84257892, 'domainName': 'mydomain.com', 'type': 'Domain', 'data': 'externaldomain.com', 'state': True}, {'id': 32236132, 'domainId': 84257892, 'domainName': 'mydomain.com', 'type': 'IPAddress', 'data': '216.29.41.0/24', 'state': True}, {'id': 32236132, 'domainId': 84257892, 'domainName': 'mydomain.com', 'type': 'IPAddress', 'data': '216.160.207.10', 'state': False}]}}
    class components_responses_200EmailBlacklistGetById:
        """#/components/responses/200EmailBlacklistGetById"""
        class R:
            description = 'Details of a blacklist.'
            content = {'application/json': {'schema': {'allOf': [lambda: Defs.components_schemas_apiResponse, lambda: Defs.components_schemas_Email_emailBlacklist]}}}
            examples = {'Success': {'statusCode': 200, 'id': 32236132, 'domainId': 84257892, 'domainName': 'mydomain.com', 'type': 'EmailAddress', 'data': 'tom@externaldomain.com', 'state': False}, 'Failure': {'exception': {'statusCode': 404, 'type': 'Request Exception', 'message': 'Invalid.'}}}
    class components_responses_200EmailDeliveryQueue:
        """#/components/responses/200EmailDeliveryQueue"""
        class R:
            description = 'A list of messages in delivery queue.'
            content = {'application/json': {'schema': {'allOf': [lambda: Defs.components_schemas_apiResponse, {'type': 'object', 'properties': {'domains': {'type': 'array', 'items': lambda: Defs.components_schemas_Email_emailDeliveryQueueMessage}}}]}}}
            examples = {'default': {'statusCode': 200, 'domains': [{'uid': '9A0F4682B7A5', 'from': 'tom@externaldomain.com', 'to': 'jackie@mydomain.com', 'tries': 3, 'createdOn': '2017-04-12T23:20:50.52Z', 'nextRetryOn': '2017-04-12T23:28:50.52Z'}, {'uid': '9A0F4682B7A5', 'from': 'deepak@externaldomain.com', 'to': 'jackie@mydomain.com', 'tries': 0, 'createdOn': '2017-04-13T23:20:50.52Z'}, {'uid': '9A0F4682B7A5', 'from': 'jackie@mydomain.com', 'to': 'lauren@mydomain.com', 'tries': 19, 'createdOn': '2017-04-11T09:20:50.52Z', 'nextRetryOn': '2017-04-13T23:25:50.52Z'}]}}
    class components_responses_200EmailGetById:
        """#/components/responses/200EmailGetById"""
        class R:
            description = 'Details of an email service.'
            content = {'application/json': {'schema': {'allOf': [lambda: Defs.components_schemas_apiResponse, {'oneOf': [lambda: Defs.components_schemas_Email_emailBackup, lambda: Defs.components_schemas_Email_emailForward, lambda: Defs.components_schemas_Email_emailFullService, lambda: Defs.components_schemas_Email_emailSMTPOutboundRelay, lambda: Defs.components_schemas_Email_emailStoreForward]}]}}}
            examples = {'Success': {'statusCode': 200, 'id': 358362, 'name': 'mydomain.com', 'unicodeName': 'mydomain.com', 'state': 'Complete', 'type': 'EmailStoreForward', 'autoRenew': True, 'antiSpam': False, 'createdOn': '2014-04-12T23:20:50.52Z', 'updatedOn': '2017-07-19T13:42:08.52Z', 'expires': '2019-04-12T23:32:13.52Z', 'etrnHost': 'mail.myemailserver.com', 'etrnPort': 2525, 'etrnConnectionSecurity': 'None', 'etrnRetryInterval': 10}, 'Failure': {'exception': {'statusCode': 404, 'type': 'Request Exception', 'message': 'Invalid.'}}}
    class components_responses_200EmailWhitelist:
        """#/components/responses/200EmailWhitelist"""
        class R:
            description = 'A list of whitelist.'
            content = {'application/json': {'schema': {'allOf': [lambda: Defs.components_schemas_apiResponse, {'type': 'object', 'properties': {'whitelists': {'type': 'array', 'items': lambda: Defs.components_schemas_Email_emailWhitelist}}}]}}}
            examples = {'default': {'statusCode': 200, 'whitelists': [{'id': 32236132, 'domainId': 84257892, 'domainName': 'mydomain.com', 'type': 'EmailAddress', 'data': 'tom@externaldomain.com', 'state': True}, {'id': 32236132, 'domainId': 84257892, 'domainName': 'mydomain.com', 'type': 'Domain', 'data': 'externaldomain.com', 'state': True}, {'id': 32236132, 'domainId': 84257892, 'domainName': 'mydomain.com', 'type': 'IPAddress', 'data': '216.29.41.0/24', 'state': True}, {'id': 32236132, 'domainId': 84257892, 'domainName': 'mydomain.com', 'type': 'IPAddress', 'data': '216.160.207.10', 'state': False}]}}
    class components_responses_200EmailWhitelistGetById:
        """#/components/responses/200EmailWhitelistGetById"""
        class R:
            description = 'Details of a whitelist.'
            content = {'application/json': {'schema': {'allOf': [lambda: Defs.components_schemas_apiResponse, lambda: Defs.components_schemas_Email_emailWhitelist]}}}
            examples = {'Success': {'statusCode': 200, 'id': 32236132, 'domainId': 84257892, 'domainName': 'mydomain.com', 'type': 'EmailAddress', 'data': 'tom@externaldomain.com', 'state': False}, 'Failure': {'exception': {'statusCode': 404, 'type': 'Request Exception', 'message': 'Invalid.'}}}
    class components_responses_200Monitor:
        """#/components/responses/200Monitor"""
        class R:
            description = 'A list of monitors.'
            content = {'application/json': {'schema': {'allOf': [lambda: Defs.components_schemas_apiResponse, {'type': 'object', 'properties': {'monitors': {'type': 'array', 'items': {'anyOf': [lambda: Defs.components_schemas_Monitor_monitorDNS, lambda: Defs.components_schemas_Monitor_monitorHTTP, lambda: Defs.components_schemas_Monitor_monitorKeyword, lambda: Defs.components_schemas_Monitor_monitorPing, lambda: Defs.components_schemas_Monitor_monitorPort]}}}}]}}}
            examples = {'default': {'statusCode': 200, 'monitors': [{'id': 358362, 'name': 'HTTP monitor for http://www.dynu.com', 'type': 'HTTP', 'checkInterval': 10, 'state': 'UP', 'paused': False, 'lastCheck': '2016-04-12T23:20:50.52Z', 'nextCheck': '2016-04-12T23:30:50.52Z', 'lastSuccessfulCheck': '2016-04-12T23:20:50.52Z', 'url': 'http://www.dynu.com'}, {'id': 858657, 'name': 'ns1.dynu.com', 'type': 'DNS', 'checkInterval': 20, 'state': 'NONE', 'paused': True, 'lastCheck': '2016-04-12T23:20:50.52Z', 'nextCheck': None, 'lastSuccessfulCheck': '2016-04-12T23:20:50.52Z', 'nameServer': 'ns1.dynu.com', 'hostname': 'monitoring.org'}]}}
    class components_responses_200MonitorAdd:
        """#/components/responses/200MonitorAdd"""
        class R:
            description = 'The response to addition of new monitor operation.'
            content = {'application/json': {'schema': lambda: Defs.components_schemas_apiResponse}}
            examples = {'Success': {'statusCode': 200}, 'Parse Exception': {'exception': {'statusCode': 502, 'type': 'Parse Exception', 'message': 'Invalid.'}}}
    class components_responses_200MonitorGetById:
        """#/components/responses/200MonitorGetById"""
        class R:
            description = 'Details of a monitor.'
            content = {'application/json': {'schema': {'allOf': [lambda: Defs.components_schemas_apiResponse, {'oneOf': [lambda: Defs.components_schemas_Monitor_monitorDNS, lambda: Defs.components_schemas_Monitor_monitorHTTP, lambda: Defs.components_schemas_Monitor_monitorKeyword, lambda: Defs.components_schemas_Monitor_monitorPing, lambda: Defs.components_schemas_Monitor_monitorPort]}]}}}
            examples = {'Success': {'statusCode': 200, 'id': 358362, 'name': 'HTTP monitor for http://www.dynu.com', 'type': 'HTTP', 'checkInterval': 10, 'state': 'UP', 'paused': False, 'lastCheck': '2016-04-12T23:20:50.52Z', 'nextCheck': '2016-04-12T23:30:50.52Z', 'lastSuccessfulCheck': '2016-04-12T23:20:50.52Z', 'url': 'http://www.dynu.com'}, 'Failure': {'exception': {'statusCode': 404, 'type': 'Request Exception', 'message': 'Invalid.'}}}
    class components_responses_200MonitorLimit:
        """#/components/responses/200MonitorLimit"""
        class R:
            description = 'Limits associated with monitoring.'
            content = {'application/json': {'schema': {'allOf': [lambda: Defs.components_schemas_apiResponse, lambda: Defs.components_schemas_Monitor_limit]}}}
            examples = {'Success': {'statusCode': 200, 'activeCount': 32, 'remainingCount': 68}, 'Failure': {'statusCode': 503, 'type': 'Quota Exception', 'message': 'Failed.'}}
    class components_responses_200Ping:
        """#/components/responses/200Ping"""
        class R:
            description = 'The response to ping operation.'
            content = {'application/json': {'schema': lambda: Defs.components_schemas_Ping_pong}}
            examples = {'Test Ping': {'statusCode': 200, 'message': 'test'}}
    class components_responses_200WebRedirect:
        """#/components/responses/200WebRedirect"""
        class R:
            description = 'A list of web redirects.'
            content = {'application/json': {'schema': {'allOf': [lambda: Defs.components_schemas_apiResponse, {'type': 'object', 'properties': {'webRedirects': {'type': 'array', 'items': lambda: Defs.components_schemas_DNS_webRedirect}}}]}}}
            examples = {'Success': {'statusCode': 200, 'webRedirects': [{'id': 35836280, 'domainId': 8246254, 'domainName': 'mydomain.com', 'nodeName': 'cms', 'hostname': 'cms.mydomain.com', 'redirectType': 'PF', 'state': True, 'updatedOn': '2018-07-19T13:42:08.52Z', 'host': 'cms.myotherdomain.com', 'port': 8080, 'includeQueryString': True}, {'id': 45805321, 'domainId': 8246254, 'domainName': 'mydomain.com', 'nodeName': 'www', 'hostname': 'www.mydomain.com', 'redirectType': 'UF', 'state': True, 'updatedOn': '2018-07-19T13:42:08.52Z', 'url': 'https://www.mydomain.com'}]}, 'Failure': {'exception': {'statusCode': 404, 'type': 'Request Exception', 'message': 'Invalid.'}}}
    class components_responses_200WebRedirectGetById:
        """#/components/responses/200WebRedirectGetById"""
        class R:
            description = 'Details of the web redirect.'
            content = {'application/json': {'schema': {'allOf': [lambda: Defs.components_schemas_apiResponse, lambda: Defs.components_schemas_DNS_webRedirect]}}}
            examples = {'Success': {'statusCode': 200, 'id': 35836280, 'domainId': 8246254, 'domainName': 'mydomain.com', 'nodeName': 'cms', 'hostname': 'cms.mydomain.com', 'redirectType': 'PF', 'state': True, 'updatedOn': '2018-07-19T13:42:08.52Z', 'host': 'cms.myotherdomain.com', 'port': 8080, 'includeQueryString': True}, 'Failure': {'exception': {'statusCode': 404, 'type': 'Request Exception', 'message': 'Invalid.'}}}
    class components_responses_401:
        """#/components/responses/401"""
        class R:
            description = 'Authentication and/or authorized has failed.'
            content = {'application/json': {'schema': lambda: Defs.components_schemas_apiResponse}}
            examples = {'Authentication Exception': {'exception': {'statusCode': 401, 'type': 'Authentication Exception', 'message': 'Failed.'}}}
    class components_responses_500:
        """#/components/responses/500"""
        class R:
            description = 'The operation failed on the server due to an unexpected error.'
            content = {'application/json': {'schema': lambda: Defs.components_schemas_apiResponse}}
            examples = {'Server Exception': {'exception': {'statusCode': 500, 'type': 'Server Exception', 'message': 'Failed.'}}}
    class components_responses_501:
        """#/components/responses/501"""
        class R:
            description = 'Arguments are missing or invalid.'
            content = {'application/json': {'schema': lambda: Defs.components_schemas_apiResponse}}
            examples = {'Argument Exception': {'exception': {'statusCode': 501, 'type': 'Argument Exception', 'message': 'Invalid.'}}}
    class components_responses_502:
        """#/components/responses/502"""
        class R:
            description = 'There was an error when parsing the request and its parameters.'
            content = {'application/json': {'schema': lambda: Defs.components_schemas_apiResponse}}
            examples = {'Parse Exception': {'exception': {'statusCode': 502, 'type': 'Parse Exception', 'message': 'Invalid.'}}}
    class components_responses_503:
        """#/components/responses/503"""
        class R:
            description = 'An error was encountered due to quota restrictions.'
            content = {'application/json': {'schema': lambda: Defs.components_schemas_apiResponse}}
            examples = {'Quota Exception': {'exception': {'statusCode': 503, 'type': 'Quota Exception', 'message': 'Failed.'}}}
    class components_schemas_DNS_dnsGroup:
        """#/components/schemas/DNS.dnsGroup"""
        class R:
            type = 'object'
            _attrs = ['id', 'groupName', 'groupPassword', 'passwordProtected']
            id = {'type': 'integer', 'format': 'int32', 'readOnly': True}
            groupName = {'type': 'string', 'example': 'work'}
            groupPassword = {'type': 'string', 'example': 'A64Cce8cHx37'}
            passwordProtected = {'type': 'boolean', 'readOnly': True, 'example': True}
        R.id = id
        R.groupName = 'work'
        R.groupPassword = 'A64Cce8cHx37'
        R.passwordProtected = True
    class components_schemas_DNS_dnsRecord:
        """#/components/schemas/DNS.dnsRecord"""
        class R:
            type = 'object'
            _attrs = ['id', 'domainId', 'domainName', 'nodeName', 'hostname', 'recordType', 'state', 'content', 'updatedOn']
            id = {'type': 'integer', 'format': 'int32', 'readOnly': True}
            domainId = {'type': 'integer', 'format': 'int32'}
            domainName = {'type': 'string', 'example': 'mydomain.com', 'readOnly': True}
            nodeName = {'type': 'string', 'example': 'www'}
            hostname = {'type': 'string', 'example': 'www.mydomain.com', 'readOnly': True}
            recordType = {'type': 'string', 'enum': ['A', 'AAAA', 'CAA', 'CNAME', 'HINFO', 'LOC', 'MX', 'NS', 'PTR', 'PF', 'RP', 'SOA', 'TXT', 'UF', 'URI'], 'example': 'A'}
            state = {'type': 'boolean'}
            content = {'type': 'string', 'example': '', 'readOnly': True}
            updatedOn = {'type': 'string', 'format': 'date-time', 'readOnly': True}
        R.id = id
        R.domainId = 0
        R.domainName = 'mydomain.com'
        R.nodeName = 'www'
        R.hostname = hostname
        R.recordType = 'A'
        R.state = True
        R.content = str_dflt
        R.updatedOn = '2020-12-12'
    class components_schemas_DNS_dnsRecordA:
        """#/components/schemas/DNS.dnsRecordA"""
        class R:
            allOf = [lambda: Defs.components_schemas_DNS_dnsRecord, {'type': 'object', 'properties': {'group': {'type': 'string', 'example': 'work'}, 'ipv4Address': {'type': 'string', 'example': '1.2.3.4'}}}]
    class components_schemas_DNS_dnsRecordAAAA:
        """#/components/schemas/DNS.dnsRecordAAAA"""
        class R:
            allOf = [lambda: Defs.components_schemas_DNS_dnsRecord, {'type': 'object', 'properties': {'group': {'type': 'string', 'example': 'work'}, 'ipv6Address': {'type': 'string', 'example': '1111:2222:3333::4444'}}}]
    class components_schemas_DNS_dnsRecordCAA:
        """#/components/schemas/DNS.dnsRecordCAA"""
        class R:
            allOf = [lambda: Defs.components_schemas_DNS_dnsRecord, {'type': 'object', 'properties': {'flags': {'type': 'integer', 'format': 'int32'}, 'tag': {'type': 'string', 'enum': ['issue', 'issuewild', 'iodef'], 'example': 'issue'}, 'value': {'type': 'string', 'example': 'dynuca.org'}}}]
    class components_schemas_DNS_dnsRecordCNAME:
        """#/components/schemas/DNS.dnsRecordCNAME"""
        class R:
            allOf = [lambda: Defs.components_schemas_DNS_dnsRecord, {'type': 'object', 'properties': {'host': {'type': 'string', 'example': 'www.anotherdomain.com'}}}]
    class components_schemas_DNS_dnsRecordHINFO:
        """#/components/schemas/DNS.dnsRecordHINFO"""
        class R:
            allOf = [lambda: Defs.components_schemas_DNS_dnsRecord, {'type': 'object', 'properties': {'CPU': {'type': 'string', 'example': 'Xeon'}, 'OperatingSystem': {'type': 'string', 'example': 'Linux'}}}]
    class components_schemas_DNS_dnsRecordLOC:
        """#/components/schemas/DNS.dnsRecordLOC"""
        class R:
            allOf = [lambda: Defs.components_schemas_DNS_dnsRecord, {'type': 'object', 'properties': {'latitude': {'type': 'number', 'format': 'double', 'example': 61.1833}, 'longitude': {'type': 'number', 'format': 'double', 'example': -149.8333}, 'altitude': {'type': 'number', 'format': 'double', 'example': 10}, 'size': {'type': 'number', 'format': 'double', 'example': 1000}, 'horizontalPrecision': {'type': 'number', 'format': 'double', 'example': 10000}, 'verticalPrecision': {'type': 'number', 'format': 'double', 'example': 10}}}]
    class components_schemas_DNS_dnsRecordMX:
        """#/components/schemas/DNS.dnsRecordMX"""
        class R:
            allOf = [lambda: Defs.components_schemas_DNS_dnsRecord, {'type': 'object', 'properties': {'host': {'type': 'string', 'example': 'mail.anotherdomain.com'}, 'priority': {'type': 'integer', 'format': 'int32', 'example': 10}}}]
    class components_schemas_DNS_dnsRecordNS:
        """#/components/schemas/DNS.dnsRecordNS"""
        class R:
            allOf = [lambda: Defs.components_schemas_DNS_dnsRecord, {'type': 'object', 'properties': {'host': {'type': 'string', 'example': 'ns2.anotherdomain.com'}}}]
    class components_schemas_DNS_dnsRecordPTR:
        """#/components/schemas/DNS.dnsRecordPTR"""
        class R:
            allOf = [lambda: Defs.components_schemas_DNS_dnsRecord, {'type': 'object', 'properties': {'host': {'type': 'string', 'example': '10.207.160.216.in-addr.arpa'}}}]
    class components_schemas_DNS_dnsRecordRP:
        """#/components/schemas/DNS.dnsRecordRP"""
        class R:
            allOf = [lambda: Defs.components_schemas_DNS_dnsRecord, {'type': 'object', 'properties': {'mailBox': {'type': 'string', 'example': 'admin.domain.com'}, 'txtDomainName': {'type': 'string', 'example': 'domain.com'}}}]
    class components_schemas_DNS_dnsRecordSOA:
        """#/components/schemas/DNS.dnsRecordSOA"""
        class R:
            allOf = [lambda: Defs.components_schemas_DNS_dnsRecord, {'type': 'object', 'properties': {'masterName': {'type': 'string', 'example': 'ns1.dynu.com'}, 'responsibleName': {'type': 'string', 'example': 'administrator.dynu.com'}, 'refresh': {'type': 'integer', 'format': 'int32', 'example': 1800}, 'retry': {'type': 'integer', 'format': 'int32', 'example': 300}, 'expire': {'type': 'integer', 'format': 'int32', 'example': 86400}, 'negativeTTL': {'type': 'integer', 'format': 'int32', 'example': 300}}}]
    class components_schemas_DNS_dnsRecordSPF:
        """#/components/schemas/DNS.dnsRecordSPF"""
        class R:
            allOf = [lambda: Defs.components_schemas_DNS_dnsRecord, {'type': 'object', 'properties': {'textData': {'type': 'string', 'example': 'v=spf1 include:_spf.somedomain.com ~all'}}}]
    class components_schemas_DNS_dnsRecordSRV:
        """#/components/schemas/DNS.dnsRecordSRV"""
        class R:
            allOf = [lambda: Defs.components_schemas_DNS_dnsRecord, {'type': 'object', 'properties': {'host': {'type': 'string', 'example': 'sip.mydomain.com'}, 'priority': {'type': 'integer', 'format': 'int32', 'example': 10}, 'weight': {'type': 'integer', 'format': 'int32', 'example': 0}, 'port': {'type': 'integer', 'format': 'int32', 'example': 5060}}}]
    class components_schemas_DNS_dnsRecordSSHFP:
        """#/components/schemas/DNS.dnsRecordSSHFP"""
        class R:
            allOf = [lambda: Defs.components_schemas_DNS_dnsRecord, {'type': 'object', 'properties': {'algorithm': {'type': 'integer', 'format': 'int32', 'example': 1, 'minimum': 0, 'maximum': 4}, 'fingerPrintType': {'type': 'integer', 'format': 'int32', 'example': 1, 'minimum': 0, 'maximum': 2}, 'fingerPrint': {'type': 'string', 'example': 'f9e3c9b1df3569c99ea3c5af4e9686d90ae778b484af86d37e96603e9895ea7d'}}}]
    class components_schemas_DNS_dnsRecordTLSA:
        """#/components/schemas/DNS.dnsRecordTLSA"""
        class R:
            allOf = [lambda: Defs.components_schemas_DNS_dnsRecord, {'type': 'object', 'properties': {'certificateUsage': {'type': 'integer', 'format': 'int32', 'example': 3, 'minimum': 0, 'maximum': 3}, 'selector': {'type': 'integer', 'format': 'int32', 'example': 1, 'minimum': 0, 'maximum': 1}, 'matchingType': {'type': 'integer', 'format': 'int32', 'example': 1, 'minimum': 0, 'maximum': 2}, 'certificateAssociatedData': {'type': 'string', 'example': '0D6FCE3320315023FF499A3F3DE1C362C88F8380311AC8C036890DAB13243AA7'}}}]
    class components_schemas_DNS_dnsRecordTXT:
        """#/components/schemas/DNS.dnsRecordTXT"""
        class R:
            allOf = [lambda: Defs.components_schemas_DNS_dnsRecord, {'type': 'object', 'properties': {'textData': {'type': 'string', 'example': 'facebook-domain-verification=22rm551cu4k0ab0bxsw536tlds4h95'}}}]
    class components_schemas_DNS_dnsRecordURI:
        """#/components/schemas/DNS.dnsRecordURI"""
        class R:
            allOf = [lambda: Defs.components_schemas_DNS_dnsRecord, {'type': 'object', 'properties': {'priority': {'type': 'integer', 'format': 'int32', 'example': 10}, 'weight': {'type': 'integer', 'format': 'int32', 'example': 1}, 'targetUri': {'type': 'string', 'example': 'ftp://ftp.example.com/public'}}}]
    class components_schemas_DNS_dnsSec:
        """#/components/schemas/DNS.dnsSec"""
        class R:
            type = 'object'
            _attrs = ['id', 'domainName', 'dsRecord', 'digest', 'digestType', 'algorithm', 'publicKey', 'keyTag', 'flags']
            id = {'type': 'integer', 'format': 'int32'}
            domainName = {'type': 'string'}
            dsRecord = {'type': 'string'}
            digest = {'type': 'string'}
            digestType = {'type': 'string', 'enum': ['Sha1', 'Sha256', 'EccGost', 'Sha384']}
            algorithm = {'type': 'integer', 'format': 'int32'}
            publicKey = {'type': 'string'}
            keyTag = {'type': 'integer', 'format': 'int32'}
            flags = {'type': 'integer', 'format': 'int32'}
        R.id = id
        R.domainName = str_dflt
        R.dsRecord = str_dflt
        R.digest = str_dflt
        R.digestType = 'Sha1'
        R.algorithm = 0
        R.publicKey = str_dflt
        R.keyTag = 0
        R.flags = 0
    class components_schemas_DNS_domain:
        """#/components/schemas/DNS.domain"""
        class R:
            type = 'object'
            _attrs = ['id', 'name', 'unicodeName', 'token', 'state', 'group', 'ipv4Address', 'ipv6Address', 'ttl', 'ipv4', 'ipv6', 'ipv4WildcardAlias', 'ipv6WildcardAlias', 'allowZoneTransfer', 'dnssec', 'createdOn', 'updatedOn']
            id = {'type': 'integer', 'format': 'int32', 'readOnly': True}
            name = {'type': 'string', 'example': 'somedomain.com'}
            unicodeName = {'type': 'string', 'readOnly': True}
            token = {'type': 'string', 'readOnly': True}
            state = {'type': 'string', 'enum': ['AwaitingPayment', 'AwaitingAuthorizationCode', 'AwaitingIPSTAGChange', 'Complete', 'Cancelled', 'Expired', 'TransferPending', 'TransferFailed', 'RedemptionPeriod', 'Provisioning'], 'readOnly': True}
            group = {'type': 'string', 'example': 'office'}
            ipv4Address = {'type': 'string', 'example': '1.2.3.4'}
            ipv6Address = {'type': 'string', 'example': '1111:2222:3333::4444'}
            ttl = {'type': 'integer', 'format': 'int32', 'example': 90}
            ipv4 = {'type': 'boolean', 'example': True}
            ipv6 = {'type': 'boolean', 'example': True}
            ipv4WildcardAlias = {'type': 'boolean', 'example': True}
            ipv6WildcardAlias = {'type': 'boolean', 'example': True}
            allowZoneTransfer = {'type': 'boolean', 'example': False}
            dnssec = {'type': 'boolean', 'example': False}
            createdOn = {'type': 'string', 'format': 'date-time', 'readOnly': True}
            updatedOn = {'type': 'string', 'format': 'date-time', 'readOnly': True}
        R.id = id
        R.name = 'somedomain.com'
        R.unicodeName = str_dflt
        R.token = str_dflt
        R.state = 'AwaitingPayment'
        R.group = 'office'
        R.ipv4Address = '1.2.3.4'
        R.ipv6Address = '1111:2222:3333::4444'
        R.ttl = 90
        R.ipv4 = True
        R.ipv6 = True
        R.ipv4WildcardAlias = True
        R.ipv6WildcardAlias = True
        R.allowZoneTransfer = True
        R.dnssec = True
        R.createdOn = '2020-12-12'
        R.updatedOn = '2020-12-12'
    class components_schemas_DNS_hostname:
        """#/components/schemas/DNS.hostname"""
        class R:
            type = 'object'
            _attrs = ['id', 'hostname', 'domainName', 'node']
            id = {'type': 'integer', 'format': 'int32'}
            hostname = {'type': 'string'}
            domainName = {'type': 'string'}
            node = {'type': 'string'}
        R.id = id
        R.hostname = hostname
        R.domainName = str_dflt
        R.node = str_dflt
    class components_schemas_DNS_ipUpdate:
        """#/components/schemas/DNS.ipUpdate"""
        class R:
            type = 'object'
            _attrs = ['id', 'responseId', 'updateStatus', 'ipv4Address', 'ipv6Address', 'queryString', 'userAgent', 'ssl', 'updatedOn']
            id = {'type': 'integer', 'format': 'int32', 'readOnly': True}
            responseId = {'type': 'string'}
            updateStatus = {'type': 'string', 'enum': ['Good', 'Bad Authentication', 'DNS Error', 'Server Error', '911', 'Not Fully Qualified Domain Name', 'No Change', 'Abuse', 'No Host', 'Too Many Hosts', 'Not Member', 'Old Version', 'Unknown'], 'readOnly': True}
            ipv4Address = {'type': 'string', 'readOnly': True}
            ipv6Address = {'type': 'string', 'readOnly': True}
            queryString = {'type': 'string', 'readOnly': True}
            userAgent = {'type': 'string', 'readOnly': True}
            ssl = {'type': 'boolean'}
            updatedOn = {'type': 'string', 'format': 'date-time', 'readOnly': True}
        R.id = id
        R.responseId = str_dflt
        R.updateStatus = 'Good'
        R.ipv4Address = str_dflt
        R.ipv6Address = str_dflt
        R.queryString = str_dflt
        R.userAgent = str_dflt
        R.ssl = True
        R.updatedOn = '2020-12-12'
    class components_schemas_DNS_limit:
        """#/components/schemas/DNS.limit"""
        class R:
            type = 'object'
            _attrs = ['activeCount', 'remainingCount']
            activeCount = {'type': 'integer', 'format': 'int32', 'example': 132}
            remainingCount = {'type': 'integer', 'format': 'int32', 'example': 368}
        R.activeCount = 132
        R.remainingCount = 368
    class components_schemas_DNS_recordLimit:
        """#/components/schemas/DNS.recordLimit"""
        class R:
            type = 'object'
            _attrs = ['recordTypes', 'activeCount', 'remainingCount']
            recordTypes = {'type': 'array', 'items': {'type': 'string', 'example': 'MX'}, 'example': ['A', 'AAAA']}
            activeCount = {'type': 'integer', 'format': 'int32', 'example': 132}
            remainingCount = {'type': 'integer', 'format': 'int32', 'example': 368}
        R.recordTypes = ['A', 'AAAA']
        R.activeCount = 132
        R.remainingCount = 368
    class components_schemas_DNS_webRedirect:
        """#/components/schemas/DNS.webRedirect"""
        class R:
            type = 'object'
            required = ['id', 'domainId', 'domainName', 'nodeName', 'hostname', 'redirectType', 'state', 'updatedOn', 'url', 'host', 'port']
            _attrs = ['id', 'domainId', 'domainName', 'nodeName', 'hostname', 'redirectType', 'state', 'updatedOn', 'url', 'host', 'port', 'useDynamicIPv4Address', 'useDynamicIPv6Address', 'cloak', 'includeQueryString', 'redirect301', 'title', 'metaKeywords', 'metaDescription']
            id = {'type': 'integer', 'format': 'int32', 'readOnly': True}
            domainId = {'type': 'integer', 'format': 'int32', 'readOnly': True}
            domainName = {'type': 'string', 'example': 'mydomain.com', 'readOnly': True}
            nodeName = {'type': 'string', 'example': 'www'}
            hostname = {'type': 'string', 'example': 'www.mydomain.com', 'readOnly': True}
            redirectType = {'type': 'string', 'enum': ['PF', 'UF'], 'example': 'PF', 'descr': "UF stands for 'URL Forwarding' and PF stands for 'Port Forwarding'"}
            state = {'type': 'boolean'}
            updatedOn = {'type': 'string', 'format': 'date-time', 'readOnly': True}
            url = {'type': 'string', 'example': 'https://www.mydomain.com', 'descr': 'This property only applies when redirectType is UF'}
            host = {'type': 'string', 'example': 'www.mydomain.com', 'descr': 'This property only applies when redirectType is PF'}
            port = {'type': 'integer', 'format': 'int32', 'example': 8080, 'descr': 'This property only applies when redirectType is PF'}
            useDynamicIPv4Address = {'type': 'boolean'}
            useDynamicIPv6Address = {'type': 'boolean'}
            cloak = {'type': 'boolean'}
            includeQueryString = {'type': 'boolean'}
            redirect301 = {'type': 'boolean'}
            title = {'type': 'string', 'example': 'Acme, Inc.'}
            metaKeywords = {'type': 'string', 'example': 'plumbing, water supply, contract work'}
            metaDescription = {'type': 'string', 'example': 'Our company performs general plumbing and contract work.'}
        R.id = id
        R.domainId = 0
        R.domainName = 'mydomain.com'
        R.nodeName = 'www'
        R.hostname = hostname
        R.redirectType = 'PF'
        R.state = True
        R.updatedOn = '2020-12-12'
        R.url = 'https://www.mydomain.com'
        R.host = 'www.mydomain.com'
        R.port = 8080
        R.useDynamicIPv4Address = True
        R.useDynamicIPv6Address = True
        R.cloak = True
        R.includeQueryString = True
        R.redirect301 = True
        R.title = 'Acme, Inc.'
        R.metaKeywords = 'plumbing, water supply, contract work'
        R.metaDescription = 'Our company performs general plumbing and contract work.'
    class components_schemas_Domain_domain:
        """#/components/schemas/Domain.domain"""
        class R:
            type = 'object'
            _attrs = ['id', 'name', 'unicodeName', 'token', 'state', 'autoRenew', 'whoisProtected', 'expiresOn', 'createdOn', 'updatedOn', 'transferState', 'transferAuthorizationCode', 'transferInitiatedOn', 'transferUpdatedOn']
            id = {'type': 'integer', 'format': 'int32', 'readOnly': True}
            name = {'type': 'string'}
            unicodeName = {'type': 'string', 'readOnly': True}
            token = {'type': 'string', 'readOnly': True}
            state = {'type': 'string', 'enum': ['AwaitingPayment', 'AwaitingAuthorizationCode', 'AwaitingIPSTAGChange', 'Complete', 'Cancelled', 'Expired', 'TransferPending', 'TransferFailed', 'RedemptionPeriod', 'Provisioning'], 'readOnly': True}
            autoRenew = {'type': 'boolean'}
            whoisProtected = {'type': 'boolean'}
            expiresOn = {'type': 'string', 'format': 'date-time', 'readOnly': True}
            createdOn = {'type': 'string', 'format': 'date-time', 'readOnly': True}
            updatedOn = {'type': 'string', 'format': 'date-time', 'readOnly': True}
            transferState = {'type': 'string', 'enum': ['TRANSFERPENDINGAUTHCODE', 'TRANSFERPENDINGOPS_WHOIS', 'TRANSFERPENDINGAPPROVAL', 'TRANSFERPENDING', 'TRANSFERCOMPLETE', 'TRANSFERFAILED', 'TRANSFERCANCELLED'], 'readOnly': True}
            transferAuthorizationCode = {'type': 'string'}
            transferInitiatedOn = {'type': 'string', 'format': 'date-time', 'readOnly': True}
            transferUpdatedOn = {'type': 'string', 'format': 'date-time', 'readOnly': True}
        R.id = id
        R.name = str_dflt
        R.unicodeName = str_dflt
        R.token = str_dflt
        R.state = 'AwaitingPayment'
        R.autoRenew = True
        R.whoisProtected = True
        R.expiresOn = '2020-12-12'
        R.createdOn = '2020-12-12'
        R.updatedOn = '2020-12-12'
        R.transferState = 'TRANSFERPENDINGAUTHCODE'
        R.transferAuthorizationCode = str_dflt
        R.transferInitiatedOn = '2020-12-12'
        R.transferUpdatedOn = '2020-12-12'
    class components_schemas_Email_email:
        """#/components/schemas/Email.email"""
        class R:
            type = 'object'
            _attrs = ['id', 'name', 'unicodeName', 'token', 'state', 'type', 'autoRenew', 'antiSpam', 'expiresOn', 'createdOn', 'updatedOn']
            id = {'type': 'integer', 'format': 'int32', 'readOnly': True}
            name = {'type': 'string'}
            unicodeName = {'type': 'string', 'readOnly': True}
            token = {'type': 'string', 'readOnly': True}
            state = {'type': 'string', 'enum': ['AwaitingPayment', 'Complete', 'OnHold', 'Cancelled', 'Expired', 'Provisioning', 'Other'], 'readOnly': True}
            type = {'type': 'string', 'enum': ['EmailBackup', 'EmailForward', 'EmailStoreForward', 'FullServiceEmail', 'SMTPOutboundRelay']}
            autoRenew = {'type': 'boolean'}
            antiSpam = {'type': 'boolean'}
            expiresOn = {'type': 'string', 'format': 'date-time', 'readOnly': True}
            createdOn = {'type': 'string', 'format': 'date-time', 'readOnly': True}
            updatedOn = {'type': 'string', 'format': 'date-time', 'readOnly': True}
        R.id = id
        R.name = str_dflt
        R.unicodeName = str_dflt
        R.token = str_dflt
        R.state = 'AwaitingPayment'
        R.type = 'EmailBackup'
        R.autoRenew = True
        R.antiSpam = True
        R.expiresOn = '2020-12-12'
        R.createdOn = '2020-12-12'
        R.updatedOn = '2020-12-12'
    class components_schemas_Email_emailAccount:
        """#/components/schemas/Email.emailAccount"""
        class R:
            type = 'object'
            _attrs = ['id', 'emailId', 'emailAddress', 'unicodeEmailAddress', 'state', 'useForwarding', 'keepOriginalMessage', 'forwardAddress', 'password']
            id = {'type': 'integer', 'format': 'int32', 'readOnly': True}
            emailId = {'type': 'integer', 'format': 'int32'}
            emailAddress = {'type': 'string'}
            unicodeEmailAddress = {'type': 'string', 'readOnly': True}
            state = {'type': 'string', 'enum': ['Active', 'InActive']}
            useForwarding = {'type': 'boolean'}
            keepOriginalMessage = {'type': 'boolean'}
            forwardAddress = {'type': 'string'}
            password = {'type': 'string'}
        R.id = id
        R.emailId = 0
        R.emailAddress = str_dflt
        R.unicodeEmailAddress = str_dflt
        R.state = 'Active'
        R.useForwarding = True
        R.keepOriginalMessage = True
        R.forwardAddress = str_dflt
        R.password = str_dflt
    class components_schemas_Email_emailBackup:
        """#/components/schemas/Email.emailBackup"""
        class R:
            allOf = [lambda: Defs.components_schemas_Email_email, {'type': 'object', 'properties': {'etrnHost': {'type': 'string'}, 'etrnPort': {'type': 'integer', 'format': 'int32'}, 'etrnConnectionSecurity': {'type': 'string', 'enum': ['None', 'SSLTLS', 'STARTTLSOptional', 'STARTTLSRequired']}, 'etrnRetryInterval': {'type': 'integer', 'format': 'int32'}}}]
    class components_schemas_Email_emailBlacklist:
        """#/components/schemas/Email.emailBlacklist"""
        class R:
            type = 'object'
            _attrs = ['id', 'domainId', 'domainName', 'type', 'data', 'state']
            id = {'type': 'integer', 'format': 'int32', 'readOnly': True}
            domainId = {'type': 'integer', 'format': 'int32', 'readOnly': True}
            domainName = {'type': 'string', 'readOnly': True}
            type = {'type': 'string', 'enum': ['EmailAddress', 'Domain', 'IPAddress'], 'example': 'EmailAddress'}
            data = {'type': 'string'}
            state = {'type': 'boolean'}
        R.id = id
        R.domainId = 0
        R.domainName = str_dflt
        R.type = 'EmailAddress'
        R.data = str_dflt
        R.state = True
    class components_schemas_Email_emailDeliveryQueueMessage:
        """#/components/schemas/Email.emailDeliveryQueueMessage"""
        class R:
            type = 'object'
            _attrs = ['uid', 'from', 'to', 'tries', 'createdOn', 'nextRetryOn']
            uid = {'type': 'string'}
            from__ = {'type': 'string'}
            to = {'type': 'string'}
            tries = {'type': 'integer', 'format': 'int32'}
            createdOn = {'type': 'string', 'format': 'date-time', 'readOnly': True}
            nextRetryOn = {'type': 'string', 'format': 'date-time', 'readOnly': True}
        R.uid = str_dflt
        R.from__ = str_dflt
        R.to = str_dflt
        R.tries = 0
        R.createdOn = '2020-12-12'
        R.nextRetryOn = '2020-12-12'
    class components_schemas_Email_emailForward:
        """#/components/schemas/Email.emailForward"""
        class R:
            allOf = [lambda: Defs.components_schemas_Email_email, {'type': 'object', 'properties': {'catchAllAddress': {'type': 'string'}, 'plusAddressing': {'type': 'boolean'}, 'plusAddressingCharacter': {'type': 'string'}, 'greyListing': {'type': 'boolean'}}}]
    class components_schemas_Email_emailFullService:
        """#/components/schemas/Email.emailFullService"""
        class R:
            allOf = [lambda: Defs.components_schemas_Email_email, {'type': 'object', 'properties': {'catchAllAddress': {'type': 'string'}, 'plusAddressing': {'type': 'boolean'}, 'plusAddressingCharacter': {'type': 'string'}, 'greyListing': {'type': 'boolean'}}}]
    class components_schemas_Email_emailSMTPOutboundRelay:
        """#/components/schemas/Email.emailSMTPOutboundRelay"""
        class R:
            allOf = [lambda: Defs.components_schemas_Email_email, {'type': 'object', 'properties': {}}]
    class components_schemas_Email_emailStoreForward:
        """#/components/schemas/Email.emailStoreForward"""
        class R:
            allOf = [lambda: Defs.components_schemas_Email_email, {'type': 'object', 'properties': {'etrnHost': {'type': 'string'}, 'etrnPort': {'type': 'integer', 'format': 'int32'}, 'etrnConnectionSecurity': {'type': 'string', 'enum': ['None', 'SSLTLS', 'STARTTLSOptional', 'STARTTLSRequired']}, 'etrnRetryInterval': {'type': 'integer', 'format': 'int32'}}}]
    class components_schemas_Email_emailWhitelist:
        """#/components/schemas/Email.emailWhitelist"""
        class R:
            type = 'object'
            _attrs = ['id', 'domainId', 'domainName', 'type', 'data', 'state']
            id = {'type': 'integer', 'format': 'int32', 'readOnly': True}
            domainId = {'type': 'integer', 'format': 'int32', 'readOnly': True}
            domainName = {'type': 'string', 'readOnly': True}
            type = {'type': 'string', 'enum': ['EmailAddress', 'Domain', 'IPAddress'], 'example': 'EmailAddress'}
            data = {'type': 'string'}
            state = {'type': 'boolean'}
        R.id = id
        R.domainId = 0
        R.domainName = str_dflt
        R.type = 'EmailAddress'
        R.data = str_dflt
        R.state = True
    class components_schemas_Monitor_limit:
        """#/components/schemas/Monitor.limit"""
        class R:
            type = 'object'
            _attrs = ['activeCount', 'remainingCount']
            activeCount = {'type': 'integer', 'format': 'int32', 'example': 32}
            remainingCount = {'type': 'integer', 'format': 'int32', 'example': 68}
        R.activeCount = 32
        R.remainingCount = 68
    class components_schemas_Monitor_monitor:
        """#/components/schemas/Monitor.monitor"""
        class R:
            type = 'object'
            _attrs = ['id', 'name', 'type', 'checkInterval', 'state', 'paused', 'lastCheck', 'nextCheck', 'lastSuccessfulCheck']
            id = {'type': 'integer', 'format': 'int32', 'readOnly': True}
            name = {'type': 'string', 'example': 'HTTP monitor for www.dynu.com'}
            type = {'type': 'string', 'enum': ['DNS', 'HTTP', 'KEYWORD', 'PING', 'PORT'], 'example': 'HTTP'}
            checkInterval = {'type': 'integer', 'format': 'int32', 'example': 10}
            state = {'type': 'string', 'enum': ['NONE', 'PAUSED', 'WARNING', 'UP', 'DOWN'], 'readOnly': True}
            paused = {'type': 'boolean'}
            lastCheck = {'type': 'string', 'format': 'date-time', 'readOnly': True}
            nextCheck = {'type': 'string', 'format': 'date-time', 'readOnly': True}
            lastSuccessfulCheck = {'type': 'string', 'format': 'date-time', 'readOnly': True}
        R.id = id
        R.name = 'HTTP monitor for www.dynu.com'
        R.type = 'HTTP'
        R.checkInterval = 10
        R.state = 'NONE'
        R.paused = True
        R.lastCheck = '2020-12-12'
        R.nextCheck = '2020-12-12'
        R.lastSuccessfulCheck = '2020-12-12'
    class components_schemas_Monitor_monitorDNS:
        """#/components/schemas/Monitor.monitorDNS"""
        class R:
            allOf = [lambda: Defs.components_schemas_Monitor_monitor, {'type': 'object', 'properties': {'protocol': {'type': 'string', 'enum': ['TCP', 'UDP'], 'example': 'UDP'}, 'nameServer': {'type': 'string', 'example': 'ns1.dynu.com'}, 'hostname': {'type': 'string', 'example': 'www.dynu.com'}}}]
    class components_schemas_Monitor_monitorHTTP:
        """#/components/schemas/Monitor.monitorHTTP"""
        class R:
            allOf = [lambda: Defs.components_schemas_Monitor_monitor, {'type': 'object', 'properties': {'url': {'type': 'string', 'example': 'https://www.dynu.com'}, 'authenticationType': {'type': 'string', 'example': 'NONE'}, 'username': {'type': 'string'}, 'password': {'type': 'string'}}}]
    class components_schemas_Monitor_monitorKeyword:
        """#/components/schemas/Monitor.monitorKeyword"""
        class R:
            allOf = [lambda: Defs.components_schemas_Monitor_monitor, {'type': 'object', 'properties': {'url': {'type': 'string'}, 'keyword': {'type': 'string'}, 'keywordExists': {'type': 'boolean'}, 'authenticationType': {'type': 'string', 'example': 'NONE'}, 'username': {'type': 'string'}, 'password': {'type': 'string'}}}]
    class components_schemas_Monitor_monitorPing:
        """#/components/schemas/Monitor.monitorPing"""
        class R:
            allOf = [lambda: Defs.components_schemas_Monitor_monitor, {'type': 'object', 'properties': {'host': {'type': 'string', 'example': 'mail.dynu.com'}}}]
    class components_schemas_Monitor_monitorPort:
        """#/components/schemas/Monitor.monitorPort"""
        class R:
            allOf = [lambda: Defs.components_schemas_Monitor_monitor, {'type': 'object', 'properties': {'host': {'type': 'string', 'example': 'mail.dynu.com'}, 'port': {'type': 'integer', 'format': 'int32', 'example': 25}}}]
    class components_schemas_Ping_ping:
        """#/components/schemas/Ping.ping"""
        class R:
            type = 'object'
            required = ['message']
            _attrs = ['message']
            message = {'type': 'string', 'example': 'test'}
        R.message = 'test'
    class components_schemas_Ping_pong:
        """#/components/schemas/Ping.pong"""
        class R:
            type = 'object'
            _attrs = ['statusCode', 'message']
            statusCode = {'type': 'integer', 'format': 'int32', 'example': 200}
            message = {'type': 'string', 'example': 'test'}
        R.statusCode = 200
        R.message = 'test'
    class components_schemas_apiException:
        """#/components/schemas/apiException"""
        class R:
            type = 'object'
            _attrs = ['statusCode', 'type', 'message']
            statusCode = {'type': 'integer', 'format': 'int32'}
            type = {'type': 'string', 'enum': ['Application Exception', 'Argument Exception', 'Authentication Exception', 'Authorization Exception', 'IO Exception', 'Not Implemented', 'Parse Exception', 'Quota Exception', 'Timeout Exception', 'Request Exception', 'Server Exception', 'Validation Exception']}
            message = {'type': 'string'}
        R.statusCode = 0
        R.type = 'Application Exception'
        R.message = str_dflt
    class components_schemas_apiResponse:
        """#/components/schemas/apiResponse"""
        class R:
            type = 'object'
            _attrs = ['statusCode', 'exception']
            statusCode = {'type': 'integer', 'format': 'int32'}
            exception = {'type': 'object', '$ref': lambda: Defs.components_schemas_apiException}
        R.statusCode = 0
        R.exception = lambda: Defs.components_schemas_apiException

class dns:
    pth = "/dns"

    class get:
        """ Get a list of domains for DNS service."""
        class R:
            _ = {'tags': ['dns'], 'operationId': 'dnsGet', 'responses': {'200': Defs.components_responses_200DNSDomain, '401': Defs.components_responses_401, '500': Defs.components_responses_500}, 'security': [{'apiKey': []}, {'oauth2': []}]}

    class post:
        """ Add a new DNS service."""
        class R:
            _body = ['body'];
            _ = {'tags': ['dns'], 'operationId': 'dnsPost', 'requestBody': {'content': {}}, 'responses': {'200': Defs.components_responses_200, '500': Defs.components_responses_500, '501': Defs.components_responses_501, '502': Defs.components_responses_502}, 'security': [{'apiKey': []}, {'oauth2': []}], 'mime': 'application/json'}
            body = Defs.components_schemas_DNS_domain
        R.body = Defs.components_schemas_DNS_domain

class dns__getroot___hostname_:
    pth = "/dns/getroot/{hostname}"

    class get:
        """ Get the root domain name based on a hostname."""
        class R:
            _path = ['hostname'];
            _ = {'tags': ['dns'], 'operationId': 'dnsGetrootHostnameGet', 'responses': {'200': Defs.components_responses_200DNSHostnameGetGetrootByHostname, '401': Defs.components_responses_401, '500': Defs.components_responses_500, '502': Defs.components_responses_502}, 'security': [{'apiKey': []}, {'oauth2': []}]}
            hostname = {'type': 'string', 'example': 'test.mydomain.com'}
        R.hostname = hostname

class dns__record___hostname_:
    pth = "/dns/record/{hostname}"

    class get:
        """ Get DNS records based on a hostname and resource record type."""
        class R:
            _query = ['recordType']; _path = ['hostname'];
            _ = {'tags': ['dns'], 'operationId': 'dnsRecordHostnameGetRecordType', 'responses': {'200': Defs.components_responses_200DNSRecord, '401': Defs.components_responses_401, '500': Defs.components_responses_500, '502': Defs.components_responses_502}, 'security': [{'apiKey': []}, {'oauth2': []}]}
            hostname = {'type': 'string', 'example': 'test.mydomain.com'}
            recordType = {'type': 'string', 'enum': ['A', 'AAAA', 'CAA', 'CNAME', 'HINFO', 'LOC', 'MX', 'NS', 'PTR', 'PF', 'RP', 'SPF', 'TXT', 'UF', 'URI'], 'example': 'TXT'}
        R.hostname = hostname
        R.recordType = 'TXT'

class dns___id_:
    pth = "/dns/{id}"

    class get:
        """ Get details of a domain for DNS service."""
        class R:
            _path = ['id'];
            _ = {'tags': ['dns'], 'operationId': 'dnsIdGet', 'responses': {'200': Defs.components_responses_200DNSDomainGetById, '401': Defs.components_responses_401, '500': Defs.components_responses_500, '502': Defs.components_responses_502}, 'security': [{'apiKey': []}, {'oauth2': []}]}
            id = {'type': 'integer', 'format': 'int32', 'example': 8358362}
        R.id = id

    class post:
        """ Update an existing DNS service."""
        class R:
            _path = ['id']; _body = ['body'];
            _ = {'tags': ['dns'], 'operationId': 'dnsIdPost', 'requestBody': {'content': {}}, 'responses': {'200': Defs.components_responses_200, '500': Defs.components_responses_500, '501': Defs.components_responses_501, '502': Defs.components_responses_502}, 'security': [{'apiKey': []}, {'oauth2': []}], 'mime': 'application/json'}
            id = {'type': 'integer', 'format': 'int32', 'example': 1583628575}
            body = Defs.components_schemas_DNS_domain
        R.id = id
        R.body = Defs.components_schemas_DNS_domain

    class delete:
        """ Remove domain from DNS service."""
        class R:
            _path = ['id'];
            _ = {'tags': ['dns'], 'operationId': 'dnsIdDelete', 'responses': {'200': Defs.components_responses_200, '401': Defs.components_responses_401, '500': Defs.components_responses_500, '502': Defs.components_responses_502}, 'security': [{'apiKey': []}, {'oauth2': []}]}
            id = {'type': 'integer', 'format': 'int32', 'example': 358362}
        R.id = id

class dns___id___dnssec:
    pth = "/dns/{id}/dnssec"

    class get:
        """ DS record of DNSSEC for DNS service."""
        class R:
            _path = ['id'];
            _ = {'tags': ['dns'], 'operationId': 'dnsIdDNSSECGet', 'responses': {'200': Defs.components_responses_200DNSDNSSECGetById, '401': Defs.components_responses_401, '500': Defs.components_responses_500, '502': Defs.components_responses_502}, 'security': [{'apiKey': []}, {'oauth2': []}]}
            id = {'type': 'integer', 'format': 'int32', 'example': 1583624578}
        R.id = id

class dns___id___dnssec__enable:
    pth = "/dns/{id}/dnssec/enable"

    class get:
        """ Enable DNSSEC for DNS service."""
        class R:
            _path = ['id'];
            _ = {'tags': ['dns'], 'operationId': 'dnsIdDNSSECEnableId', 'responses': {'200': Defs.components_responses_200, '401': Defs.components_responses_401, '500': Defs.components_responses_500, '502': Defs.components_responses_502}, 'security': [{'apiKey': []}, {'oauth2': []}]}
            id = {'type': 'integer', 'format': 'int32', 'example': 358362457}
        R.id = id

class dns___id___dnssec__disable:
    pth = "/dns/{id}/dnssec/disable"

    class get:
        """ Disable DNSSEC for DNS service."""
        class R:
            _path = ['id'];
            _ = {'tags': ['dns'], 'operationId': 'dnsIdDNSSECDisableGet', 'responses': {'200': Defs.components_responses_200, '401': Defs.components_responses_401, '500': Defs.components_responses_500, '502': Defs.components_responses_502}, 'security': [{'apiKey': []}, {'oauth2': []}]}
            id = {'type': 'integer', 'format': 'int32', 'example': 1583624587}
        R.id = id

class dns___id___record:
    pth = "/dns/{id}/record"

    class get:
        """ Get a list of DNS records for DNS service."""
        class R:
            _path = ['id'];
            _ = {'tags': ['dns'], 'operationId': 'dnsIdRecordGet', 'responses': {'200': Defs.components_responses_200DNSRecord, '401': Defs.components_responses_401, '500': Defs.components_responses_500}, 'security': [{'apiKey': []}, {'oauth2': []}]}
            id = {'type': 'integer', 'format': 'int32', 'example': 35836275}
        R.id = id

    class post:
        """ Add a new DNS record for DNS service."""
        class R:
            _path = ['id']; _body = ['body'];
            _ = {'tags': ['dns'], 'operationId': 'dnsIdRecordPost', 'requestBody': {'content': {}}, 'responses': {'200': Defs.components_responses_200DNSRecordGetById, '401': Defs.components_responses_401, '500': Defs.components_responses_500, '501': Defs.components_responses_501, '502': Defs.components_responses_502, '503': Defs.components_responses_503}, 'security': [{'apiKey': []}, {'oauth2': []}], 'mime': 'application/json'}
            id = {'type': 'integer', 'format': 'int32', 'example': 35836275}
            body = {'oneOf': [Defs.components_schemas_DNS_dnsRecordA, Defs.components_schemas_DNS_dnsRecordAAAA, Defs.components_schemas_DNS_dnsRecordCAA, Defs.components_schemas_DNS_dnsRecordCNAME, Defs.components_schemas_DNS_dnsRecordHINFO, Defs.components_schemas_DNS_dnsRecordLOC, Defs.components_schemas_DNS_dnsRecordMX, Defs.components_schemas_DNS_dnsRecordNS, Defs.components_schemas_DNS_dnsRecordPTR, Defs.components_schemas_DNS_dnsRecordRP, Defs.components_schemas_DNS_dnsRecordSOA, Defs.components_schemas_DNS_dnsRecordSPF, Defs.components_schemas_DNS_dnsRecordSRV, Defs.components_schemas_DNS_dnsRecordSSHFP, Defs.components_schemas_DNS_dnsRecordTLSA, Defs.components_schemas_DNS_dnsRecordTXT, Defs.components_schemas_DNS_dnsRecordURI], 'example': {'nodeName': 'mail', 'recordType': 'A', 'ttl': 300, 'state': True, 'group': '', 'ipv4Address': '204.25.79.214'}}
        R.id = id
        R.body = {'nodeName': 'mail', 'recordType': 'A', 'ttl': 300, 'state': True, 'group': '', 'ipv4Address': '204.25.79.214'},

class dns___id___record___dnsRecordId_:
    pth = "/dns/{id}/record/{dnsRecordId}"

    class get:
        """ Get details of a DNS record for DNS service."""
        class R:
            _path = ['id', 'dnsRecordId'];
            _ = {'tags': ['dns'], 'operationId': 'dnsIdRecordDnsRecordIdGet', 'responses': {'200': Defs.components_responses_200DNSRecordGetById, '401': Defs.components_responses_401, '500': Defs.components_responses_500, '502': Defs.components_responses_502}, 'security': [{'apiKey': []}, {'oauth2': []}]}
            id = {'type': 'integer', 'format': 'int32', 'example': 35836278}
            dnsRecordId = {'type': 'integer', 'format': 'int32', 'example': 758426278}
        R.id = id
        R.dnsRecordId = dnsRecordId

    class post:
        """ Update an existing DNS record for DNS service."""
        class R:
            _path = ['id', 'dnsRecordId']; _body = ['body'];
            _ = {'tags': ['dns'], 'operationId': 'dnsIdRecordDnsRecordIdPost', 'requestBody': {'content': {}}, 'responses': {'200': Defs.components_responses_200DNSRecordGetById, '500': Defs.components_responses_500, '501': Defs.components_responses_501, '502': Defs.components_responses_502}, 'security': [{'apiKey': []}, {'oauth2': []}], 'mime': 'application/json'}
            id = {'type': 'integer', 'format': 'int32', 'example': 1583628575}
            dnsRecordId = {'type': 'integer', 'format': 'int32', 'example': 758426278}
            body = {'oneOf': [Defs.components_schemas_DNS_dnsRecordA, Defs.components_schemas_DNS_dnsRecordAAAA, Defs.components_schemas_DNS_dnsRecordCAA, Defs.components_schemas_DNS_dnsRecordCNAME, Defs.components_schemas_DNS_dnsRecordHINFO, Defs.components_schemas_DNS_dnsRecordLOC, Defs.components_schemas_DNS_dnsRecordMX, Defs.components_schemas_DNS_dnsRecordNS, Defs.components_schemas_DNS_dnsRecordPTR, Defs.components_schemas_DNS_dnsRecordRP, Defs.components_schemas_DNS_dnsRecordSOA, Defs.components_schemas_DNS_dnsRecordSPF, Defs.components_schemas_DNS_dnsRecordSRV, Defs.components_schemas_DNS_dnsRecordSSHFP, Defs.components_schemas_DNS_dnsRecordTLSA, Defs.components_schemas_DNS_dnsRecordTXT, Defs.components_schemas_DNS_dnsRecordURI], 'example': {'nodeName': 'mail', 'recordType': 'A', 'ttl': 300, 'state': True, 'group': '', 'ipv4Address': '204.25.79.214'}}
        R.id = id
        R.dnsRecordId = dnsRecordId
        R.body = {'nodeName': 'mail', 'recordType': 'A', 'ttl': 300, 'state': True, 'group': '', 'ipv4Address': '204.25.79.214'},

    class delete:
        """ Remove a DNS record from DNS service."""
        class R:
            _path = ['id', 'dnsRecordId'];
            _ = {'tags': ['dns'], 'operationId': 'dnsIdRecordDnsRecordIdDelete', 'responses': {'200': Defs.components_responses_200, '401': Defs.components_responses_401, '500': Defs.components_responses_500, '502': Defs.components_responses_502}, 'security': [{'apiKey': []}, {'oauth2': []}]}
            id = {'type': 'integer', 'format': 'int32', 'example': 789245718}
            dnsRecordId = {'type': 'integer', 'format': 'int32', 'example': 754258952}
        R.id = id
        R.dnsRecordId = dnsRecordId

class dns___id___webredirect:
    pth = "/dns/{id}/webredirect"

    class get:
        """ Get a list of web redirects."""
        class R:
            _path = ['id'];
            _ = {'tags': ['dns', 'webredirect'], 'operationId': 'dnsIdWebRedirectGet', 'responses': {'200': Defs.components_responses_200WebRedirect, '401': Defs.components_responses_401, '500': Defs.components_responses_500}, 'security': [{'apiKey': []}, {'oauth2': []}]}
            id = {'type': 'integer', 'format': 'int32', 'example': 35836275}
        R.id = id

    class post:
        """ Add a new web redirect."""
        class R:
            _path = ['id']; _body = ['body'];
            _ = {'tags': ['dns', 'webredirect'], 'operationId': 'dnsIdWebRedirectPost', 'requestBody': {'content': {}}, 'responses': {'200': Defs.components_responses_200WebRedirectGetById, '401': Defs.components_responses_401, '500': Defs.components_responses_500, '501': Defs.components_responses_501, '502': Defs.components_responses_502, '503': Defs.components_responses_503}, 'security': [{'apiKey': []}, {'oauth2': []}], 'mime': 'application/json'}
            id = {'type': 'integer', 'format': 'int32', 'example': 35836275}
            body = {'$ref': Defs.components_schemas_DNS_webRedirect, 'example': {'domainId': 123456789, 'nodeName': 'www', 'redirectType': 'PF', 'state': True, 'host': 'www.myotherdomain.com', 'port': 8080, 'includeQueryString': True}}
        R.id = id
        R.body = {'domainId': 123456789, 'nodeName': 'www', 'redirectType': 'PF', 'state': True, 'host': 'www.myotherdomain.com', 'port': 8080, 'includeQueryString': True},

class dns___id___webRedirect___webRedirectId_:
    pth = "/dns/{id}/webRedirect/{webRedirectId}"

    class get:
        """ Get details of the web redirect."""
        class R:
            _path = ['id', 'webRedirectId'];
            _ = {'tags': ['dns', 'webredirect'], 'operationId': 'dnsIdWebRedirectWebRedirectIdGet', 'responses': {'200': Defs.components_responses_200WebRedirectGetById, '401': Defs.components_responses_401, '500': Defs.components_responses_500, '502': Defs.components_responses_502}, 'security': [{'apiKey': []}, {'oauth2': []}]}
            id = {'type': 'integer', 'format': 'int32', 'example': 35836278}
            webRedirectId = {'type': 'integer', 'format': 'int32', 'example': 758426278}
        R.id = id
        R.webRedirectId = webRedirectId

    class post:
        """ Update an existing web redirect."""
        class R:
            _path = ['id', 'webRedirectId']; _body = ['body'];
            _ = {'tags': ['dns', 'webredirect'], 'operationId': 'dnsIdWebRedirectWebRedirectIdPost', 'requestBody': {'content': {}}, 'responses': {'200': Defs.components_responses_200WebRedirectGetById, '500': Defs.components_responses_500, '501': Defs.components_responses_501, '502': Defs.components_responses_502}, 'security': [{'apiKey': []}, {'oauth2': []}], 'mime': 'application/json'}
            id = {'type': 'integer', 'format': 'int32', 'example': 583628575}
            webRedirectId = {'type': 'integer', 'format': 'int32', 'example': 758426278}
            body = {'$ref': Defs.components_schemas_DNS_webRedirect, 'example': {'nodeName': 'www', 'redirectType': 'PF', 'state': True, 'port': 8080, 'useDynamicIPv4Address': True, 'useDynamicIPv6Address': True, 'cloak': True}}
        R.id = id
        R.webRedirectId = webRedirectId
        R.body = {'nodeName': 'www', 'redirectType': 'PF', 'state': True, 'port': 8080, 'useDynamicIPv4Address': True, 'useDynamicIPv6Address': True, 'cloak': True},

    class delete:
        """ Remove a web redirect."""
        class R:
            _path = ['id', 'webRedirectId'];
            _ = {'tags': ['dns', 'webredirect'], 'operationId': 'dnsIdWebRedirectWebRedirectIdDelete', 'responses': {'200': Defs.components_responses_200, '401': Defs.components_responses_401, '500': Defs.components_responses_500, '502': Defs.components_responses_502}, 'security': [{'apiKey': []}, {'oauth2': []}]}
            id = {'type': 'integer', 'format': 'int32', 'example': 789245718}
            webRedirectId = {'type': 'integer', 'format': 'int32', 'example': 542589526}
        R.id = id
        R.webRedirectId = webRedirectId

class dns__ipUpdateHistory:
    pth = "/dns/ipUpdateHistory"

    class get:
        """ Get a list of IP address updates."""
        class R:
            _ = {'tags': ['dns'], 'operationId': 'dnsIPUpdateHistoryGet', 'responses': {'200': Defs.components_responses_200DNSIPUpdateHistory, '401': Defs.components_responses_401, '500': Defs.components_responses_500}, 'security': [{'apiKey': []}, {'oauth2': []}]}

class dns__group:
    pth = "/dns/group"

    class get:
        """ Get a list of groups to which hosts are assigned to."""
        class R:
            _ = {'tags': ['dns', 'group'], 'operationId': 'dnsGroupGet', 'responses': {'200': Defs.components_responses_200DNSGroup, '401': Defs.components_responses_401, '500': Defs.components_responses_500}, 'security': [{'apiKey': []}, {'oauth2': []}]}

    class post:
        """ Add a new group."""
        class R:
            _body = ['body'];
            _ = {'tags': ['dns', 'group'], 'operationId': 'dnsGroupPost', 'requestBody': {'content': {}}, 'responses': {'200': Defs.components_responses_200DNSGroupGetById, '500': Defs.components_responses_500, '501': Defs.components_responses_501, '502': Defs.components_responses_502}, 'security': [{'apiKey': []}, {'oauth2': []}], 'mime': 'application/json'}
            body = {'$ref': Defs.components_schemas_DNS_dnsGroup, 'example': {'groupName': 'work'}}
        R.body = {'groupName': 'work'},

class dns__group___id_:
    pth = "/dns/group/{id}"

    class post:
        """ Update an existing group."""
        class R:
            _path = ['id']; _body = ['body'];
            _ = {'tags': ['dns', 'group'], 'operationId': 'dnsGroupIdPost', 'requestBody': {'content': {}}, 'responses': {'200': Defs.components_responses_200DNSGroupGetById, '500': Defs.components_responses_500, '501': Defs.components_responses_501, '502': Defs.components_responses_502}, 'security': [{'apiKey': []}, {'oauth2': []}], 'mime': 'application/json'}
            id = {'type': 'integer', 'format': 'int32', 'example': 358362857}
            body = {'$ref': Defs.components_schemas_DNS_dnsGroup, 'example': {'id': 35836285753, 'groupName': 'work', 'groupPassword': 'A8ce83cl31'}}
        R.id = id
        R.body = {'id': 35836285753, 'groupName': 'work', 'groupPassword': 'A8ce83cl31'},

    class delete:
        """ Remove a group."""
        class R:
            _path = ['id'];
            _ = {'tags': ['dns', 'group'], 'operationId': 'dnsGroupIdDelete', 'responses': {'200': Defs.components_responses_200, '401': Defs.components_responses_401, '500': Defs.components_responses_500, '502': Defs.components_responses_502}, 'security': [{'apiKey': []}, {'oauth2': []}]}
            id = {'type': 'integer', 'format': 'int32', 'example': 358362}
        R.id = id

class dns__limit:
    pth = "/dns/limit"

    class get:
        """ Limits associated with hostnames."""
        class R:
            _ = {'tags': ['dns', 'limit'], 'operationId': 'dnsLimitGet', 'responses': {'200': Defs.components_responses_200DNSLimit, '401': Defs.components_responses_401, '500': Defs.components_responses_500}, 'security': [{'apiKey': []}, {'oauth2': []}]}

class dns___id___limit:
    pth = "/dns/{id}/limit"

    class get:
        """ Limits associated with DNS records."""
        class R:
            _path = ['id'];
            _ = {'tags': ['dns', 'limit'], 'operationId': 'dnsRecordLimitGet', 'responses': {'200': Defs.components_responses_200DNSRecordLimit, '401': Defs.components_responses_401, '500': Defs.components_responses_500}, 'security': [{'apiKey': []}, {'oauth2': []}]}
            id = {'type': 'integer', 'format': 'int32', 'example': 35836275}
        R.id = id

class domain:
    pth = "/domain"

    class get:
        """ Get a list of domains for domain registration service."""
        class R:
            _ = {'tags': ['domain'], 'operationId': 'domainGet', 'responses': {'200': Defs.components_responses_200Domain, '401': Defs.components_responses_401, '500': Defs.components_responses_500}, 'security': [{'apiKey': []}, {'oauth2': []}]}

class domain___id_:
    pth = "/domain/{id}"

    class get:
        """ Get details of a domain registration domain."""
        class R:
            _path = ['id'];
            _ = {'tags': ['domain'], 'operationId': 'domainGetId', 'responses': {'200': Defs.components_responses_200DomainGetById, '401': Defs.components_responses_401, '500': Defs.components_responses_500, '502': Defs.components_responses_502}, 'security': [{'apiKey': []}, {'oauth2': []}]}
            id = {'type': 'integer', 'format': 'int32', 'example': 358362}
        R.id = id

class domain___id___autorenewEnable:
    pth = "/domain/{id}/autorenewEnable"

    class get:
        """ Enable autorenewal for a domain."""
        class R:
            _path = ['id'];
            _ = {'tags': ['domain'], 'operationId': 'domainAutorenewEnableGetId', 'responses': {'200': Defs.components_responses_200, '401': Defs.components_responses_401, '500': Defs.components_responses_500, '502': Defs.components_responses_502}, 'security': [{'apiKey': []}, {'oauth2': []}]}
            id = {'type': 'integer', 'format': 'int32', 'example': 358362}
        R.id = id

class domain___id___autorenewDisable:
    pth = "/domain/{id}/autorenewDisable"

    class get:
        """ Disable autorenewal for a domain."""
        class R:
            _path = ['id'];
            _ = {'tags': ['domain'], 'operationId': 'domainAutorenewDisableGetId', 'responses': {'200': Defs.components_responses_200, '401': Defs.components_responses_401, '500': Defs.components_responses_500, '502': Defs.components_responses_502}, 'security': [{'apiKey': []}, {'oauth2': []}]}
            id = {'type': 'integer', 'format': 'int32', 'example': 358362}
        R.id = id

class domain___id___lock:
    pth = "/domain/{id}/lock"

    class get:
        """ Lock a domain."""
        class R:
            _path = ['id'];
            _ = {'tags': ['domain'], 'operationId': 'domainLockGetId', 'responses': {'200': Defs.components_responses_200, '401': Defs.components_responses_401, '500': Defs.components_responses_500, '502': Defs.components_responses_502}, 'security': [{'apiKey': []}, {'oauth2': []}]}
            id = {'type': 'integer', 'format': 'int32', 'example': 358362}
        R.id = id

class domain___id___unlock:
    pth = "/domain/{id}/unlock"

    class get:
        """ Unlock a domain."""
        class R:
            _path = ['id'];
            _ = {'tags': ['domain'], 'operationId': 'domainUnlockGetId', 'responses': {'200': Defs.components_responses_200, '401': Defs.components_responses_401, '500': Defs.components_responses_500, '502': Defs.components_responses_502}, 'security': [{'apiKey': []}, {'oauth2': []}]}
            id = {'type': 'integer', 'format': 'int32', 'example': 358362}
        R.id = id

class domain___id___nameServer:
    pth = "/domain/{id}/nameServer"

    class get:
        """ Get a list of name servers for a domain."""
        class R:
            _path = ['id'];
            _ = {'tags': ['domain'], 'operationId': 'domainNameServerGet', 'responses': {'200': Defs.components_responses_200DomainNameServer, '401': Defs.components_responses_401, '500': Defs.components_responses_500}, 'security': [{'apiKey': []}, {'oauth2': []}]}
            id = {'type': 'integer', 'format': 'int32', 'example': 358362}
        R.id = id

    class delete:
        """ Delete a name server of a domain."""
        class R:
            _query = ['nameServer']; _path = ['id'];
            _ = {'tags': ['domain'], 'operationId': 'domainNameServerDeleteGetId', 'responses': {'200': Defs.components_responses_200, '401': Defs.components_responses_401, '500': Defs.components_responses_500, '502': Defs.components_responses_502}, 'security': [{'apiKey': []}, {'oauth2': []}]}
            id = {'type': 'integer', 'format': 'int32', 'example': 358362}
            nameServer = {'type': 'string', 'example': 'ns3.dynu.com'}
        R.id = id
        R.nameServer = 'ns3.dynu.com'

class domain___id___nameServer__add:
    pth = "/domain/{id}/nameServer/add"

    class get:
        """ Add a name server to a domain."""
        class R:
            _query = ['nameServer']; _path = ['id'];
            _ = {'tags': ['domain'], 'operationId': 'domainNameServerAddGetId', 'responses': {'200': Defs.components_responses_200, '401': Defs.components_responses_401, '500': Defs.components_responses_500, '502': Defs.components_responses_502}, 'security': [{'apiKey': []}, {'oauth2': []}]}
            id = {'type': 'integer', 'format': 'int32', 'example': 358362}
            nameServer = {'type': 'string', 'example': 'ns3.dynu.com'}
        R.id = id
        R.nameServer = 'ns3.dynu.com'

class domain___id___nameServer__primary:
    pth = "/domain/{id}/nameServer/primary"

    class get:
        """ Make a name server the primary name server of a domain."""
        class R:
            _query = ['nameServer']; _path = ['id'];
            _ = {'tags': ['domain'], 'operationId': 'domainNameServerPrimaryGetId', 'responses': {'200': Defs.components_responses_200, '401': Defs.components_responses_401, '500': Defs.components_responses_500, '502': Defs.components_responses_502}, 'security': [{'apiKey': []}, {'oauth2': []}]}
            id = {'type': 'integer', 'format': 'int32', 'example': 358362}
            nameServer = {'type': 'string', 'example': 'ns1.dynu.com'}
        R.id = id
        R.nameServer = 'ns1.dynu.com'

class domain___id___cancel:
    pth = "/domain/{id}/cancel"

    class get:
        """ Cancel a domain."""
        class R:
            _path = ['id'];
            _ = {'tags': ['domain'], 'operationId': 'domainCancelGetId', 'responses': {'200': Defs.components_responses_200, '401': Defs.components_responses_401, '500': Defs.components_responses_500, '502': Defs.components_responses_502}, 'security': [{'apiKey': []}, {'oauth2': []}]}
            id = {'type': 'integer', 'format': 'int32', 'example': 358362}
        R.id = id

class email:
    pth = "/email"

    class get:
        """ Get a list of email services."""
        class R:
            _ = {'tags': ['email'], 'operationId': 'emailGet', 'responses': {'200': Defs.components_responses_200Email, '401': Defs.components_responses_401, '500': Defs.components_responses_500}, 'security': [{'apiKey': []}, {'oauth2': []}]}

class email___id_:
    pth = "/email/{id}"

    class get:
        """ Get details of an email service."""
        class R:
            _path = ['id'];
            _ = {'tags': ['email'], 'operationId': 'emailGetId', 'responses': {'200': Defs.components_responses_200EmailGetById, '401': Defs.components_responses_401, '500': Defs.components_responses_500, '502': Defs.components_responses_502}, 'security': [{'apiKey': []}, {'oauth2': []}]}
            id = {'type': 'integer', 'format': 'int32', 'example': 358362}
        R.id = id

class email___id___deliveryQueue:
    pth = "/email/{id}/deliveryQueue"

    class get:
        """ Get a list of messages in delivery queue."""
        class R:
            _path = ['id'];
            _ = {'tags': ['email'], 'operationId': 'emailDeliveryQueueGet', 'responses': {'200': Defs.components_responses_200EmailDeliveryQueue, '401': Defs.components_responses_401, '500': Defs.components_responses_500}, 'security': [{'apiKey': []}, {'oauth2': []}]}
            id = {'type': 'integer', 'format': 'int32', 'example': 358362}
        R.id = id

class email___id___blacklist:
    pth = "/email/{id}/blacklist"

    class get:
        """ Get a list of blacklist."""
        class R:
            _path = ['id'];
            _ = {'tags': ['email'], 'operationId': 'emailBlacklistGet', 'responses': {'200': Defs.components_responses_200EmailBlacklist, '401': Defs.components_responses_401, '500': Defs.components_responses_500}, 'security': [{'apiKey': []}, {'oauth2': []}]}
            id = {'type': 'integer', 'format': 'int32', 'example': 358362}
        R.id = id

    class post:
        """ Add a new blacklist for email service."""
        class R:
            _path = ['id']; _body = ['body'];
            _ = {'tags': ['email'], 'operationId': 'emailIdBlacklistPost', 'requestBody': {'content': {}}, 'responses': {'200': Defs.components_responses_200EmailBlacklistGetById, '401': Defs.components_responses_401, '500': Defs.components_responses_500, '501': Defs.components_responses_501, '502': Defs.components_responses_502, '503': Defs.components_responses_503}, 'security': [{'apiKey': []}, {'oauth2': []}], 'mime': 'application/json'}
            id = {'type': 'integer', 'format': 'int32', 'example': 35836275}
            body = {'$ref': Defs.components_schemas_Email_emailBlacklist, 'example': {'type': 'EmailAddress', 'data': 'bademail@externaldomain.com', 'state': True}}
        R.id = id
        R.body = {'type': 'EmailAddress', 'data': 'bademail@externaldomain.com', 'state': True},

class email___id___blacklist___blacklistId_:
    pth = "/email/{id}/blacklist/{blacklistId}"

    class get:
        """ Get details of a blacklist for email service."""
        class R:
            _path = ['id', 'blacklistId'];
            _ = {'tags': ['email'], 'operationId': 'emailIdBlacklistBlacklistIdGet', 'responses': {'200': Defs.components_responses_200EmailBlacklistGetById, '401': Defs.components_responses_401, '500': Defs.components_responses_500, '502': Defs.components_responses_502}, 'security': [{'apiKey': []}, {'oauth2': []}]}
            id = {'type': 'integer', 'format': 'int32', 'example': 35836278}
            blacklistId = {'type': 'integer', 'format': 'int32', 'example': 758426278}
        R.id = id
        R.blacklistId = blacklistId

    class post:
        """ Update details of an existing blacklist for email service."""
        class R:
            _path = ['id', 'blacklistId']; _body = ['body'];
            _ = {'tags': ['email'], 'operationId': 'emailIdBlacklistBlacklistIdPost', 'requestBody': {'content': {}}, 'responses': {'200': Defs.components_responses_200EmailBlacklistGetById, '401': Defs.components_responses_401, '500': Defs.components_responses_500, '502': Defs.components_responses_502}, 'security': [{'apiKey': []}, {'oauth2': []}], 'mime': 'application/json'}
            id = {'type': 'integer', 'format': 'int32', 'example': 35836278}
            blacklistId = {'type': 'integer', 'format': 'int32', 'example': 758426278}
            body = {'$ref': Defs.components_schemas_Email_emailBlacklist, 'example': {'type': 'EmailAddress', 'data': 'bademail@externaldomain.com', 'state': True}}
        R.id = id
        R.blacklistId = blacklistId
        R.body = {'type': 'EmailAddress', 'data': 'bademail@externaldomain.com', 'state': True},

    class delete:
        """ Remove a blacklist from email service."""
        class R:
            _path = ['id', 'blacklistId'];
            _ = {'tags': ['email'], 'operationId': 'emailIdBlacklistBlacklistIdDelete', 'responses': {'200': Defs.components_responses_200, '401': Defs.components_responses_401, '500': Defs.components_responses_500, '502': Defs.components_responses_502}, 'security': [{'apiKey': []}, {'oauth2': []}]}
            id = {'type': 'integer', 'format': 'int32', 'example': 578924571}
            blacklistId = {'type': 'integer', 'format': 'int32', 'example': 754258952}
        R.id = id
        R.blacklistId = blacklistId

class email___id___whitelist:
    pth = "/email/{id}/whitelist"

    class get:
        """ Get a list of whitelist."""
        class R:
            _path = ['id'];
            _ = {'tags': ['email'], 'operationId': 'emailWhitelistGet', 'responses': {'200': Defs.components_responses_200EmailWhitelist, '401': Defs.components_responses_401, '500': Defs.components_responses_500}, 'security': [{'apiKey': []}, {'oauth2': []}]}
            id = {'type': 'integer', 'format': 'int32', 'example': 358362}
        R.id = id

    class post:
        """ Add a new whitelist for email service."""
        class R:
            _path = ['id']; _body = ['body'];
            _ = {'tags': ['email'], 'operationId': 'emailIdWhitelistPost', 'requestBody': {'content': {}}, 'responses': {'200': Defs.components_responses_200EmailWhitelistGetById, '401': Defs.components_responses_401, '500': Defs.components_responses_500, '501': Defs.components_responses_501, '502': Defs.components_responses_502, '503': Defs.components_responses_503}, 'security': [{'apiKey': []}, {'oauth2': []}], 'mime': 'application/json'}
            id = {'type': 'integer', 'format': 'int32', 'example': 35836275}
            body = {'$ref': Defs.components_schemas_Email_emailWhitelist, 'example': {'type': 'EmailAddress', 'data': 'bademail@externaldomain.com', 'state': True}}
        R.id = id
        R.body = {'type': 'EmailAddress', 'data': 'bademail@externaldomain.com', 'state': True},

class email___id___whitelist___whitelistId_:
    pth = "/email/{id}/whitelist/{whitelistId}"

    class get:
        """ Get details of a whitelist for email service."""
        class R:
            _path = ['id', 'whitelistId'];
            _ = {'tags': ['email'], 'operationId': 'emailIdWhitelistWhitelistIdGet', 'responses': {'200': Defs.components_responses_200EmailWhitelistGetById, '401': Defs.components_responses_401, '500': Defs.components_responses_500, '502': Defs.components_responses_502}, 'security': [{'apiKey': []}, {'oauth2': []}]}
            id = {'type': 'integer', 'format': 'int32', 'example': 35836278}
            whitelistId = {'type': 'integer', 'format': 'int32', 'example': 758426278}
        R.id = id
        R.whitelistId = whitelistId

    class post:
        """ Update details of an existing whitelist for email service."""
        class R:
            _path = ['id', 'whitelistId']; _body = ['body'];
            _ = {'tags': ['email'], 'operationId': 'emailIdWhitelistWhitelistIdPost', 'requestBody': {'content': {}}, 'responses': {'200': Defs.components_responses_200EmailWhitelistGetById, '401': Defs.components_responses_401, '500': Defs.components_responses_500, '502': Defs.components_responses_502}, 'security': [{'apiKey': []}, {'oauth2': []}], 'mime': 'application/json'}
            id = {'type': 'integer', 'format': 'int32', 'example': 35836278}
            whitelistId = {'type': 'integer', 'format': 'int32', 'example': 758426278}
            body = {'$ref': Defs.components_schemas_Email_emailWhitelist, 'example': {'type': 'EmailAddress', 'data': 'bademail@externaldomain.com', 'state': True}}
        R.id = id
        R.whitelistId = whitelistId
        R.body = {'type': 'EmailAddress', 'data': 'bademail@externaldomain.com', 'state': True},

    class delete:
        """ Remove a whitelist from email service."""
        class R:
            _path = ['id', 'whitelistId'];
            _ = {'tags': ['email'], 'operationId': 'emailIdWhitelistWhitelistIdDelete', 'responses': {'200': Defs.components_responses_200, '401': Defs.components_responses_401, '500': Defs.components_responses_500, '502': Defs.components_responses_502}, 'security': [{'apiKey': []}, {'oauth2': []}]}
            id = {'type': 'integer', 'format': 'int32', 'example': 789245718}
            whitelistId = {'type': 'integer', 'format': 'int32', 'example': 754258952}
        R.id = id
        R.whitelistId = whitelistId

class monitor__limit:
    pth = "/monitor/limit"

    class get:
        """ Limits associated with monitoring."""
        class R:
            _ = {'tags': ['monitor', 'limit'], 'operationId': 'monitorLimitGet', 'responses': {'200': Defs.components_responses_200MonitorLimit, '401': Defs.components_responses_401, '500': Defs.components_responses_500}, 'security': [{'apiKey': []}, {'oauth2': []}]}

class monitor:
    pth = "/monitor"

    class get:
        """ Get a list of monitors."""
        class R:
            _ = {'tags': ['monitor'], 'operationId': 'monitorGet', 'responses': {'200': Defs.components_responses_200Monitor, '401': Defs.components_responses_401, '500': Defs.components_responses_500}, 'security': [{'apiKey': []}, {'oauth2': []}]}

    class post:
        """ Add a new monitor."""
        class R:
            _body = ['body'];
            _ = {'tags': ['monitor'], 'operationId': 'monitorAddPost', 'requestBody': {'content': {}}, 'responses': {'200': Defs.components_responses_200MonitorAdd, '401': Defs.components_responses_401, '500': Defs.components_responses_500, '501': Defs.components_responses_501, '502': Defs.components_responses_502, '503': Defs.components_responses_503}, 'security': [{'apiKey': []}, {'oauth2': []}], 'mime': 'application/json'}
            body = {'oneOf': [Defs.components_schemas_Monitor_monitorDNS, Defs.components_schemas_Monitor_monitorHTTP, Defs.components_schemas_Monitor_monitorKeyword, Defs.components_schemas_Monitor_monitorPing, Defs.components_schemas_Monitor_monitorPort], 'example': {'name': 'HTTP monitor for www.dynu.com', 'type': 'HTTP', 'checkInterval': 10, 'url': 'https://www.dynu.com', 'authenticationType': 'NONE'}}
        R.body = {'name': 'HTTP monitor for www.dynu.com', 'type': 'HTTP', 'checkInterval': 10, 'url': 'https://www.dynu.com', 'authenticationType': 'NONE'},

class monitor___id_:
    pth = "/monitor/{id}"

    class get:
        """ Get details of a monitor."""
        class R:
            _path = ['id'];
            _ = {'tags': ['monitor'], 'operationId': 'monitorGetId', 'responses': {'200': Defs.components_responses_200MonitorGetById, '401': Defs.components_responses_401, '500': Defs.components_responses_500, '502': Defs.components_responses_502}, 'security': [{'apiKey': []}, {'oauth2': []}]}
            id = {'type': 'integer', 'format': 'int32', 'example': 358362}
        R.id = id

    class delete:
        """ Delete a monitor."""
        class R:
            _path = ['id'];
            _ = {'tags': ['monitor'], 'operationId': 'monitorDeleteGetId', 'responses': {'200': Defs.components_responses_200, '401': Defs.components_responses_401, '500': Defs.components_responses_500, '502': Defs.components_responses_502}, 'security': [{'apiKey': []}, {'oauth2': []}]}
            id = {'type': 'integer', 'format': 'int32', 'example': 358362}
        R.id = id

class monitor___id___pause:
    pth = "/monitor/{id}/pause"

    class get:
        """ Pause a monitor."""
        class R:
            _path = ['id'];
            _ = {'tags': ['monitor'], 'operationId': 'monitorPauseGetId', 'responses': {'200': Defs.components_responses_200, '401': Defs.components_responses_401, '500': Defs.components_responses_500, '502': Defs.components_responses_502}, 'security': [{'apiKey': []}, {'oauth2': []}]}
            id = {'type': 'integer', 'format': 'int32', 'example': 358362}
        R.id = id

class monitor___id___unpause:
    pth = "/monitor/{id}/unpause"

    class get:
        """ Unpause a monitor."""
        class R:
            _path = ['id'];
            _ = {'tags': ['monitor'], 'operationId': 'monitorUnpauseGetId', 'responses': {'200': Defs.components_responses_200, '401': Defs.components_responses_401, '500': Defs.components_responses_500, '502': Defs.components_responses_502}, 'security': [{'apiKey': []}, {'oauth2': []}]}
            id = {'type': 'integer', 'format': 'int32', 'example': 358362}
        R.id = id

class ping:
    pth = "/ping"

    class get:
        """ Ping the API server to obtain the pong response."""
        class R:
            _query = ['message'];
            _ = {'tags': ['ping'], 'operationId': 'pingGet', 'responses': {'200': Defs.components_responses_200Ping, '500': Defs.components_responses_500, '501': Defs.components_responses_501, '502': Defs.components_responses_502}, 'security': []}
            message = {'type': 'string', 'example': 'test'}
        R.message = 'test'

    class post:
        """ Ping the API server to obtain the pong response."""
        class R:
            _body = ['body'];
            _ = {'tags': ['ping'], 'operationId': 'pingPost', 'requestBody': {'content': {}}, 'responses': {'200': Defs.components_responses_200Ping, '500': Defs.components_responses_500, '501': Defs.components_responses_501, '502': Defs.components_responses_502}, 'security': [], 'mime': 'application/json'}
            body = Defs.components_schemas_Ping_ping
        R.body = Defs.components_schemas_Ping_ping

# ─────────────── Tools ─────────────────────
import requests, json, functools, inspect, os

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
        if is_(def_, str) and def_.startswith('obj:'):
            def_ = getattr(Defs, def_[4:])
        if is_(def_, (float, int, bool, str)):
            return def_
        obj = Tools.obj
        if is_(def_, list):
            return [obj(def_[0])]
        if is_(def_, dict):
            return {k: obj(v) for k, v in def_.items()}
        R = g(def_, 'R', 0)
        if R:
            return obj(R)
        l = g(def_, '_attrs', [i for i in dir(def_) if not i[0] == '_'])
        return {k: obj(g(def_, k)) for k in l if not is_(g(def_, k), dict)}

    @staticmethod
    def send(meth, *args):
        if args:
            meth = args[0]   # ico in line
        env = os.environ.get
        getenv = lambda v: env(v[1:], '') if (v and v[0] == '$') else v

        def repl(s, keyw={'for', 'async', 'from', 'if', 'import', 'while'}):
            if isinstance(s, str):
                for k in keyw:
                    s = s.replace(f'{k}__', k)
            else:
                s = json.loads(repl(json.dumps(s)))
            return s

        # if '__user_id' in str(meth): breakpoint() # FIXME BREAKPOINT
        try:
            methd, pth, params, data, h = Tools.build_req(meth)
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
    