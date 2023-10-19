#main entry point

from contextSetting import execute_function_call
from functionSetting import functions
from functionSetting import summaryFunctions

#and util imports 
from utils.openAIutils import chat_completion_request
from utils.openAIutils import pretty_print_conversation

def entry(question:str):
    '''
    main entry point into the function
    Takes in a question, returns an answer
    '''
    messages = []
    messages.append({"role": "system", "content": "Answer user questions by generating SQL queries against the Chinook Music Database " +
                    "\n" +
                    "        And then executing the SQL query on SQLite"})


    # question = input("Input your question based on chinook's Database here!" 
    #             + "\n"
    #             + "For example: who are the top 5 most popular artists based on total albums?")

    messages.append({"role": "user", "content": question})
    chat_response = chat_completion_request(messages, functions)
    assistant_message = chat_response.json()["choices"][0]["message"]
    messages.append(assistant_message)

    ##NOW, do the summary!
    chat_response = chat_completion_request(messages, summaryFunctions)
    assistant_message = chat_response.json()["choices"][0]["message"]
    messages.append(assistant_message)
    results = ""
    if assistant_message.get("function_call"):
        results = execute_function_call(assistant_message)
        messages.append({"role": "function", "name": assistant_message["function_call"]["name"], "content": results})


    pretty_print_conversation(messages)
    return messages[-1]["content"]


