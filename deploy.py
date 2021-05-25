import requests
import semantic_version

def get_LucidDynamodb_version():
    url = "https://pypi.org/pypi/LucidDynamodb/json"
    response = requests.request("GET", url, headers={}, data={})
    result = response.json()
    return result.get("info").get("version")

if __name__ == "__main__":
   LucidDynamodb_version = str(get_LucidDynamodb_version())
   current_version = semantic_version.Version(LucidDynamodb_version)
   next_version = current_version.next_patch()
   print(next_version)

