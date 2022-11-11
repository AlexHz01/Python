from xml.etree.ElementTree import parse


doc = parse('archivo.xml')
for elemento in doc.findall('nombre'):
    print(elemento.text)
