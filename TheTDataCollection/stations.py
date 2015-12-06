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

def moveHtml(data):         ##move point to next item
    startPoint = re.search(r'</td>',data);
    data = data[startPoint.end():];
    return data;
    

def main():
    response = urllib.request.urlopen('file:///Users/lishensi/Documents/Processing/HW4/TheTDataCollection/data.html');
    html = response.read();
    html = html.decode('GBK');
    numStations = range(126*2);
    labelStation = 0;
    writer = csv.writer(open('stations.csv','w', newline=''));   #open csv file
    for i in numStations:
        if labelStation == 0:
            strf = findTable(html);
            labelStation = 1;
        else:
            strf = findTable(html);
            labelStation = 0;
            writer.writerow([strf]);        #writer in csv file
#           print(strf);
        html = moveHtml(html);
    
    
if __name__=="__main__":
    main();
