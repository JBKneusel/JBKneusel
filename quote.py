import requests

# URL for API endpoint
quote_url = "https://api.quotable.io/random"

def fetch_quote():
    try:
        # Send a GET request to the API
        response = requests.get(quote_url)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            quote = data['content']
            author = data['author']

            # Return the quote and author
            return f'"{quote}" - {author}'

        else:
            # Handle errors (non-200 response)
            return "Error: Could not fetch a quote."
    
    except Exception as e:
        return f"Error: {str(e)}"