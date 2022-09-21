from brownie import accounts, config, network, interface, FlashLoanReceiver, SimpleFlashLoanReceiver
from scripts.helper_functions import get_address_provider, get_token, get_account


tx_url = "https://goerli-optimism.etherscan.io/tx/{}"

pool = interface.IPool(get_address_provider().getPool())

flashloan_receiver = FlashLoanReceiver[len(FlashLoanReceiver) -1]

dai = get_token("DAI")
usdc = get_token("USDC")
usdt = get_token("USDT")
susd = get_token("SUSD")
weth = get_token("WETH")
wbtc = get_token("WBTC")
aave = get_token("AAVE")
link = get_token("LINK")

dai_amount = 10000 * 10** dai.decimals()
usdc_amount = 10000 * 10** usdc.decimals()
usdt_amount = 10000 * 10** usdt.decimals()
susd_amount = 10000 * 10** susd.decimals() 
weth_amount = 100 * 10** weth.decimals()
wbtc_amount = 10 * 10** wbtc.decimals()
aave_amount = 1000 * 10** aave.decimals()
link_amount = 10000 * 10** link.decimals()

def flip_a_loan():
    acct = get_account()
    receiver = flashloan_receiver
    assets = [dai, usdc, usdt, susd, weth, wbtc, aave, link]
    amounts = [dai_amount, usdc_amount, usdt_amount, susd_amount, weth_amount, wbtc_amount, aave_amount, link_amount]
    interest = [0, 0, 0, 0, 0, 0, 0, 0]
    behalf_of = receiver
    params = receiver.address
    referral = 0
    tx = pool.flashLoan(receiver, assets, amounts, interest, behalf_of, params, referral, {"from": acct})
    tx.wait(3)
    # print(f"Congrats! You have flipped a flashloan. Check it out! {tx_url.format(tx.txid)}")
    return tx.events

def main():
    flip_a_loan()