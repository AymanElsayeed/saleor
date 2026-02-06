#!/usr/bin/env python3
"""Create Saleor admin user if none exists. Idempotent; safe to run on every startup."""

import os
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "saleor.settings")

import django

django.setup()

from saleor.account.utils import create_superuser  # noqa: E402

email = os.environ.get("ADMIN_EMAIL", "admin@example.com")
password = os.environ.get("ADMIN_PASSWORD", "admin")
msg = create_superuser({"email": email, "password": password})
sys.stderr.write(f"{msg}\n")
