# coding=utf-8
# *** WARNING: this file was generated by Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['AlzArchitectureArgs', 'AlzArchitecture']

@pulumi.input_type
class AlzArchitectureArgs:
    def __init__(__self__, *,
                 architecture_name: pulumi.Input[str],
                 location: pulumi.Input[str],
                 root_management_group_id: pulumi.Input[str]):
        """
        The set of arguments for constructing a AlzArchitecture resource.
        :param pulumi.Input[str] architecture_name: The name of the ALZ architecture from the library.
        :param pulumi.Input[str] location: The default location of the architecture.
        :param pulumi.Input[str] root_management_group_id: The root management group ID.
        """
        pulumi.set(__self__, "architecture_name", architecture_name)
        pulumi.set(__self__, "location", location)
        pulumi.set(__self__, "root_management_group_id", root_management_group_id)

    @property
    @pulumi.getter(name="architectureName")
    def architecture_name(self) -> pulumi.Input[str]:
        """
        The name of the ALZ architecture from the library.
        """
        return pulumi.get(self, "architecture_name")

    @architecture_name.setter
    def architecture_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "architecture_name", value)

    @property
    @pulumi.getter
    def location(self) -> pulumi.Input[str]:
        """
        The default location of the architecture.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: pulumi.Input[str]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="rootManagementGroupId")
    def root_management_group_id(self) -> pulumi.Input[str]:
        """
        The root management group ID.
        """
        return pulumi.get(self, "root_management_group_id")

    @root_management_group_id.setter
    def root_management_group_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "root_management_group_id", value)


class AlzArchitecture(pulumi.ComponentResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 architecture_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 root_management_group_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a AlzArchitecture resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] architecture_name: The name of the ALZ architecture from the library.
        :param pulumi.Input[str] location: The default location of the architecture.
        :param pulumi.Input[str] root_management_group_id: The root management group ID.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AlzArchitectureArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a AlzArchitecture resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param AlzArchitectureArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AlzArchitectureArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 architecture_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 root_management_group_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is not None:
            raise ValueError('ComponentResource classes do not support opts.id')
        else:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AlzArchitectureArgs.__new__(AlzArchitectureArgs)

            if architecture_name is None and not opts.urn:
                raise TypeError("Missing required property 'architecture_name'")
            __props__.__dict__["architecture_name"] = architecture_name
            if location is None and not opts.urn:
                raise TypeError("Missing required property 'location'")
            __props__.__dict__["location"] = location
            if root_management_group_id is None and not opts.urn:
                raise TypeError("Missing required property 'root_management_group_id'")
            __props__.__dict__["root_management_group_id"] = root_management_group_id
            __props__.__dict__["website_url"] = None
        super(AlzArchitecture, __self__).__init__(
            'azure:index:AlzArchitecture',
            resource_name,
            __props__,
            opts,
            remote=True)

    @property
    @pulumi.getter(name="websiteUrl")
    def website_url(self) -> pulumi.Output[str]:
        """
        The website URL.
        """
        return pulumi.get(self, "website_url")

