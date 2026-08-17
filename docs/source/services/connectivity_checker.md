# Connectivity Checker Service

## Endpoints

### `POST` `/connectivity_checker/v202410beta1/create`

Create a Connectivity Checker Report.

Create a connectivity checker report based on configuration provided in the request.

**Parameters**

| Name | In | Type | Required |
|------|----|------|----------|
| `data` | body | `CreateConnectivityReportRequest` | Yes |

**Responses**

| Status | Description | Model |
|--------|--------------|-------|
| 200 | A successful response. | `CreateConnectivityReportResponse` |
| default | An unexpected error response. | `rpcStatus` |

**Example**

```python
from kentik_api.client import KentikAPI

client = KentikAPI()  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.connectivity_checker.create_connectivity_report(
    data=CreateConnectivityReportRequest(...),
)
```

## Data Models

```{eval-rst}
.. autoclass:: kentik_api.gen.connectivity_checker.models.CloudProvider
   :members:
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.connectivity_checker.models.CreateConnectivityReportRequest
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.connectivity_checker.models.CreateConnectivityReportResponse
```

```{eval-rst}
.. autoclass:: kentik_api.gen.connectivity_checker.models.EntityType
   :members:
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.connectivity_checker.models.protobufAny
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.connectivity_checker.models.rpcStatus
```
