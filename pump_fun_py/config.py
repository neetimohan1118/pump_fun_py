from solana.rpc.api import Client
from solders.keypair import Keypair #type: ignore

PUB_KEY = "EpbLWya1NpeCp7TWz5ojwdHvFsSJ7922xBmxYMaFuwpC" # WALLET ADDRESS
PRIV_KEY = "6xR1qMya4oRFc72wXrFje4tJYgLv37aGJjqEkUdVKXg2AN8jrjbjWAj217YxX7KtSDgAvCoUsirA3MHBnsBchrQ" # BASE58 STRING FORMAT
RPC = "https://mainnet.helius-rpc.com/?api-key=1c21a13b-a496-44f7-b50e-45548d735241" # Use Helius or Quicknode for better performance
client = Client(RPC)
payer_keypair = Keypair.from_base58_string(PRIV_KEY)
