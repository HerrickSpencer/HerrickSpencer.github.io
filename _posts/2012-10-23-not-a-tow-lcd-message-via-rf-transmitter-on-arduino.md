---
layout: WPArchive
title: Not a TOW - LCD message via RF transmitter on Arduino
date: 2012-10-23 15:52
author: herrickspencer
comments: true
categories: [Programming, Technology]
tags: [Arduino, IOT Maker]
---
Thought I’d hijack my own DL to show you something fun…. (and send to LI office)

#### I did a little project with my [Arduino Duemilanove](https://www.arduino.cc/)

I made an intranet site to send text to a 20x4 LCD screen sitting on the edge of my cube.  
Messages are formatted to fit a 20 column by 4 row screen. Each send will clear the screen and set the new text on the screen.  
The message is routed through [this website](https://herricks-dev/LCDMessage/), to a RF 2.4gz transmitter, wirelessly to a similar transmitter sitting on the Arduino Duemilanove that I programmed to handle reading the serial data, formatting it, and sending it on to the screen.

Beware: The site also tracks the username of the person sending the message… because already dirty messages have been sent. J

Note: the site if VERY basic, and has not had a lot of testing done.

##### Future plans

I plan on wiring up the LCD a bit more permanently, and making a nice enclosure for the whole package.  Then I want to place it in the Long Island break room near the coffee machine.  This will allow anyone to send messages to the break room for fun-zees.

#### The site

![clip_image001](/{{ site.postMedia }}/2012/10/clip_image001.jpg "clip_image001")_Here’s a shot of the website, complete with picture of the cube wall_

[![clip_image003](/{{ site.postMedia }}/2012/10/clip_image003_thumb.jpg "clip_image003")_Here’s a shot of the Arduino wired to the transmitter and LCD_](/{{ site.postMedia }}/2012/10/clip_image003.jpg)