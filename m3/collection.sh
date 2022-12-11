# Populate collection

curl -X POST -H 'Content-type:application/json' --data-binary @./indexing.json http://localhost:8983/solr/core/schema
curl -X POST -H 'Content-type:application/json' --data-binary @./suggester.json http://localhost:8983/solr/     
curl -X POST -H 'Content-type:application/csv' --data-binary @./data/wiki_movie_final.csv http://localhost:8983/solr/core/update?commit=true
