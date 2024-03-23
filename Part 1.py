#10 Exploits
#Apache HTTP Server 2.4.50 - https://www.exploit-db.com/exploits/50512
import shodan

shodan_key ="VDs85RsZxokySdVardSvqS8nf2NyO2LE"
api = shodan.Shodan(shodan_key)

#results = input(shodan.Shodan.search)
#print (results)

search = input("Shodan Searching Bar:\n")
try:
    results = api.search(search)
    print(results)
except:
    print("error")


