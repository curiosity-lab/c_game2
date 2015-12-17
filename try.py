import xml.etree.ElementTree as ET


curiosity_q = ET.parse('curiosity_q.xml')
root_curiosity_q = curiosity_q.getroot()
ET.fromstring(root_curiosity_q)
print root_curiosity_q.tag

#for child in root_curiosity_q:
 #   child = ET.fromstring(child.tag)
  #  print child