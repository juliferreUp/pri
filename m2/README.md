# QUERIES

**Query 1:**
  Drama movies with american origin in the XXI century
  
**Query 2:**
  Movies starring Robert de Niro and Al Pacino
  
**Query 3:**
  Thriller movies directed by David Fincher
  
**Query 4:**
  Police movies from the range of years 2000-2005

---

## How to run

1. Open terminal 
2. $ `cd m2`
3. $ `docker build . -t pri_solr && docker run --rm -it -p 8983:8983 pri_solr`
4. Open new terminal
5. $ `bash collection.sh`
6. Open browser in localhost:8983