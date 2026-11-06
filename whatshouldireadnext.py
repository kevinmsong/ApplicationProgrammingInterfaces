import argparse
import os

def require_env(name):
    value = os.environ.get(name, "").strip()
    if not value:
        raise SystemExit(
            f"Missing required environment variable {name}. "
            "Set it before running this script (see .env.example)."
        )
    return value

def fetch(url, params):
    import requests

    try:
        return requests.get(url, params=params)
    except requests.RequestException:
        raise SystemExit("Big Book API request failed.") from None

def get_similar_books(query):
    api_key = require_env("BIGBOOK_API_KEY")

    # Search for the book by title or author
    search_url = "https://api.bigbookapi.com/search-books"
    params = {"query": query, "api-key": api_key}
    response = fetch(search_url, params)

    if response.status_code == 200:
        data = response.json()

        if data.get("books"):
            # Get the ID of the top search result
            book_id = data["books"][0][0]["id"]

            # Fetch similar books for the top result
            similar_books_url = f"https://api.bigbookapi.com/{book_id}/similar/"
            params = {"api-key": api_key}
            similar_books_response = fetch(similar_books_url, params)

            if similar_books_response.status_code == 200:
                similar_books_data = similar_books_response.json()

                if similar_books_data.get("similar_books"):
                    print(f"Similar books for '{query}':\n")
                    for book in similar_books_data["similar_books"]:
                        title = book.get("title", "N/A")
                        print(f"{title}")
                        print()
                else:
                    print("No similar books found.")
            else:
                print(f"Error: HTTP {similar_books_response.status_code}")
        else:
            print("No books found for the given query.")
    else:
        print(f"Error: HTTP {response.status_code}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Get similar books for a title or author query.")
    parser.add_argument("query", help="The book title or author to search for.")
    args = parser.parse_args()

    get_similar_books(args.query)