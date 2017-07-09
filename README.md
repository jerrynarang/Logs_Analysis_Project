# Logs Analysis Project


### About the logs analysis project
You've been hired onto a team working on a newspaper site. The user-facing newspaper site frontend itself, and the database behind it, are already built and running. You've been asked to build an internal reporting tool that will use information from the database to discover what kind of articles the site's readers like.

The database contains newspaper articles, as well as the web server log for the site. The log has a database row for each time a reader loaded a web page. Using that information, your code will answer questions about the site's user activity.

The program you write in this project will run from the command line. It won't take any input from the user. Instead, it will connect to that database, use SQL queries to analyze the log data, and print out the answers to some questions.


### Basic skills required :
Completing this project will exercise your database skills. Here are some portions of the Relational Databases course that you might want to review:

* Joining tables
* The select ...where statement
* Select clauses
* Writing code with DB-API
* Views

### The PostgreSQL documentation
In this project, you'll be using a PostgreSQL database. If you'd like to know a lot more about the kinds of queries that you can use in this dialect of SQL, check out the PostgreSQL documentation. It's a lot of detail, but it spells out all the many things the database can do.

Here are some parts that may be particularly useful to refer to:
* The select statement
* SQL string functions
* Aggregate functions


### Questions
1. What are the most popular three articles of all time?
  Which articles have been accessed the most?
  Present this information as a sorted list with the most popular article at the top
2. Who are the most popular article authors of all time?
  That is, when you sum up all of the articles each author has written, which authors get the most page views?
  Present this as a sorted list with the most popular author at the top.
3. On which days did more than 1% of requests lead to errors?
  The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser.


## Requirements
* Python 3.5.3
* psycopg2
* Postgresql 9.6

## How to run

* load the data onto the database
```sql
psql -d news -f newsdata.sql
```
* connect to the database
```sql
psql -d news
```
* create views
* python3 LogsAnalysis.py

### Create Views
```sql
CREATE VIEW author_info AS
SELECT authors.name, articles.title, articles.slug
FROM articles, authors
WHERE articles.author = authors.id
ORDER BY authors.name;
```

```sql
CREATE VIEW path_view AS
SELECT path, COUNT(*) AS view
FROM log
GROUP BY path
ORDER BY path;
```

```sql
CREATE VIEW article_view AS
SELECT author_info.name, author_info.title, path_view.view
FROM author_info, path_view
WHERE path_view.path = CONCAT('/article/', author_info.slug)
ORDER BY author_info.name;
```

```sql
CREATE VIEW total_view AS
SELECT date(time), COUNT(*) AS views
FROM log 
GROUP BY date(time)
ORDER BY date(time);
```

```sql
CREATE VIEW error_view AS
SELECT date(time), COUNT(*) AS errors
FROM log WHERE status = '404 NOT FOUND' 
GROUP BY date(time) 
ORDER BY date(time);
```

```sql
CREATE VIEW error_percent AS
SELECT total_view.date, (100.0*error_view.errors/total_view.views) AS percentage
FROM total_view, error_view
WHERE total_view.date = error_view.date
ORDER BY total_view.date;
```

