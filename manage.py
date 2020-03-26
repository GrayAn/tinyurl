#!/usr/bin/env python
from migrate.versioning.shell import main

from tinyurl.config import get_config

if __name__ == '__main__':
    cfg = get_config()
    main(repository='tinyurl/migrations', url=cfg.db_url)
