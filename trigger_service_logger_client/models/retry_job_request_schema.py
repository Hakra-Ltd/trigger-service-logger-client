# coding: utf-8

"""
    FastAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from trigger_service_logger_client.models.failure_reason import FailureReason
from typing import Optional, Set
from typing_extensions import Self

class RetryJobRequestSchema(BaseModel):
    """
    RetryJobRequestSchema
    """ # noqa: E501
    finished: datetime
    success: StrictBool
    process_notes: Optional[Dict[str, Any]] = None
    error_reason: Optional[StrictStr] = None
    retry_reached: Optional[StrictBool] = None
    started: datetime
    failure_reason: FailureReason
    scrap_notes: Optional[Dict[str, Any]] = None
    __properties: ClassVar[List[str]] = ["finished", "success", "process_notes", "error_reason", "retry_reached", "started", "failure_reason", "scrap_notes"]

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
        """Create an instance of RetryJobRequestSchema from a JSON string"""
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
        # set to None if process_notes (nullable) is None
        # and model_fields_set contains the field
        if self.process_notes is None and "process_notes" in self.model_fields_set:
            _dict['process_notes'] = None

        # set to None if error_reason (nullable) is None
        # and model_fields_set contains the field
        if self.error_reason is None and "error_reason" in self.model_fields_set:
            _dict['error_reason'] = None

        # set to None if retry_reached (nullable) is None
        # and model_fields_set contains the field
        if self.retry_reached is None and "retry_reached" in self.model_fields_set:
            _dict['retry_reached'] = None

        # set to None if scrap_notes (nullable) is None
        # and model_fields_set contains the field
        if self.scrap_notes is None and "scrap_notes" in self.model_fields_set:
            _dict['scrap_notes'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RetryJobRequestSchema from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "finished": obj.get("finished"),
            "success": obj.get("success"),
            "process_notes": obj.get("process_notes"),
            "error_reason": obj.get("error_reason"),
            "retry_reached": obj.get("retry_reached"),
            "started": obj.get("started"),
            "failure_reason": obj.get("failure_reason"),
            "scrap_notes": obj.get("scrap_notes")
        })
        return _obj


