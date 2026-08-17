# Plan Service

## Endpoints

### `GET` `/plans/v202501alpha1`

List Plans

Returns all plans configured for the user's company.

**Responses**

| Status | Description | Model |
|--------|--------------|-------|
| 200 | A successful response. | `ListPlansResponse` |
| default | An unexpected error response. | `rpcStatus` |

**Example**

```python
from kentik_api.client import KentikAPI

client = KentikAPI()  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.plan.list_plans()
```

## Data Models

```{eval-rst}
.. autoclass:: kentik_api.gen.plan.models.DeviceSubtype
   :members:
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.plan.models.ListPlansResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.plan.models.Plan
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.plan.models.PlanDevice
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.plan.models.protobufAny
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.plan.models.rpcStatus
```
