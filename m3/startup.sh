#!/bin/bash

precreate-core core

# Start Solr in background mode so we can use the API to upload the schema
solr start

# Restart in foreground mode so we can access the interface
solr restart -f