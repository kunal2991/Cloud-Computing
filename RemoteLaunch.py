import boto.ec2  
import sys
import time

noOfInstances = int(sys.argv[1])  #Storing the number of instances to be launched from the command line

print "No of instances to be launched------->"+str(noOfInstances)+'\n'

conn = boto.ec2.connect_to_region(sys.argv[2],aws_access_key_id='Your ACCESS KEY goes here',aws_secret_access_key='Your SECRET ACCESS KEY goes here')

#myInstances = ["" for x in range(noOfInstances)]
myInstances = []
for i in range(0,noOfInstances):
	reservation = conn.run_instances("ami-9ff7e8af", instance_type='t2.micro')
	myInstances.append(reservation.instances[0])
	print myInstances

time.sleep(10)

print "Do you want to delete the instances? - Press Y or N\n"
response = raw_input()

if response.lower() in ['y','yes']: 
	for instance in myInstances:
		instance.terminate()
else:
	sys.exit(0)
"""
for instance in myInstances
	instance.instances[0].terminate()
	print myInstances.instances[0]
"""
