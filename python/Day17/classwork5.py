import xml.etree.ElementTree as ET
 
# Read and parse the XML file
tree = ET.parse(r"C:\Users\harsh\Desktop\harsha_wipro\python\Day17\dataj.xml")
root = tree.getroot()
 
# Extract data
for child in root:
    print(f"{child.tag}: {child.text}")