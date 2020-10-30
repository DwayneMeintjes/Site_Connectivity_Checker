import requests

class check:

    def __init__(self,web):
        self.web = web

    def active(self):
        i = 0
        while i < 3:
            response = requests.get(self.web)
            i += 1
        return response

    def test(self,result):
        if result.status_code == 200:
            print("The website is active!")
        else:
            print("The website seems to be down!")


if __name__ == "__main__":
    try:
        web_url = str(input("Please enter the website you which to test : "))
    except IOError:
        print("Please enter a valid URL!")
    
    Check = check(web_url)
    result = Check.active()
    Check.test(result)