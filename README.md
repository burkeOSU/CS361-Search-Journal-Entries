# CS361-Search-Journal-Entries
A microservice using ZeroMQ to communicate with a main program to search all journal entries for a keyword.
If running on Windows, 'pip install pyzmq' is required to access the ZeroMQ communication pipeline.

# Instructions
To request data from this microservice, use the following parameters:
- mode: a string that represents whether the user is using a terminal or json program
- keyword: a string that represents the keyword to search for
- filePath: a string that represents the relative path to the folder containing the entries to search through