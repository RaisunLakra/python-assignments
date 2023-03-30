"""
Write a Python script to print indices of all occurrences of a given element in a given
list.
"""
mylist = [2, 3, 4, 2, 1, 2, 4, 5]
element = 2

indices=[i for i in range(len(mylist)) if element==mylist[i]]
print(indices)

"""
indices=[i for i in range(len(mylist)) if element==mylist[i]]
यह लाइन पहले for लूप के माध्यम से लिस्ट के सभी इंडेक्स पर चलती है जो len() फंक्शन के माध्यम से लिस्ट की लंबाई के बराबर होते हैं। फिर इंडेक्स के संख्यात्मक मान के साथ if स्टेटमेंट चलाते हुए यह देखती है कि लिस्ट में वह एलिमेंट मौजूद है या नहीं। यदि वह उपलब्ध होता है, तो इंडेक्स को सूची में शामिल कर दिया जाता है।
"""