# Linkding

Bookmark manager [Linkding](https://github.com/sissbruecker/linkding).

## Role Variables

### `linkding_service_directory`*
Directory under `services_path` where this service should store its files in.

### `linkding_service_port`*
Port on which this service should be exposed.

### `linkding_container_prefix` (optional)
Prefix for container names.

### `linkding_service_path` (optional)
Path where this service should store its files in. Alternative to `linkding_service_directory`.

### `linkding_volume_data` (optional)
Path of the data volume.

### `linkding_volume_db` (optional)
Path of the database's volume.

### `linkding_network` (optional)
Network name.