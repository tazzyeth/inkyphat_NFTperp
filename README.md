
![miladyeyespng](https://user-images.githubusercontent.com/132207345/235407693-9b1fa04c-4c45-4d5e-9f5b-19203c51fdcb.png)

Inkyphat_NFTperp is a Python script that fetches cryptocurrency data from the nftperp.xyz API and displays it on an InkyPHAT black display hat for Raspberry Pi. The script displays the mark price, the index price and a specific wallets Profit and loss percentage. You can add in more api calls from nftperp from here https://nftperp.readme.io/reference/mark-price.

👌 Pre-requisites

Raspberry Pi with InkyPHAT Black display hat

Python 3.x

Inky library

Pillow library

Requests library

🛸 Installation

1. Clone this repository

2. Install required libraries

3. Change the wallet address to the wallet you would like to see the PnL of (or watch mine)

4. Run the script: python3 perpmilady.py

5. Setup Cron to run the script every x minutes


This is what it should look like once run

![inkyphat-nftperp](https://user-images.githubusercontent.com/132207345/235453339-c0715fca-eee4-4ae8-a766-86c77977cd90.jpg)
