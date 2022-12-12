## Things to add for M3
- Adding a rating to the movies
    - Read title.akas.tsv
    - Match title comlumn from our csv with its title 
    - Match the titleId to get the ratings
- Improve the types for the attributes in our schema
- Words related to a theme
- Movie recomendations -> Similar movies to the one searched
---

## How to run
1. Open terminal 
2. $ `cd m3`
3. $ `docker build . -t pri_solr && docker run --rm -it -p 8983:8983 pri_solr`
4. Open new terminal
5. $ `bash collection.sh`
6. Open browser in localhost:8983


## Change the solrconf.xml
1. Open container bash > $`docker exec -u 0 -it <mycontainer> bash`
2. $`cd ../../var/solr/data/core/conf`
3. $`apt-get update && apt-get install nano`
4. $`nano solrconfig.xml`
2. Update solrconf.xml with [this](solrconfig.xml)
3. Reload Solr in interface (Core Admin > Reload)