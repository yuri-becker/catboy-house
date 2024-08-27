# Mealie

Recipe manager [Mealie](https://mealie.io/).

## Role Variables

### `mealie_service_port`*
Port on which this service should be exposed.

### `mealie-domain`*
Domain name for Mealie

### `mealie_postgres_user`*
Username for the internal postgres user.

### `mealie_postgres_password`* 
Password for the internal postgres user.

### `smtp_server`*
SMTP server for sending mails.

### `smtp_port`*
SMTP server's port

### `mealie_smtp_user`*
Username of the SMTP user at `smtp_server`

### `mealie_smtp_password`*
Password fot the SMTP user.

### `mealie_service_directory` (optional)
Directory under `services_path` where this service should store its files in.

### `mealie_container_prefix` (optional)
Prefix for container names.

### `mealie_service_path` (optional)
Path where this service should store its files in. Alternative to `mealie_service_directory`.

### `mealie_volume_data` (optional)
Path of the data volume

### `mealie_volume_db` (optional)
Path of the database's volume