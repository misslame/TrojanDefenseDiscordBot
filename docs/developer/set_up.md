---
title: Developer Setup
description: Set up and run TrojanDefenseDiscordBot with uv
---

## Install Dependencies

Install [uv](https://docs.astral.sh/uv/getting-started/installation/) and sync
the locked dependencies:

```bash
uv sync
```

## Configure the Environment

Copy `EXAMPLE.env` to `.env`, then replace the example values with your Discord
application credentials.

## Run the Bot

Start the bot in production mode:

```bash
uv run bot.py
```

Pass `--test` to sync commands to the configured test server immediately:

```bash
uv run bot.py --test
```
