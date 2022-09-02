from datetime import datetime
from web3 import Web3
import cryptocode
import pwinput
import pathlib
import json
import time
import sys

workingPath = pathlib.Path(__file__).parent.absolute()
with open(f'{workingPath}/config.json') as f:
    config = json.load(f)

walletAddress = config['walletAddress']
walletPrivateKey = config['walletPrivateKey']

bscNode = 'https://bsc-dataseed.binance.org/'
bswAddress = '0xCCc78DF56470b70cb901FCc324A8fBbE8Ab5304B'
bspAddress = '0xb00ed7e3671af2675c551a1c26ffdcc5b425359b'


web3 = Web3(Web3.HTTPProvider(bscNode))
walletAddress = web3.toChecksumAddress(walletAddress)
bswAddress = web3.toChecksumAddress(bswAddress)
bspAddress = web3.toChecksumAddress(bspAddress)
bswABI = '[{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"gameIndex","type":"uint256"}],"name":"GameAdded","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"gameIndex","type":"uint256"}],"name":"GameDisable","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"gameIndex","type":"uint256"}],"name":"GameEnable","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"user","type":"address"},{"indexed":true,"internalType":"uint256","name":"gameIndex","type":"uint256"},{"indexed":false,"internalType":"bool","name":"userWin","type":"bool"},{"indexed":false,"internalType":"address[]","name":"rewardTokens","type":"address[]"},{"indexed":false,"internalType":"uint128[]","name":"rewardAmount","type":"uint128[]"}],"name":"GamePlay","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"gameIndex","type":"uint256"}],"name":"GameSetNewGameParam","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"account","type":"address"}],"name":"Paused","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"gameIndex","type":"uint256"}],"name":"RewardTokenChanged","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"bytes32","name":"previousAdminRole","type":"bytes32"},{"indexed":true,"internalType":"bytes32","name":"newAdminRole","type":"bytes32"}],"name":"RoleAdminChanged","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":true,"internalType":"address","name":"sender","type":"address"}],"name":"RoleGranted","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":true,"internalType":"address","name":"sender","type":"address"}],"name":"RoleRevoked","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"account","type":"address"}],"name":"Unpaused","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"user","type":"address"},{"components":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint128","name":"rewardInUSD","type":"uint128"},{"internalType":"uint128","name":"rewardInToken","type":"uint128"}],"indexed":false,"internalType":"struct MainSquidGame.RewardToken[]","name":"_rewardBalance","type":"tuple[]"}],"name":"Withdrew","type":"event"},{"inputs":[],"name":"DEFAULT_ADMIN_ROLE","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[{"components":[{"internalType":"uint128","name":"minSeAmount","type":"uint128"},{"internalType":"uint128","name":"minStakeAmount","type":"uint128"},{"internalType":"uint256","name":"chanceToWin","type":"uint256"},{"components":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint128","name":"rewardInUSD","type":"uint128"},{"internalType":"uint128","name":"rewardInToken","type":"uint128"}],"internalType":"struct MainSquidGame.RewardToken[]","name":"rewardTokens","type":"tuple[]"},{"internalType":"string","name":"name","type":"string"},{"internalType":"bool","name":"enable","type":"bool"}],"internalType":"struct MainSquidGame.Game","name":"_game","type":"tuple"}],"name":"addNewGame","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"components":[{"internalType":"uint32","name":"duration","type":"uint32"},{"internalType":"uint128","name":"priceInUSD","type":"uint128"},{"internalType":"bool","name":"enable","type":"bool"}],"internalType":"struct MainSquidGame.PlayerContract","name":"_playerContract","type":"tuple"}],"name":"addPlayerContract","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"autoBsw","outputs":[{"internalType":"contract IautoBsw","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"bswToken","outputs":[{"internalType":"contract IERC20Upgradeable","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"busNFT","outputs":[{"internalType":"contract ISquidBusNFT","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256[]","name":"_tokensId","type":"uint256[]"},{"internalType":"uint256","name":"_contractIndex","type":"uint256"}],"name":"buyContracts","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_user","type":"address"}],"name":"checkGameRequirements","outputs":[{"internalType":"bool","name":"busAndPlayersAmount","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"decreaseWithdrawalFeeByDay","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_gameIndex","type":"uint256"}],"name":"disableGame","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_gameIndex","type":"uint256"}],"name":"enableGame","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"firstGameCountdownSE","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"games","outputs":[{"internalType":"uint128","name":"minSeAmount","type":"uint128"},{"internalType":"uint128","name":"minStakeAmount","type":"uint128"},{"internalType":"uint256","name":"chanceToWin","type":"uint256"},{"internalType":"string","name":"name","type":"string"},{"internalType":"bool","name":"enable","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getGameCount","outputs":[{"internalType":"uint256","name":"count","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_user","type":"address"}],"name":"getGameInfo","outputs":[{"components":[{"internalType":"uint256","name":"index","type":"uint256"},{"components":[{"internalType":"uint128","name":"minSeAmount","type":"uint128"},{"internalType":"uint128","name":"minStakeAmount","type":"uint128"},{"internalType":"uint256","name":"chanceToWin","type":"uint256"},{"components":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint128","name":"rewardInUSD","type":"uint128"},{"internalType":"uint128","name":"rewardInToken","type":"uint128"}],"internalType":"struct MainSquidGame.RewardToken[]","name":"rewardTokens","type":"tuple[]"},{"internalType":"string","name":"name","type":"string"},{"internalType":"bool","name":"enable","type":"bool"}],"internalType":"struct MainSquidGame.Game","name":"game","type":"tuple"},{"internalType":"bool","name":"playerAndBusAmount","type":"bool"},{"internalType":"bool","name":"bswStake","type":"bool"},{"internalType":"bool","name":"seAmount","type":"bool"}],"internalType":"struct MainSquidGame.GameInfo[]","name":"","type":"tuple[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"}],"name":"getRoleAdmin","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_user","type":"address"}],"name":"getUserRewardBalances","outputs":[{"internalType":"address[]","name":"","type":"address[]"},{"internalType":"uint128[]","name":"","type":"uint128[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"grantRole","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"hasRole","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"contract IERC20Upgradeable","name":"_usdtToken","type":"address"},{"internalType":"contract IERC20Upgradeable","name":"_bswToken","type":"address"},{"internalType":"contract ISquidBusNFT","name":"_busNFT","type":"address"},{"internalType":"contract ISquidPlayerNFT","name":"_playerNFT","type":"address"},{"internalType":"contract IOracle","name":"_oracle","type":"address"},{"internalType":"contract IMasterChef","name":"_masterChef","type":"address"},{"internalType":"contract IautoBsw","name":"_autoBsw","type":"address"},{"internalType":"address","name":"_treasuryAddress","type":"address"},{"internalType":"uint256","name":"_recoveryTime","type":"uint256"}],"name":"initialize","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"masterChef","outputs":[{"internalType":"contract IMasterChef","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"oracle","outputs":[{"internalType":"contract IOracle","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"pause","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"paused","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_gameIndex","type":"uint256"},{"internalType":"uint256[]","name":"_playersId","type":"uint256[]"}],"name":"playGame","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_pcIndex","type":"uint256"},{"internalType":"uint128","name":"newPrice","type":"uint128"},{"internalType":"bool","name":"_state","type":"bool"}],"name":"playerContractState","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"playerContracts","outputs":[{"internalType":"uint32","name":"duration","type":"uint32"},{"internalType":"uint128","name":"priceInUSD","type":"uint128"},{"internalType":"bool","name":"enable","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"playerNFT","outputs":[{"internalType":"contract ISquidPlayerNFT","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"recoveryTime","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"renounceRole","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"revokeRole","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_gameIndex","type":"uint256"},{"internalType":"uint128","name":"_minSeAmount","type":"uint128"},{"internalType":"uint128","name":"_minStakeAmount","type":"uint128"},{"internalType":"uint256","name":"_chanceToWin","type":"uint256"}],"name":"setGameParameters","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_newRecoveryTime","type":"uint256"}],"name":"setRecoveryTime","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_gameIndex","type":"uint256"},{"components":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint128","name":"rewardInUSD","type":"uint128"},{"internalType":"uint128","name":"rewardInToken","type":"uint128"}],"internalType":"struct MainSquidGame.RewardToken[]","name":"_rewardTokens","type":"tuple[]"}],"name":"setRewardTokensToGame","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_treasuryAddress","type":"address"}],"name":"setTreasuryAddress","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_decreaseWithdrawalFeeByDay","type":"uint256"},{"internalType":"uint256","name":"_withdrawalFee","type":"uint256"}],"name":"setWithdrawalFee","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes4","name":"interfaceId","type":"bytes4"}],"name":"supportsInterface","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"treasuryAddress","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"unpause","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"usdtToken","outputs":[{"internalType":"contract IERC20Upgradeable","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_user","type":"address"}],"name":"userInfo","outputs":[{"components":[{"internalType":"uint256","name":"busBalance","type":"uint256"},{"internalType":"uint256","name":"allowedBusBalance","type":"uint256"},{"internalType":"uint256","name":"secToNextBus","type":"uint256"},{"internalType":"uint256","name":"playerBalance","type":"uint256"},{"internalType":"uint256","name":"allowedSeatsInBuses","type":"uint256"},{"internalType":"uint256","name":"availableSEAmount","type":"uint256"},{"internalType":"uint256","name":"totalSEAmount","type":"uint256"},{"internalType":"uint256","name":"stakedAmount","type":"uint256"},{"internalType":"uint256","name":"bswBalance","type":"uint256"},{"components":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint128","name":"rewardInUSD","type":"uint128"},{"internalType":"uint128","name":"rewardInToken","type":"uint128"}],"internalType":"struct MainSquidGame.RewardToken[]","name":"rewardBalance","type":"tuple[]"},{"internalType":"uint256","name":"currentFee","type":"uint256"}],"internalType":"struct MainSquidGame.UserInfo","name":"","type":"tuple"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"withdrawReward","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"withdrawTimeLock","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"withdrawalFee","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"}]'
bspABI = '[{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"approved","type":"address"},{"indexed":true,"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"operator","type":"address"},{"indexed":false,"internalType":"bool","name":"approved","type":"bool"}],"name":"ApprovalForAll","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"bool","name":"state","type":"bool"},{"indexed":false,"internalType":"uint256","name":"seDivide","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"gracePeriod","type":"uint256"}],"name":"ChangeSEDivideState","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"string","name":"baseURI","type":"string"}],"name":"Initialize","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256[]","name":"_tokenId","type":"uint256[]"},{"indexed":false,"internalType":"uint32","name":"contractEndTimestamp","type":"uint32"}],"name":"NewContract","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"bytes32","name":"previousAdminRole","type":"bytes32"},{"indexed":true,"internalType":"bytes32","name":"newAdminRole","type":"bytes32"}],"name":"RoleAdminChanged","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":true,"internalType":"address","name":"sender","type":"address"}],"name":"RoleGranted","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":true,"internalType":"address","name":"sender","type":"address"}],"name":"RoleRevoked","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256[]","name":"_tokenId","type":"uint256[]"},{"indexed":false,"internalType":"uint128[]","name":"addition","type":"uint128[]"}],"name":"SEIncrease","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":true,"internalType":"uint256","name":"tokenId","type":"uint256"},{"indexed":false,"internalType":"uint8","name":"rarity","type":"uint8"},{"indexed":false,"internalType":"uint128","name":"squidEnergy","type":"uint128"}],"name":"TokenMint","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256[]","name":"_tokenId","type":"uint256[]"},{"indexed":false,"internalType":"uint32","name":"busyTo","type":"uint32"},{"indexed":false,"internalType":"uint128[]","name":"decreaseSE","type":"uint128[]"}],"name":"TokensLock","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":true,"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"Transfer","type":"event"},{"inputs":[],"name":"DEFAULT_ADMIN_ROLE","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"GAME_ROLE","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"SE_BOOST_ROLE","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"TOKEN_FREEZER","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"TOKEN_MINTER_ROLE","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"approve","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_user","type":"address"},{"internalType":"uint256","name":"_from","type":"uint256"},{"internalType":"uint256","name":"_to","type":"uint256"}],"name":"arrayUserPlayers","outputs":[{"components":[{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"uint8","name":"rarity","type":"uint8"},{"internalType":"address","name":"tokenOwner","type":"address"},{"internalType":"uint128","name":"squidEnergy","type":"uint128"},{"internalType":"uint128","name":"maxSquidEnergy","type":"uint128"},{"internalType":"uint32","name":"contractEndTimestamp","type":"uint32"},{"internalType":"uint32","name":"busyTo","type":"uint32"},{"internalType":"uint32","name":"createTimestamp","type":"uint32"},{"internalType":"bool","name":"stakeFreeze","type":"bool"},{"internalType":"string","name":"uri","type":"string"}],"internalType":"struct SquidPlayerNFT.TokensViewFront[]","name":"","type":"tuple[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_user","type":"address"}],"name":"arrayUserPlayers","outputs":[{"components":[{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"uint8","name":"rarity","type":"uint8"},{"internalType":"address","name":"tokenOwner","type":"address"},{"internalType":"uint128","name":"squidEnergy","type":"uint128"},{"internalType":"uint128","name":"maxSquidEnergy","type":"uint128"},{"internalType":"uint32","name":"contractEndTimestamp","type":"uint32"},{"internalType":"uint32","name":"busyTo","type":"uint32"},{"internalType":"uint32","name":"createTimestamp","type":"uint32"},{"internalType":"bool","name":"stakeFreeze","type":"bool"},{"internalType":"string","name":"uri","type":"string"}],"internalType":"struct SquidPlayerNFT.TokensViewFront[]","name":"","type":"tuple[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_user","type":"address"},{"internalType":"uint256","name":"_from","type":"uint256"},{"internalType":"uint256","name":"_to","type":"uint256"}],"name":"arrayUserPlayersWithValidContracts","outputs":[{"components":[{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"uint8","name":"rarity","type":"uint8"},{"internalType":"address","name":"tokenOwner","type":"address"},{"internalType":"uint128","name":"squidEnergy","type":"uint128"},{"internalType":"uint128","name":"maxSquidEnergy","type":"uint128"},{"internalType":"uint32","name":"contractEndTimestamp","type":"uint32"},{"internalType":"uint32","name":"busyTo","type":"uint32"},{"internalType":"uint32","name":"createTimestamp","type":"uint32"},{"internalType":"bool","name":"stakeFreeze","type":"bool"},{"internalType":"string","name":"uri","type":"string"}],"internalType":"struct SquidPlayerNFT.TokensViewFront[]","name":"","type":"tuple[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_user","type":"address"}],"name":"arrayUserPlayersWithValidContracts","outputs":[{"components":[{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"uint8","name":"rarity","type":"uint8"},{"internalType":"address","name":"tokenOwner","type":"address"},{"internalType":"uint128","name":"squidEnergy","type":"uint128"},{"internalType":"uint128","name":"maxSquidEnergy","type":"uint128"},{"internalType":"uint32","name":"contractEndTimestamp","type":"uint32"},{"internalType":"uint32","name":"busyTo","type":"uint32"},{"internalType":"uint32","name":"createTimestamp","type":"uint32"},{"internalType":"bool","name":"stakeFreeze","type":"bool"},{"internalType":"string","name":"uri","type":"string"}],"internalType":"struct SquidPlayerNFT.TokensViewFront[]","name":"","type":"tuple[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_user","type":"address"}],"name":"availableSEAmount","outputs":[{"internalType":"uint128","name":"amount","type":"uint128"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_tokenId","type":"uint256"}],"name":"burn","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"enableSeDivide","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"getApproved","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"}],"name":"getRoleAdmin","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_tokenId","type":"uint256"}],"name":"getToken","outputs":[{"components":[{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"uint8","name":"rarity","type":"uint8"},{"internalType":"address","name":"tokenOwner","type":"address"},{"internalType":"uint128","name":"squidEnergy","type":"uint128"},{"internalType":"uint128","name":"maxSquidEnergy","type":"uint128"},{"internalType":"uint32","name":"contractEndTimestamp","type":"uint32"},{"internalType":"uint32","name":"busyTo","type":"uint32"},{"internalType":"uint32","name":"createTimestamp","type":"uint32"},{"internalType":"bool","name":"stakeFreeze","type":"bool"},{"internalType":"string","name":"uri","type":"string"}],"internalType":"struct SquidPlayerNFT.TokensViewFront","name":"","type":"tuple"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"gracePeriod","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"grantRole","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"hasRole","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"baseURI","type":"string"},{"internalType":"uint128","name":"_seDivide","type":"uint128"},{"internalType":"uint256","name":"_gracePeriod","type":"uint256"},{"internalType":"bool","name":"_enableSeDivide","type":"bool"}],"name":"initialize","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"operator","type":"address"}],"name":"isApprovedForAll","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256[]","name":"tokenId","type":"uint256[]"},{"internalType":"uint32","name":"busyTo","type":"uint32"},{"internalType":"bool","name":"willDecrease","type":"bool"},{"internalType":"address","name":"user","type":"address"}],"name":"lockTokens","outputs":[{"internalType":"uint128","name":"","type":"uint128"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint128","name":"squidEnergy","type":"uint128"},{"internalType":"uint32","name":"contractEndTimestamp","type":"uint32"},{"internalType":"uint8","name":"rarity","type":"uint8"}],"name":"mint","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"ownerOf","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"renounceRole","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"revokeRole","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"safeTransferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"bytes","name":"_data","type":"bytes"}],"name":"safeTransferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"seDivide","outputs":[{"internalType":"uint128","name":"","type":"uint128"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"operator","type":"address"},{"internalType":"bool","name":"approved","type":"bool"}],"name":"setApprovalForAll","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"newBaseUri","type":"string"}],"name":"setBaseURI","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256[]","name":"tokenId","type":"uint256[]"},{"internalType":"uint32","name":"contractEndTimestamp","type":"uint32"},{"internalType":"address","name":"user","type":"address"}],"name":"setPlayerContract","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint128[5]","name":"newRarityLimits","type":"uint128[5]"}],"name":"setRarityLimitsTable","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bool","name":"_enableSeDivide","type":"bool"},{"internalType":"uint128","name":"_seDivide","type":"uint128"},{"internalType":"uint256","name":"_gracePeriod","type":"uint256"}],"name":"setSeDivide","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256[]","name":"tokenId","type":"uint256[]"},{"internalType":"uint128[]","name":"deduction","type":"uint128[]"},{"internalType":"address","name":"user","type":"address"}],"name":"squidEnergyDecrease","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256[]","name":"tokenId","type":"uint256[]"},{"internalType":"uint128[]","name":"addition","type":"uint128[]"},{"internalType":"address","name":"user","type":"address"}],"name":"squidEnergyIncrease","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes4","name":"interfaceId","type":"bytes4"}],"name":"supportsInterface","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"index","type":"uint256"}],"name":"tokenByIndex","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_tokenId","type":"uint256"}],"name":"tokenFreeze","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"uint256","name":"index","type":"uint256"}],"name":"tokenOfOwnerByIndex","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"tokenURI","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_tokenId","type":"uint256"}],"name":"tokenUnfreeze","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_user","type":"address"}],"name":"totalSEAmount","outputs":[{"internalType":"uint128","name":"amount","type":"uint128"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"transferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"}]'
bswContract = web3.eth.contract(address=bswAddress, abi=bswABI)
bspContract = web3.eth.contract(address=bspAddress, abi=bspABI)


