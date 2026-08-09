---
title: TrojanDefenseDiscordBot
description: Discord bot for USC community moderation, organization, and onboarding
---

A bot used for all the USC Discord needs, including moderation, organization,
and onboarding.

## Setup

Install [uv](https://docs.astral.sh/uv/getting-started/installation/) and sync
the locked dependencies:

```bash
uv sync
```

Copy `EXAMPLE.env` to `.env`, then replace the example values with your Discord
application credentials.

## Run

Start the bot in production mode:

```bash
uv run bot.py
```

Pass `--test` to sync commands to the configured test server immediately:

```bash
uv run bot.py --test
```
