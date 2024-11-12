# pyload

Download manager [pyLoad](https://pyload.net/).

## Role Variables

### `pyload_port`*
Port on which pyload should run.

### `downloads_path`*
Directory to put downloads in.

### `pyload_service_directory` (optional)
Directory under `services_path` where this service should store its files in.

### `pyload_service_path` (optional)
Path where this service should store its files in. Alternative to `pyload_service_directory`.

### `pyload_volume_config` (optional)
Path of the config volume.

### `pyload_container_name` (optional)
Container name
