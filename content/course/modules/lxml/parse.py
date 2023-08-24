import xml.etree.ElementTree as et

## Parse

tree = et.parse('input.xml') # Get xml filed parsed version
root = tree.getroot() # Devide a roots and elements of list

## Find

# tag = root.tag # Get tag area of bracked
# tag_order = root[0].tag # Get first elements of list of root
# attrib = root[0].attrib # Get the attributes of elements

# for x in root.findall('book'):
#     author = x.find("author")
#     title = x.find("title")
#     genre = x.find("genre")
#     price = x.find("price")
#     print(author.text, title.text, genre.text, price.text)

## Modifying

# for x in root.iter('description'):
#     a = str(x.text) + 'Description updated'
#     x.text = str(a)
#     x.set('updated','yes')
# tree.write('updated.xml')


## Update all section 

# sub_elem = et.SubElement(root[0],'description')

# for x in root.iter('description'):
#     b = 'Updated description'
#     x.text = str(b)
# tree.write("new.xml")

## Delete attribute

# root[0].attrib.pop('id')
# tree.write('new2.xml')

## Delete elements item

# root[0].remove(root[0][0])
# tree.write("new3.xml")

## Reset all processes on the detected xml file

# root[0].clear()
# tree.write('new4.xml')