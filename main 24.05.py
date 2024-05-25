import shodan_whois
#API - EHY3AZgqN4rHGgNoaEXfAylKn02XnFRG

starting_message = """Hello, This program will scan websites on Shodan platform by 3 vulnerabilities are defined in this program,
and will send anonymous mail to the owner of the websites with the exploit that he needs to repair."""

def is_valid_api_key(api_key):
    if len(api_key) == 32 and api_key.isalnum():
            return shodan_whois.validate_api_key(api_key)
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


def get_users_choice(vuln_search: shodan_whois.VulnSearch) -> None:
    for i in range(3):
        info = vuln_search.api.info()
        print("API Plan: ", info['plan'])
        print("Remaining Credits: ", info['query_credits'])
        print ('''Choose an vulnerabilitie:
        1 For Apache 2.4.50
        2 For ProFTPd 1.3.5
        3 For Lighttpd 1.4.15''')
        choice = input("Enter Your Choose: ")
        match choice:
            case '1':
                vuln_search.search_vulnerabilities('Apache 2.4.50')
            case '2':
                vuln_search.search_vulnerabilities('ProFTPd 1.3.5')
            case '3':
                vuln_search.search_vulnerabilities('Lighttpd 1.4.15')
            case _:
                if i < 2:
                    print(f"Invalid choice. Please try again. You have left {2 - i} attempts.")
                else:
                    print("Maximum attempts reached. Exiting program.")

def main():
    print(starting_message)
    api_key = get_api_key()
    if api_key:
        vuln_search = shodan_whois.VulnSearch(api_key)
        get_users_choice(vuln_search)



if __name__ == "__main__":
    main()
