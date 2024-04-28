# Mealie

Recipe manager [Mealie](https://mealie.io/).

## Role Variables

### `mealie_service_directory`*
Directory under `services_path` where this service should store its files in.

### `mealie_service_port`*
Port on which this service should be exposed.

### `mealie-domain`*
Domain name for Mealie

### `mealie_container_prefix` (optional)
Prefix for container names.

### `mealie_service_path` (optional)
Path where this service should store its files in. Alternative to `mealie_service_directory`.

### `mealie_volume_data` (optional)
Path of the data volume

### `mealie_volume_db` (optional)
Path of the database's volume

### `mealie_network` (optional)
Network name