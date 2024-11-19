# coding: utf-8

"""
    Listing Data Storage

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from listing_data_storage_client.models.evenue_price_seat_store_schema import EvenuePriceSeatStoreSchema
from typing import Optional, Set
from typing_extensions import Self

class UpdateEvenueSeatStoreSchema(BaseModel):
    """
    UpdateEvenueSeatStoreSchema
    """ # noqa: E501
    add_place: List[EvenuePriceSeatStoreSchema] = Field(alias="addPlace")
    remove_place: List[StrictStr] = Field(alias="removePlace")
    update_place: List[EvenuePriceSeatStoreSchema] = Field(alias="updatePlace")
    empty_event: Optional[StrictBool] = Field(default=False, alias="emptyEvent")
    __properties: ClassVar[List[str]] = ["addPlace", "removePlace", "updatePlace", "emptyEvent"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of UpdateEvenueSeatStoreSchema from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in add_place (list)
        _items = []
        if self.add_place:
            for _item_add_place in self.add_place:
                if _item_add_place:
                    _items.append(_item_add_place.to_dict())
            _dict['addPlace'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in update_place (list)
        _items = []
        if self.update_place:
            for _item_update_place in self.update_place:
                if _item_update_place:
                    _items.append(_item_update_place.to_dict())
            _dict['updatePlace'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UpdateEvenueSeatStoreSchema from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "addPlace": [EvenuePriceSeatStoreSchema.from_dict(_item) for _item in obj["addPlace"]] if obj.get("addPlace") is not None else None,
            "removePlace": obj.get("removePlace"),
            "updatePlace": [EvenuePriceSeatStoreSchema.from_dict(_item) for _item in obj["updatePlace"]] if obj.get("updatePlace") is not None else None,
            "emptyEvent": obj.get("emptyEvent") if obj.get("emptyEvent") is not None else False
        })
        return _obj


