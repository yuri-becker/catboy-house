# romm

Rom Manager with integrated emulator.
See [https://romm.app](https://romm.app).

## Role Variables

### `romm_domain`*
Domain this role should run on.

### `romm_port`*
Port which this role should bind to.

### `romm_uid`*
UID for the unix user.

### `romm_database_user`*
Username for the database.

### `romm_database_password`*
Password for the database.

### `romm_database_root_password`*
Password for the database's root user.

### `romm_auth_secret_key`*
Secret for authentication. Generate with `openssl rand -hex 32`.

### `romm_steamgriddb_api_key`*
API Key for [SteamGridDb](https://www.steamgriddb.com).
See https://github.com/rommapp/romm/wiki/Generate-API-Keys#steamgriddb.

### `romm_igdb_client_id`*
Client ID for an IGDB API Client.
See https://api-docs.igdb.com/#account-creation.

### `romm_igdb_client_secret`*
Secret for the IGDB API Client specificed in `romm_igdb_client_id`.

### `romm_mobygames_api_key`*
API Key for [MobyGames](https://www.mobygames.com).
See https://github.com/rommapp/romm/wiki/Generate-API-Keys#mobygames.

### `romm_volume_resources` (optional)
Resources fetched from IGDB (covers, screenshots, etc.)

### `romm_volume_redis` (optional)
Cached data for background tasks.

### `romm_volume_library` (optional)
Game Library directory.
See https://github.com/rommapp/romm?tab=readme-ov-file#folder-structure for folder structure.

### `romm_volume_assets` (optional)
Uploaded saves, states, etc.

### `romm_volume_config` (optional)
Folder where the config is stored in.

### `romm_user_name` (optional)
Name for the user assigned with `romm_uid`.