import urllib.request
import re
import sys
import csv

##################################################################
def findTable(data):       ## find the connection     
    strStart = re.search(r'<td>',data);
    strEnd = re.search(r'</td>',data);
    strTmp = data[strStart.end():strEnd.start()];
    return strTmp;

def moveHtml(data):         ## move point to next item
    startPoint = re.search(r'</td>',data);
    data = data[startPoint.end():];
    return data;
    

def main():
    response = urllib.request.urlopen('file:///Users/lishensi/Documents/Processing/HW4/TheTDataCollection/data.html');
    html = response.read();
    html = html.decode('GBK');
    numStations = range((126*2+121*5));
    label = 0;
    writer = csv.writer(open('connections.csv','w', newline=''));   #open csv file
    for i in numStations:
        if i >= (126*2):
            if label == 0:
                label = 1;
            else:
                if label == 1:                      #find from node
                    fromNode = findTable(html);
                    label = 2;
                else:
                    if label == 2:                  #find to node
                        toNode = findTable(html);
                        label = 3;
                    else:
                        if label == 3:              #find color
                            color = findTable(html);
                            label = 4;
                        else:
                            if label == 4:          #find minute
                                minute = findTable(html);
                                label = 0;
                                writer.writerow([fromNode,toNode,color,minute]);    #writer in csv file      
        html = moveHtml(html);
    
    
if __name__=="__main__":
    main();
