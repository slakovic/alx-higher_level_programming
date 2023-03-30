#!/bin/bash
# Displays the body of the response of a curl POST request
curl -sLX PUT -d "You got me!" -H "Origin:HolbertonSchool" 0.0.0.0:5000/catch_me

