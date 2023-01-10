# PiNet: My Home Automation Solution.

## No Cloud. No Data-sharing. Simple browser interface.

Why describe my home control network here?  Well, it's complicated.  Bottom line, if I did it, you can do it.  And you might want to.  So here's how it started, and here's what I did.

There are a bunch of Home Automation options out there, but none of them made me feel good.  Besides that, I really didn't set out to do a whole centralized control system, it just sorta morphed from a simple wish.

### One Simple Wish - the garage door,

It started with my wish to know whether my garage door was open or not.  In 2015 I wrote my first Python program, and [ohd](https://github.com/casspop/ohd) was born.

### then the pool,

Then we got a in-ground pool in the backyard.  The commercial controller was abominable, so I picked up another Raspberry Pi, a relay board, and wrote my second Python application, [poolApp.py](https://github.com/casspop/PoolControls).

### then the Weather Station,

When I dumped the second Accurite weather station into the trash in only two years, I started my quest for a Reliable, Robust, Repairable Raspberry Pi-based [Weather Station](https://github.com/casspop/Pi-based-weather-station). The station lives outside on a pole, but I wanted the database in the house.

I had a little i3 Lenovo computer that really wasn't doing anything, so I thought it made sense to put it to work holding the mySQL database for the weather station.  So I stuck a 4TB hard drive in it that I pulled out of a WD MyBook external and put it to work.

### then the web-based UI (VPN or local-only, not Internet),

Not much later I realized I needed a single interface for all this stuff, and [allApp.py](https://github.com/casspop/Pi-based-weather-station/tree/master/Code/all) was born.  It runs on Brilliant, the little i3 Lenovo.  (allApp is currently housed in the WeatherPi repo.)

### and then Eyes (cameras),

Zoneminder runs headless on Ubuntu on a fairly hairy gaming computer bought on sale from Best Buy (this one I didn't build myself).  I have four 4K TCP/IP cameras and the Raspberry Pi Camera in WeatherPi feeding into it.  Our interface to that system is part of the allApp.py running on that cutesy little i3 Lenovo.

### and then the shop,

I built myself a pretty nice shop in the back yard.  It has A/C for the summer, and heat in the winter.  I hated the GE cloud-based App controls for the window unit, so I ripped out the controls electronics and built my own out of, you guessed it, another Pi and relay board.  [ShopPi](https://github.com/casspop/ShopPi) was born.

### and then the P-Pi's: PlayerPi, PoohPi, and PiddlePi.

Discovering the joy of the 2004 LCD module caused the addition of PlayerPi, PiddlePi and PoohPi to the mix. To be technically accurate, PlayerPi already existed, but didn't have the LCD. At any rate, now there are three, all displaying whatever I want. It's very fun.

That pretty well describes in a concise manner the PiNet as it exists today.  More to come.  

Check out the [functional diagram](https://github.com/casspop/PiNet/blob/main/Docs/PiNet%20Block%20Diagram.pdf) AND [The Screens of PiNet](https://github.com/casspop/PiNet/blob/main/Docs/The%20Screens%20of%20PiNet.pdf) in the Docs folder.

(c) 2023 - Gregory A Sanders
