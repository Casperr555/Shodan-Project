import shodan
import csv
from tkinter import filedialog, Tk

class VulnSearch:
    def __init__(self, api_key):
        self.api_key = api_key
        self.api = shodan.Shodan(api_key)

    def authenticate(self):
        for _ in range(3):  # Three login attempts
            try:
                self.api.search('test')  # Just a test query to check authentication
                print("Authentication successful.")
                return True
            except shodan.APIError as e:
                print("Authentication failed. Remaining attempts:", 2 - _)
                if _ == 2:
                    print("Maximum login attempts reached. Exiting program.")
                    return False

    def get_api_info(self):
        try:
            info = self.api.info()
            print("API Plan: ", info['plan'])
            print("Remaining Credits: ", info['query_credits'])
        except shodan.APIError as e:
            print("Error retrieving API information:", e)

    def search_vulnerabilities(self, query):
        try:
            results = self.api.search(query)
            print("Search results:", results)
            return results
        except shodan.APIError as e:
            print("Error during search:", e)
            return None

    def export_to_csv(self, results):
        if results:
            root = Tk()
            root.withdraw()
            file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])
            if file_path:
                with open(file_path, mode='w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(['IP Address', 'Domain'])

                    for result in results['matches']:
                        ip_address = result['ip_str']
                        domain = result['hostnames'][0] if result['hostnames'] else "N/A"
                        writer.writerow([ip_address, domain])
                print("Results exported to", file_path)
        else:
            print("No results to export")

if __name__ == "__main__":
    api_key = input("Enter your Shodan API Key: ")
    shodan_search = VulnSearch(api_key)
    authenticated = shodan_search.authenticate()

    if authenticated:
        shodan_search.get_api_info()  # Print API info after successful authentication

        query = input("Enter your search query: ")
        results = shodan_search.search_vulnerabilities(query)
        shodan_search.export_to_csv(results)
