import re
import tkinter as tk
import xlwings as xw
from tkinter import filedialog

############################## Opening correct txt ###################################################
def open_read_file(path):
    Select_File=tk.Tk()
    Select_File.withdraw()
    My_filetypes=[("Text Files","*.txt")]
    path_logs= path
    filename=filedialog.askopenfilename(parent=Select_File, initialdir= path_logs, title="Select a file", filetypes=My_filetypes)
    log = open(filename, 'r')
    Select_File.destroy()
    content = log.read() # Read the entire content of the file as a single string
    log.close()
    return content

########################## Regexing the content of content ################################################
def regex_content(content):
    pattern_line= r"(\w{7,})\s+(\d{4}-\d{2}-\d{2})\s+(\d{1,3})\s+(\S{1,3})\s+(\d{1,3})\s+(\d{1,3})\s+(\S+)"
    pattern_line_found= re.findall(pattern_line ,content)
    #print(pattern_line_found)
    #print(len(pattern_line_found))
    #for i in pattern_line_found:
    #    print(i)
    return pattern_line_found

########################### Creating a list to exchange columns ###########################################
def exchange_columns(pattern_line_found):
    new_list=[]

    for l in pattern_line_found:
        new_list.append(list(l))
    for i in new_list:
        i[0], i[1] = i[1], i[0]
    
    return new_list

##################### Creating the list ####################################################################
def create_list(new_list):
    for n in range(34):
        #print(n)
        if n <= 13: #Computadoras
            new_list[n].insert(2, "N/A")
            new_list[n].insert(6, "Ok")
            new_list[n].insert(7, "Ok")
            new_list[n].insert(9, "No") #Confirmar en el excel si se pintan de color rojo los mayores a 28
            new_list[n].insert(11, "JCM")
            if new_list[n][1] in ["izopsws4", "izopsws5", "izengws1", "izengws2", "izengdss1", "mx3dss1"]:
                new_list[n].insert(3, "N/A")
            else:
                new_list[n].insert(3, "Ok")
        else: #Servidores
            new_list[n].insert(2, "Ok")
            new_list[n].insert(3, "N/A")
            new_list[n].insert(7, "Ok")
            new_list[n].insert(8, "Ok")
            new_list[n].insert(10, "No")
            new_list[n].insert(12, "JCM")
    return new_list



    #for i in new_list:
        #print(i)

################## Writting in Excel #########################################################################
def write_excel(new_list):
    wb= xw.Book('Registro Mantenimientos Iztapalapa - dummy.xlsm')
    sheet= wb.sheets['Equipos']
    #row= sheet.range("A11").end("down").row+1
    row= sheet.range('A' + str(sheet.cells.last_cell.row)).end('up').row+1
    sheet.range(f"A{row}:M{row+len(new_list)}").value=new_list
    #wb.save()
    #wb.close()


try:
    content= open_read_file("C:\\Users\Joel\Documents\Python\logs_generator\automate_fill")
    pattern_line_found= regex_content(content)
    #print(len(pattern_line_found))
    if len(pattern_line_found) == 34:
        new_list= exchange_columns(pattern_line_found)
        list_xl= create_list(new_list)
        write_excel(list_xl)
    else:
        print("Se finalizó la automatización porque no se encuentran todos los equipos")
except:
    print("Se ha finalizado la automatización")
