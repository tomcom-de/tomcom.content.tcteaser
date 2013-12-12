from archetypes.schemaextender.interfaces import ISchemaModifier
from archetypes.schemaextender.interfaces import IBrowserLayerAwareExtender
from plone.app.widgets.interfaces import IWidgetsLayer
from zope.interface import implements
from zope.component import adapts
from plone.app.widgets import at

from tcteaser import ITCTeaser

class Extender(object):
    """
    """

    implements(ISchemaModifier, IBrowserLayerAwareExtender)
    adapts(ITCTeaser)
    layer = IWidgetsLayer

    def __init__(self, context):
        self.context = context

    def fiddle(self, schema):
        for field in schema.fields():
            old = field.widget

            if field.__name__ == 'internal_link':
                field.widget = at.RelatedItemsWidget(
                    label=old.label,
                    description=old.description
                )
