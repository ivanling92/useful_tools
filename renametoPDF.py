# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 13:34:34 2021

@author: ivanl
"""

import os 
  
# Function to rename multiple files 
def main():
    #filepath = "//paper//"
    for count, filename in enumerate(os.listdir('.')): 
        if not("json" in filename):
            dst = filename + ".pdf"
            src = filename 
            dst = dst 
          
        # rename() function will 
        # rename all the files 
        os.rename(src, dst) 
  
# Driver Code 
if __name__ == '__main__': 
      
    # Calling main() function 
    main() 