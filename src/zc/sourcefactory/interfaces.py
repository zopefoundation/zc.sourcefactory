##############################################################################
#
# Copyright (c) 2006 Zope Corporation. All Rights Reserved.
#
# This software is subject to the provisions of the Zope Visible Source
# License, Version 1.0 (ZVSL).  A copy of the ZVSL should accompany this
# distribution.
#
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""Interfaces for zc.sourcefactory.

"""
__docformat__ = "reStructuredText"


import zope.interface
import zope.schema.interfaces

class ISourceFactory(zope.interface.Interface):

    def __call__():
        """Create and return the source or source binder."""


class IFactoredSource(zope.schema.interfaces.IIterableSource):
    """An iterable source that was created from a source factory."""

    factory = zope.interface.Attribute("The source factory.")


class IContextualSource(IFactoredSource):
    """A source operating in context."""

    context = zope.interface.Attribute("The context the source is bound to.")
    factory = zope.interface.Attribute("The source factory.")


class INamedSource(zope.interface.Interface):
    """A marker interface to register named source for."""


class IToken(zope.interface.Interface):
    """A string representing a token that uniquely identifies a value."""


# Policies

class ITokenPolicy(zope.interface.Interface):
    """The token policy maps values and tokens."""

    def getValue(source, token):
        """Return a token for the value."""

    def getToken(value):
        """Return a token for the value."""


class ITermPolicy(zope.interface.Interface):
    """The term policy creates terms and provides data for terms."""

    def createTerm(source, value, title, token, request):
        """Create and return a term object."""

    def getTitle(value):
        """Return a title for the value.

        The return value should not be localized; that is the
        responsibility of the user.  The title may be an
        internationalized message value.

        """


class IValuePolicy(zope.interface.Interface):
    """The value policy retrieves and filters values for a source."""

    def getValues():
        """Return the values for the source."""

    def filterValue(value):
        """Determine whether the value should be filtered out or not."""


class IContextualValuePolicy(zope.interface.Interface):
    """The contextual value policy retrieves and filters values for a source
    within context.

    """

    def getValues(context):
        """Return the values for the source in the given context."""

    def filterValue(context, value):
        """Return the values for the source in the given context."""

# Standard combined policies

class ISourcePolicy(ITokenPolicy, ITermPolicy, IValuePolicy):
    pass


class IContextualSourcePolicy(
    ITokenPolicy, ITermPolicy, IContextualValuePolicy):
    pass
