Tinfoil Store
=========

[Tinfoil](https://tinfoil.io/) store using [Ownfoil](https://github.com/a1ex4/ownfoil) to serve files from [Seafile](https://github.com/yuri-becker/seafile-mount).

Enables me to download homebrew games to my switch by just putting them in the respective folder on my Seafile.

No public access, sorry. 😔

Role Variables
--------------

- `tinfoil_store_service_directory`<br/>
   directory under `services_path` where this service should store its files in
- `tinfoil_store_service_port`<br/>
   port on which this service should be exposed
- `tinfoil_store_container_prefix`<br/>
  Prefix for container names.<br/>
  Defaults to "tinfoil-store".
- `tinfoil_store_seafile_client_name`<br/>
   Seafile client name.<br/>
   **Defaults** to "catboy-store".
- `tinfoil_store_seafile_cache_size_limit`<br/>
  Cache size limit.<br/>
  **Defaults** to "10GB".
- `tinfoil_store_seafile_clean_cache_interval`<br/>
  Seafile Cache Clean Interval.<br/>
  **Defaults** to "120".