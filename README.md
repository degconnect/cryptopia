# cryptopia
Python API for Cryptopia(https://www.cryptopia.co.nz/)

##### Not ready for python 3.4 yet

#### Basic Public Setup (no API Key/Secret):
```python
from cryptopia import Cryptopia

crypto = Cryptopia()

currencies, err = crypto.get_currencies()
if err is None:
    for coin in currencies: 
        print(coin)

```

#### Basic Private Setup(with API Key/Secret)

````python
import os

from cryptopia import Cryptopia

CRYPTOPIA_API_KEY = os.environ.get('CRYPTOPIA_API_KEY')
CRYPTOPIA_API_SECRET = os.environ.get('CRYPTOPIA_API_SECRET')

crypto = Cryptopia(CRYPTOPIA_API_KEY, CRYPTOPIA_API_SECRET)

deposits, err = crypto.get_transactions('Deposit')
data, _ = deposits
for item in data:
    print(item)
    
````
