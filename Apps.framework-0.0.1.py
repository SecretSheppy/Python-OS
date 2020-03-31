#Python OS Apps framework:

#imports
import os

#functions
def Directory_Creation():
    try:
        #making the directory for the App
        os.mkdir("__apps__/" + "<your file name here>")

        #you can delete this - only the initial status report
        Operation_Successful = True

        return(Operation_Successful)

    except FileExistsError:
        #if the directory already exists

        #you can delete this - only the initial status report
        Operation_Successful = False

        return(Operation_Successful)

#main script

#you can delete this - only the initial status report
Operation_Successful = Directory_Creation()

print("Directory :: Status :: " + Operation_Successful)