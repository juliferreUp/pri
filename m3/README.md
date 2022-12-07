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