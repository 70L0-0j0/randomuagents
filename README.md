# RandomUAgents

Library for fetching random user agents based on device type (desktop, mobile, etc.).

## Installation

You can install the library using `pip`:

```bash
pip install RandomUAgents
```

# Usage

## Get random user-agent

```bash
ua_instance = UA()
random_ua = ua_instance._uGet()
print(random_ua)
```
## Get random user-agent for desktop

```bash
ua_instance = UA("desktop")
random_ua = ua_instance._uGet()
print(random_ua)
```
## Get random user-agent for mobile

```bash
ua_instance = UA("mobile")
random_ua = ua_instance._uGet()
print(random_ua)
```