def estimateGas(tx):
    gas = web3.eth.estimateGas(
        {
            'from': tx['from'],
            'to': tx['to'],
            'value': tx['value'],
            'data': tx['data'],
        }
    )
    gas = gas + (gas / 10)
    estimateGasInBNB = Web3.fromWei(gas * web3.eth.gas_price, 'ether')
    print(f'Estimated gas fee: {estimateGasInBNB:.8f} BNB')
    return gas


def getPlayerData(walletAddress):
    rawPlayerData = bspContract.functions.arrayUserPlayersWithValidContracts(
        walletAddress
    ).call()
    if len(rawPlayerData) == 0:
        print('Unable to find avaliable player.')
        sys.exit()
    playerIdList = [i[0] for i in rawPlayerData]
    cdTimestamp = max([i[6] for i in rawPlayerData])
    return playerIdList, cdTimestamp


def getRewardBalance(walletAddress):
    rewardBalance = bswContract.functions.getUserRewardBalances(walletAddress).call()
    return rewardBalance[1][0], rewardBalance[1][1]


def pickGame(walletAddress):
    gameInfoList = bswContract.functions.getGameInfo(walletAddress).call()
    for i in reversed(gameInfoList):
        if i[1][-1]:
            if i[-1] and i[-2] and i[-3]:
                return i[0]
    else:
        print('Unable to find avaliable game.')
        sys.exit()


