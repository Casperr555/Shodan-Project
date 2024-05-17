import shodan
import csv
from tkinter import filedialog, Tk

#API - Shodan EHY3AZgqN4rHGgNoaEXfAylKn02XnFRG

class VulnSearch:
    def __init__(self, api_key):
        api_key = api_key
        api = shodan.Shodan(api_key)

    def authenticate(self):
        for i in range(3):  # Three login attempts
            try:
                self.api.search('test')  # Just a test query to check authentication
                print("Authentication successful.")
                return True
            except shodan.APIError as e:
                print("Authentication failed. Remaining attempts:", 2, i)
                if i == 2:
                    print("Maximum login attempts reached. Exiting program.")
                    return False

    def get_api_info(self):
        try:
            info = self.api.info()
            print("API Plan: ", info['plan'])
            print("Remaining Credits: ", info['query_credits'])
        except shodan.APIError as e:
            print("Error retrieving API information:", e)

    def search_vulnerabilities(self):
        if choice =='1':
            choice = input("Enter Your Choose: ")
        try:
            results = self.api.search('Tel Aviv')
            print(f"Results found: {results['total']}")
            for result in results['matches']:
                print(f"IP: {result['ip_str']}")
                print(f"Data: {result['data']}\n")
        except shodan.APIError as e:
            print(f"Error: {e}")
 #           results = shodan_search.search_vulnerabilities('Apache 2.4.50')
  #          print("Search results:", results)
   #         return results
    #    except shodan.APIError as e:
     #       print("Error during search:", e)
      #      return None

if __name__ == "__main__":
    api_key = input("Enter your Shodan API Key: ")
    shodan_search = VulnSearch(api_key)
    authenticated = shodan_search.authenticate()

    if authenticated:
        shodan_search.get_api_info()
        print ('''Choose an vulnerabilities:
        1 For Apache 2.4.50
        2 For X
        3 For Y''')

            

       
        #choosen_vuln = input("Enter your search query: ")
        #results = shodan_search.search_vulnerabilities(choosen_vuln)
