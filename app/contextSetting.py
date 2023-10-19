import sqlite3
import json

conn = sqlite3.connect("data/chinook.db")
print("Opened database successfully")


def get_table_names(conn):
    """Return a list of table names."""
    table_names = []
    tables = conn.execute("SELECT name FROM sqlite_master WHERE type='table';")
    for table in tables.fetchall():
        table_names.append(table[0])
    return table_names


def get_column_names(conn, table_name):
    """Return a list of column names."""
    column_names = []
    columns = conn.execute(f"PRAGMA table_info('{table_name}');").fetchall()
    for col in columns:
        column_names.append(col[1])
    return column_names


def get_database_info(conn):
    """Return a list of dicts containing the table name and columns for each table in the database."""
    table_dicts = []
    for table_name in get_table_names(conn):
        columns_names = get_column_names(conn, table_name)
        table_dicts.append({"table_name": table_name, "column_names": columns_names})
    return table_dicts


database_schema_dict = get_database_info(conn)

##actually, the most important thing in this app is to get the "context"
## so we have a massive string with format:
## Table1: [column_names]
## Table2: [column_names]

##to improve accuracy, we can try using langchain to feed the context in together with training data (e.g: User Qn, Correct Answer)
##but for a demo, this works tbh
database_schema_string = "\n".join(
    [
        f"Table: {table['table_name']}\nColumns: {', '.join(table['column_names'])}"
        for table in database_schema_dict
    ]
)


def ask_database(conn, query):
    """Function to query SQLite database with a provided SQL query."""
    try:
        results = str(conn.execute(query).fetchall())
    except Exception as e:
        results = f"query failed with error: {e}"
    return results

def execute_function_call(message):
    print(message["function_call"]["name"])
    if message["function_call"]["name"] == "ask_database":
        query = json.loads(message["function_call"]["arguments"])["query"]
        results = ask_database(conn, query)

    elif message["function_call"]["name"] == "summarize_results":
        results = json.loads(message["function_call"]["arguments"])["summary"]

    else:
        results = f"Error: function {message['function_call']['name']} does not exist"
    return results