def playGame(gameIndex, playerId):
    proposedTx = bswContract.functions.playGame(gameIndex, playerId).buildTransaction(
        {
            'from': walletAddress,
            'gasPrice': web3.eth.gas_price,
            'nonce': web3.eth.getTransactionCount(walletAddress),
        }
    )
    proposedTx.update({'gas': int(estimateGas(proposedTx))})
    signedTx = web3.eth.account.signTransaction(proposedTx, walletPrivateKey)
    tx = web3.eth.sendRawTransaction(signedTx.rawTransaction)
    txHash = web3.toHex(tx)

    print(f'Transaction ID: {txHash}')
    print('Waiting for confirmation...')
    txReceipt = web3.eth.waitForTransactionReceipt(txHash, 60)
    return txReceipt


def bswLoop():
    walletBalance = web3.fromWei(web3.eth.get_balance(walletAddress), 'ether')
    print(f'Wallet balance: {walletBalance:.4f} BNB')

    rewardBalance = getRewardBalance(walletAddress)
    bswBalance = web3.fromWei(rewardBalance[0], 'ether')
    bnbBalance = web3.fromWei(rewardBalance[1], 'ether')
    print(f'Reward balance: {bswBalance:.4f} BSW, {bnbBalance:.4f} BNB')

    playerIdList, cdTimestamp = getPlayerData(walletAddress)
    cdStr = datetime.fromtimestamp(cdTimestamp)
    print(f'Cooldown: {cdStr}')

    while True:
        currentTimestamp = int(time.time())

        if currentTimestamp > (cdTimestamp + 2 * 60):
            print('Cooldown expired. Trying to play a game...')
            gameIndex = pickGame(walletAddress)
            txReceipt = playGame(gameIndex, playerIdList)
            if not txReceipt['status']:
                print('Transaction failed.')
                sys.exit()

            txLog = txReceipt['logs'][-1]['data']
            bswReward = web3.fromWei(web3.toInt(hexstr=txLog[-128:-64]), 'ether')
            bnbReward = web3.fromWei(web3.toInt(hexstr=txLog[-64:]), 'ether')

            if max(bnbReward, bswReward) > 0:
                print(f'You won {bswReward:.4f} BSW, {bnbReward:.4f} BNB.')
            else:
                print('You did not win anything.')

            break

        time.sleep(60)


