import argparse
import requests

API_KEY = "869610e1a4b3492a843fc2e77c043b48"  # Replace with your API key

def get_similar_books(query):
    # Search for the book by title or author
    search_url = "https://api.bigbookapi.com/search-books"
    params = {"query": query, "api-key": API_KEY}
    response = requests.get(search_url, params=params)

    if response.status_code == 200:
        data = response.json()

        if data.get("books"):
            # Get the ID of the top search result
            book_id = data["books"][0][0]["id"]

            # Fetch similar books for the top result
            similar_books_url = f"https://api.bigbookapi.com/{book_id}/similar/?api-key=869610e1a4b3492a843fc2e77c043b48"
            params = {"api-key": API_KEY}
            similar_books_response = requests.get(similar_books_url, params=params)

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
                print(f"Error: {similar_books_response.status_code} - {similar_books_response.text}")
        else:
            print("No books found for the given query.")
    else:
        print(f"Error: {response.status_code} - {response.text}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Get similar books for a title or author query.")
    parser.add_argument("query", help="The book title or author to search for.")
    args = parser.parse_args()

    get_similar_books(args.query)