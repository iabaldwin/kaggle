#!/bin/bash

echo 'Starting server on 8000...'
python -m SimpleHTTPServer 8000 > /dev/null 2>&1 &
echo 'Done'

