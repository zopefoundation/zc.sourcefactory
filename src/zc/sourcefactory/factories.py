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
"""Basic factories.

"""
__docformat__ = "reStructuredText"


import zope.interface
import zope.schema.interfaces

import zc.sourcefactory.interfaces
import zc.sourcefactory.source


class BasicSourceFactory(object):
    """Abstract base class for a source factory.

    Implementors must provide an implementation for `getValues`.
    """

    zope.interface.implements(zc.sourcefactory.interfaces.ISourceFactory)

    def __new__(cls):
        """Create the factory object and return source."""
        factory = object.__new__(cls)
        factory.__init__()
        return zc.sourcefactory.source.FactoredSource(factory)


class ContextualSourceFactory(BasicSourceFactory):
    """Abstract base class for a source factory for a context-bound source.

    Implementors must provide an implementation for `getValues`.
    """

    def __new__(cls):
        """Create the factory object and return source."""
        factory = object.__new__(cls)
        factory.__init__()
        return FactoredContextualSourceBinder(factory)


class FactoredContextualSourceBinder(object):
    """A context source binder for factored sources."""

    zope.interface.implements(zope.schema.interfaces.IContextSourceBinder)

    def __init__(self, factory):
        self.factory = factory

    def __call__(self, context):
        return zc.sourcefactory.source.FactoredContextualSource(
            self.factory, context)
