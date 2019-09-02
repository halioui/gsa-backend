# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from reactome_analysis_api.models.base_model_ import Model
from reactome_analysis_api.models.external_data_default_parameters import ExternalDataDefaultParameters  # noqa: F401,E501
from reactome_analysis_api.models.external_data_sample_metadata import ExternalDataSampleMetadata  # noqa: F401,E501
from reactome_analysis_api import util


class ExternalData(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, id: str=None, title: str=None, type: str=None, description: str=None, group: str=None, sample_ids: List[str]=None, sample_metadata: List[ExternalDataSampleMetadata]=None, default_parameters: List[ExternalDataDefaultParameters]=None):  # noqa: E501
        """ExternalData - a model defined in Swagger

        :param id: The id of this ExternalData.  # noqa: E501
        :type id: str
        :param title: The title of this ExternalData.  # noqa: E501
        :type title: str
        :param type: The type of this ExternalData.  # noqa: E501
        :type type: str
        :param description: The description of this ExternalData.  # noqa: E501
        :type description: str
        :param group: The group of this ExternalData.  # noqa: E501
        :type group: str
        :param sample_ids: The sample_ids of this ExternalData.  # noqa: E501
        :type sample_ids: List[str]
        :param sample_metadata: The sample_metadata of this ExternalData.  # noqa: E501
        :type sample_metadata: List[ExternalDataSampleMetadata]
        :param default_parameters: The default_parameters of this ExternalData.  # noqa: E501
        :type default_parameters: List[ExternalDataDefaultParameters]
        """
        self.swagger_types = {
            'id': str,
            'title': str,
            'type': str,
            'description': str,
            'group': str,
            'sample_ids': List[str],
            'sample_metadata': List[ExternalDataSampleMetadata],
            'default_parameters': List[ExternalDataDefaultParameters]
        }

        self.attribute_map = {
            'id': 'id',
            'title': 'title',
            'type': 'type',
            'description': 'description',
            'group': 'group',
            'sample_ids': 'sample_ids',
            'sample_metadata': 'sample_metadata',
            'default_parameters': 'default_parameters'
        }

        self._id = id
        self._title = title
        self._type = type
        self._description = description
        self._group = group
        self._sample_ids = sample_ids
        self._sample_metadata = sample_metadata
        self._default_parameters = default_parameters

    @classmethod
    def from_dict(cls, dikt) -> 'ExternalData':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ExternalData of this ExternalData.  # noqa: E501
        :rtype: ExternalData
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this ExternalData.

        The dataset's id  # noqa: E501

        :return: The id of this ExternalData.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this ExternalData.

        The dataset's id  # noqa: E501

        :param id: The id of this ExternalData.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def title(self) -> str:
        """Gets the title of this ExternalData.

        The dataset's title  # noqa: E501

        :return: The title of this ExternalData.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title: str):
        """Sets the title of this ExternalData.

        The dataset's title  # noqa: E501

        :param title: The title of this ExternalData.
        :type title: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def type(self) -> str:
        """Gets the type of this ExternalData.

        The data type of the dataset. This value is the same as for submitted datasets.  # noqa: E501

        :return: The type of this ExternalData.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str):
        """Sets the type of this ExternalData.

        The data type of the dataset. This value is the same as for submitted datasets.  # noqa: E501

        :param type: The type of this ExternalData.
        :type type: str
        """
        allowed_values = ["rnaseq_counts", "rnaseq_norm", "proteomics_int", "proteomics_sc", "microarray_norm"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def description(self) -> str:
        """Gets the description of this ExternalData.

        A more verbose description of the dataset.  # noqa: E501

        :return: The description of this ExternalData.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str):
        """Sets the description of this ExternalData.

        A more verbose description of the dataset.  # noqa: E501

        :param description: The description of this ExternalData.
        :type description: str
        """

        self._description = description

    @property
    def group(self) -> str:
        """Gets the group of this ExternalData.

        Some datasets may be grouped together. In this case, they will share a common group id  # noqa: E501

        :return: The group of this ExternalData.
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group: str):
        """Sets the group of this ExternalData.

        Some datasets may be grouped together. In this case, they will share a common group id  # noqa: E501

        :param group: The group of this ExternalData.
        :type group: str
        """

        self._group = group

    @property
    def sample_ids(self) -> List[str]:
        """Gets the sample_ids of this ExternalData.

        For some datasets, the sample ids (corresponding to the column headers in the expression matrix) may be available.  # noqa: E501

        :return: The sample_ids of this ExternalData.
        :rtype: List[str]
        """
        return self._sample_ids

    @sample_ids.setter
    def sample_ids(self, sample_ids: List[str]):
        """Sets the sample_ids of this ExternalData.

        For some datasets, the sample ids (corresponding to the column headers in the expression matrix) may be available.  # noqa: E501

        :param sample_ids: The sample_ids of this ExternalData.
        :type sample_ids: List[str]
        """

        self._sample_ids = sample_ids

    @property
    def sample_metadata(self) -> List[ExternalDataSampleMetadata]:
        """Gets the sample_metadata of this ExternalData.


        :return: The sample_metadata of this ExternalData.
        :rtype: List[ExternalDataSampleMetadata]
        """
        return self._sample_metadata

    @sample_metadata.setter
    def sample_metadata(self, sample_metadata: List[ExternalDataSampleMetadata]):
        """Sets the sample_metadata of this ExternalData.


        :param sample_metadata: The sample_metadata of this ExternalData.
        :type sample_metadata: List[ExternalDataSampleMetadata]
        """

        self._sample_metadata = sample_metadata

    @property
    def default_parameters(self) -> List[ExternalDataDefaultParameters]:
        """Gets the default_parameters of this ExternalData.

        For some datasets, default values for certain parameters may be available.  # noqa: E501

        :return: The default_parameters of this ExternalData.
        :rtype: List[ExternalDataDefaultParameters]
        """
        return self._default_parameters

    @default_parameters.setter
    def default_parameters(self, default_parameters: List[ExternalDataDefaultParameters]):
        """Sets the default_parameters of this ExternalData.

        For some datasets, default values for certain parameters may be available.  # noqa: E501

        :param default_parameters: The default_parameters of this ExternalData.
        :type default_parameters: List[ExternalDataDefaultParameters]
        """

        self._default_parameters = default_parameters
