from xml.dom import minidom

def loadTestData():
    """
    test data is an xml file from the knb data folder.
    this function is just here to speed up pulling it in.
    """
    filename = "data/NIN/knb-lter-nin.0.3.xml"
    testfile = open(filename,'r')
    xmldoc = minidom.parse(testfile)
    testfile.close()
    return xmldoc

def getOneNodeContent(xmldoc, desiredString):
    """
    returns the desired element/its internals based on a string query; does not make to xml or text
    """
    for node in xmldoc.getElementsByTagName(desiredString):
        return node, node.nodeName, node.nodeValue, node.childNodes

def getOneNode(xmldoc, desiredString):
    """
    return the desired element/text element based on a string query
    string is the most internal node you are looking for
    element comes back as an xml string
    """
    for node in xmldoc.getElementsByTagName(desiredString):
        xmltext = node.toxml()
        return str(xmltext)

def getManyNode(xmldoc, desiredString):
    """
    same as getOneNode but gets all the nodes which have the desired string
    """
    results = []
    for node in xmldoc.getElementsByTagName(desiredString):
        results.append(node.toxml())

    if len(results) > 1:
        return results
    elif len(results) == 1:
        return results[0]
    elif len(results) <= 0:
        return "That is not a valid string query"

def cleanTheNode(tagged_node, desiredString):
    left_strip_string = "<" + desiredString + ">"
    right_strip_string = "</" + desiredString + ">"

    cleaned_node = tagged_node.lstrip(left_strip_string).rstrip(right_strip_string)

    return cleaned_node


if __name__ == "__main__":
    myXMLFile = loadTestData()
    print "\n"
    myNodeMemLoc, myRawNodeName, myRawNodeValue, myRawNodeChildren = getOneNodeContent(myXMLFile,'objectName')
    print "Test 1. Gathering the raw XML when gathering from specific string:"
    print "the location of my node is:"
    print myNodeMemLoc
    print "the name of my node is:"
    print myRawNodeName
    print "the value of my node is:"
    print myRawNodeValue
    print "the children of my node are:"
    print myRawNodeChildren
    print "\n"
    print "Test 2. Name of one Node, will default to the last one"
    mySingleNode = getOneNode(myXMLFile,'objectName')
    print mySingleNode
    print "\n"
    print "Test 3. Name of many nodes, if you think you might have more than 1:"
    print "\n"
    myManyNode = getManyNode(myXMLFile,'objectName')
    print myManyNode
    print "\n"
    print "Test 4. Parse the node name to a string for one node (loop this for many node):"
    myCleanNode = cleanTheNode(mySingleNode,'objectName')
    print myCleanNode
