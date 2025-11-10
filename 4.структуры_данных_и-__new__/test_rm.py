from ResourceManager import ResourceManager

rm1 = ResourceManager (" CPU " , 4, 1)
rm2 = ResourceManager (" GPU " , 2, 2)
rm1.allocate()
rm2.release() 
print ("Capacity: " , rm1.capacity) 
print(rm1.capacity == rm2.capacity)