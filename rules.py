
def nodeExist(templateData):
    controlList = []
    #for each node
    for node in templateData["nodes"]:
        #entities do not generate controls
        if node['type'] == 'Entity': continue
        #initialize lists for data flows in input and output
        inputLabels = []
        outputLabels = []
        #iterate over data flows to retrieve input and output
        for link in templateData['links']:
            if (link['target'] == node['id']): inputLabels.append(link['label'])
            if (link['source'] == node['id']): outputLabels.append(link['label'])
        #build control: node existance
        control = 'There is a "' + node['id'] + '" ' + node['type'] + '. '
        #if there are inputs add them
        if len(inputLabels) > 0:
            control += 'It has the following Data Flows in input: '
            control += str(inputLabels).strip('[]') + '. '
        #if there are outputs add them
        if len(outputLabels) > 0:
            control += 'It has the following Data Flows in output: '
            control += str(outputLabels).strip('[]') + '. '
        #add control to the  list
        controlList.append(control)
    return controlList

def nodeC(templateData):
    controlList = []
    #for each node
    for node in templateData["nodes"]:
        #build controls: Confidentiality requirements
        if 'C' in node['flags']: 
            control = 'There is a security measure preserving Confidentiality for the '  + node['type'] + ' "' + node['id'] + '". '
            controlList.append(control)
    return controlList

def nodeI(templateData):
    controlList = []
    #for each node
    for node in templateData["nodes"]:
        #build controls: Integrity requirements
        if 'I' in node['flags']: 
            control = 'There is a security measure preserving Integrity for the '  + node['type'] + ' "' + node['id'] + '". '
            controlList.append(control)
    return controlList


def nodeA(templateData):
    controlList = []
    #for each node
    for node in templateData["nodes"]:
        #build controls: Availability requirements
        if 'A' in node['flags']: 
            control = 'There is a security measure preserving Availability for the '  + node['type'] + ' "' + node['id'] + '". '
            controlList.append(control)
    return controlList

def nodeCIA(templateData):
    controlList = []
    #for each data flow generate controls
    for node in templateData['nodes']:
        control = ""
        #build controls: CIA requirements
        if 'C' in node['flags']:
            control += 'There is a security measure preserving Confidentiality for the '  + node['type'] + ' "' + node['id'] + '". '
        if 'I' in node['flags']:
            control += 'There is a security measure preserving Integrity for the '  + node['type'] + ' "' + node['id'] + '". '
        if 'A' in node['flags']:
            control += 'There is a security measure preserving Availability for the '  + node['type'] + ' "' + node['id'] + '". '
        if(len(control)>0):
            controlList.append(control)
    return controlList


def flowExist(templateData):
    controlList = []
    #for each data flow generate controls
    for flow in templateData['links']:
        #build control: flow existance
        control = 'There is a "' + flow['label'] + '" Data Flow, with type "' + flow['type'] + '" flowing from the Node "'+flow['source']+'" to the Node "'+flow['target']+ '". '
        controlList.append(control)
    return controlList


def flowC(templateData):
    controlList = []
    #for each data flow generate controls
    for flow in templateData['links']:
        #build controls: CIA requirements
        if 'C' in flow['flags']:
            control = 'There is a security measure preserving Confidentiality for the Data Flow with label "' + flow['label'] + '". '
            controlList.append(control)
    return controlList

def flowI(templateData):
    controlList = []
    #for each data flow generate controls
    for flow in templateData['links']:
        #build controls: CIA requirements
        if 'I' in flow['flags']:
            control = 'There is a security measure preserving Integrity for the Data Flow with label "' + flow['label'] + '". '
            controlList.append(control)
    return controlList

def flowA(templateData):
    controlList = []
    #for each data flow generate controls
    for flow in templateData['links']:
        #build controls: CIA requirements
        if 'A' in flow['flags']:
            control = 'There is a security measure preserving Availability for the Data Flow with label "' + flow['label'] + '". '
            controlList.append(control)
    return controlList

def flowP(templateData):
    controlList = []
    #for each data flow generate controls
    for flow in templateData['links']:
        #build controls: privacy requirements
        if flow['type']=='Personal':
            control = 'There is a security measure preserving Privacy requirements for the Personal Data Flow with label "' + flow['label'] + '". '
            controlList.append(control)
    return controlList

