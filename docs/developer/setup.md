---
title: Developer Setup
description: Set up and run TrojanDefenseDiscordBot with uv
---

## Supported Shells

The root `bot` script works in Git Bash, WSL on Windows, Linux, and macOS.

## Install Dependencies

Install [uv](https://docs.astral.sh/uv/getting-started/installation/) and sync
the locked dependencies:

```bash
./bot --setup
```

## Configure the Environment

Copy `EXAMPLE.env` to `.env`, then replace the example values with your Discord
application credentials.

## Run the Bot

Start the bot in production mode:

```bash
./bot --run
```

Pass `--test` to sync commands to the configured test server immediately:

```bash
./bot --run --test
```

The dispatcher is intentionally invoked as `./bot`; it does not install a global
`bot` command or shell alias.

## Reset Generated State

To remove only the generated local database state, run:

```bash
./bot --reset
```

The command asks for confirmation and preserves configuration, source files,
dependencies, hooks, and documentation.
