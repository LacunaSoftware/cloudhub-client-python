# coding: utf-8

"""
    Cloudhub API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class SignHashRequest(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'session': 'str',
        'hash': 'str',
        'digest_algorithm': 'str',
        'digest_algorithm_oid': 'str',
        'certificate_alias': 'str'
    }

    attribute_map = {
        'session': 'session',
        'hash': 'hash',
        'digest_algorithm': 'digestAlgorithm',
        'digest_algorithm_oid': 'digestAlgorithmOid',
        'certificate_alias': 'certificateAlias'
    }

    def __init__(self, session=None, hash=None, digest_algorithm=None, digest_algorithm_oid=None, certificate_alias=None):  # noqa: E501
        """SignHashRequest - a model defined in Swagger"""  # noqa: E501
        self._session = None
        self._hash = None
        self._digest_algorithm = None
        self._digest_algorithm_oid = None
        self._certificate_alias = None
        self.discriminator = None
        self.session = session
        self.hash = hash
        if digest_algorithm is not None:
            self.digest_algorithm = digest_algorithm
        if digest_algorithm_oid is not None:
            self.digest_algorithm_oid = digest_algorithm_oid
        if certificate_alias is not None:
            self.certificate_alias = certificate_alias

    @property
    def session(self):
        """Gets the session of this SignHashRequest.  # noqa: E501


        :return: The session of this SignHashRequest.  # noqa: E501
        :rtype: str
        """
        return self._session

    @session.setter
    def session(self, session):
        """Sets the session of this SignHashRequest.


        :param session: The session of this SignHashRequest.  # noqa: E501
        :type: str
        """
        if session is None:
            raise ValueError("Invalid value for `session`, must not be `None`")  # noqa: E501

        self._session = session

    @property
    def hash(self):
        """Gets the hash of this SignHashRequest.  # noqa: E501


        :return: The hash of this SignHashRequest.  # noqa: E501
        :rtype: str
        """
        return self._hash

    @hash.setter
    def hash(self, hash):
        """Sets the hash of this SignHashRequest.


        :param hash: The hash of this SignHashRequest.  # noqa: E501
        :type: str
        """
        if hash is None:
            raise ValueError("Invalid value for `hash`, must not be `None`")  # noqa: E501

        self._hash = hash

    @property
    def digest_algorithm(self):
        """Gets the digest_algorithm of this SignHashRequest.  # noqa: E501


        :return: The digest_algorithm of this SignHashRequest.  # noqa: E501
        :rtype: str
        """
        return self._digest_algorithm

    @digest_algorithm.setter
    def digest_algorithm(self, digest_algorithm):
        """Sets the digest_algorithm of this SignHashRequest.


        :param digest_algorithm: The digest_algorithm of this SignHashRequest.  # noqa: E501
        :type: str
        """

        self._digest_algorithm = digest_algorithm

    @property
    def digest_algorithm_oid(self):
        """Gets the digest_algorithm_oid of this SignHashRequest.  # noqa: E501


        :return: The digest_algorithm_oid of this SignHashRequest.  # noqa: E501
        :rtype: str
        """
        return self._digest_algorithm_oid

    @digest_algorithm_oid.setter
    def digest_algorithm_oid(self, digest_algorithm_oid):
        """Sets the digest_algorithm_oid of this SignHashRequest.


        :param digest_algorithm_oid: The digest_algorithm_oid of this SignHashRequest.  # noqa: E501
        :type: str
        """

        self._digest_algorithm_oid = digest_algorithm_oid

    @property
    def certificate_alias(self):
        """Gets the certificate_alias of this SignHashRequest.  # noqa: E501


        :return: The certificate_alias of this SignHashRequest.  # noqa: E501
        :rtype: str
        """
        return self._certificate_alias

    @certificate_alias.setter
    def certificate_alias(self, certificate_alias):
        """Sets the certificate_alias of this SignHashRequest.


        :param certificate_alias: The certificate_alias of this SignHashRequest.  # noqa: E501
        :type: str
        """

        self._certificate_alias = certificate_alias

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(SignHashRequest, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SignHashRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
