from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .message_rule import MessageRule

@dataclass
class MessageRuleCollectionResponse(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The OdataNextLink property
    odata_next_link: Optional[str] = None
    # The value property
    value: Optional[List[MessageRule]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MessageRuleCollectionResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MessageRuleCollectionResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MessageRuleCollectionResponse()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .message_rule import MessageRule

        from .message_rule import MessageRule

        fields: Dict[str, Callable[[Any], None]] = {
            "@odata.nextLink": lambda n : setattr(self, 'odata_next_link', n.get_str_value()),
            "value": lambda n : setattr(self, 'value', n.get_collection_of_object_values(MessageRule)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("@odata.nextLink", self.odata_next_link)
        writer.write_collection_of_object_values("value", self.value)
        writer.write_additional_data_value(self.additional_data)
    
