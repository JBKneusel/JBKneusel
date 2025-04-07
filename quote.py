import requests

# URL for API endpoint
quote_url = "https://api.quotable.io/random"

def fetch_quote():
    try:
        
        response = requests.get(quote_url)

        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            quote = data['content']
            author = data['author']
            
            return f'"{quote}" - {author}'

        else:
            return "Error: Could not fetch a quote."
    
    except Exception as e:
        return f"Error: {str(e)}"
