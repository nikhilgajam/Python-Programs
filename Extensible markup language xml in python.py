import xml.etree.ElementTree as Et

xml = '''
<users>

    <people>
    
        <user>    
            <name>Ben</name>
            <age>100</age>
            
        </user>
        <user>
            <name>Gwen</name>
            <age>100</age>
        </user>
        <user>
            <name>Max</name>
            <age>1000</age>
        </user>
        
    </people>
    
    <creators>
    
        <creator>
            <name>Azmuth</name>
            <email hide="Yes" />
        </creator>
        
    </creators>
    
</users>
'''

# Data retrieved as list
data = Et.fromstring(xml)
people = data.findall('people/user')

print("Extensible'X' Markup Language (XML)\n")
print("People:", len(people), '\n')

for person in people:
    print("Name:", person.find('name').text)
    print("Age:", person.find('age').text)
    print()

creators = data.findall('creators')

# creator = creators[0].find('creator').find('name').text
creator = creators[0].find('creator')

print("Creator:", creator.find('name').text)
print("Email Hidden(Yes):", creator.find('email').get('hide'))
print()
