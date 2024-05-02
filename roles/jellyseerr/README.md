# Jellyseerr

Request management and media discover [Jellyseerr](https://github.com/Fallenbagel/jellyseerr).

## Role Variables

### `jellyseerr_service_directory`*
Directory under `services_path` where this service should store its files in.

### `jellyseerr_service_port`*
Port on which this service should be exposed.

### `jellyseerr_container_name` (optional)
Container names.

### `jellyseerr_service_path` (optional)
Path where this service should store its files in. Alternative to `jellyseerr_service_directory`.

### `jellyseerr_volume_config` (optional)
Path of the config volume.