def createPassphrase():
    passphrase = pwinput.pwinput(prompt='Password: ')
    confirmPassphrase = pwinput.pwinput(prompt='Confirm password: ')
    if passphrase != confirmPassphrase:
        print('Passwords do not match. Please try again.')
        return createPassphrase()
    else:
        return passphrase


def decryptPrivateKey():
    passphrase = pwinput.pwinput(prompt='Please enter your password: ')
    privateKey = cryptocode.decrypt(walletPrivateKey, passphrase)
    if not privateKey:
        print('Passwords do not match. Please try again.')
        return decryptPrivateKey()
    else:
        return privateKey


if __name__ == '__main__':
    print(f'Now using wallet: {walletAddress}')

    if walletPrivateKey == '':
        walletPrivateKey = pwinput.pwinput(prompt='Please enter your private key: ')
        print('Please enter a password to encrypt your private key.')
        passphrase = createPassphrase()
        encryptedPrivateKey = cryptocode.encrypt(walletPrivateKey, passphrase)
        config['walletPrivateKey'] = encryptedPrivateKey
        with open(f'{workingPath}/config.json', 'w') as f:
            json.dump(config, f, indent=4)
    else:
        walletPrivateKey = decryptPrivateKey()

    while True:
        bswLoop()
        time.sleep(60)
