headers = {"Authorization": "token 1f36137fbbe1602f779300dad26e4c1b7fbab631"}

# GET
response = requests.get("https://api.github.com/users/VikParuchuri/orgs", headers=headers)
org_url = response.json()[0]['url']

# POST
payload = {"name": "learning-about-apis"}
response = requests.post("https://api.github.com/user/repos", json=payload, headers=headers)
status = response.status_code

# PUT/PATCH
payload = {"description": "Learning about requests!", "name": "learning-about-apis"}
response = requests.patch("https://api.github.com/repos/VikParuchuri/learning-about-apis", json=payload, headers=headers)
status = response.status_code

# DELETE
response = requests.delete("https://api.github.com/repos/VikParuchuri/learning-about-apis", headers=headers)
status = response.status_code
