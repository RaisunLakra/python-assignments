'''
 Write a python script to create a Phone class with 2 methods to print the features
(calling and sms).
'''

class Phone:
    def calling(self):
        print("calling")
    
    def sms(self):
        print("SMS")

if __name__=="__main__":
    iphone=Phone()
    iphone.call()
    iphone.sms()