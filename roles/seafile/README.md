# Seafile

Cloud storage [Seafile](https://www.seafile.com/en/home/).

## Role Variables

### `seafile_service_port`*
Port on which this service should be exposed.

### `seafile_domain`*
Domain for this Service

### `seafile_mysql_password`*
Password for the internal MariaDB user

### `seafile_service_directory` (optional)
Directory under `services_path` where this service should store its files in.

### `seafile_service_path` (optional)
Path where this service should store its files in. Alternative to `seafile_service_directory`.  

### `seafile_container_prefix` (optional)
Prefix for container names.

### `seafile_volume_data` (optional)
Path of the data volume.  

### `seafile_volume_db` (optional)
Path of the database's volume.  
