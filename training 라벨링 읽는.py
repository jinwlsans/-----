import xml.etree.ElementTree as ET
tree = ET.parse('C:/Users/진정욱/Desktop/대회/Training/[Training 라벨링]underwater photo/bundle of ropes_002_00012.xml')
root = tree.getroot()


for child in root:
    print(child.tag, child.attrib)
    