# ./eml2_1_0.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:44d30457824d226add3a2ad8c773df896776dac4
# Generated 2015-08-28 15:11:58.475503 by PyXB version 1.2.3
# Namespace eml://ecoinformatics.org/eml-2.1.0

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
import pyxb.binding.datatypes
import _nsgroup as _ImportedBinding__nsgroup

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI(u'eml://ecoinformatics.org/eml-2.1.0', create_if_missing=True)
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


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/servilla/local/lib/eml-2.1.0/eml.xsd', 222, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _HasWildcardElement = True
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/servilla/local/lib/eml-2.1.0/eml.xsd', 103, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element access uses Python identifier access
    __access = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'access'), 'access', '__emlecoinformatics_orgeml_2_1_0_CTD_ANON__access', False, pyxb.utils.utility.Location('/home/servilla/local/lib/eml-2.1.0/eml.xsd', 105, 8), )

    
    access = property(__access.value, __access.set, None, u'')

    
    # Element dataset uses Python identifier dataset
    __dataset = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'dataset'), 'dataset', '__emlecoinformatics_orgeml_2_1_0_CTD_ANON__dataset', False, pyxb.utils.utility.Location('/home/servilla/local/lib/eml-2.1.0/eml.xsd', 115, 10), )

    
    dataset = property(__dataset.value, __dataset.set, None, u'')

    
    # Element citation uses Python identifier citation
    __citation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'citation'), 'citation', '__emlecoinformatics_orgeml_2_1_0_CTD_ANON__citation', False, pyxb.utils.utility.Location('/home/servilla/local/lib/eml-2.1.0/eml.xsd', 128, 10), )

    
    citation = property(__citation.value, __citation.set, None, u'')

    
    # Element software uses Python identifier software
    __software = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'software'), 'software', '__emlecoinformatics_orgeml_2_1_0_CTD_ANON__software', False, pyxb.utils.utility.Location('/home/servilla/local/lib/eml-2.1.0/eml.xsd', 140, 10), )

    
    software = property(__software.value, __software.set, None, u'')

    
    # Element protocol uses Python identifier protocol
    __protocol = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'protocol'), 'protocol', '__emlecoinformatics_orgeml_2_1_0_CTD_ANON__protocol', False, pyxb.utils.utility.Location('/home/servilla/local/lib/eml-2.1.0/eml.xsd', 153, 10), )

    
    protocol = property(__protocol.value, __protocol.set, None, u'')

    
    # Element additionalMetadata uses Python identifier additionalMetadata
    __additionalMetadata = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'additionalMetadata'), 'additionalMetadata', '__emlecoinformatics_orgeml_2_1_0_CTD_ANON__additionalMetadata', True, pyxb.utils.utility.Location('/home/servilla/local/lib/eml-2.1.0/eml.xsd', 166, 8), )

    
    additionalMetadata = property(__additionalMetadata.value, __additionalMetadata.set, None, u'')

    
    # Attribute packageId uses Python identifier packageId
    __packageId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'packageId'), 'packageId', '__emlecoinformatics_orgeml_2_1_0_CTD_ANON__packageId', pyxb.binding.datatypes.string, required=True)
    __packageId._DeclarationLocation = pyxb.utils.utility.Location('/home/servilla/local/lib/eml-2.1.0/eml.xsd', 253, 6)
    __packageId._UseLocation = pyxb.utils.utility.Location('/home/servilla/local/lib/eml-2.1.0/eml.xsd', 253, 6)
    
    packageId = property(__packageId.value, __packageId.set, None, u'')

    
    # Attribute system uses Python identifier system
    __system = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'system'), 'system', '__emlecoinformatics_orgeml_2_1_0_CTD_ANON__system', _ImportedBinding__nsgroup.SystemType, required=True)
    __system._DeclarationLocation = pyxb.utils.utility.Location('/home/servilla/local/lib/eml-2.1.0/eml.xsd', 267, 6)
    __system._UseLocation = pyxb.utils.utility.Location('/home/servilla/local/lib/eml-2.1.0/eml.xsd', 267, 6)
    
    system = property(__system.value, __system.set, None, None)

    
    # Attribute scope uses Python identifier scope
    __scope = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'scope'), 'scope', '__emlecoinformatics_orgeml_2_1_0_CTD_ANON__scope', _ImportedBinding__nsgroup.ScopeType, fixed=True, unicode_default=u'system')
    __scope._DeclarationLocation = pyxb.utils.utility.Location('/home/servilla/local/lib/eml-2.1.0/eml.xsd', 268, 6)
    __scope._UseLocation = pyxb.utils.utility.Location('/home/servilla/local/lib/eml-2.1.0/eml.xsd', 268, 6)
    
    scope = property(__scope.value, __scope.set, None, u'')

    _ElementMap.update({
        __access.name() : __access,
        __dataset.name() : __dataset,
        __citation.name() : __citation,
        __software.name() : __software,
        __protocol.name() : __protocol,
        __additionalMetadata.name() : __additionalMetadata
    })
    _AttributeMap.update({
        __packageId.name() : __packageId,
        __system.name() : __system,
        __scope.name() : __scope
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/servilla/local/lib/eml-2.1.0/eml.xsd', 180, 10)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element describes uses Python identifier describes
    __describes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'describes'), 'describes', '__emlecoinformatics_orgeml_2_1_0_CTD_ANON_2_describes', True, pyxb.utils.utility.Location('/home/servilla/local/lib/eml-2.1.0/eml.xsd', 182, 14), )

    
    describes = property(__describes.value, __describes.set, None, u'')

    
    # Element metadata uses Python identifier metadata
    __metadata = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'metadata'), 'metadata', '__emlecoinformatics_orgeml_2_1_0_CTD_ANON_2_metadata', False, pyxb.utils.utility.Location('/home/servilla/local/lib/eml-2.1.0/eml.xsd', 199, 14), )

    
    metadata = property(__metadata.value, __metadata.set, None, u'')

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'id'), 'id', '__emlecoinformatics_orgeml_2_1_0_CTD_ANON_2_id', _ImportedBinding__nsgroup.IDType)
    __id._DeclarationLocation = pyxb.utils.utility.Location('/home/servilla/local/lib/eml-2.1.0/eml.xsd', 249, 12)
    __id._UseLocation = pyxb.utils.utility.Location('/home/servilla/local/lib/eml-2.1.0/eml.xsd', 249, 12)
    
    id = property(__id.value, __id.set, None, None)

    _ElementMap.update({
        __describes.name() : __describes,
        __metadata.name() : __metadata
    })
    _AttributeMap.update({
        __id.name() : __id
    })



