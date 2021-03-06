import numpy as np
import nanogen as ng
fname = "meetOct1_Run{0:s}_F{1:s}pN"
forces = [0.03, 0.05, 0.1, 0.2, 0.4, 0.8]

for i in range(1,5):

	for force in forces:
		
		strForce = "{:.2f}".format(force) 
		strFname = fname.format(str(i),strForce)

		print "##########\n##########\n##########\nStarting Simulation of "+strFname+"\n##########\n##########\n##########\n"
		ng.main( strFname, 600, -1, 4, 4, 5, 50000, force, 8000 )
		print "##########\n##########\n##########\nFinished Simulation of "+strFname+"\n###########\n###########\n###########\n"