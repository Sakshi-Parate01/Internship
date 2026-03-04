import os
from dotenv import load_dotenv
from agents.router import Router
load_dotenv()

def main():
    print(f"Welcome to {os.getenv('APP_NAME')}")
    router = Router()

    while True:
        query = input("\nEnter command (or type exit): ")
        if query.lower() == "exit":
            print("Goodbye!")
            break

        response = router.route(query)
        print(response)

if __name__ == "__main__":
    main()