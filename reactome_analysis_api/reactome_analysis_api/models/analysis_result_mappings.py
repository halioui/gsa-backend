# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from reactome_analysis_api.models.base_model_ import Model
from reactome_analysis_api import util


class AnalysisResultMappings(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, identifier: str=None, mapped_to: List[str]=None):  # noqa: E501
        """AnalysisResultMappings - a model defined in Swagger

        :param identifier: The identifier of this AnalysisResultMappings.  # noqa: E501
        :type identifier: str
        :param mapped_to: The mapped_to of this AnalysisResultMappings.  # noqa: E501
        :type mapped_to: List[str]
        """
        self.swagger_types = {
            'identifier': str,
            'mapped_to': List[str]
        }

        self.attribute_map = {
            'identifier': 'identifier',
            'mapped_to': 'mapped_to'
        }

        self._identifier = identifier
        self._mapped_to = mapped_to

    @classmethod
    def from_dict(cls, dikt) -> 'AnalysisResultMappings':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AnalysisResult_mappings of this AnalysisResultMappings.  # noqa: E501
        :rtype: AnalysisResultMappings
        """
        return util.deserialize_model(dikt, cls)

    @property
    def identifier(self) -> str:
        """Gets the identifier of this AnalysisResultMappings.

        The originally submitted identifier  # noqa: E501

        :return: The identifier of this AnalysisResultMappings.
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier: str):
        """Sets the identifier of this AnalysisResultMappings.

        The originally submitted identifier  # noqa: E501

        :param identifier: The identifier of this AnalysisResultMappings.
        :type identifier: str
        """
        if identifier is None:
            raise ValueError("Invalid value for `identifier`, must not be `None`")  # noqa: E501

        self._identifier = identifier

    @property
    def mapped_to(self) -> List[str]:
        """Gets the mapped_to of this AnalysisResultMappings.

        All identifiers this identifier was mapped to.  # noqa: E501

        :return: The mapped_to of this AnalysisResultMappings.
        :rtype: List[str]
        """
        return self._mapped_to

    @mapped_to.setter
    def mapped_to(self, mapped_to: List[str]):
        """Sets the mapped_to of this AnalysisResultMappings.

        All identifiers this identifier was mapped to.  # noqa: E501

        :param mapped_to: The mapped_to of this AnalysisResultMappings.
        :type mapped_to: List[str]
        """
        if mapped_to is None:
            raise ValueError("Invalid value for `mapped_to`, must not be `None`")  # noqa: E501

        self._mapped_to = mapped_to
