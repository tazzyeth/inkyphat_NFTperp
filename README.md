# Inkyphat_NFTperp

![miladyeyespng](https://user-images.githubusercontent.com/132207345/235407693-9b1fa04c-4c45-4d5e-9f5b-19203c51fdcb.png)

Inkyphat_NFTperp is a Python script that fetches cryptocurrency data from the nftperp.xyz API and displays it on an InkyPHAT black display hat for Raspberry Pi. The script displays the mark price and index price for Milady and a specific wallet's Profit and Loss percentage. You can add more API calls from nftperp from [here](https://nftperp.readme.io/reference/mark-price).


## Pre-requisites 👌

- Raspberry Pi with InkyPHAT Black display hat
- Python 3.x
- Inky library
- Pillow library
- Requests library

If you haven't installed these libraries, you can install them by running the following commands

```
sudo apt-get install python3-pip
sudo pip3 install inky Pillow requests
```

## Installation 🛸

1. Clone this repository:

```
git clone https://github.com/<username>/Inkyphat_NFTperp.git
```

2. Navigate to the cloned repository:

```
cd inkyphat-nftperp
```

3. Change the wallet address to the wallet you would like to see the PnL of (or watch mine):

![image](https://user-images.githubusercontent.com/132207345/235553130-11b43125-7141-4b74-a278-89c0fb0785a7.png)

4. Run the script makling sure you are in the right directory:

```
python3 perpmilady.py
```

5. Setup Cron to run the script every x minutes:

```
crontab -e
```

6. Add the following line to your crontab file, replacing "x" with the number of minutes you want to wait between updates.
You will need to also input the working directory of the scrip and the username:

```
* * * * * cd <enter-working-directory> && /usr/bin/python3.9 perpmilady2.py >> /home/<enter-username>/cron.log 2>&1

```
To get the crontask to work you need to make sure all the directory information is correct. 
the last part of the code will create a log for you to troubleshoot whats happening on your main directory.

This is what it should look like once run:

![image](https://user-images.githubusercontent.com/132207345/235553724-c737a48e-8584-4946-af67-7fa53b0fde66.png)

## Related links

- [Inky](https://github.com/pimoroni/inky)
- [Pillow](https://github.com/python-pillow/Pillow)
- [Requests](https://github.com/psf/requests)
- [nftperp API](https://nftperp.readme.io/reference/mark-price)
