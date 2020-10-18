# Simple crawler
(targeted on simple.wikipedia.org)

## Run

Docker-compose (for Kafka). Visit localhost:9000 for management. Topic should be created and specified.

```docker-compose up```


*Tip: if crawler can't poll messages change Queue.py consumer group_id to None, run and revert back to random string.*


Activate venv and install requirements for workers
```pip install -r requirements.txt```


Initialize database

```
sqlite3 crawler.db
.read init.sql
```

Run crawlers (as much instances as you want to; check configs in main.py)

```python main.py```

For pagerank (after crawlers did some part of work)

```python pagerank_main.py```


## Final results

Processed:

```
sqlite> select count(*) from pages;
172519
sqlite> select count(*) from edges;
4887786
sqlite> select count(*) from processed;
1653813
```

### Pagerank top:

```
[('United_States', 0.0032922490541611), ('IMDb', 0.002493638421258287), ('France', 0.0018665272604735327),  
 ('Geographic_coordinate_system', 0.0014998574721566088), ('Departments_of_France', 0.0013993061821948724),  
 ('ISBN_(identifier)', 0.0012269350644286599), ('City', 0.0011745491175918941), ('Americans', 0.0011495237386781052),  
 ('Wiktionary', 0.0010505870037046485), ('Communes_of_France', 0.0009903201345658201)]
```

Note: original pagerank algorithm works only for graphs without end-nodes (those, which have no liks on other pages). So, here is modified algorithm, which needed to be normalized.
