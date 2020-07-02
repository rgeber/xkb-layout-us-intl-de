import xml.etree.ElementTree as ET
import os
import sys

PATH_EVDEV = '/usr/share/X11/xkb/rules/evdev.xml'
PATH_SYMBOLS = '/usr/share/X11/xkb/symbols/us'
dir_path = os.path.dirname(os.path.realpath(__file__))

# Append the symbols file
with open(os.path.join(dir_path, 'intlde'), 'r') as intde_file:
    with open(PATH_SYMBOLS, 'a') as system_symbols_file:
        system_symbols_file.write(intde_file.read())

# Fix evdev.xml
# root = ET.parse(path.join(getenv('HOME'), 'evdev.xml')).getroot()
root = ET.parse(PATH_EVDEV).getroot()
for layout in root.find('layoutList').findall('layout'):
    if layout.find('configItem').find('name').text != 'us':
        continue

    variantList = layout.find('variantList')

    newET = ET.Element('variant')
    newETCI = ET.SubElement(newET, 'configItem')

    newETName = ET.SubElement(newETCI, 'name')
    newETName.text = 'intlde'

    newETDesc = ET.SubElement(newETCI, 'description')
    newETDesc.text = 'English (US, intl., German)'

    variantList.append(newET)


tree = ET.ElementTree(root)
tree.write(PATH_EVDEV)


print ('Done')
sys.exit(0)
