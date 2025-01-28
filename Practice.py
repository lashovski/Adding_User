import subprocess
#For using Linux commands
import optparse
#For parsing user input

def get_user_input():
    parser = optparse.OptionParser()
    parser.add_option("-u", dest="username", help="Username to create")
    parser.add_option("-p", dest="password", help="Password for the user")

    (user_input, arguments) = parser.parse_args()

    if not user_input.username or not user_input.password:
        parser.error("Both username and password requierd brother!")

    return user_input

def create_user(username):
    print(f"Creating user '{username}'...")
    subprocess.call(["sudo", "useradd", "-m", username])

def set_user_password(username, password):
    print(f"Creating password for {username}")
    subprocess.call(["sudo", "bash", "-c", f"echo '{username}:{password}' | chpasswd"])

def grant_privileges(username):
    print(f"Grant all privileges to {username}")
    subprocess.call(["sudo", "usermod", "-aG", "sudo", username])

print("User Account Manager Program")

user_input = get_user_input()
create_user(user_input.username)
set_user_password(user_input.username, user_input.password)
grant_privileges(user_input.username)

print(f"User '{user_input.username}' created successfully with full privileges!")
