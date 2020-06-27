import tensorwatch as tw
import time
import pyshark

# streams will be stored in test.log file
w = tw.Watcher(filename='test.log')

# create a stream for logging
s = w.create_stream(name='metric1')

# generate Jupyter Notebook to view real-time streams
w.make_notebook()

#initialize the pyshark capture module
cap =pyshark.LiveCapture(interface='wlan0')

i=0

for packet in cap.sniff_continuously():
	if 'IP' in packet:
		#print(packet)
		#print(packet.ip.field_names)
		print(packet.ip.ttl, i)
		#print(packet.ip.flags)
		#print("Source: "+packet.ip.src+" Destination: "+packet.ip.dst)
		s.write(int(packet.ip.ttl), i)
		i=i+1
