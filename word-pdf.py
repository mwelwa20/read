from docx2pdf import convert

try:
    print(" \n ************** word To PDF converter ********\n ")
    inputDoc = input("Enter the Word File Name to Convert: ")
    outputPDF = input("Enter File Name to save as PDf: ")

    convert( inputDoc + ".docx",outputPDF + ".pdf")
    print("\n Success! ")
except:
    print("\n Something went Wrong \n")
