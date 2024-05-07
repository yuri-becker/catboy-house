# Jellyfin

Media system, see [https://jellyfin.org/](https://jellyfin.org/).

## Role Variables

### `jellyfin_service_port`*
Port on which this service should be exposed.

### `movies_path`*
Path where Jellyfin should look for movies in.

### `tv_path`*
Path for shows.

### `jellyfin_service_directory` (optional)
Directory under `services_path` where this service should store its files in.

### `jellyfin_container_name` (optional)
Container name.

### `jellyfin_service_path` (optional)
Path where this service should store its files in. Alternative to `jellyfin_service_directory`.

### `jellyfin_volume_config` (optional)
Path of the config volume.

### `jellyfin_volume_web` (optional)
Path of the web config volume.