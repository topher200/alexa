import json

import requests

import config


OFF_STATE = 0
ON_STATE = 0
OFF_STATE_REQUEST = "{\"system\":{\"set_relay_state\":{\"state\":0}}}"
ON_STATE_REQUEST = "{\"system\":{\"set_relay_state\":{\"state\":1}}}"
GET_SYS_INFO = "{\"system\":{\"get_sysinfo\":{}}}"


def lambda_handler(event, _):
    print("Received event: " + json.dumps(event, indent=2))

    # make request to get current status
    url = 'https://%s/?token=%s' % (config.KASA_URL, config.KASA_TOKEN)
    sys_info_request_payload = {
        'method': 'passthrough',
        'params': {
            'deviceId': config.KASA_DEVICE_ID,
            'requestData': GET_SYS_INFO
        }
    }
    status_response = requests.post(url, json=sys_info_request_payload).json()
    print ('sys_info response: "%s"' % status_response)
    current_state = json.loads(
        status_response['result']['responseData']
    )['system']['get_sysinfo']['relay_state']

    # determine next status
    if event['clickType'] == 'SINGLE':
        # toggle
        if current_state == OFF_STATE:
            print('current state is OFF')
            state = ON_STATE_REQUEST
        else:
            print('current state is ON')
            state = OFF_STATE_REQUEST
    if event['clickType'] == 'DOUBLE':
        # just turn off
        state = OFF_STATE_REQUEST
    if event['clickType'] == 'LONG':
        # don't do anything
        return

    # make request to change status
    url = 'https://%s/?token=%s' % (config.KASA_URL, config.KASA_TOKEN)
    payload = {
        'method': 'passthrough',
        'params': {
            'deviceId': config.KASA_DEVICE_ID,
            'requestData': state
        }
    }
    print('making request to %s with %s' % (url, payload))
    res = requests.post(url, json=payload)
    res.raise_for_status()

    print('change state response: "%s"' % res.json())
