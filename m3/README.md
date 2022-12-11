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
1. Open container bash
2. Change solrconf.xml

<searchComponent name="suggest" class="solr.SuggestComponent">
  <lst name="suggester">
    <str name="name">mySuggester</str>
    <!-- Look at this field -->
    <str name="lookupImpl">AnalyzingLookupFactory</str>
    <!-- <str name="lookupImpl">JaspellLookupFactory</str> -->

    <str name="dictionaryImpl">DocumentDictionaryFactory</str>
    <str name="field">Genre</str>
    <str name="weightField">averageRating</str>
    <str name="suggestAnalyzerFieldType">string</str>
    <str name="buildOnStartup">false</str>
  </lst>
</searchComponent>
<requestHandler name="/suggest" class="solr.SearchHandler" startup="lazy">    
    <lst name="defaults">
      <str name="terms">true</str>
      <str name="distrib">false</str>
    </lst>
    <arr name="components">
      <str>suggest</str>
    </arr>
  </requestHandler>

3. Reload Solr in interface 