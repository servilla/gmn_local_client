# ./_sr.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:96fdadc4efd7d7d08016558f7fa99c2b701bfe4d
# Generated 2015-08-28 15:11:58.472094 by PyXB version 1.2.3
# Namespace eml://ecoinformatics.org/spatialRaster-2.1.0 [xmlns:sr]

import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:6a2e302a-4dc9-11e5-a116-000c2950e125')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.3'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# Import bindings for namespaces imported into schema
import _nsgroup as _ImportedBinding__nsgroup

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI(u'eml://ecoinformatics.org/spatialRaster-2.1.0', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, unicode):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)

from _nsgroup import spatialRaster # {eml://ecoinformatics.org/spatialRaster-2.1.0}spatialRaster
from _nsgroup import CTD_ANON_68 as CTD_ANON # None
from _nsgroup import CTD_ANON_69 as CTD_ANON_ # None
from _nsgroup import STD_ANON_22 as STD_ANON # None
from _nsgroup import CTD_ANON_70 as CTD_ANON_2 # None
from _nsgroup import STD_ANON_23 as STD_ANON_ # None
from _nsgroup import CTD_ANON_71 as CTD_ANON_3 # None
from _nsgroup import CTD_ANON_72 as CTD_ANON_4 # None
from _nsgroup import BandType # {eml://ecoinformatics.org/spatialRaster-2.1.0}BandType
from _nsgroup import CellValueType # {eml://ecoinformatics.org/spatialRaster-2.1.0}CellValueType
from _nsgroup import ImagingConditionCode # {eml://ecoinformatics.org/spatialRaster-2.1.0}ImagingConditionCode
from _nsgroup import rasterOriginType # {eml://ecoinformatics.org/spatialRaster-2.1.0}rasterOriginType
from _nsgroup import CellGeometryType # {eml://ecoinformatics.org/spatialRaster-2.1.0}CellGeometryType
from _nsgroup import DataQuality # {eml://ecoinformatics.org/spatialRaster-2.1.0}DataQuality
from _nsgroup import CTD_ANON_73 as CTD_ANON_5 # None
from _nsgroup import SpatialRasterType # {eml://ecoinformatics.org/spatialRaster-2.1.0}SpatialRasterType
