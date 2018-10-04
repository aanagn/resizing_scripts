import re
import os
path= os.path.dirname(os.path.abspath(__file__))
files = os.listdir(path)
if os.path.exists(path+'/out')==0:
	os.mkdir(path+'/out')
for file in files:
	if '.xml' not in file:
		continue

	outputfilename=path+"/out/"+file #file.replace('.xml','_out.xml')
	with open(outputfilename,"a") as myfile:
		for line in open (file):

			if 'xmin' in line:
				start='<xmin>'
				end='</xmin>'
				s=line
				value=s[s.find(start)+len(start):s.rfind(end)]
				value=int(value)
				print(value)
				printvar = '<xmin>'+str(round(value/5))+'</xmin>'
				myfile.write(printvar+"\n")
			elif 'xmax' in line:
				start='<xmax>'
				end='</xmax>'
				s=line
				value=s[s.find(start)+len(start):s.rfind(end)]
				value=int(value)
				print(value)
				printvar = '<xmax>'+str(round(value/5))+'</xmax>'
				myfile.write(printvar+"\n")
			elif 'ymax' in line:
				start='<ymax>'
				end='</ymax>'
				s=line
				value=s[s.find(start)+len(start):s.rfind(end)]
				value=int(value)
				print(value)
				printvar = '<ymax>'+str(round(value/5))+'</ymax>'
				myfile.write(printvar+"\n")
			elif 'ymin' in line:
				start='<ymin>'
				end='</ymin>'
				s=line
				value=s[s.find(start)+len(start):s.rfind(end)]
				value=int(value)
				print(value)
				printvar = '<ymin>'+str(round(value/5))+'</ymin>'
				myfile.write(printvar+"\n")
			elif 'width' in line:
				start='<width>'
				end='</width>'
				s=line
				value=s[s.find(start)+len(start):s.rfind(end)]
				value=int(value)
				print(value)
				printvar = '<width>'+str(round(value/5))+'</width>'
				myfile.write(printvar+"\n")
			elif 'height' in line:
				start='<height>'
				end='</height>'
				s=line
				value=s[s.find(start)+len(start):s.rfind(end)]
				value=int(value)
				print(value)
				printvar = '<height>'+str(round(value/5))+'</height>'
				myfile.write(printvar+"\n")
			else:
				myfile.write(line)

