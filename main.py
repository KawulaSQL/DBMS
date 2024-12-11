import sys
sys.path.append("./Query_Processor")
sys.path.append("./Query_Processor/Query_Optimizer")
sys.path.append("./Query_Processor/Storage_Manager")
sys.path.append("./Query_Processor/Concurrency_Control_Manager")

from Query_Processor.QueryProcessor import QueryProcessor
from Query_Processor.utils.result import ExecutionResult, display_result

if __name__ == "__main__":
    base_path = "./storage"
    query_processor = QueryProcessor(base_path)

    print(r"""  $$\   $$\                                  $$\            $$$$$$\   $$$$$$\  $$\       """)
    print(r"""  $$ | $$  |                                 $$ |          $$  __$$\ $$  __$$\ $$ |      """)
    print(r"""  $$ |$$  / $$$$$$\  $$\  $$\  $$\ $$\   $$\ $$ | $$$$$$\  $$ /  \__|$$ /  $$ |$$ |      """)
    print(r"""  $$$$$  /  \____$$\ $$ | $$ | $$ |$$ |  $$ |$$ | \____$$\ \$$$$$$\  $$ |  $$ |$$ |      """)
    print(r"""  $$  $$<   $$$$$$$ |$$ | $$ | $$ |$$ |  $$ |$$ | $$$$$$$ | \____$$\ $$ |  $$ |$$ |      """)
    print(r"""  $$ |\$$\ $$  __$$ |$$ | $$ | $$ |$$ |  $$ |$$ |$$  __$$ |$$\   $$ |$$ $$\$$ |$$ |      """)
    print(r"""  $$ | \$$\\$$$$$$$ |\$$$$$\$$$$  |\$$$$$$  |$$ |\$$$$$$$ |\$$$$$$  |\$$$$$$ / $$$$$$$$\ """)
    print(r"""  \__|  \__|\_______| \_____\____/  \______/ \__| \_______| \______/  \___$$$\ \________|""")
    print(r"""                                                                          \___|          """)
    print("   .     .     .     .     .     .     .     .     .     .     .     .     .     .     .   ")
    print("_.` `._.` `._.` `._.` `._.` `._.` `._.` `._.` `._.` `._.` `._.` `._.` `._.` `._.` `._.` `._")
    print("\n")
    print("Welcome to KawulaSQL!")
    print("Enter your SQL query or type 'exit' to quit.\n")
    while True:
        query = input("[KawulaSQL] >>> ")
        if query.lower() == "exit":
            print("Exiting KawulaSQL. Goodbye!")
            break
        try:
            result = query_processor.process_query(query)
            if isinstance(result, ExecutionResult):
                display_result(result)
            else:
                print("Unexpected result type.")
        except Exception as e:
            print(f"Error processing query: {str(e)}")
