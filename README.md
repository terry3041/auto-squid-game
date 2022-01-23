# auto-squid-game

自動烤魷魚腳本會偵測所有持有合約的玩家的魷魚能量，並自動進行遊戲。

## 開始使用

### 環境需求

-   [Python 3.6+](https://www.python.org/downloads/)

### 安裝方式

若要執行 auto-squid-game，需要安裝額外的套件，使用終端機至此專案的資料夾中執行此指令：

```
pip install -r requirements.txt
```

### 設定

用任意的文字編輯器開啟 `config.json`，在

```
{
    "walletAddress": "",
    "walletPrivateKey": ""
}
```

**只填入 MetaMask 錢包的地址**，如下：  
(腳本會在首次運行時提示你創建密碼以加密私鑰)

```
{
    "walletAddress": "0x0F60be...",
    "walletPrivateKey": ""
}
```

### 使用方式

使用終端機至專案資料夾執行此指令：

```
python main.py
```

## 抖內 へ(´д ｀へ)

### 小弟的錢包

`0x96D99BB2bC9694310Dbc2ae63253a23E75C275eE`
