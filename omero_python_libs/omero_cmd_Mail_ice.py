# -*- coding: utf-8 -*-
# **********************************************************************
#
# Copyright (c) 2003-2017 ZeroC, Inc. All rights reserved.
#
# This copy of Ice is licensed to you under the terms described in the
# ICE_LICENSE file included in this distribution.
#
# **********************************************************************
#
# Ice version 3.6.4
#
# <auto-generated>
#
# Generated from file `Mail.ice'
#
# Warning: do not edit this file.
#
# </auto-generated>
#

from sys import version_info as _version_info_
import Ice, IcePy
import omero_Collections_ice
import omero_System_ice
import omero_cmd_API_ice

# Included module omero
_M_omero = Ice.openModule('omero')

# Included module omero.model
_M_omero.model = Ice.openModule('omero.model')

# Included module Ice
_M_Ice = Ice.openModule('Ice')

# Included module omero.sys
_M_omero.sys = Ice.openModule('omero.sys')

# Included module omero.api
_M_omero.api = Ice.openModule('omero.api')

# Included module Glacier2
_M_Glacier2 = Ice.openModule('Glacier2')

# Included module omero.cmd
_M_omero.cmd = Ice.openModule('omero.cmd')

# Start of module omero
__name__ = 'omero'

# Start of module omero.cmd
__name__ = 'omero.cmd'

if 'SendEmailRequest' not in _M_omero.cmd.__dict__:
    _M_omero.cmd.SendEmailRequest = Ice.createTempClass()
    class SendEmailRequest(_M_omero.cmd.Request):
        """
        Requests an email to be send to all users of the omero
        determines inactive users, an active members of given groups
        and/or specific users.
        examples:
        - omero.cmd.SendEmailRequest(subject, body, everyone=True)
        sends message to everyone who has email set
        and is an active user
        - omero.cmd.SendEmailRequest(subject, body, everyone=True, inactive=True)
        sends message to everyone who has email set,
        even inactive users
        - omero.cmd.SendEmailRequest(subject, body, groupIds=\[...],
        userIds=\[...] )
        sends email to active members of given groups and selected users
        - extra=\[...] allows to set extra email address if not in DB
        """
        def __init__(self, subject='', body='', html=False, userIds=None, groupIds=None, extra=None, inactive=False, everyone=False):
            _M_omero.cmd.Request.__init__(self)
            self.subject = subject
            self.body = body
            self.html = html
            self.userIds = userIds
            self.groupIds = groupIds
            self.extra = extra
            self.inactive = inactive
            self.everyone = everyone

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::omero::cmd::Request', '::omero::cmd::SendEmailRequest')

        def ice_id(self, current=None):
            return '::omero::cmd::SendEmailRequest'

        def ice_staticId():
            return '::omero::cmd::SendEmailRequest'
        ice_staticId = staticmethod(ice_staticId)

        def __str__(self):
            return IcePy.stringify(self, _M_omero.cmd._t_SendEmailRequest)

        __repr__ = __str__

    _M_omero.cmd.SendEmailRequestPrx = Ice.createTempClass()
    class SendEmailRequestPrx(_M_omero.cmd.RequestPrx):

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_omero.cmd.SendEmailRequestPrx.ice_checkedCast(proxy, '::omero::cmd::SendEmailRequest', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_omero.cmd.SendEmailRequestPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

        def ice_staticId():
            return '::omero::cmd::SendEmailRequest'
        ice_staticId = staticmethod(ice_staticId)

    _M_omero.cmd._t_SendEmailRequestPrx = IcePy.defineProxy('::omero::cmd::SendEmailRequest', SendEmailRequestPrx)

    _M_omero.cmd._t_SendEmailRequest = IcePy.defineClass('::omero::cmd::SendEmailRequest', SendEmailRequest, -1, (), False, False, _M_omero.cmd._t_Request, (), (
        ('subject', (), IcePy._t_string, False, 0),
        ('body', (), IcePy._t_string, False, 0),
        ('html', (), IcePy._t_bool, False, 0),
        ('userIds', (), _M_omero.sys._t_LongList, False, 0),
        ('groupIds', (), _M_omero.sys._t_LongList, False, 0),
        ('extra', (), _M_omero.api._t_StringSet, False, 0),
        ('inactive', (), IcePy._t_bool, False, 0),
        ('everyone', (), IcePy._t_bool, False, 0)
    ))
    SendEmailRequest._ice_type = _M_omero.cmd._t_SendEmailRequest

    _M_omero.cmd.SendEmailRequest = SendEmailRequest
    del SendEmailRequest

    _M_omero.cmd.SendEmailRequestPrx = SendEmailRequestPrx
    del SendEmailRequestPrx

if 'SendEmailResponse' not in _M_omero.cmd.__dict__:
    _M_omero.cmd.SendEmailResponse = Ice.createTempClass()
    class SendEmailResponse(_M_omero.cmd.Response):
        """
        Successful response for {@code SendEmailRequest}. Contains
        a list of invalid users that has no email address set.
        If no recipients or invalid users found, an {@code ERR} will be
        returned.
        - invalidusers is a list of userIds that email didn't pass criteria
        such as was empty or less then 5 characters
        - invalidemails is a list of email addresses that send email failed
        - total is a total number of email in the pull to be sent.
        - success is a number of emails that were sent successfully.
        """
        def __init__(self, total=0, success=0, invalidusers=None, invalidemails=None):
            _M_omero.cmd.Response.__init__(self)
            self.total = total
            self.success = success
            self.invalidusers = invalidusers
            self.invalidemails = invalidemails

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::omero::cmd::Response', '::omero::cmd::SendEmailResponse')

        def ice_id(self, current=None):
            return '::omero::cmd::SendEmailResponse'

        def ice_staticId():
            return '::omero::cmd::SendEmailResponse'
        ice_staticId = staticmethod(ice_staticId)

        def __str__(self):
            return IcePy.stringify(self, _M_omero.cmd._t_SendEmailResponse)

        __repr__ = __str__

    _M_omero.cmd.SendEmailResponsePrx = Ice.createTempClass()
    class SendEmailResponsePrx(_M_omero.cmd.ResponsePrx):

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_omero.cmd.SendEmailResponsePrx.ice_checkedCast(proxy, '::omero::cmd::SendEmailResponse', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_omero.cmd.SendEmailResponsePrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

        def ice_staticId():
            return '::omero::cmd::SendEmailResponse'
        ice_staticId = staticmethod(ice_staticId)

    _M_omero.cmd._t_SendEmailResponsePrx = IcePy.defineProxy('::omero::cmd::SendEmailResponse', SendEmailResponsePrx)

    _M_omero.cmd._t_SendEmailResponse = IcePy.defineClass('::omero::cmd::SendEmailResponse', SendEmailResponse, -1, (), False, False, _M_omero.cmd._t_Response, (), (
        ('total', (), IcePy._t_long, False, 0),
        ('success', (), IcePy._t_long, False, 0),
        ('invalidusers', (), _M_omero.api._t_LongList, False, 0),
        ('invalidemails', (), _M_omero.api._t_StringSet, False, 0)
    ))
    SendEmailResponse._ice_type = _M_omero.cmd._t_SendEmailResponse

    _M_omero.cmd.SendEmailResponse = SendEmailResponse
    del SendEmailResponse

    _M_omero.cmd.SendEmailResponsePrx = SendEmailResponsePrx
    del SendEmailResponsePrx

# End of module omero.cmd

__name__ = 'omero'

# End of module omero