eml = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'eml'), CTD_ANON_, documentation=u'', location=pyxb.utils.utility.Location('/home/servilla/local/lib/eml-2.1.0/eml.xsd', 83, 2))
Namespace.addCategoryObject('elementBinding', eml.name().localName(), eml)



def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=pyxb.binding.content.Wildcard.NC_any), pyxb.utils.utility.Location('/home/servilla/local/lib/eml-2.1.0/eml.xsd', 224, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton()




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'access'), _ImportedBinding__nsgroup.AccessType, scope=CTD_ANON_, documentation=u'', location=pyxb.utils.utility.Location('/home/servilla/local/lib/eml-2.1.0/eml.xsd', 105, 8)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'dataset'), _ImportedBinding__nsgroup.DatasetType, scope=CTD_ANON_, documentation=u'', location=pyxb.utils.utility.Location('/home/servilla/local/lib/eml-2.1.0/eml.xsd', 115, 10)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'citation'), _ImportedBinding__nsgroup.CitationType, scope=CTD_ANON_, documentation=u'', location=pyxb.utils.utility.Location('/home/servilla/local/lib/eml-2.1.0/eml.xsd', 128, 10)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'software'), _ImportedBinding__nsgroup.SoftwareType, scope=CTD_ANON_, documentation=u'', location=pyxb.utils.utility.Location('/home/servilla/local/lib/eml-2.1.0/eml.xsd', 140, 10)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'protocol'), _ImportedBinding__nsgroup.ProtocolType, scope=CTD_ANON_, documentation=u'', location=pyxb.utils.utility.Location('/home/servilla/local/lib/eml-2.1.0/eml.xsd', 153, 10)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'additionalMetadata'), CTD_ANON_2, scope=CTD_ANON_, documentation=u'', location=pyxb.utils.utility.Location('/home/servilla/local/lib/eml-2.1.0/eml.xsd', 166, 8)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/home/servilla/local/lib/eml-2.1.0/eml.xsd', 105, 8))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/home/servilla/local/lib/eml-2.1.0/eml.xsd', 166, 8))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, u'access')), pyxb.utils.utility.Location('/home/servilla/local/lib/eml-2.1.0/eml.xsd', 105, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, u'dataset')), pyxb.utils.utility.Location('/home/servilla/local/lib/eml-2.1.0/eml.xsd', 115, 10))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, u'citation')), pyxb.utils.utility.Location('/home/servilla/local/lib/eml-2.1.0/eml.xsd', 128, 10))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, u'software')), pyxb.utils.utility.Location('/home/servilla/local/lib/eml-2.1.0/eml.xsd', 140, 10))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, u'protocol')), pyxb.utils.utility.Location('/home/servilla/local/lib/eml-2.1.0/eml.xsd', 153, 10))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, u'additionalMetadata')), pyxb.utils.utility.Location('/home/servilla/local/lib/eml-2.1.0/eml.xsd', 166, 8))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_._Automaton = _BuildAutomaton_()




CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'describes'), _ImportedBinding__nsgroup.NonEmptyStringType, scope=CTD_ANON_2, documentation=u'', location=pyxb.utils.utility.Location('/home/servilla/local/lib/eml-2.1.0/eml.xsd', 182, 14)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'metadata'), CTD_ANON, scope=CTD_ANON_2, documentation=u'', location=pyxb.utils.utility.Location('/home/servilla/local/lib/eml-2.1.0/eml.xsd', 199, 14)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/home/servilla/local/lib/eml-2.1.0/eml.xsd', 182, 14))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(None, u'describes')), pyxb.utils.utility.Location('/home/servilla/local/lib/eml-2.1.0/eml.xsd', 182, 14))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(None, u'metadata')), pyxb.utils.utility.Location('/home/servilla/local/lib/eml-2.1.0/eml.xsd', 199, 14))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_2._Automaton = _BuildAutomaton_2()

