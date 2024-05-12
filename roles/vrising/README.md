# V Rising

Game server for [V Rising](https://store.steampowered.com/app/1604030/V_Rising/), a vampire game. 👀
Based on the [Docker image by TrueOsiris](https://github.com/TrueOsiris/docker-vrising).

Variable descriptions are taken from [the wiki](https://vrising.fandom.com/wiki/V_Rising_Dedicated_Server#Server_Host_Settings) when applicable. 

## Role variables

### `vrising_server_name`*
Name of the server how it should show up in the game.

### `vrising_server_description`*
Short description of server purpose, rules and/or message of the day.

### `vrising_admins` (optional)
Array of admins' steam id

### `vrising_container_name` (optional)
Name of the docker container

### `vrising_service_path` (optional)
Path where V Rising should store its files in.

### `vrising_volume_persistentdata` (optional)
Volume for save files, configs, etc.

### `vrising_volume_server` (optional)
Volume for the game files.

### `vrising_game_port` (optional)
UDP port for game traffic. Will listen on all interfaces. Defaults to 9876.

### `vrising_query_port` (optional)
UDP port for Steam server list features. Will listen on all interfaces. Defaults to 9877.

### `vrising_secure` (optional)
**I think** this defines whether you need a password to enter the server. `true`/`false`. Defaults to `true`.

### `vrising_server_password` (optional)
Password for your server. Empty by default. If you don't want your server to be protected by a password, set `vrising_secure` **probably**.

### `vrising_list_on_master_server` (optional)
Set to true to list on server list, else set to false. Defaults to false.

### `vrising_server_list_on_steam` (optional)
**I guess** whether your server should show up in the server browser and is joinable in your friends list. Set to true or false. Defaults to false.

### `vrising_list_on_eos` (optional)
No idea what eos is. Set to true or false. Defaults to false.

### `vrising_rcon_enabled` (optional)
Enables the RCON interface. Defaults to true.

### `vrising_rcon_port` (optional)
Port for RCON interface. Defaults to 9878 and is only bound to the Docker gateway.

## `vrising_auto_save_count` (optional)
Count of auto saves to keep.

## `vrising_auto_save_interval` (optional)
Interval for auto saves in seconds.

## `vrising_game_settings_preset` (optional)
Can be one of
- StandardPvE (**default**)
- StandardPvE_Easy
- StandardPvE_Hard
- Level30PvE
- Level50PvE
- Level70PvE
- StandardPvP
- StandardPvP_Easy
- StandardPvP_Hard
- HardcorePvP
- SoloPvP
- DuoPvP
- Level30PvP
- Level50PvP
- Level70PvP

## `vrising_fps` (optional)
FPS the server should run at.

## `vrising_compress_save_files` (optional)
Whether save files shall be compressed. Set to true or false.