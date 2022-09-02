# auto-squid-game

**Outdated, for V1 only**   
auto-squid-game will detect the Squid Energy (SE) of the Players you owned, and enter a game automatically.

## Getting Started

### Prerequisites

-   [Python 3.6+](https://www.python.org/downloads/)

### Installation

To run auto-squid-game, you need to install libraries inside `requirements.txt`.

```
pip install -r requirements.txt
```

### Configuration

Open `config.json` and **fill in the MetaMask address only**.  
(The script will prompt you to enter a password to encrypt the private key.)

```
{
    "walletAddress": "0x0F60be...",
    "walletPrivateKey": ""
}
```

### Usage

Run auto-squid-game by running the below command in terminal.

```
python main.py
```
