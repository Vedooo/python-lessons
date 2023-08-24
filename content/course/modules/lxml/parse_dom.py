from xml.dom import minidom


## Parse

# tree = minidom.parse('index.xml')

data = open('input.xml')
tree = minidom.parse(data)

## Find

tag = tree.getElementsByTagName('author')
# print(tag.firstChild.data)
# print(tag[0].firstChild.data)

# for x in tag:
#     print(x.firstChild.data)

## Length of the Element

print(len(tag))