
''' lxml tutorial : https://lxml.de/tutorial.html '''

''' Elements carry attributes as a dict '''


from lxml import etree

# high-level structure

root = etree.Element('data')
archival_images = etree.SubElement(root,'archival_images')
fashion_images = etree.SubElement(root, 'fashion_images')

# populate:
# for item in folder add name to tag space and path to URL space, leave all other fields empty

import os

folder = '/Users/noyakohavi/Desktop/BROWN/test_set'

allfiles = os.listdir(folder)

for x in allfiles:
    x = x.split('.')[0]
    if 'f' in x:
        etree.SubElement(fashion_images, x, url=folder+'/'+x, dom_color='', sec_color='')
    if 'a' in x:
        archival = etree.SubElement(archival_images, x, url=folder+'/'+x, dom_color='', sec_color='')

# pretty print database

print(etree.tostring(root, pretty_print=True))

# write database to file

with open('/Users/noyakohavi/Desktop/BROWN/test_database.xml','w') as f:
        f.write(etree.tostring(root,pretty_print=True))

# find similar images by feature property :

same = []
not_same = []

for archival_images in root:
    for image in archival_images:
        if image.get('dom_color') == 'red':    ### and image.get('sec_color') == 'green':# --> add multiple conditions

            same.append(image.tag)
        else:
            not_same.append(image.tag)

print 'same', same
print 'not same', not_same




