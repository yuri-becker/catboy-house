# sabnzbd

Usenet Downloader [sabnzbd](https://github.com/sabnzbd/sabnzbd).

## Role Variables

### `sabnzbd_service_port`*
Port on which sabnzbd should run.

### `downloads_path`*
Directory to put downloads in.

### `sabnzbd_service_directory` (optional)
Directory under `services_path` where this service should store its files in.

### `sabnzbd_service_path` (optional)
Path where this service should store its files in. Alternative to `sabnzbd_service_directory`.

### `sabnzbd_volume_config` (optional)
Path of the config volume.

### `sabnzbd_container_name` (optional)
Container name
