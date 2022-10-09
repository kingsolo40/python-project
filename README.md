# python-project

CloudRock Ltd is a multinational consultancy company that already has some infrastructure in AWS.

The company wants to make use of these new AMIs in the following regions. 

 

In eu-west-2 they want to provision this ami  - ami- 0d729d2846a86a9e7, 

in eu-west-1 this ami-  ami-0c1bc246476a5572b

In, us-east-1 this ami ami-0022f774911c1d690

 

#(Tasks)

Create a list of all the 3 amis and assign it to a variable called ami_list

 

#(Create a) 

for loop and loop through the ami_list variable and print each ami out

 

#(Create a)

tuple of all the 3 amis and assign it to a variable called regions_tuple

 

#(Create a) 

for loop and loop through the   regions_tuple variable and print out the ami name if the region is equal to   us-east-1 (hint: use if clause inside for loop)

 
#(creating dictionary)

Create a dictionary which is a key-value pair of region to ami and assign it to a variable called 

region_ami_dict

 

#(Create a) 

for loop and loop through the   regions_tuple variable and print each region

 

#(Import the)

 boto3 library and get a list of available resources from your aws account  using the get_available_resources() function ( refer to the lecture video on boto3)

 