def flowCIAP(templateData):
    controlList = []
    #for each data flow generate controls
    for flow in templateData['links']:
        control = ""
        #build controls: CIA requirements
        if 'C' in flow['flags']:
            control += 'There is a security measure preserving Confidentiality for the Data Flow with label "' + flow['label'] + '". '
        if 'I' in flow['flags']:
            control += 'There is a security measure preserving Integrity for the Data Flow with label "' + flow['label'] + '". '
        if 'A' in flow['flags']:
            control += 'There is a security measure preserving Availability for the Data Flow with label "' + flow['label'] + '". '
        if flow['type']=='Personal':
            control += 'There is a security measure preserving Privacy requirements for the Personal Data Flow with label "' + flow['label'] + '". '
        if(len(control)>0):
            controlList.append(control)
    return controlList


def areaExist(templateData):
    controlList = []
    for area in templateData['areas']:
        #initialize list for elements inside the area
        containedNodes = []
        containedFlows = []
        #fill the list with nodes
        for node in templateData['nodes']:
            if area['id'] in node['area']: containedNodes.append(node['id'])
        for flow in templateData['links']:
            if area['id'] in flow['area']: containedFlows.append({'label' : flow['label'], 'source': flow['source'], 'target': flow['target']})
        #build control: area existance
        control = 'The ' + area['type'] + ' "' + area['name'] + '" is defined and well documented. '
        #if the area contains nodes add them
        if(len(containedNodes)>0): 
            control += 'It contains the following Nodes: '
            control += str(containedNodes).strip('[]') + '. '
        #if the area contains data flows add them
        if(len(containedFlows)>0): 
            control += 'It contains the following Data Flows: '
            control += str(containedFlows).strip('[]') + '. '
        #add control to the list
        controlList.append(control)
    return controlList

def areaTrust(templateData):
    controlList = []
    for area in templateData['areas']:
        #build control: the area is a trust area
        if area['type'] == 'Trust Area':
            control = 'There are security measures protecting the boundaries and the elements contained inside of the "' + area['name'] + '" Trust Area. '
            controlList.append(control)
    return controlList

def areaFlowsEnter(templateData):
    controlList = []
    for area in templateData['areas']:
        #initialize list for elements inside the area
        containedNodes = []
        containedFlows = []
        #fill the list with nodes
        for node in templateData['nodes']:
            if area['id'] in node['area']: containedNodes.append(node['id'])
        for flow in templateData['links']:
            if area['id'] in flow['area']: containedFlows.append({'label' : flow['label'], 'source': flow['source'], 'target': flow['target']})
        #build control: data flows entering the area
        for flow in containedFlows:
            if not (flow['source'] in containedNodes):
                control = 'The "' + flow['label'] + '" Data Flow is managed and well documented as it enters the "' + area['name'] + '" ' + area['type'] + '. '
                controlList.append(control)
    return controlList

def areaFlowsExit(templateData):
    controlList = []
    for area in templateData['areas']:
        #initialize list for elements inside the area
        containedNodes = []
        containedFlows = []
        #fill the list with nodes
        for node in templateData['nodes']:
            if area['id'] in node['area']: containedNodes.append(node['id'])
        for flow in templateData['links']:
            if area['id'] in flow['area']: containedFlows.append({'label' : flow['label'], 'source': flow['source'], 'target': flow['target']})
        #build control: data flows exiting the area
        for flow in containedFlows:
            if not (flow['target'] in containedNodes):
                control = 'The "' + flow['label'] + '" Data Flow is managed and well documented as it exits the "' + area['name'] + '" ' + area['type'] + '. '
                controlList.append(control)
    return controlList


#ELEMENT_RULES = [nodeExist, nodeC, nodeI, nodeA, flowExist, flowC, flowI, flowA, flowP]
#AREA_RULES = [areaExist, areaTrust, areaFlowsEnter, areaFlowsExit]

#ELEMENT_RULES = [flowExist]
#AREA_RULES = []

#ELEMENT_RULES = [nodeExist, nodeCIA, flowExist, flowCIAP]
#AREA_RULES = [areaExist, areaTrust, areaFlowsEnter, areaFlowsExit]
