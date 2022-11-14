# QUERIES

**Query 1:**
  Drama movies with Bollywood origin released in 2015 or after - 29 movies found
  <!-- Correct ones will be the ones that only have drama as gender -->
  
**Query 2:**
  Movies starring Robert de Niro and are from the Italian mafia - 10 movies found
  
**Query 3:**
  Movies directed by Steven Spielberg about murder - 19 movies found
  
**Query 4:**
  Police action movies from the year 2000 - 15 movies found

---

## How to run

1. Open terminal 
2. $ `cd m2`
3. $ `docker build . -t pri_solr && docker run --rm -it -p 8983:8983 pri_solr`
4. Open new terminal
5. $ `bash collection.sh`
6. Open browser in localhost:8983