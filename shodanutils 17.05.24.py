from datetime import datetime
import shodan

class VulnSearch:
    def __init__(self, api_key):
        if not validate_api_key(api_key):
            raise ValueError("Invalid API Key")
        self.api_key = api_key
        self.api = shodan.Shodan(api_key)

    def get_api_info(self):
        try:
            info = self.api.info()
            print("API Plan: ", info['plan'])
            print("Remaining Credits: ", info['query_credits'])
        except shodan.APIError as e:
            print("Error retrieving API information:", e)


# search for vulnerabilities by query string:
    def search_vulnerabilities(self: object, query: str) -> list:
        try:
            results = self.api.search(query)
            print(f"Results found: {results['total']}")
            now = datetime.now().strftime("%Y-%m-%d")
            with open(f'shodan_results{now}.csv', 'w') as f:
                f.write("IP Address, Host-Name\n")
                for result in results['matches']:
                    print(f"IP: {result['ip_str']}\nHost-Name: {result['hostnames']}\n")
                    # write to the csv with the headlines ip and data:
                    f.write(f"{result['ip_str']},{result['hostnames']}\n")
            return list(results)
        except shodan.APIError as e:
            print(f"API Error: {str(e)}")
            return []
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return []


# validate with shodan api threw shodan.Shodan(api_key) if api_key is valid
def validate_api_key(api_key: str) -> bool:
    try:
        api = shodan.Shodan(api_key)
        api.search('test')
        return True
    except shodan.APIError as e:
        return False
    except Exception as e:
        print("An error occurred:", str(e))
        return False

    