def breakpoint(gas_price_gwei, gas_limit=21000):
    gas_fee_eth = (gas_price_gwei * gas_limit) / 1_000_000_000
    return round(gas_fee_eth + 0.00001, 8)  # +Puffer

print("Minimaler Sendebetrag für symbolischen Zuwachs:", breakpoint(2.7), "ETH")