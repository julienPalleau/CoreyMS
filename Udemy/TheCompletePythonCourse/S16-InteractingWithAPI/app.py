import time
from libs.openexchange import OpenExchangeClient

APP_ID = "6662dedac36347a8bbcd614b5221ddc4"

client = OpenExchangeClient(APP_ID)

eur_amount = 1000
start = time.time()
gbp_amount = client.convert(eur_amount, "EUR", "GBP")
end = time.time()

print(end - start)
print(f"EUR{eur_amount} is GBP{gbp_amount:.2f}")
