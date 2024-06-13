import requests

def get(url):
    print(url, end=" ")
    #print(headers)
    response = requests.get(url, headers=headers)
    print(response.status_code)
    return(response)


#GitHub REST API doc: https://docs.github.com/en/rest/copilot/copilot-usage?apiVersion=2022-11-28

# scope is focused on ORGANIZATION endpoints (vs ENTERPRISE) for now
#set org name here:
org_name = "org-name"
base_url = f"https://api.github.com/orgs/{org_name}"

# NEED A VALID BEARER TOKEN TO AUTHENTICATE THE REQUESTS
#(token would be better stored in an ENV variable but could also hard-code here for local development)
my_token = "my-secret-token"
headers = {
	"Accept": "application/vnd.github+json",
	"Authorization": f"Bearer {my_token}",
    "X-GitHub-Api-Version": "2022-11-28"
}

endpts = {
    'usage': '/copilot/usage',
    'billing': '/copilot/billing',
    'seats': '/copilot/billing/seats'
}

# interate through all defined end points above and make GET requests
for k ,v in endpts.items():
    print(k)
    target_url = base_url + v
    data = get(target_url)
    print(data.json())
    print("\n")


