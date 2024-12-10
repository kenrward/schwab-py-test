import os
import schwab

# Retrieve API credentials from environment variables
api_key = os.environ.get("SCHWAB_API_KEY")
app_secret = os.environ.get("SCHWAB_APP_SECRET")

print(api_key)
print(app_secret)

# Check if both environment variables are set
if not api_key or not app_secret:
    raise ValueError(
        "Missing Schwab API credentials. Please set SCHWAB_API_KEY and SCHWAB_APP_SECRET environment variables."
    )

# Initialize the Schwab client
client = schwab.Client.from_login_flow(
    api_key=api_key,
    app_secret=app_secret,
    callback_url="http://127.0.0.1:8080",  # Example callback URL
    token_path="token.json",  # Path to store the token
)

# The client is now authenticated and you can use it to make API calls
accounts = client.get_accounts()
print(accounts)