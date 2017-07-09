#!/usr/bin/env python3

import psycopg2


def main():
    #Connecting to an existing database
    conn = psycopg2.connect("dbname=news")

    #Open a cursor to perform database operations
    cur = conn.cursor()

    # Question 1 Solution :
    sql_popular_articles = """
      SELECT article_view.title, article_view.view
      FROM article_view
      ORDER BY article_view.view DESC
      LIMIT 3;
    """
    cur.execute(sql_popular_articles)
    print("most popular three articles of all time:")
    for (title, view) in cur.fetchall():
        print("    {} - {} views".format(title, view))
    print("-" * 50)

    # Question 2 solution :
    sql_popular_authors = """
    SELECT article_view.name, SUM(article_view.view) AS author_view
    FROM article_view
    GROUP BY article_view.name
    ORDER BY author_view DESC;
    """
    cur.execute(sql_popular_authors)
    print("most popular article authors of all time:")
    for (name, view) in cur.fetchall():
        print("    {} - {} views".format(name, view))
    print("-" * 50)

    # Question 3 solution :
    sql_more_than_one_percent_errors = """
    SELECT date
    FROM error_percent
    WHERE error_percent.percentage > 1;
    """
    cur.execute(sql_more_than_one_percent_errors)
    print("Days with more than 1% errors:")
    for (date,percentage) in cur.fetchall():
        print("    {} - {}% errors".format(date,percentage))
    

    # Close communication with the database
    cur.close()
    conn.close()

if __name__ == "__main__":
    main()
