# speedtest-python
Send from a portable raspberry pi to measure ethernet and send to your local device


## WHY?
All of my computing devices (Laptops/phones) don't have an ethernet port.
Raspberry pi supports gigabit connections and it serves as an easy way to test ethernet cable speeds.
What if you wanted to check all the ethernet ports around your house/switches to see what speeds they allow.
You can put your raspberry pi on a portable charger, and go around the rooms plugging in ethernet, once there is ethernet it will post your results to a device you configure to send to(EG. LAPTOP
The program will continuously run until you terminate the process.


# How to USE

Setup an api server to listen to api calls on an endpoint.
Change line 6 of APP.py to where your api endpoint will live


From your API server that you setup earlier, print out the request parameters


### CONSOLE FROM PYTHON RASPBERRY PI:
```json
Download: 434.8243724257
Upload: 15.9533540213374
13.843
Download: 350.6733331732185
Upload: 23.321033525388483
19.328
Download: 376.13949388131414
Upload: 22.328993267920772
12.301
Download: 414.55613522221375
Upload: 22.9286547852842
12.891
Download: 419.9953715055536
Upload: 23.364201617216104
12.227
```
### CONSOLE FROM API SERVICE
```js
[
{
  download: '376.13949388131414',
  upload: '22.328993267920772',
  ping: '12.301'
}
{
  download: '414.55613522221375',
  upload: '22.9286547852842',
  ping: '12.891'
}
{
  download: '419.9953715055536',
  upload: '23.364201617216104',
  ping: '12.227'
}
]
```
