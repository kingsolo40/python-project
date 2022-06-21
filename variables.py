# AMI to be provisioned in 
#eu-west-2: ami- 0d729d2846a86a9e7, 
#in eu-west-1: ami-0c1bc246476a5572b
#In, us-east-1: ami-0022f774911c1d690

 #list of all the 3 amis, assigned to a variable called ami_list
ami_list =  ["ami- 0d729d2846a86a9e7","ami-0c1bc246476a5572b","ami-0022f774911c1d690"]
print (ami_list)
 
 #for loop through the ami_list variable and print each ami out
ami_list = ["ami- 0d729d2846a86a9e7","ami-0c1bc246476a5572b","ami-0022f774911c1d690"]
for ami in ami_list :
      print (ami)

 #tuple of all the 3 amis and assign it to a variable called regions_tuple
regions_tuple = ("eu-west-2","eu-west-1","us-east-1")
print (regions_tuple)
for region in regions_tuple:
     print (region) 
     
 #print out the ami name if the region is equal to   us-east-1         
if region == "us-east-1" :
     print ("ami-0022f774911c1d690")

#a key-value pair of region:ami. And assigned it to a variable called region_ami_dict
region_ami_dict = {"eu-west-2" :"ami- 0d729d2846a86a9e7", "eu-west-1" : "ami-0c1bc246476a5572b", "us-east-1" : "ami-0022f774911c1d690"}
print (region_ami_dict)

#for loop and loop through the region_ami_dict and each key pair value
for dict in region_ami_dict.items():
     print (dict)
