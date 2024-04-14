# My First PostMortem


![Calma] (https://www.google.com/url?sa=i&url=https%3A%2F%2Fimgur.com%2Ft%2Fburning%2FrixnjL5&psig=AOvVaw3UtYG4Q-V6PtXwlirdkOBb&ust=1713211031679000&source=images&cd=vfe&opi=89978449&ved=0CBEQjRxqFwoTCKi5rty-woUDFQAAAAAdAAAAABAE)

## Introduction

While a postmortem covers service outage and it's effect on the service provided and also on customer's accessing the service. This README covers an imaginary outage

### Issue Summary
* from 01:00 WAT 03:39AM WAT (12th April 2024)
* Customer's faced an issue in recovering specialised preferences covering custom tweaked configs made to their respective cloud service providers.
* Following everal hours of debugging, the issue was found at one of the endpoint, this error was made during a recent pull request by the team to add a new feature to the current endpoint.

### Timeline
* The Issue was detected a few hours after the pull request specifically at of 01:00AM WAT
* The Issues was detected by a user trying but failing to fetch the data locally following a tweak made to his current config
* Once the issue was detected, a revert was made to the previous working commit whle efforts were put in place to determine where the errow was from

### Root Cause
As stated earlier, a recent update was proposed by the analytics department following request from the users to allow for tweaking and downloading the respective configs. However, there was a slight error, with a response not being properly parsed -- leading to data being sent in the wrong format for the other functions to work on.

* Resolution: An autdit was made into this complaint and the affeected end-point was looked into. The issue at first seemed innocous. However, when querying the type of data that was being sent, a slight mishap was found.

### Corrective Measures
Futher updates have been stipulated to follow strict guidelines, which include:
* Test cases for every single update 
* Testing for Null values when output does not contain valid data
* Testing across a variety of storage types
