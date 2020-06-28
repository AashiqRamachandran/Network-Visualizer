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
	if 'TCP' in packet:
		print(packet)
		#print(packet.udp.field_names)
		#print(packet.udp.time_delta,packet.ip.ttl)
		#print(packet.ip.flags)
		#print("Source: "+packet.ip.src+" Destination: "+packet.ip.dst)
		#s.write(float(packet.udp.time_delta), float(packet.ip.ttl) )
		#i=i+1
