# Portainer
Docker management [Portainer](https://www.portainer.io/).

## Role variables

### `portainer_service_port`*
Port on which Portainer should be accessible.

### `portainer_service_directory` (optional)
Directory under `services_path` where Portainer should store its files in.

### `portainer_service_path` (optional)
Path where Portainer should store its files in. Alternative to `portainer_service_directory`.

### `portainer_volume_data` (optional)
Path of the data volume.

### `portainer_docker_sock` (optional)
Path of the Docker socket.

### `portainer_container_name` (optional)
Container name