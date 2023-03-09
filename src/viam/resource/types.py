import re
import sys
from abc import abstractclassmethod, abstractmethod
from typing import TYPE_CHECKING, Callable, ClassVar, Mapping, Optional, Protocol

if sys.version_info >= (3, 10):
    from typing import TypeAlias
else:
    from typing_extensions import TypeAlias

from typing_extensions import Self

from viam.proto.app.robot import ComponentConfig
from viam.proto.common import ResourceName

if TYPE_CHECKING:
    from viam.components.component_base import ComponentBase
    from viam.robot.client import RobotClient
    from viam.utils import ValueTypes

RESOURCE_NAMESPACE_RDK = "rdk"
RESOURCE_TYPE_COMPONENT = "component"
RESOURCE_TYPE_SERVICE = "service"


class Subtype:
    """Represents a known component/service (resource) API"""

    namespace: str
    """The namespace of the resource"""

    resource_type: str
    """The type of the resource, e.g. `component` or `service`"""

    resource_subtype: str
    """The subtype of the resource e.g. `servo`, `arm`, `vision`"""

    def __init__(self, namespace: str, resource_type: str, resource_subtype: str):
        self.namespace = namespace.lower()
        self.resource_type = resource_type.lower()
        self.resource_subtype = resource_subtype.lower()

    def __str__(self) -> str:
        return f"{self.namespace}:{self.resource_type}:{self.resource_subtype}"

    def __repr__(self) -> str:
        return f"<viam.resource.types.Subtype {str(self)} at {hex(id(self))}>"

    def __hash__(self) -> int:
        return hash(str(self))

    def __eq__(self, other: "Subtype") -> bool:
        return str(self) == str(other)

    @classmethod
    def from_resource_name(cls, resource_name: ResourceName) -> Self:
        """Convert a ```ResourceName``` into a ```Subtype```

        Args:
            resource_name (ResourceName): The ResourceName to convert

        Returns:
            Self: A new Subtype
        """
        return cls(resource_name.namespace, resource_name.type, resource_name.subtype)

    @classmethod
    def from_string(cls, string: str) -> Self:
        """Create a ```Subtype``` from its string representation (namespace:resource_type:resource_subtype)

        Args:
            string (str): The Subtype as a string

        Raises:
            ValueError: Raised if the string does not represent a valid Subtype

        Returns:
            Self: A new Subtype
        """
        regex = re.compile(r"^([\w-]+):([\w-]+):([\w-]+)$")
        match = regex.match(string)
        if not match:
            raise ValueError(f"{string} is not a valid Subtype")
        return cls(match.group(1), match.group(2), match.group(3))


class ModelFamily:
    """Represents a family of related models"""

    namespace: str
    """The namespace of the model family"""

    family: str
    """The family name"""

    DEFAULT_FAMILY_NAME: ClassVar[str] = "builtin"

    DEFAULT: ClassVar["ModelFamily"]

    def __init__(self, namespace: str, family: str):
        self.namespace = namespace.lower()
        self.family = family.lower()

    def __str__(self) -> str:
        return f"{self.namespace}:{self.family}"

    def __repr__(self) -> str:
        return f"<viam.resource.types.ModelFamily {str(self)} at {hex(id(self))}>"

    def __hash__(self) -> int:
        return hash(str(self))

    def __eq__(self, other: "ModelFamily") -> bool:
        return str(self) == str(other)


ModelFamily.DEFAULT = ModelFamily(RESOURCE_NAMESPACE_RDK, ModelFamily.DEFAULT_FAMILY_NAME)


class Model:
    """Represents a specific model within a family of models"""

    model_family: ModelFamily
    """The family to which this model belongs"""

    name: str
    """The name of the model"""

    def __init__(self, model_family: ModelFamily, name: str):
        self.model_family = model_family
        self.name = name.lower()

    def __str__(self) -> str:
        return f"{self.model_family}:{self.name}"

    def __repr__(self) -> str:
        return f"<viam.resource.types.Model {str(self)} at {hex(id(self))}>"

    def __hash__(self) -> int:
        return hash(str(self))

    def __eq__(self, other: "Model") -> bool:
        return str(self) == str(other)

    @classmethod
    def from_string(cls, model: str, *, ignore_errors=False) -> Self:
        """Create a ```Model``` from its string representation (namespace:family:name).

        Args:
            model (str): The Model as a string
            ignore_errors (bool, optional): If namespace or family are not found in the string, default to empty string
                                            rather than raise an exception. Defaults to False.

        Raises:
            ValueError: Raised if the provided string is not a valid Model

        Returns:
            Self: The Model
        """
        regex = re.compile(r"^([\w-]+):([\w-]+):([\w-]+)$")
        match = regex.match(model)
        if match:
            namespace = match.group(1)
            family = match.group(2)
            name = match.group(3)
            model_family = ModelFamily(namespace, family)
        elif ignore_errors:
            model_family = ModelFamily("", "")
            name = model
        else:
            raise ValueError(f"{model} is not a valid Model")

        return cls(model_family, name)


def resource_name_from_string(string: str) -> ResourceName:
    """Create a ResourceName from its string representation (namespace:resource_type:resource_subtype:name)

    Args:
        string (str): The ResourceName as a string

    Raises:
        ValueError: Raised if the provided string is not a valid ResourceName

    Returns:
        ResourceName: The new ResourceName
    """
    parts = string.split(":")
    if len(parts) < 4:
        raise ValueError(f"{string} is not a valid ResourceName")
    return ResourceName(namespace=parts[0], type=parts[1], subtype=parts[2], name=":".join(parts[3:]))


class ResourceBase(Protocol):
    """
    The base requirements for a Resource.
    """

    SUBTYPE: ClassVar["Subtype"]
    """The Subtype of the Resource"""

    name: str
    """The name of the Resource"""

    @classmethod
    def get_resource_name(cls, name: str) -> ResourceName:
        """
        Get the ResourceName for this Resource with the given name

        Args:
            name (str): The name of the Resource
        """
        return ResourceName(
            namespace=cls.SUBTYPE.namespace,
            type=cls.SUBTYPE.resource_type,
            subtype=cls.SUBTYPE.resource_subtype,
            name=name,
        )

    @abstractclassmethod
    def from_robot(cls, robot: "RobotClient", name: str) -> Self:
        """Get the Resource named ``name`` from the provided robot.

        Args:
            robot (RobotClient): The robot
            name (str): The name of the Resource

        Returns:
            Self: The Resource, if it exists on the robot
        """
        ...

    @abstractmethod
    async def do_command(
        self, command: Mapping[str, "ValueTypes"], *, timeout: Optional[float] = None, **kwargs
    ) -> Mapping[str, "ValueTypes"]:
        """Send/Receive arbitrary commands to the Resource

        Args:
            command (Mapping[str, ValueTypes]): The command to execute

        Raises:
            NotImplementedError: Raised if the Resource does not support arbitrary commands

        Returns:
            Mapping[str, ValueTypes]: Result of the executed command
        """
        ...


ComponentCreator: TypeAlias = Callable[[Mapping[ResourceName, "ComponentBase"], ComponentConfig], "ComponentBase"]