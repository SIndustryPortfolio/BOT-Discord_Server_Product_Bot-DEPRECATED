# Discord Administration & Community Bot

A multi-purpose **Discord administration and community management bot** built with Python using :contentReference[oaicite:0]{index=0}.  
Designed to support moderation, server utilities, help-desk automation, vouching systems, and informational embeds.

---

## Overview

This bot is intended for **community or product-based Discord servers** and provides:

- Moderation tools for staff
- Public utility commands for members
- A help desk system with private responses
- Vouching and reputation tracking
- Informational embeds for rules, purchases, donations, and more

The bot relies heavily on **role-based permissions** and **channel-specific behavior**.

---

## Features

### 🛡️ Moderation
- Kick, ban, mute, unmute users
- Message purging
- Server action logging
- Role-based permission checks

### 📋 Public Utilities
- User profile display (`!display`)
- Server vouching system (`!vouch`)
- YouTube / media promotion command
- Embedded information panels

### 🧾 Help Desk System
- Channel-restricted commands
- Auto-DM responses
- Message cleanup to keep help channels tidy

### 🧠 Server Automation
- Welcome messages
- Rules posting
- Purchase & donation information
- Application and shop redirects

---

## Command Prefixes

| Prefix | Purpose |
|------|--------|
| `!` | Public / help desk commands |
| `*` | Staff-only moderation commands |

---

## Commands (Summary)

### Public Commands
- `!display @user` — Display user profile details
- `!youtube` — Show server YouTube channel info
- `!vouch <message>` — Submit a server vouch

### Staff Commands
- `*kick @user`
- `*ban @user`
- `*mute @user`
- `*unmute @user`
- `*purge <amount>`
- `*welcome`
- `*rules`
- `*purchase`
- `*donation`
- `*helpdesk`

### Help Desk (Channel-only)
- `!apply`
- `!shop`
- `!info`

---

## Required Server Setup

### Roles
The bot expects the following roles to exist:
- `Owner`
- `Developer`
- `Administrator`
- `Muted`
- `Buyer`

### Channels
The following channels are referenced by name:
- `〖server-logs〗`
- `〖rules〗`
- `〖how-to-purchase〗`
- `〖donations〗`
- `〖help-desk〗`
- `〖vouches〗`

---

## Configuration

Update the **Settings** section in the script:

```python
token = ""                # Discord bot token (recommended via ENV)
bypassedUsers = ["", ""]  # User IDs immune to moderation
botId = ""                # Bot user ID
footer = "Admin Bot"
footerImage = "<IMAGE URL>"
youtubeChannelImage = ""
