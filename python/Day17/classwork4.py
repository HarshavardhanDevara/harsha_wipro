import xml.etree.ElementTree as ET
 
# Create the root element
root = ET.Element("person")
 
# Create child elements
name = ET.SubElement(root, "name")
name.text = "muni"
 
age = ET.SubElement(root, "age")
age.text = "25"
 
city = ET.SubElement(root, "city")
city.text = "mrpalli"
 
# Convert the tree to a string
tree = ET.ElementTree(root)
with open(r"C:\Users\harsh\Desktop\harsha_wipro\python\Day17\dataj.xml", "wb") as file:
    tree.write(file, encoding="utf-8", xml_declaration=True)