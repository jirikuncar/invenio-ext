# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2011, 2012, 2013, 2014, 2015 CERN.
#
# Invenio is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# Invenio is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Invenio; if not, write to the Free Software Foundation, Inc.,
# 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.

"""Implement ZlibPickable column type."""

from sqlalchemy.types import TypeDecorator, LargeBinary
from invenio_utils.serializers import ZlibPickle


class PickleBinary(TypeDecorator):

    """Implement ZlibPickable column type."""

    impl = LargeBinary

    def process_bind_param(self, value, dialect):
        """Dump data to column using ZlibPickle."""
        if value is not None:
            value = ZlibPickle.dumps(value)
        return value

    def process_result_value(self, value, dialect):
        """Load ZlibPickled data from column."""
        if value is not None:
            value = ZlibPickle.loads(value)
        return value
