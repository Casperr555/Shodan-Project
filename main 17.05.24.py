import shodanutils

starting_message = """Hello, This program is blablabla"""

def is_valid_api_key(api_key):
    if len(api_key) == 32 and api_key.isalnum():
            return shodanutils.validate_api_key(api_key)
    return False

def get_api_key() -> str:
    for i in range(3):
        api_key = input("Enter your Shodan API Key: ")
        if is_valid_api_key(api_key):
            return api_key
        if i < 2:
            print(f"Invalid API Key. Please try again. You have left {2 - i} attempts.")
        else:
            print("Maximum login attempts reached. Exiting program.")
    return None

def get_users_choive(vuln_search: shodanutils.VulnSearch) -> None:
    for i in range(3):
        choice = input("Enter Your Choose: ")
        match choice:
            case '1':
                vuln_search.search_vulnerabilities('Apache 2.4.50')
            case '2':
                vuln_search.search_vulnerabilities('x')
            case '3':
                vuln_search.search_vulnerabilities('y')
            case _:
                if i < 2:
                    print(f"Invalid choice. Please try again. You have left {2 - i} attempts.")
                else:
                    print("Maximum attempts reached. Exiting program.")

def main():
    print(starting_message)
    api_key = get_api_key()
    if api_key:
        vuln_search = shodanutils.VulnSearch(api_key)
        get_users_choive(vuln_search)



if __name__ == "__main__":
    main()