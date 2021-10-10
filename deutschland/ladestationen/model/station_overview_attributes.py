"""
    Bundesnetzagentur: Ladesäulenregister

    API des Ladesäulenregisters der Bundesnetzagentur  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from deutschland.ladestationen.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)
from ..model_utils import OpenApiModel
from deutschland.ladestationen.exceptions import ApiAttributeError


class StationOverviewAttributes(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {}

    validations = {}

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        return (
            bool,
            date,
            datetime,
            dict,
            float,
            int,
            list,
            str,
            none_type,
        )  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        return {
            "id": (int,),  # noqa: E501
            "betreiber_": (str,),  # noqa: E501
            "standort_": (str,),  # noqa: E501
            "lngengrad_": (float,),  # noqa: E501
            "breitengrad_": (float,),  # noqa: E501
            "fr_die_berschrift_": (str,),  # noqa: E501
            "anzahl_ladepunkte_": (str,),  # noqa: E501
            "art_des_ladepunktes_": (str,),  # noqa: E501
            "ac_steckdose_typ_2__1_": (str,),  # noqa: E501
            "ac_kupplung_typ_2__1_": (str,),  # noqa: E501
            "dc_kupplung_combo__1_": (str,),  # noqa: E501
            "ac_schuko__1_": (str,),  # noqa: E501
            "ac_cee_5_polig__1_": (str,),  # noqa: E501
            "ac_cee_3_polig__1_": (str,),  # noqa: E501
            "dc_ch_ade_mo__1_": (str,),  # noqa: E501
            "sonstige_stecker__1_": (str,),  # noqa: E501
            "nennleistung_ladepunkt_1_": (str,),  # noqa: E501
            "public_key__1_": (str,),  # noqa: E501
            "art_des_ladepunktes_2_": (str,),  # noqa: E501
            "ac_steckdose_typ_2__2_": (str,),  # noqa: E501
            "ac_kupplung_typ_2__2_": (str,),  # noqa: E501
            "dc_kupplung_combo__2_": (str,),  # noqa: E501
            "ac_schuko__2_": (str,),  # noqa: E501
            "ac_cee_5_polig__2_": (str,),  # noqa: E501
            "ac_cee_3_polig__2_": (str,),  # noqa: E501
            "dc_ch_ade_mo__2_": (str,),  # noqa: E501
            "sonstige_stecker__2_": (str,),  # noqa: E501
            "nennleistung_ladepunkt_2_": (str,),  # noqa: E501
            "public_key__2_": (str,),  # noqa: E501
            "art_des_ladepunktes_3_": (str,),  # noqa: E501
            "ac_steckdose_typ_2__3_": (str,),  # noqa: E501
            "ac_kupplung_typ_2__3_": (str,),  # noqa: E501
            "dc_kupplung_combo__3_": (str,),  # noqa: E501
            "ac_schuko__3_": (str,),  # noqa: E501
            "ac_cee_5_polig__3_": (str,),  # noqa: E501
            "ac_cee_3_polig__3_": (str,),  # noqa: E501
            "dc_ch_ade_mo__3_": (str,),  # noqa: E501
            "sonstige_stecker__3_": (str,),  # noqa: E501
            "nennleistung_ladepunkt_3_": (str,),  # noqa: E501
            "public_key__3_": (str,),  # noqa: E501
            "art_des_ladepunktes_4_": (str,),  # noqa: E501
            "ac_steckdose_typ_2__4_": (str,),  # noqa: E501
            "ac_kupplung_typ_2__4_": (str,),  # noqa: E501
            "dc_kupplung_combo__4_": (str,),  # noqa: E501
            "ac_schuko__4_": (str,),  # noqa: E501
            "ac_cee_5_polig__4_": (str,),  # noqa: E501
            "ac_cee_3_polig__4_": (str,),  # noqa: E501
            "dc_ch_ade_mo__4_": (str,),  # noqa: E501
            "sonstige_stecker__4_": (str,),  # noqa: E501
            "nennleistung_ladepunkt_4_": (str,),  # noqa: E501
            "public_key__4_": (str,),  # noqa: E501
            "objectid": (int,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None

    attribute_map = {
        "id": "ID",  # noqa: E501
        "betreiber_": "Betreiber_",  # noqa: E501
        "standort_": "Standort_",  # noqa: E501
        "lngengrad_": "Längengrad_",  # noqa: E501
        "breitengrad_": "Breitengrad_",  # noqa: E501
        "fr_die_berschrift_": "für_die_Überschrift_",  # noqa: E501
        "anzahl_ladepunkte_": "Anzahl_Ladepunkte_",  # noqa: E501
        "art_des_ladepunktes_": "Art_des_Ladepunktes_",  # noqa: E501
        "ac_steckdose_typ_2__1_": "AC_Steckdose_Typ_2__1_",  # noqa: E501
        "ac_kupplung_typ_2__1_": "AC_Kupplung_Typ_2__1_",  # noqa: E501
        "dc_kupplung_combo__1_": "DC_Kupplung_Combo__1_",  # noqa: E501
        "ac_schuko__1_": "AC_Schuko__1_",  # noqa: E501
        "ac_cee_5_polig__1_": "AC_CEE_5_polig__1_",  # noqa: E501
        "ac_cee_3_polig__1_": "AC_CEE_3_polig__1_",  # noqa: E501
        "dc_ch_ade_mo__1_": "DC_CHAdeMO__1_",  # noqa: E501
        "sonstige_stecker__1_": "Sonstige_Stecker__1_",  # noqa: E501
        "nennleistung_ladepunkt_1_": "Nennleistung_Ladepunkt_1_",  # noqa: E501
        "public_key__1_": "Public_Key__1_",  # noqa: E501
        "art_des_ladepunktes_2_": "Art_des_Ladepunktes_2_",  # noqa: E501
        "ac_steckdose_typ_2__2_": "AC_Steckdose_Typ_2__2_",  # noqa: E501
        "ac_kupplung_typ_2__2_": "AC_Kupplung_Typ_2__2_",  # noqa: E501
        "dc_kupplung_combo__2_": "DC_Kupplung_Combo__2_",  # noqa: E501
        "ac_schuko__2_": "AC_Schuko__2_",  # noqa: E501
        "ac_cee_5_polig__2_": "AC_CEE_5_polig__2_",  # noqa: E501
        "ac_cee_3_polig__2_": "AC_CEE_3_polig__2_",  # noqa: E501
        "dc_ch_ade_mo__2_": "DC_CHAdeMO__2_",  # noqa: E501
        "sonstige_stecker__2_": "Sonstige_Stecker__2_",  # noqa: E501
        "nennleistung_ladepunkt_2_": "Nennleistung_Ladepunkt_2_",  # noqa: E501
        "public_key__2_": "Public_Key__2_",  # noqa: E501
        "art_des_ladepunktes_3_": "Art_des_Ladepunktes_3_",  # noqa: E501
        "ac_steckdose_typ_2__3_": "AC_Steckdose_Typ_2__3_",  # noqa: E501
        "ac_kupplung_typ_2__3_": "AC_Kupplung_Typ_2__3_",  # noqa: E501
        "dc_kupplung_combo__3_": "DC_Kupplung_Combo__3_",  # noqa: E501
        "ac_schuko__3_": "AC_Schuko__3_",  # noqa: E501
        "ac_cee_5_polig__3_": "AC_CEE_5_polig__3_",  # noqa: E501
        "ac_cee_3_polig__3_": "AC_CEE_3_polig__3_",  # noqa: E501
        "dc_ch_ade_mo__3_": "DC_CHAdeMO__3_",  # noqa: E501
        "sonstige_stecker__3_": "Sonstige_Stecker__3_",  # noqa: E501
        "nennleistung_ladepunkt_3_": "Nennleistung_Ladepunkt_3_",  # noqa: E501
        "public_key__3_": "Public_Key__3_",  # noqa: E501
        "art_des_ladepunktes_4_": "Art_des_Ladepunktes_4_",  # noqa: E501
        "ac_steckdose_typ_2__4_": "AC_Steckdose_Typ_2__4_",  # noqa: E501
        "ac_kupplung_typ_2__4_": "AC_Kupplung_Typ_2__4_",  # noqa: E501
        "dc_kupplung_combo__4_": "DC_Kupplung_Combo__4_",  # noqa: E501
        "ac_schuko__4_": "AC_Schuko__4_",  # noqa: E501
        "ac_cee_5_polig__4_": "AC_CEE_5_polig__4_",  # noqa: E501
        "ac_cee_3_polig__4_": "AC_CEE_3_polig__4_",  # noqa: E501
        "dc_ch_ade_mo__4_": "DC_CHAdeMO__4_",  # noqa: E501
        "sonstige_stecker__4_": "Sonstige_Stecker__4_",  # noqa: E501
        "nennleistung_ladepunkt_4_": "Nennleistung_Ladepunkt_4_",  # noqa: E501
        "public_key__4_": "Public_Key__4_",  # noqa: E501
        "objectid": "OBJECTID",  # noqa: E501
    }

    read_only_vars = {}

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """StationOverviewAttributes - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            id (int): [optional]  # noqa: E501
            betreiber_ (str): [optional]  # noqa: E501
            standort_ (str): [optional]  # noqa: E501
            lngengrad_ (float): [optional]  # noqa: E501
            breitengrad_ (float): [optional]  # noqa: E501
            fr_die_berschrift_ (str): [optional]  # noqa: E501
            anzahl_ladepunkte_ (str): [optional]  # noqa: E501
            art_des_ladepunktes_ (str): [optional]  # noqa: E501
            ac_steckdose_typ_2__1_ (str): [optional]  # noqa: E501
            ac_kupplung_typ_2__1_ (str): [optional]  # noqa: E501
            dc_kupplung_combo__1_ (str): [optional]  # noqa: E501
            ac_schuko__1_ (str): [optional]  # noqa: E501
            ac_cee_5_polig__1_ (str): [optional]  # noqa: E501
            ac_cee_3_polig__1_ (str): [optional]  # noqa: E501
            dc_ch_ade_mo__1_ (str): [optional]  # noqa: E501
            sonstige_stecker__1_ (str): [optional]  # noqa: E501
            nennleistung_ladepunkt_1_ (str): [optional]  # noqa: E501
            public_key__1_ (str): [optional]  # noqa: E501
            art_des_ladepunktes_2_ (str): [optional]  # noqa: E501
            ac_steckdose_typ_2__2_ (str): [optional]  # noqa: E501
            ac_kupplung_typ_2__2_ (str): [optional]  # noqa: E501
            dc_kupplung_combo__2_ (str): [optional]  # noqa: E501
            ac_schuko__2_ (str): [optional]  # noqa: E501
            ac_cee_5_polig__2_ (str): [optional]  # noqa: E501
            ac_cee_3_polig__2_ (str): [optional]  # noqa: E501
            dc_ch_ade_mo__2_ (str): [optional]  # noqa: E501
            sonstige_stecker__2_ (str): [optional]  # noqa: E501
            nennleistung_ladepunkt_2_ (str): [optional]  # noqa: E501
            public_key__2_ (str): [optional]  # noqa: E501
            art_des_ladepunktes_3_ (str): [optional]  # noqa: E501
            ac_steckdose_typ_2__3_ (str): [optional]  # noqa: E501
            ac_kupplung_typ_2__3_ (str): [optional]  # noqa: E501
            dc_kupplung_combo__3_ (str): [optional]  # noqa: E501
            ac_schuko__3_ (str): [optional]  # noqa: E501
            ac_cee_5_polig__3_ (str): [optional]  # noqa: E501
            ac_cee_3_polig__3_ (str): [optional]  # noqa: E501
            dc_ch_ade_mo__3_ (str): [optional]  # noqa: E501
            sonstige_stecker__3_ (str): [optional]  # noqa: E501
            nennleistung_ladepunkt_3_ (str): [optional]  # noqa: E501
            public_key__3_ (str): [optional]  # noqa: E501
            art_des_ladepunktes_4_ (str): [optional]  # noqa: E501
            ac_steckdose_typ_2__4_ (str): [optional]  # noqa: E501
            ac_kupplung_typ_2__4_ (str): [optional]  # noqa: E501
            dc_kupplung_combo__4_ (str): [optional]  # noqa: E501
            ac_schuko__4_ (str): [optional]  # noqa: E501
            ac_cee_5_polig__4_ (str): [optional]  # noqa: E501
            ac_cee_3_polig__4_ (str): [optional]  # noqa: E501
            dc_ch_ade_mo__4_ (str): [optional]  # noqa: E501
            sonstige_stecker__4_ (str): [optional]  # noqa: E501
            nennleistung_ladepunkt_4_ (str): [optional]  # noqa: E501
            public_key__4_ (str): [optional]  # noqa: E501
            objectid (int): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop("_check_type", True)
        _spec_property_naming = kwargs.pop("_spec_property_naming", False)
        _path_to_item = kwargs.pop("_path_to_item", ())
        _configuration = kwargs.pop("_configuration", None)
        _visited_composed_classes = kwargs.pop("_visited_composed_classes", ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments."
                % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if (
                var_name not in self.attribute_map
                and self._configuration is not None
                and self._configuration.discard_unknown_keys
                and self.additional_properties_type is None
            ):
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set(
        [
            "_data_store",
            "_check_type",
            "_spec_property_naming",
            "_path_to_item",
            "_configuration",
            "_visited_composed_classes",
        ]
    )

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """StationOverviewAttributes - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            id (int): [optional]  # noqa: E501
            betreiber_ (str): [optional]  # noqa: E501
            standort_ (str): [optional]  # noqa: E501
            lngengrad_ (float): [optional]  # noqa: E501
            breitengrad_ (float): [optional]  # noqa: E501
            fr_die_berschrift_ (str): [optional]  # noqa: E501
            anzahl_ladepunkte_ (str): [optional]  # noqa: E501
            art_des_ladepunktes_ (str): [optional]  # noqa: E501
            ac_steckdose_typ_2__1_ (str): [optional]  # noqa: E501
            ac_kupplung_typ_2__1_ (str): [optional]  # noqa: E501
            dc_kupplung_combo__1_ (str): [optional]  # noqa: E501
            ac_schuko__1_ (str): [optional]  # noqa: E501
            ac_cee_5_polig__1_ (str): [optional]  # noqa: E501
            ac_cee_3_polig__1_ (str): [optional]  # noqa: E501
            dc_ch_ade_mo__1_ (str): [optional]  # noqa: E501
            sonstige_stecker__1_ (str): [optional]  # noqa: E501
            nennleistung_ladepunkt_1_ (str): [optional]  # noqa: E501
            public_key__1_ (str): [optional]  # noqa: E501
            art_des_ladepunktes_2_ (str): [optional]  # noqa: E501
            ac_steckdose_typ_2__2_ (str): [optional]  # noqa: E501
            ac_kupplung_typ_2__2_ (str): [optional]  # noqa: E501
            dc_kupplung_combo__2_ (str): [optional]  # noqa: E501
            ac_schuko__2_ (str): [optional]  # noqa: E501
            ac_cee_5_polig__2_ (str): [optional]  # noqa: E501
            ac_cee_3_polig__2_ (str): [optional]  # noqa: E501
            dc_ch_ade_mo__2_ (str): [optional]  # noqa: E501
            sonstige_stecker__2_ (str): [optional]  # noqa: E501
            nennleistung_ladepunkt_2_ (str): [optional]  # noqa: E501
            public_key__2_ (str): [optional]  # noqa: E501
            art_des_ladepunktes_3_ (str): [optional]  # noqa: E501
            ac_steckdose_typ_2__3_ (str): [optional]  # noqa: E501
            ac_kupplung_typ_2__3_ (str): [optional]  # noqa: E501
            dc_kupplung_combo__3_ (str): [optional]  # noqa: E501
            ac_schuko__3_ (str): [optional]  # noqa: E501
            ac_cee_5_polig__3_ (str): [optional]  # noqa: E501
            ac_cee_3_polig__3_ (str): [optional]  # noqa: E501
            dc_ch_ade_mo__3_ (str): [optional]  # noqa: E501
            sonstige_stecker__3_ (str): [optional]  # noqa: E501
            nennleistung_ladepunkt_3_ (str): [optional]  # noqa: E501
            public_key__3_ (str): [optional]  # noqa: E501
            art_des_ladepunktes_4_ (str): [optional]  # noqa: E501
            ac_steckdose_typ_2__4_ (str): [optional]  # noqa: E501
            ac_kupplung_typ_2__4_ (str): [optional]  # noqa: E501
            dc_kupplung_combo__4_ (str): [optional]  # noqa: E501
            ac_schuko__4_ (str): [optional]  # noqa: E501
            ac_cee_5_polig__4_ (str): [optional]  # noqa: E501
            ac_cee_3_polig__4_ (str): [optional]  # noqa: E501
            dc_ch_ade_mo__4_ (str): [optional]  # noqa: E501
            sonstige_stecker__4_ (str): [optional]  # noqa: E501
            nennleistung_ladepunkt_4_ (str): [optional]  # noqa: E501
            public_key__4_ (str): [optional]  # noqa: E501
            objectid (int): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop("_check_type", True)
        _spec_property_naming = kwargs.pop("_spec_property_naming", False)
        _path_to_item = kwargs.pop("_path_to_item", ())
        _configuration = kwargs.pop("_configuration", None)
        _visited_composed_classes = kwargs.pop("_visited_composed_classes", ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments."
                % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if (
                var_name not in self.attribute_map
                and self._configuration is not None
                and self._configuration.discard_unknown_keys
                and self.additional_properties_type is None
            ):
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(
                    f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                    f"class with read only attributes."
                )