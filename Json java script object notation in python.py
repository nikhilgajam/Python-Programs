import json

# Json data only dictionary
json_data_d = '''
{
    "name" : {"Ben" : 100, "Gwen" : 100, "Max" : 1000},
    "email" :{"hide" : "Yes"}
}
'''

print("Java Script Object Notation (JSON)\n")
# Json represents data as the internal data in programming languages

# loads means load string
jsd = json.loads(json_data_d)

for n, a in jsd['name'].items():
    print("Name:", n, "\n", "Age:", a, "\n")

print("Email Hidden(Yes):", jsd['email']['hide'])

# Json data with list and dictionary
json_data_ld = '''
[

    {
        "name" : "Ben",
        "age" : 100
    }
    ,
    {
        "name" : "Gwen",
        "age" : 100
    }
    ,
    {
        "name" : "Max",
        "age" : 1000
    }

]
'''

print("\nList and dictionary JSON\n")

users = json.loads(json_data_ld)
# Getting the data
for user in users:
    print("Name:", user['name'])
    print("Age:", user['age'])
    print()
