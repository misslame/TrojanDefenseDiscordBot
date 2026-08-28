import argparse


def parse_arguments():
    """Defines and parses command-line choices."""
    parser = argparse.ArgumentParser(description="Run the Discord Bot.")

    parser.add_argument(
        "--test",
        action="store_true",
        help="Run bot in local test mode (instant guild-specific sync)",
    )
    parser.add_argument(
        "--env",
        type=str,
        default="dev",
        choices=["dev", "staging", "prod"],
        help="Target environment (default: dev)",
    )
    parser.add_argument(
        "--count",
        type=int,
        default=0,
        help="Custom initialization counter/limit (default: 0)",
    )

    return parser.parse_args()
