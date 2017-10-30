## UPDATE

Now that TP-Link's Kasa supports IFTTT, I'd highly recommend using that instead of bothering with skimming the API credentials and doing it manually.

In addition, the credentials I grabbed with fiddler stopped working after about a month. So one who wanted to fake Kasa API calls using this repo would likely have to re-update their credentials every month.

# Summary

Make requests to Kasa IOT electrical plug using python.

Following the guide from
http://itnerd.space/2017/01/22/how-to-control-your-tp-link-hs100-smartplug-from-internet/
on how to make the requests. Got my Kasa credentials from fiddler.

# Getting it set up
## Configuration
fill out `config.py`. requires these fields:
```
KASA_TOKEN = <from the kasa app>
KASA_DEVICE_ID = <from the kasa app>
KASA_TERM_ID = <from the kasa app>
KASA_URL = <from the kasa app>
IOT_BUTTON_SERIAL_NUMBER = <from your IOT button. optional, only for `test.py`>
```

Here's an example config (modified values):
```
KASA_TOKEN = '74xdxc7e-6xf7-4xc1-ax51-xxxxxxxxxxxx'
KASA_DEVICE_ID = '800XXXXXXXXXXXC54C55896BFA2XXXXXXXXXXXXX'
KASA_URL = 'use1-wap.tplinkcloud.com'
IOT_BUTTON_SERIAL_NUMBER = "G0XXXX020XXXXUQR"
```

## install python
* create a virtualenv with python3.6 runtime
  * `mkvirtualenv -p python3.6 alexa`
* install python dependencies with `setup.sh`
  * we install them in the local directory so that we can upload them to lambda


## upload to lambda
* make a lambda function with python3.6 runtime
* set the function name in `package.sh`
* set up the `aws` cli with lambda upload permissions
* create a package and upload to lambda with `package.sh`
