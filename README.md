## PiNet: The Evolution of a Simple Wish

Why describe my home control network here?  Well, it's complicated.  Bottom line, if I did it, you can do it.  And you might want to.  So here's how it started, and here's what I did.

There are a bunch of Home Automation options out there, but none of them made me feel good.  Besides that, I really didn't set out to do a whole centralized control system, it just sorta morphed from a simple wish.

#### One Simple Wish

It started with my wish to know whether my garage door was open or not.  In 2015 I wrote my first Python program, and [ohd](https://github.com/casspop/ohd) was born.

Then we got a in-ground pool in the backyard.  The commercial controller was abominable, so I picked up another Raspberry Pi, a relay board, and wrote my second Python application, [poolApp.py](https://github.com/casspop/PoolControls).

When I dumped the second Accurite weather station into the trash in only two years, I started my quest for a Reliable, Robust, Repairable Raspberry Pi-based [Weather Station](https://github.com/casspop/Pi-based-weather-station).

I had a little i3 Lenovo computer that really wasn't doing anything, so I thought it made sense to put it to work holding the mySQL database for the weather station.  

Not much later, I realized I needed a single interface for all this stuff, and allApp.py was born.  It runs on Brilliant, the little i3 Lenovo.

Zoneminder runs on Ubuntu on a fairly hairy gaming computer bought on sale from Best Buy (this one I didn't build myself).  Our interface to that system, however, is part of the allApp.py running on that sad little i3 Lenovo.

That pretty well describes in a concise manner the Pi-Net as it exists today.  More to come.  

Check out the functional diagram in the Docs folder.
