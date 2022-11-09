FROM solr:8.10

COPY ./data/ /data/processed_data/

COPY indexing.json /data/indexing.json

COPY startup.sh /scripts/startup.sh

ENTRYPOINT ["/scripts/startup.sh"]