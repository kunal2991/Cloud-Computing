import boto.ec2
import sys

conn = boto.ec2.connect_to_region(sys.argv[1],aws_access_key_id='Your ACCESS KEY goes here',aws_secret_access_key='Your SECRET ACCESS KEY goes here')

myList = []

reservation = conn.get_all_reservations()

for instance in reservation:
	print instance.instances[0]
	print instance.instances[0].state

