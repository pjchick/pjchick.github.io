---
title: Overview
date: 2025-01-15
draft: false
---

# Goals

I want to try and test the limits of what a relay computer is ultimately capable of. Using the amazing Harry Porter and Paul Law designs as a starting point I want to see where I can take it.


## These goals include:-
- Support ALL logic gate functions (AND, OR, NAND, NOR, XOR, XNOR, NOT).
- Add Subtract, increment and decrement.
- a Stack with PUSH, POP and PEEK (Circular buffer).
- a basic hardware interrupt.

## Side projects (so far) include:
- Building some form of paper tape reader / writer (for 12-bit data!)
- A 'ROM cartridge' / boot loader.
- Custom case to make it 'portable' (but I'll settle for luggable!). I want to be able to take this to maker fair's and let people interact with it as much as possible.
- A true Random Number Generator. I'm imagining a marble drop machine with 12 channels at the bottom, when you ask for a random number it reads the colour of the balls (black or white) before re circulating them back up to be dropped again. Loud, Madness but fun!
- Human Clock. The main computer clock will similar to other designs, however I want to build a large box with a hand wheel, where someone can literally 'crank' the clock pulses into the machine. 
  
# Constraints

- Everything to do with the core computing functions of the machine has to be done by relay's (except Memory - see below).
- Diodes can be used to stop back-feeding signals but at a minimum.
- LED's are allowed for monitoring and purposes on the card's - the more blinkin' lights the better!

It's not to say that my machine will be silicon free! - far from...

- A RAM chip will be used for main memory. However I want to integrate some other discreet memory devices along side (Relay RAM or Capacitor RAM) just to prove it *could* work if I had enough time or budget to build a 4096 * 12 bit memory storage by hand! This I feel is an honourable compromise. 
  If I'm going to ~~cheat~~ compromise on the RAM - I might as well make the most of it! So my plan will be to use a microcontroller (with wifi) for the RAM. In normal operation the microcontroller will function as basic RAM - implemented as many others have done. However it will also give me the ability to write a debugging interface. The goal will be to view, edit, load and save the memory from a terminal browser or telnet session etc.
  
- A Diagnostic card is also planned that will be able to view the busses and manipulate the key control lines. Again useful for diagnostics as it's being built but would also server another purpose as the ultimate goal would be to put this computer 'on the net' so people could write their own programs and run them remotely! 

- Finally no electronics project would be complete without a '555' timer! So their will be a second clock source built around one of these - just to annoy the purists!

# Specification

The computer is 12-bits. 12-bit Address bus, 12-bit Data bus and 12-bit ALU. 

Using a 12-bit data bus and 12-bit instruction register has given me much more flexibility with the instruction set. I settled on 12-bits as I thought is was the sweetspot (for me). I can play with large'ish numbers (4095 max), I can have a much larger instruction set, and I'd never need more that 4096 bytes of memory in reality - a 16 bit address range would be overkill. As for the number of relay's used - it will take more relays - but I don't think the amount will be as significant as I first thought as I am increasing the data-bus but reducing the address bus across the design.


The main ALU can add , subtract , increment and decrement. The shifting card can Shift or Rotate the B or C register. Using a 12-bit data bus and 12-bit instruction register has given me much more flexibility with the instruction set. I settled on 12-bits as I thought is was the sweetspot (for me). I can play with large'ish numbers (4095 max), I can have a much larger instruction set, and I'd never need more that 4096 bytes of memory in reality - a 16 bit address range would be overkill. As for the number of relay's used - it will take more relays - but I don't think the amount will be as significant as I first thought as I am increasing the data-bus but reducing the address bus. The majority of my inspiration and designs are based on the EXCELLENT relay computers built by Paul Law - [https://www.youtube.com/@paul80nd](https://www.youtube.com/@paul80nd), DipDot - [http://www.youtube.com/@dipdoting](http://www.youtube.com/@dipdoting) and Harry Porter - [http://www.youtube.com/@hhp3](http://www.youtube.com/@hhp3) ...with just a little of my own lunacy thrown in!