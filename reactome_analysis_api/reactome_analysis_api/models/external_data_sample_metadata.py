# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from reactome_analysis_api.models.base_model_ import Model
from reactome_analysis_api import util


class ExternalDataSampleMetadata(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, name: str=None, values: List[str]=None):  # noqa: E501
        """ExternalDataSampleMetadata - a model defined in Swagger

        :param name: The name of this ExternalDataSampleMetadata.  # noqa: E501
        :type name: str
        :param values: The values of this ExternalDataSampleMetadata.  # noqa: E501
        :type values: List[str]
        """
        self.swagger_types = {
            'name': str,
            'values': List[str]
        }

        self.attribute_map = {
            'name': 'name',
            'values': 'values'
        }

        self._name = name
        self._values = values

    @classmethod
    def from_dict(cls, dikt) -> 'ExternalDataSampleMetadata':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ExternalData_sample_metadata of this ExternalDataSampleMetadata.  # noqa: E501
        :rtype: ExternalDataSampleMetadata
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self) -> str:
        """Gets the name of this ExternalDataSampleMetadata.

        Name of the property  # noqa: E501

        :return: The name of this ExternalDataSampleMetadata.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this ExternalDataSampleMetadata.

        Name of the property  # noqa: E501

        :param name: The name of this ExternalDataSampleMetadata.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def values(self) -> List[str]:
        """Gets the values of this ExternalDataSampleMetadata.

        Values for the specified properties. This array will follow the same sort order as the 'sample_ids' array.  # noqa: E501

        :return: The values of this ExternalDataSampleMetadata.
        :rtype: List[str]
        """
        return self._values

    @values.setter
    def values(self, values: List[str]):
        """Sets the values of this ExternalDataSampleMetadata.

        Values for the specified properties. This array will follow the same sort order as the 'sample_ids' array.  # noqa: E501

        :param values: The values of this ExternalDataSampleMetadata.
        :type values: List[str]
        """

        self._values = values