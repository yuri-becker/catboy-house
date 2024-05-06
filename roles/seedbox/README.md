# Seedbox

Seedbox built with [qBittorrent](https://www.qbittorrent.org/) and [gluetun](https://github.com/qdm12/gluetun).

## Role variables

### `seedbox_webui_port`*
Port on which the WebUI should be exposed.

### `seedbox_vpn_service_provider`*

Name of the VPN service provider, according to [the list in glueton](https://github.com/qdm12/gluetun-wiki/tree/main/setup/providers). 

### `seedbox_vpn_server_countries`*
Name(s) of the provider countrie(s), as on the [provider's documentation](https://github.com/qdm12/gluetun-wiki/tree/main/setup/providers).

### `seedbox_vpn_input_port`*
Port that is forwarded by your VPN provider.

### `downloads_path`*
Path where downloads should be put.

### `seedbox_service_directory` (optional)
Directory under `services_path` where this service should store its files in.

### `seedbox_service_path` (optional)
Path where this service should store its files in. Alternative to `seedbox_service_directory`.  

### `seedbox_container_prefix` (optional)
Prefix for container names.

### `seedbox_network_name` (optional)
Name of the network.

### `seedbox_volume_gluetun` (optional)
Path of gluetun's volume.

### `seedbox_volume_qbittorrent` (optional)
Path to qbittorrent's volume (this is not where qbittorrent puts its downloads).
