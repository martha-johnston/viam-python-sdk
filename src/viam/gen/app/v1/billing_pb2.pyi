"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.timestamp_pb2
import sys
import typing
if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions
DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _PaymentMethodType:
    ValueType = typing.NewType('ValueType', builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _PaymentMethodTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_PaymentMethodType.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    PAYMENT_METHOD_TYPE_UNSPECIFIED: _PaymentMethodType.ValueType
    PAYMENT_METHOD_TYPE_CARD: _PaymentMethodType.ValueType

class PaymentMethodType(_PaymentMethodType, metaclass=_PaymentMethodTypeEnumTypeWrapper):
    ...
PAYMENT_METHOD_TYPE_UNSPECIFIED: PaymentMethodType.ValueType
PAYMENT_METHOD_TYPE_CARD: PaymentMethodType.ValueType
global___PaymentMethodType = PaymentMethodType

class _UsageCostType:
    ValueType = typing.NewType('ValueType', builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _UsageCostTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_UsageCostType.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    USAGE_COST_TYPE_UNSPECIFIED: _UsageCostType.ValueType
    USAGE_COST_TYPE_DATA_UPLOAD: _UsageCostType.ValueType
    USAGE_COST_TYPE_DATA_EGRESS: _UsageCostType.ValueType
    USAGE_COST_TYPE_REMOTE_CONTROL: _UsageCostType.ValueType
    USAGE_COST_TYPE_STANDARD_COMPUTE: _UsageCostType.ValueType
    USAGE_COST_TYPE_CLOUD_STORAGE: _UsageCostType.ValueType
    USAGE_COST_TYPE_BINARY_DATA_CLOUD_STORAGE: _UsageCostType.ValueType
    USAGE_COST_TYPE_OTHER_CLOUD_STORAGE: _UsageCostType.ValueType
    USAGE_COST_TYPE_PER_MACHINE: _UsageCostType.ValueType
    USAGE_COST_TYPE_TRIGGER_NOTIFICATION: _UsageCostType.ValueType
    USAGE_COST_TYPE_TABULAR_DATA_CLOUD_STORAGE: _UsageCostType.ValueType
    USAGE_COST_TYPE_CONFIG_HISTORY_CLOUD_STORAGE: _UsageCostType.ValueType
    USAGE_COST_TYPE_LOGS_CLOUD_STORAGE: _UsageCostType.ValueType
    USAGE_COST_TYPE_TRAINING_LOGS_CLOUD_STORAGE: _UsageCostType.ValueType
    USAGE_COST_TYPE_PACKAGES_CLOUD_STORAGE: _UsageCostType.ValueType
    USAGE_COST_TYPE_BINARY_DATA_UPLOAD: _UsageCostType.ValueType
    USAGE_COST_TYPE_TABULAR_DATA_UPLOAD: _UsageCostType.ValueType
    USAGE_COST_TYPE_LOGS_UPLOAD: _UsageCostType.ValueType
    USAGE_COST_TYPE_BINARY_DATA_EGRESS: _UsageCostType.ValueType
    USAGE_COST_TYPE_TABULAR_DATA_EGRESS: _UsageCostType.ValueType
    USAGE_COST_TYPE_LOGS_EGRESS: _UsageCostType.ValueType
    USAGE_COST_TYPE_TRAINING_LOGS_EGRESS: _UsageCostType.ValueType

class UsageCostType(_UsageCostType, metaclass=_UsageCostTypeEnumTypeWrapper):
    ...
USAGE_COST_TYPE_UNSPECIFIED: UsageCostType.ValueType
USAGE_COST_TYPE_DATA_UPLOAD: UsageCostType.ValueType
USAGE_COST_TYPE_DATA_EGRESS: UsageCostType.ValueType
USAGE_COST_TYPE_REMOTE_CONTROL: UsageCostType.ValueType
USAGE_COST_TYPE_STANDARD_COMPUTE: UsageCostType.ValueType
USAGE_COST_TYPE_CLOUD_STORAGE: UsageCostType.ValueType
USAGE_COST_TYPE_BINARY_DATA_CLOUD_STORAGE: UsageCostType.ValueType
USAGE_COST_TYPE_OTHER_CLOUD_STORAGE: UsageCostType.ValueType
USAGE_COST_TYPE_PER_MACHINE: UsageCostType.ValueType
USAGE_COST_TYPE_TRIGGER_NOTIFICATION: UsageCostType.ValueType
USAGE_COST_TYPE_TABULAR_DATA_CLOUD_STORAGE: UsageCostType.ValueType
USAGE_COST_TYPE_CONFIG_HISTORY_CLOUD_STORAGE: UsageCostType.ValueType
USAGE_COST_TYPE_LOGS_CLOUD_STORAGE: UsageCostType.ValueType
USAGE_COST_TYPE_TRAINING_LOGS_CLOUD_STORAGE: UsageCostType.ValueType
USAGE_COST_TYPE_PACKAGES_CLOUD_STORAGE: UsageCostType.ValueType
USAGE_COST_TYPE_BINARY_DATA_UPLOAD: UsageCostType.ValueType
USAGE_COST_TYPE_TABULAR_DATA_UPLOAD: UsageCostType.ValueType
USAGE_COST_TYPE_LOGS_UPLOAD: UsageCostType.ValueType
USAGE_COST_TYPE_BINARY_DATA_EGRESS: UsageCostType.ValueType
USAGE_COST_TYPE_TABULAR_DATA_EGRESS: UsageCostType.ValueType
USAGE_COST_TYPE_LOGS_EGRESS: UsageCostType.ValueType
USAGE_COST_TYPE_TRAINING_LOGS_EGRESS: UsageCostType.ValueType
global___UsageCostType = UsageCostType

class _SourceType:
    ValueType = typing.NewType('ValueType', builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _SourceTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_SourceType.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    SOURCE_TYPE_UNSPECIFIED: _SourceType.ValueType
    SOURCE_TYPE_ORG: _SourceType.ValueType
    SOURCE_TYPE_FRAGMENT: _SourceType.ValueType

class SourceType(_SourceType, metaclass=_SourceTypeEnumTypeWrapper):
    ...
SOURCE_TYPE_UNSPECIFIED: SourceType.ValueType
SOURCE_TYPE_ORG: SourceType.ValueType
SOURCE_TYPE_FRAGMENT: SourceType.ValueType
global___SourceType = SourceType

@typing.final
class InvoiceSummary(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ID_FIELD_NUMBER: builtins.int
    INVOICE_DATE_FIELD_NUMBER: builtins.int
    INVOICE_AMOUNT_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    DUE_DATE_FIELD_NUMBER: builtins.int
    PAID_DATE_FIELD_NUMBER: builtins.int
    id: builtins.str
    invoice_amount: builtins.float
    status: builtins.str

    @property
    def invoice_date(self) -> google.protobuf.timestamp_pb2.Timestamp:
        ...

    @property
    def due_date(self) -> google.protobuf.timestamp_pb2.Timestamp:
        ...

    @property
    def paid_date(self) -> google.protobuf.timestamp_pb2.Timestamp:
        ...

    def __init__(self, *, id: builtins.str=..., invoice_date: google.protobuf.timestamp_pb2.Timestamp | None=..., invoice_amount: builtins.float=..., status: builtins.str=..., due_date: google.protobuf.timestamp_pb2.Timestamp | None=..., paid_date: google.protobuf.timestamp_pb2.Timestamp | None=...) -> None:
        ...

    def HasField(self, field_name: typing.Literal['due_date', b'due_date', 'invoice_date', b'invoice_date', 'paid_date', b'paid_date']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing.Literal['due_date', b'due_date', 'id', b'id', 'invoice_amount', b'invoice_amount', 'invoice_date', b'invoice_date', 'paid_date', b'paid_date', 'status', b'status']) -> None:
        ...
global___InvoiceSummary = InvoiceSummary

@typing.final
class PaymentMethodCard(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    BRAND_FIELD_NUMBER: builtins.int
    LAST_FOUR_DIGITS_FIELD_NUMBER: builtins.int
    brand: builtins.str
    last_four_digits: builtins.str

    def __init__(self, *, brand: builtins.str=..., last_four_digits: builtins.str=...) -> None:
        ...

    def ClearField(self, field_name: typing.Literal['brand', b'brand', 'last_four_digits', b'last_four_digits']) -> None:
        ...
global___PaymentMethodCard = PaymentMethodCard

@typing.final
class GetCurrentMonthUsageRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ORG_ID_FIELD_NUMBER: builtins.int
    org_id: builtins.str

    def __init__(self, *, org_id: builtins.str=...) -> None:
        ...

    def ClearField(self, field_name: typing.Literal['org_id', b'org_id']) -> None:
        ...
global___GetCurrentMonthUsageRequest = GetCurrentMonthUsageRequest

@typing.final
class UsageCost(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    RESOURCE_TYPE_FIELD_NUMBER: builtins.int
    COST_FIELD_NUMBER: builtins.int
    resource_type: global___UsageCostType.ValueType
    cost: builtins.float

    def __init__(self, *, resource_type: global___UsageCostType.ValueType=..., cost: builtins.float=...) -> None:
        ...

    def ClearField(self, field_name: typing.Literal['cost', b'cost', 'resource_type', b'resource_type']) -> None:
        ...
global___UsageCost = UsageCost

@typing.final
class ResourceUsageCostsBySource(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    SOURCE_TYPE_FIELD_NUMBER: builtins.int
    RESOURCE_USAGE_COSTS_FIELD_NUMBER: builtins.int
    TIER_NAME_FIELD_NUMBER: builtins.int
    source_type: global___SourceType.ValueType
    tier_name: builtins.str

    @property
    def resource_usage_costs(self) -> global___ResourceUsageCosts:
        ...

    def __init__(self, *, source_type: global___SourceType.ValueType=..., resource_usage_costs: global___ResourceUsageCosts | None=..., tier_name: builtins.str=...) -> None:
        ...

    def HasField(self, field_name: typing.Literal['resource_usage_costs', b'resource_usage_costs']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing.Literal['resource_usage_costs', b'resource_usage_costs', 'source_type', b'source_type', 'tier_name', b'tier_name']) -> None:
        ...
global___ResourceUsageCostsBySource = ResourceUsageCostsBySource

@typing.final
class ResourceUsageCosts(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    USAGE_COSTS_FIELD_NUMBER: builtins.int
    DISCOUNT_FIELD_NUMBER: builtins.int
    TOTAL_WITH_DISCOUNT_FIELD_NUMBER: builtins.int
    TOTAL_WITHOUT_DISCOUNT_FIELD_NUMBER: builtins.int
    discount: builtins.float
    total_with_discount: builtins.float
    total_without_discount: builtins.float

    @property
    def usage_costs(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___UsageCost]:
        ...

    def __init__(self, *, usage_costs: collections.abc.Iterable[global___UsageCost] | None=..., discount: builtins.float=..., total_with_discount: builtins.float=..., total_without_discount: builtins.float=...) -> None:
        ...

    def ClearField(self, field_name: typing.Literal['discount', b'discount', 'total_with_discount', b'total_with_discount', 'total_without_discount', b'total_without_discount', 'usage_costs', b'usage_costs']) -> None:
        ...
global___ResourceUsageCosts = ResourceUsageCosts

@typing.final
class GetCurrentMonthUsageResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    START_DATE_FIELD_NUMBER: builtins.int
    END_DATE_FIELD_NUMBER: builtins.int
    RESOURCE_USAGE_COSTS_BY_SOURCE_FIELD_NUMBER: builtins.int
    SUBTOTAL_FIELD_NUMBER: builtins.int
    CLOUD_STORAGE_USAGE_COST_FIELD_NUMBER: builtins.int
    DATA_UPLOAD_USAGE_COST_FIELD_NUMBER: builtins.int
    DATA_EGRES_USAGE_COST_FIELD_NUMBER: builtins.int
    REMOTE_CONTROL_USAGE_COST_FIELD_NUMBER: builtins.int
    STANDARD_COMPUTE_USAGE_COST_FIELD_NUMBER: builtins.int
    DISCOUNT_AMOUNT_FIELD_NUMBER: builtins.int
    TOTAL_USAGE_WITH_DISCOUNT_FIELD_NUMBER: builtins.int
    TOTAL_USAGE_WITHOUT_DISCOUNT_FIELD_NUMBER: builtins.int
    PER_MACHINE_USAGE_COST_FIELD_NUMBER: builtins.int
    BINARY_DATA_CLOUD_STORAGE_USAGE_COST_FIELD_NUMBER: builtins.int
    OTHER_CLOUD_STORAGE_USAGE_COST_FIELD_NUMBER: builtins.int
    subtotal: builtins.float
    cloud_storage_usage_cost: builtins.float
    'all fields below are deprecated'
    data_upload_usage_cost: builtins.float
    data_egres_usage_cost: builtins.float
    remote_control_usage_cost: builtins.float
    standard_compute_usage_cost: builtins.float
    discount_amount: builtins.float
    total_usage_with_discount: builtins.float
    total_usage_without_discount: builtins.float
    per_machine_usage_cost: builtins.float
    binary_data_cloud_storage_usage_cost: builtins.float
    other_cloud_storage_usage_cost: builtins.float

    @property
    def start_date(self) -> google.protobuf.timestamp_pb2.Timestamp:
        ...

    @property
    def end_date(self) -> google.protobuf.timestamp_pb2.Timestamp:
        ...

    @property
    def resource_usage_costs_by_source(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ResourceUsageCostsBySource]:
        ...

    def __init__(self, *, start_date: google.protobuf.timestamp_pb2.Timestamp | None=..., end_date: google.protobuf.timestamp_pb2.Timestamp | None=..., resource_usage_costs_by_source: collections.abc.Iterable[global___ResourceUsageCostsBySource] | None=..., subtotal: builtins.float=..., cloud_storage_usage_cost: builtins.float=..., data_upload_usage_cost: builtins.float=..., data_egres_usage_cost: builtins.float=..., remote_control_usage_cost: builtins.float=..., standard_compute_usage_cost: builtins.float=..., discount_amount: builtins.float=..., total_usage_with_discount: builtins.float=..., total_usage_without_discount: builtins.float=..., per_machine_usage_cost: builtins.float=..., binary_data_cloud_storage_usage_cost: builtins.float=..., other_cloud_storage_usage_cost: builtins.float=...) -> None:
        ...

    def HasField(self, field_name: typing.Literal['end_date', b'end_date', 'start_date', b'start_date']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing.Literal['binary_data_cloud_storage_usage_cost', b'binary_data_cloud_storage_usage_cost', 'cloud_storage_usage_cost', b'cloud_storage_usage_cost', 'data_egres_usage_cost', b'data_egres_usage_cost', 'data_upload_usage_cost', b'data_upload_usage_cost', 'discount_amount', b'discount_amount', 'end_date', b'end_date', 'other_cloud_storage_usage_cost', b'other_cloud_storage_usage_cost', 'per_machine_usage_cost', b'per_machine_usage_cost', 'remote_control_usage_cost', b'remote_control_usage_cost', 'resource_usage_costs_by_source', b'resource_usage_costs_by_source', 'standard_compute_usage_cost', b'standard_compute_usage_cost', 'start_date', b'start_date', 'subtotal', b'subtotal', 'total_usage_with_discount', b'total_usage_with_discount', 'total_usage_without_discount', b'total_usage_without_discount']) -> None:
        ...
global___GetCurrentMonthUsageResponse = GetCurrentMonthUsageResponse

@typing.final
class GetOrgBillingInformationRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ORG_ID_FIELD_NUMBER: builtins.int
    org_id: builtins.str

    def __init__(self, *, org_id: builtins.str=...) -> None:
        ...

    def ClearField(self, field_name: typing.Literal['org_id', b'org_id']) -> None:
        ...
global___GetOrgBillingInformationRequest = GetOrgBillingInformationRequest

@typing.final
class GetOrgBillingInformationResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    TYPE_FIELD_NUMBER: builtins.int
    BILLING_EMAIL_FIELD_NUMBER: builtins.int
    METHOD_FIELD_NUMBER: builtins.int
    BILLING_TIER_FIELD_NUMBER: builtins.int
    type: global___PaymentMethodType.ValueType
    billing_email: builtins.str
    billing_tier: builtins.str
    'Only return billing_tier for billing dashboard admin users'

    @property
    def method(self) -> global___PaymentMethodCard:
        """defined if type is PAYMENT_METHOD_TYPE_CARD"""

    def __init__(self, *, type: global___PaymentMethodType.ValueType=..., billing_email: builtins.str=..., method: global___PaymentMethodCard | None=..., billing_tier: builtins.str | None=...) -> None:
        ...

    def HasField(self, field_name: typing.Literal['_billing_tier', b'_billing_tier', '_method', b'_method', 'billing_tier', b'billing_tier', 'method', b'method']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing.Literal['_billing_tier', b'_billing_tier', '_method', b'_method', 'billing_email', b'billing_email', 'billing_tier', b'billing_tier', 'method', b'method', 'type', b'type']) -> None:
        ...

    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal['_billing_tier', b'_billing_tier']) -> typing.Literal['billing_tier'] | None:
        ...

    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal['_method', b'_method']) -> typing.Literal['method'] | None:
        ...
global___GetOrgBillingInformationResponse = GetOrgBillingInformationResponse

@typing.final
class GetInvoicesSummaryRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ORG_ID_FIELD_NUMBER: builtins.int
    org_id: builtins.str

    def __init__(self, *, org_id: builtins.str=...) -> None:
        ...

    def ClearField(self, field_name: typing.Literal['org_id', b'org_id']) -> None:
        ...
global___GetInvoicesSummaryRequest = GetInvoicesSummaryRequest

@typing.final
class GetInvoicesSummaryResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    OUTSTANDING_BALANCE_FIELD_NUMBER: builtins.int
    INVOICES_FIELD_NUMBER: builtins.int
    outstanding_balance: builtins.float
    'all unpaid balances at the end of the last billing cycle'

    @property
    def invoices(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___InvoiceSummary]:
        """all previous invoices"""

    def __init__(self, *, outstanding_balance: builtins.float=..., invoices: collections.abc.Iterable[global___InvoiceSummary] | None=...) -> None:
        ...

    def ClearField(self, field_name: typing.Literal['invoices', b'invoices', 'outstanding_balance', b'outstanding_balance']) -> None:
        ...
global___GetInvoicesSummaryResponse = GetInvoicesSummaryResponse

@typing.final
class GetInvoicePdfRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ID_FIELD_NUMBER: builtins.int
    ORG_ID_FIELD_NUMBER: builtins.int
    id: builtins.str
    org_id: builtins.str

    def __init__(self, *, id: builtins.str=..., org_id: builtins.str=...) -> None:
        ...

    def ClearField(self, field_name: typing.Literal['id', b'id', 'org_id', b'org_id']) -> None:
        ...
global___GetInvoicePdfRequest = GetInvoicePdfRequest

@typing.final
class GetInvoicePdfResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CHUNK_FIELD_NUMBER: builtins.int
    chunk: builtins.bytes

    def __init__(self, *, chunk: builtins.bytes=...) -> None:
        ...

    def ClearField(self, field_name: typing.Literal['chunk', b'chunk']) -> None:
        ...
global___GetInvoicePdfResponse = GetInvoicePdfResponse

@typing.final
class SendPaymentRequiredEmailRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CUSTOMER_ORG_ID_FIELD_NUMBER: builtins.int
    BILLING_OWNER_ORG_ID_FIELD_NUMBER: builtins.int
    customer_org_id: builtins.str
    billing_owner_org_id: builtins.str

    def __init__(self, *, customer_org_id: builtins.str=..., billing_owner_org_id: builtins.str=...) -> None:
        ...

    def ClearField(self, field_name: typing.Literal['billing_owner_org_id', b'billing_owner_org_id', 'customer_org_id', b'customer_org_id']) -> None:
        ...
global___SendPaymentRequiredEmailRequest = SendPaymentRequiredEmailRequest

@typing.final
class SendPaymentRequiredEmailResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(self) -> None:
        ...
global___SendPaymentRequiredEmailResponse = SendPaymentRequiredEmailResponse