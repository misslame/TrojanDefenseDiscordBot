from dotenv import dotenv_values

# Define the mandatory tokens you need
REQUIRED_TOKENS = ["DISCORD_BOT_TOKEN"]

# Load the .env file into a dictionary map
_env_map = dotenv_values(".env")

# Validate on initialization so the script fails immediately upon import
_missing_tokens = [
    token for token in REQUIRED_TOKENS if token not in _env_map or not _env_map[token]
]

if _missing_tokens:
    raise KeyError(
        f"Configuration error: Missing or empty required tokens in .env file: {', '.join(_missing_tokens)}"
    )


def get_env_variable(key: str) -> str:
    """Retrieve an environment variable value from the map by its key name."""
    if key not in _env_map:
        raise KeyError(
            f"The environment variable token '{key}' does not exist on environment variables map."
        )
    return _env_map[key]
