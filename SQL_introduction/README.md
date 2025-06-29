# SQL Introduction

This project is part of the **Holberton School by Academy Tuwaiq**  curriculum and aims to teach the fundamentals of working with relational databases using SQL (MySQL specifically).

## 🎯 Project Objectives

- Learn basic SQL commands such as `CREATE`, `DROP`, `SELECT`, `INSERT`, `UPDATE`, and `DELETE`.
- Practice managing databases and tables.
- Execute simple analytical queries using `GROUP BY`, `ORDER BY`, and aggregate functions.
- Understand and apply UTF-8 encoding conversion in databases, tables, and fields.

## 📌 Common SQL Commands

| Command                 | Description                                              | Example                                                      |
|-------------------------|----------------------------------------------------------|--------------------------------------------------------------|
| `SHOW DATABASES;`       | List all databases                                        | `SHOW DATABASES;`                                            |
| `CREATE DATABASE`       | Create a new database                                     | `CREATE DATABASE hbtn_0c_0;`                                 |
| `DROP DATABASE`         | Delete a database                                         | `DROP DATABASE hbtn_0c_0;`                                   |
| `SHOW TABLES;`          | List all tables in a database                             | `SHOW TABLES;`                                               |
| `CREATE TABLE`          | Create a new table                                        | `CREATE TABLE first_table (id INT, name VARCHAR(256));`     |
| `INSERT INTO`           | Add new data to a table                                   | `INSERT INTO first_table (id, name) VALUES (89, 'Best');`   |
| `SELECT * FROM`         | View all rows in a table                                  | `SELECT * FROM first_table;`                                |
| `SELECT COUNT(*)`       | Count rows that meet a condition                          | `SELECT COUNT(*) FROM first_table WHERE id = 89;`           |
| `UPDATE`                | Update data in a table                                    | `UPDATE second_table SET score = 10 WHERE name = 'Bob';`    |
| `DELETE FROM`           | Delete rows based on a condition                          | `DELETE FROM second_table WHERE score <= 5;`                |
| `ORDER BY`              | Sort results by a column                                  | `SELECT * FROM second_table ORDER BY score DESC;`           |
| `GROUP BY`              | Group results by column values                            | `SELECT score, COUNT(*) FROM second_table GROUP BY score;`  |
| `AVG()`                 | Calculate the average                                     | `SELECT AVG(score) AS average FROM second_table;`           |
| `MAX()`                 | Get the maximum value                                     | `SELECT MAX(score) FROM second_table;`                      |

## 🛠 How to Execute

To run a script:

```bash
cat <file_name>.sql | mysql -hlocalhost -uroot -p <database_name>
```

Example:

```bash
cat 6-list_values.sql | mysql -uroot -p hbtn_0c_0
```
## 🗂 File Descriptions

| File                     | Description                                                                 |
|--------------------------|-----------------------------------------------------------------------------|
| 0-list_databases.sql     | Lists all databases on the MySQL server.                                   |
| 1-create_database.sql    | Creates the database `hbtn_0c_0` if it does not exist.                      |
| 2-remove_database.sql    | Deletes the database `hbtn_0c_0` if it exists.                              |
| 3-list_tables.sql        | Lists all tables of a specific database.                                    |
| 4-first_table.sql        | Creates a table `first_table` with two columns: `id` and `name`.           |
| 5-full_table.sql         | Displays the SQL statement used to create `first_table`.                   |
| 6-list_values.sql        | Lists all rows from the `first_table`.                                     |
| 7-insert_value.sql       | Inserts a new row into `first_table` (id=89, name='Best School').          |
| 8-count_89.sql           | Counts the number of records with id = 89.                                 |
| 9-full_creation.sql      | Creates the `second_table` and inserts multiple rows.                      |
| 10-top_score.sql         | Displays all rows ordered by score in descending order.                    |
| 11-best_score.sql        | Lists rows with `score >= 10`.                                             |
| 12-no_cheating.sql       | Updates Bob’s score to 10 using the name only.                             |
| 13-change_class.sql      | Deletes rows with `score <= 5`.                                           |
| 14-average.sql           | Computes the average score of `second_table`.                              |
| 15-groups.sql            | Groups and counts records by score, sorted by frequency.                   |
| 16-no_link.sql           | Lists rows where the `name` column is not empty.                           |
| 100-move_to_utf8.sql     | Converts the database, table, and name column to UTF-8.                    |
| 101-avg_temperatures.sql | Shows average temperature by city (descending).                            |
| 102-top_city.sql         | Displays top 3 cities with highest temperatures in July and August.        |
| 103-max_state.sql        | Shows max temperature per state, sorted by state name.                     |

