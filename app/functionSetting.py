##this is the json that we're gonna throw into GPT's API
from contextSetting import database_schema_string

functions = [
    {
        "name": "ask_database",
        "description": "Use this function to answer user questions about music. Input should be a fully formed SQL query.",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": f"""
                            SQL query extracting info to answer the user's question.
                            SQL should be written using this database schema:
                            {database_schema_string}
                            The query should be returned in plain text, not in JSON.
                            """,
                }
            },
            "required": ["query"],


        },
    },
]

summaryFunctions = [
    {
        "name": "summarize_results",
        "description": "Use this function to summarize SQL results into a human readable format. Input should a JSON-like string containing results.",
        "parameters": {
            "type": "object",
            "properties": {
                "summary": {
                    "type": "string",
                    "description": f"""
                            Summary should be based on the SQL results generated previously by the assistant.
                            Translate the given results in a way that is human readable, and answers the original question from the user.
                            """,
                }
            },
            "required": ["summary"],
        },
    },
]


