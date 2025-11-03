#!/bin/bash

# Exit on any error
set -o errexit

echo "--- Building project ---"

# 1. Install dependencies
python3 -m pip install -r requirements.txt

echo "--- Dependencies installed ---"

# 2. Run Migrations
python3 manage.py migrate --noinput

echo "--- Migrations complete ---"

# 3. Collect Static Files
python3 manage.py collectstatic --noinput --clear

echo "--- Build finished ---"