# Tinfoil Store

[Tinfoil](https://tinfoil.io/) store using [Ownfoil](https://github.com/a1ex4/ownfoil) to serve files from [Seafile](https://github.com/yuri-becker/seafile-mount).

Enables downloading homebrew games to a switch by just putting them in the respective folder on a Seafile.

## Role Variables

### `tinfoil_store_service_port`*
Port on which this service should be exposed

### `tinfoil_store_service_directory` (optional)
Directory under `services_path` where this service should store its files in

### `tinfoil_store_container_prefix` (optional)
Prefix for container names.

### `tinfoil_store_seafile_client_name` (optional)
Seafile client name.

### `tinfoil_store_seafile_cache_size_limit` (optional)
Cache size limit.

### `tinfoil_store_seafile_clean_cache_interval` (optional)
Seafile Cache Clean Interval.