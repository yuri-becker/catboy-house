# Paperless

Runs [paperless-ngx](https://docs.paperless-ngx.com) on Postgres+Redis+Gotenberg+Tika.

## Role variables

### `paperless_domain`*
Domain on which paperless should be accessible.

### `paperless_service_port`*
Port on which paperless should run.

### `paperless_secret`*
Random, secret string for secret generation.

### `paperless_uid`*
UID paperless's should have.

### `paperless_postgres_user`*
Username the database should use for paperless.

### `paperless_postgres_password`*
Password the database should use for paperless.

### `paperless_smtp_user`*
SMTP user.

### `paperless_smtp_password`*
SMTP password.

### `paperless_smtp_use_tls`*
Whether TLS should be used for email sending (`true`/`false`). 

### `paperless_ocr_languages` (optional)
Defaults to `eng`.

Space-seperated list of languages that the optical language recognition should install.
See https://packages.debian.org/search?keywords=tesseract-ocr-&searchon=names&suite=buster for possible values.

### `paperless_ocr_language` (optional)
Defaults to `eng`.

Default language for character regoniction. Should be one of [paperless_ocr_languages](#paperless_ocr_languages).

### `paperless_task_workers` (optional)
Defaults to `1`.

Amount of task workers paperless should use.

### `paperless_threads_per_worker` (optional)
Defaults to `1`.

Amount of threads per task worker.

### `paperless_user_name` (optional)
Name of the user for [paperless_uid](#paperless_uid).

### `paperless_app_title` (optional)
Defaults to `paperless`.

Page title.

### `paperless_smtp_sender` (optional)

Defaults to [paperless_smtp_user](#paperless_smtp_user).
