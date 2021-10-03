
# app_id = '262243108989293'
# app_secret = 'a4dbd0c68675c55687f7433a76c8c14f'
# token = 'EAADugjtbKW0BAKFs1znmf10T9TOTD7FUMlvQxfoMUBazCpvvtqXwiWAdHjy4ZBukw0Rf7kpXt0Ra0XZBdZClQJRT9av646QlNvz6ivoetWsOCoiLpKXQqIDQ7OjqYcmwKRtQws0jBw0AmogBYzeUM0DoSbq3lqDzN4vMn55ZCnEDnFn4FQfn'
# page_id = '262243108989293'

api_key = 'd75ba2ad'
api_secrete = 'BSYrvJbh5acUU9OD'
my_message = "hello yasser form the python script"
bot_number = "14157386170"
bot_id = "100069562545422"
# yasser_id = "4175433945889126 "
# mama_id = "4340565582699536"
client_id = ""



import requests
import json


def send_message(send_by:str,message:str):
    print("sendMessage method start now ")
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
    }

    whatsapp_data = {
        "from": {
            "type": "whatsapp", "number": "14157386170"
        },
        "to": {
            "type": "whatsapp", "number": "213798257795"
        },
        "message": {
            "content": {
                "type": "text",
                "text": message
            }
        }
    }
    messanger_data = {
        "from": {
            "type": "messenger", "id": "107083064136738"
        },
        "to": {
            "type": "messenger", "id": client_id
        },
        "message": {
            "content": {
                "type": "text",
                "text": message
            }
        }
    }
    # turn the json to string
    if(send_by == "whatsapp"):
        data = json.dumps(whatsapp_data)
    elif(send_by == "messanger"):
        data = json.dumps(messanger_data)
    else:
        print("error when select the 'send_by' parametre\nmake sure  that you select {whatsapp or messanger } without {}")


    # send the message (post)
    response = requests.post('https://messages-sandbox.nexmo.com/v0.1/messages', headers=headers, data=data, auth=(api_key, api_secrete))
    print("reponse status: ",response.status_code)

    print("sendMessage method end  ")




