file1 = open("myfile.txt","w")
L = ["This is Delhi \n","This is Paris \n","This is London \n"] 
  
# \n is placed to indicate EOL (End of Line)
file1.write("Hello \n")
file1.writelines(L)
file1.close()

file1 = open("other.txt","w")
L = ["This is Pune \n","This is Paris \n","This is London \n"] 
  
# \n is placed to indicate EOL (End of Line)
file1.write("Hello \n")
file1.writelines(L)
file1.close()

