import os
import re


####### Week 2 - Assignment 
path = os.getcwd()
print path

os.chdir('C:\Users\murugesan.r\Downloads')

## Looping through each line ##


file_1 = open('regex_sum_210495.txt')

for each in file_1:
    words = each.split()
      
    
    for word in words:
        print word
        
sum_list2 = 0
sum_list = 0


count = 0
for line in file_1:
    
    print line
    #sum_list += sum([int(x) for x in re.findall('[0-9.]+',line.strip())])
    count += 1
    
    if(count == 5):
        break
    
file_2 = open('regex_sum_42.txt')
for line_2 in file_2:
    
    print re.findall('[0-9]+',line_2)
    sum_list2 += sum([int(x) for x in re.findall('[0-9.]+',line_2)])
        
        
########## Week 3 - Assignment 

import socket

my_soc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
my_soc.connect(('www.pythonlearn.com',80))

my_soc.send('GET http://www.pythonlearn.com/code/intro-short.txt HTTP/1.0 \n\n')

print my_soc.recv(1024)


#################### Week 4 assignment  Week 4 part 2
import re
import os
path = os.getcwd()
print path

os.chdir('C:\Users\murugesan.r\Downloads')

from BeautifulSoup import *
import urllib


url_user = raw_input('Enter the url:  ')
pos_user = int(raw_input('Enter position: '))
rep_user = int(raw_input('Enter repetition:' ))

#req_soup = soup_1('a')

def  name_loop(req_soup,pos,count_pos):
    
    for each in req_soup:
        url_each = each.get('href',None)
        name = re.findall('>(.*)<',str(each))
        
        if count_pos == pos:
            
            
            print 'Retreiving: ',url_each
            url_new = urllib.urlopen(url_each).read()
            soup_new = BeautifulSoup(url_new)                    
                            
            return ([soup_new,name[0]])
        
        count_pos += 1


#Run the program from here

url_file = urllib.urlopen(url_user).read()
soup_1 = BeautifulSoup(url_file)

pos = pos_user
count_pos = 1
rep_value = rep_user

for rep in range(1,rep_value+1):
    
    
    soup_new_val = name_loop(soup_1('a'),pos,count_pos)
    soup_1 = soup_new_val[0]
    
    if(rep == rep_value):
        print soup_new_val[1]

######################################### Week 4 part 1

import re
import os
path = os.getcwd()
print path

os.chdir('C:\Users\murugesan.r\Downloads')

from BeautifulSoup import *
import urllib

url_get = raw_input('Enter URL: ')

url_file = urllib.urlopen(url_get).read()
soup = BeautifulSoup(url_file)

count = 0
sum_val = 0 
for each in soup('span'):
    x = each.contents
    sum_val += int(each.contents[0])
    count += 1
    
    
###################### Week 5 Assignment ###########################
    
import urllib
import xml.etree.ElementTree as ET

url_xml = raw_input('Enter the url which containts xml: ')

web_xml = urllib.urlopen(url_xml)

xml_data = web_xml.read()

xml_parse = ET.fromstring(xml_data)

#xml_parse is created with element 'commentinfo' as the base
#So you can't go about and search that again
# You can start with next avaiable tag - note, comments, name, count...


all_counts = xml_parse.findall('.//count')

sum_val = sum([int(each_c.text) for each_c in all_counts])
print sum_val


########################### Week 6 Assignment 

#JSON is either a list or a dictionary
#Java has arrays and hash maps
# Python has list and dictionary. JSON is kinda similar to python
#

# For using twitter API using (OATH), see the Week6 last video of 
# Python specialization(Programming for Everybody)'s 3rd course
# Accessing web data using Python 
#// Else use Stack overflow to see how to use OATH


import urllib
import json

url_read = raw_input('Enter the url to be read: ')

url_file = urllib.urlopen(url_read)

url_header = url_file.info()

url_body = url_file.read()

json_data = json.loads(url_body)

print(json_data)

#With proper indetation format
print json.dumps(json_data,indent = 4)

sum_value = sum([int(dict_val['count']) for dict_val in json_data['comments']])

print sum_value



# Week 6 assignment 2 ###################################

import urllib
import json

url_original = 'http://python-data.dr-chuck.net/geojson?'

place = raw_input('Enter the location: ')

url_total = url_original + urllib.urlencode({'sensor': 'false', 'address': place})
url_file1 = urllib.urlopen(url_total).read()

print "Retrieved data of length", len(url_file1)


try: json_data = json.loads(str(url_file1))
except: json_data = None

if 'status' not in json_data or json_data['status'] != "OK":
    print "===============Failed to retrieve==========="

print json.dumps(json_data, indent = 4)


print "Place id:", json_data['results'][0]['place_id']














    
