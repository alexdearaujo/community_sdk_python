# Contract: hand-written helpers

**Feature**: [../spec.md](../spec.md) | **Models**: [../data-model.md](../data-model.md)

Every helper that calls the API calls the generated wrapper, so every request
goes through `request_json()` (Principle II). No helper module imports
`httpx` or `request_json` (FR-007, checked by T027a).

## `kentik_api.v5_tools` (base install)

```python
def decode_chart(response: ChartResponse) -> ChartImage: ...
```

- Returns the image bytes and the image type from the data URI.
- Raises `HTTPException(502)` with a message that names the problem when the
  data URI is not valid.

```python
def split_batch(
    upserts: Sequence[BatchUpsert],
    deletes: Sequence[BatchDelete] = (),
    *,
    replace_all: bool = False,
    max_bytes: int = 4_000_000,
) -> list[BatchPart]: ...
```

- Every part serializes to at most `max_bytes`. Only the last part has
  `complete=True`. Every part has the same `replace_all`.
- Deletes follow every upsert. The API applies deletes only after the last
  part arrives, so their position does not change the result.
- Raises `ValueError` when one upsert or delete alone is larger than
  `max_bytes`.

```python
def send_batch(
    send: Callable[..., BatchResponse],
    parts: Sequence[BatchPart],
) -> str: ...
```

- Calls `send(data=part)` for each part, in order. It copies the `guid`
  from the first response into every later part, and returns the `guid`.
- Raises `BatchSendError(guid, sent, cause)` on the first failure. It never
  resends.
- Usage: `send_batch(client.v5.batch_tags, parts)` or
  `send_batch(partial(client.v5.batch_populators, dimensionName="c_x"), parts)`.

```python
def wait_for_batch(
    client: KentikAPI,
    guid: str,
    *,
    timeout: float = 600.0,
    interval: float = 5.0,
) -> BatchStatus: ...
```

- Polls `client.v5.batch_status(guid=guid)` until `is_complete` is true, and
  returns that status.
- Raises `BatchWaitTimeout(guid, last_status)` when `timeout` expires.
- Raises the error of a failed status call at once. It never resends the
  batch.

## `kentik_api.devices` (base install)

```python
class DeviceLookup:
    @classmethod
    def from_api(cls, client: KentikAPI) -> "DeviceLookup": ...
    def device(self, id_or_name: str | int) -> Device: ...
    def interface(self, device: str | int, id_or_name: str | int) -> Interface: ...
    def link_name(self, device: str | int, interface: str | int) -> str: ...
    def link_speed(self, link_name: str) -> int: ...
    def save(self, path: str | os.PathLike[str]) -> None: ...
    @classmethod
    def load(cls, path: str | os.PathLike[str]) -> "DeviceLookup": ...
```

- `Device` and `Interface` are the generated V6 models.
- `save()` and `load()` use JSON only.

## `kentik_api.analytics` (extra `analytics`)

- Importing the package without the extra raises `ImportError` with the text
  `pip install "kentik-api[analytics]"`. The rest of the SDK still imports.
- `QueryDefinition.from_dict(d)`, `QueryDefinition.from_yaml(path)`, and
  `QueryDefinition.get_data(client, start, end) -> dict[str, DataFrame]`
  (one DataFrame for each bucket, with typed columns and a time index).
- `DataFrameCache(directory, step).get(definition, client, start, end) ->
  DataFrame`.
- `flatness_analysis(...)`: the V5 signature and output.
- A SQL definition raises `ValueError("Kentik retired the V5 SQL query
  endpoint on 2025-05-01. Use a top-X definition.")`.
- An `@fixup:` mapping raises `ValueError` that names the safe options: a
  column rename, a type, or a post-processing function in the caller's code.
