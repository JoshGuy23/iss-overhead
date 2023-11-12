# ISS Overhead

## Introduction

This program detects whether the International Space Station is visible from your location using the ISS Now and Sunrise Sunset APIs.

## Using the Program

Before starting the program, please get your current latitude and longitude (MY_LAT and MY_LONG) from https://www.latlong.net/ and replace the value of MY_EMAIL with your email address.

Please note that the Sunrise Sunset API returns the current time in UTC, so I had to create a function to convert it to my local time. You may have to do the same for the program to work correctly. Currently, this program only works for CST.

This program runs every 60 seconds. If the International Space Station is within 5 degrees of the user's current location and it is currently dark out, an email will be sent to the user notifying them to look up at the night sky to find the ISS.

## Requirements

To run main.py, you will need the requests package.
