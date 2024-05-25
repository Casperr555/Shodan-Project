import subprocess
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
            print("API Plan:", info['plan'])
            print("Remaining Credits:", info['query_credits'])
        except shodan.APIError as e:
            print("Error retrieving API information:", e)

    def search_vulnerabilities(self, query: str) -> list:
        try:
            results = self.api.search(query)
            print(f"Results found: {results['total']}")
            now = datetime.now().strftime("%Y-%m-%d-%H-%M")
            with open(f'shodan_results_{now}.csv', 'w') as f:
                f.write("IP Address, Domain, OrgAbuseEmail\n")
                for result in results['matches']:
                    ip = result['ip_str']
                    domains = result['hostnames'][0] if result['hostnames'] else 'N/A'
                    whois_data = get_whois_data(ip)
                    contact_info = extract_contact_info(whois_data)
                    org_abuse_email = contact_info.get('OrgAbuseEmail', 'N/A')
                    print(f"IP: {ip}\nDomains: {domains}\nOrgAbuseEmail: {org_abuse_email}\n")
                    f.write(f"{ip},{domains},{org_abuse_email}\n")
            return list(results)
        except shodan.APIError as e:
            print(f"API Error: {str(e)}")
            return []
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return []

def validate_api_key(api_key: str) -> bool:
    try:
        api = shodan.Shodan(api_key)
        api.search('test')
        return True
    except shodan.APIError:
        return False

def get_whois_data(ip):
    try:
        result = subprocess.run(['whois', ip], capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def extract_contact_info(whois_data):
    contact_info = {}
    for line in whois_data.splitlines():
        if "OrgAbuseEmail:" in line:
            contact_info['OrgAbuseEmail'] = line.split(":")[1].strip()
    return contact_info

if __name__ == "__main__":
    api_key = "YOUR_SHODAN_API_KEY"
    vuln_search = VulnSearch(api_key)
    vuln_search.get_api_info()
    query_string = "vulnerable service"
    vuln_search.search_vulnerabilities(query_string)
