```python
# Open the file in read mode ('r')
log = open(r'C:\Users\Joel\Documents\Python\logs_generator\automate_fill\2025-11-10.txt', 'r')

# Read the entire content of the file as a single string
content = log.read()
print(content)

# Close the file
log.close()
```

    Hostname	Date Y-M-D	%C/home	%D/root	%RAMuse	DaysUp	OpMan	Execution_time
    izopsws1	2025-11-10	67	N/A	60	6	N/A	2025-11-10 09:00:00.770836
    izopsws2	2025-11-10	71	N/A	54	5	N/A	2025-11-10 09:02:00.637555
    izopsws3	2025-11-10	76	N/A	44	7	N/A	2025-11-10 09:04:00.806376
    izopsws4	2025-11-10	81	N/A	34	5	N/A	2025-11-10 09:06:01.214880
    izopsws5	2025-11-10	80	N/A	48	2	N/A	2025-11-10 09:08:00.813388
    izengws1	2025-11-10	10	N/A	57	3	N/A	2025-11-10 09:10:00.989853
    izengws2	2025-11-10	53	N/A	42	3	N/A	2025-11-10 09:12:01.908494
    izengws3	2025-11-10	31	N/A	44	7	N/A	2025-11-10 09:14:02.092179
    izengws4	2025-11-10	80	N/A	30	5	N/A	2025-11-10 09:16:02.608688
    izengws5	2025-11-10	80	N/A	31	2	N/A	2025-11-10 09:18:01.355615
    izengws6	2025-11-10	79	N/A	35	3	N/A	2025-11-10 09:20:01.904900
    izengws7	2025-11-10	41	N/A	28	3	N/A	2025-11-10 09:22:01.217746
    izengdss1	2025-11-10	13	90	1	3	N/A	2025-11-10 09:24:02.439180
    mx3dss1	2025-11-10	72	N/A	29	3	N/A	2025-11-10 09:26:01.157407
    izopsfep0	2025-11-10	53	72	16	12	Ok	2025-11-10 09:28:02.265922
    izopsfep2	2025-11-10	79	72	11	12	Ok	2025-11-10 09:30:02.281922
    izopsfep3	2025-11-10	85	72	13	12	Ok	2025-11-10 09:32:02.227168
    izopsgs1	2025-11-10	21	93	19	11	Ok	2025-11-10 09:34:04.277518
    izopsgs2	2025-11-10	16	94	18	11	Ok	2025-11-10 09:36:01.777264
    izopsmc1	2025-11-10	31	67	18	11	Ok	2025-11-10 09:38:01.255012
    izopsmc2	2025-11-10	37	100	14	11	Ok	2025-11-10 09:40:01.264766
    izengnas0	2025-11-10	76	27	29	10	Revisar	2025-11-10 09:42:18.511156
    izengnas2	2025-11-10	77	27	20	9	Revisar	2025-11-10 09:44:05.685054
    izengnas3	2025-11-10	93	35	20	9	Revisar	2025-11-10 09:46:05.886556
    izenggs1	2025-11-10	15	63	33	10	Ok	2025-11-10 09:48:01.882736
    izenggs2	2025-11-10	18	63	54	10	Ok	2025-11-10 09:50:05.244636
    izengfep1	2025-11-10	45	80	25	10	Ok	2025-11-10 09:52:02.408157
    izengarc1	2025-11-10	95	79	7	10	Ok	2025-11-10 09:54:02.253158
    izengcds1	2025-11-10	39	10	26	2	Ok	2025-11-10 09:56:07.515762
    izengcps1	2025-11-10	2	98	17	9	Ok	2025-11-10 09:58:03.063787
    izm3tmc1	2025-11-10	71	97	18	10	Ok	2025-11-10 10:00:03.129241
    izm3tmc2	2025-11-10	47	90	36	10	Revisar	2025-11-10 10:02:06.978787
    mnc_a_mexcity	2025-11-10	53	61	9	11	Ok	2025-11-10 09:56:00.824747
    mnc_b_mexcity	2025-11-10	44	46	13	11	Ok	2025-11-10 09:57:00.463328
    \\izengnas0\d$\NFS_backup\ground_2025_w44_backup.iso -> F:\Backup\archive\IZT\2025\GROUND\ground_2025_w44_backup.iso
    \\izengnas0\d$\NFS_backup\ground_2025_w44_backup.iso.log -> F:\Backup\archive\IZT\2025\GROUND\ground_2025_w44_backup.iso.log
    \\izengnas0\d$\NFS_backup\ground_2025_w44_backup.log -> F:\Backup\archive\IZT\2025\GROUND\ground_2025_w44_backup.log
    3 File(s) copied
    \\hmengnas0\d$\NFS_backup\ground_2025_w44_backup.iso -> F:\Backup\archive\HMO\2025\GROUND\ground_2025_w44_backup.iso
    \\hmengnas0\d$\NFS_backup\ground_2025_w44_backup.iso.log -> F:\Backup\archive\HMO\2025\GROUND\ground_2025_w44_backup.iso.log
    \\hmengnas0\d$\NFS_backup\ground_2025_w44_backup.log -> F:\Backup\archive\HMO\2025\GROUND\ground_2025_w44_backup.log
    3 File(s) copied
    \\izengnas0\d$\NFS_backup\mx3_2025_w44_backup.iso -> F:\Backup\archive\IZT\2025\MX3\mx3_2025_w44_backup.iso
    1 File(s) copied
    \\hmengnas0\d$\NFS_backup\mx3_2025_w44_backup.iso -> F:\Backup\archive\HMO\2025\MX3\mx3_2025_w44_backup.iso
    1 File(s) copied
    
    


```python
import re

pattern_line= r"(\w{7,})\s+(\d{4}-\d{2}-\d{2})\s+(\d{1,3})\s+(\S{1,3})\s+(\d{1,3})\s+(\d{1,3})\s+(\S+)"
pattern_line_found= re.findall(pattern_line ,content)
#print(pattern_line_finded)
print(len(pattern_line_found))

for i in pattern_line_found:
    print(i)

print(pattern_line_found[0][1])
```

    34
    ('izopsws1', '2025-11-10', '67', 'N/A', '60', '6', 'N/A')
    ('izopsws2', '2025-11-10', '71', 'N/A', '54', '5', 'N/A')
    ('izopsws3', '2025-11-10', '76', 'N/A', '44', '7', 'N/A')
    ('izopsws4', '2025-11-10', '81', 'N/A', '34', '5', 'N/A')
    ('izopsws5', '2025-11-10', '80', 'N/A', '48', '2', 'N/A')
    ('izengws1', '2025-11-10', '10', 'N/A', '57', '3', 'N/A')
    ('izengws2', '2025-11-10', '53', 'N/A', '42', '3', 'N/A')
    ('izengws3', '2025-11-10', '31', 'N/A', '44', '7', 'N/A')
    ('izengws4', '2025-11-10', '80', 'N/A', '30', '5', 'N/A')
    ('izengws5', '2025-11-10', '80', 'N/A', '31', '2', 'N/A')
    ('izengws6', '2025-11-10', '79', 'N/A', '35', '3', 'N/A')
    ('izengws7', '2025-11-10', '41', 'N/A', '28', '3', 'N/A')
    ('izengdss1', '2025-11-10', '13', '90', '1', '3', 'N/A')
    ('mx3dss1', '2025-11-10', '72', 'N/A', '29', '3', 'N/A')
    ('izopsfep0', '2025-11-10', '53', '72', '16', '12', 'Ok')
    ('izopsfep2', '2025-11-10', '79', '72', '11', '12', 'Ok')
    ('izopsfep3', '2025-11-10', '85', '72', '13', '12', 'Ok')
    ('izopsgs1', '2025-11-10', '21', '93', '19', '11', 'Ok')
    ('izopsgs2', '2025-11-10', '16', '94', '18', '11', 'Ok')
    ('izopsmc1', '2025-11-10', '31', '67', '18', '11', 'Ok')
    ('izopsmc2', '2025-11-10', '37', '100', '14', '11', 'Ok')
    ('izengnas0', '2025-11-10', '76', '27', '29', '10', 'Revisar')
    ('izengnas2', '2025-11-10', '77', '27', '20', '9', 'Revisar')
    ('izengnas3', '2025-11-10', '93', '35', '20', '9', 'Revisar')
    ('izenggs1', '2025-11-10', '15', '63', '33', '10', 'Ok')
    ('izenggs2', '2025-11-10', '18', '63', '54', '10', 'Ok')
    ('izengfep1', '2025-11-10', '45', '80', '25', '10', 'Ok')
    ('izengarc1', '2025-11-10', '95', '79', '7', '10', 'Ok')
    ('izengcds1', '2025-11-10', '39', '10', '26', '2', 'Ok')
    ('izengcps1', '2025-11-10', '2', '98', '17', '9', 'Ok')
    ('izm3tmc1', '2025-11-10', '71', '97', '18', '10', 'Ok')
    ('izm3tmc2', '2025-11-10', '47', '90', '36', '10', 'Revisar')
    ('mnc_a_mexcity', '2025-11-10', '53', '61', '9', '11', 'Ok')
    ('mnc_b_mexcity', '2025-11-10', '44', '46', '13', '11', 'Ok')
    2025-11-10
    


```python
from datetime import datetime

#print(pattern_line_finded[0][1])
date_year=str(pattern_line_found[0][1])[:4]
date_month=str(pattern_line_found[0][1])[-5:-3]
date_day=str(pattern_line_found[0][1])[-2:]
#print(date_year)
#print(date_month)
#print(date_day)


date_xl=datetime(int(date_year), int(date_month), int(date_day))
#print(date_year)
#ans=datetime(int(year),int(month),int(day),int(hour),int(minute)).timestamp()-J2000.timestamp()
#print(ans)
#print(ans.days*60*60*24+ans.seconds)

formatted_date = date_xl.strftime("%b-%d-%Y")
print(str(formatted_date).lower())
```

    nov-10-2025
    


```python
#print(pattern_line_found)
#print(list(pattern_line_found[0]))
pattern_line_found_list= list(pattern_line_found[0])
print(pattern_line_found_list)
pattern_line_found_list[1]= str(formatted_date).lower()
print(pattern_line_found_list)

#for i in pattern_line_finded:
    #print(i)
```

    ['izopsws1', '2025-11-10', '67', 'N/A', '60', '6', 'N/A']
    ['izopsws1', 'nov-10-2025', '67', 'N/A', '60', '6', 'N/A']
    


```python
#print(pattern_line_found)
new_list=[]

for i in pattern_line_found:
    new_list.append(list(i))

for j in new_list:
    #print(j)
    j[1]= str(formatted_date).lower()
    print(j)

#print(new_list)
```

    ['izopsws1', 'nov-10-2025', '67', 'N/A', '60', '6', 'N/A']
    ['izopsws2', 'nov-10-2025', '71', 'N/A', '54', '5', 'N/A']
    ['izopsws3', 'nov-10-2025', '76', 'N/A', '44', '7', 'N/A']
    ['izopsws4', 'nov-10-2025', '81', 'N/A', '34', '5', 'N/A']
    ['izopsws5', 'nov-10-2025', '80', 'N/A', '48', '2', 'N/A']
    ['izengws1', 'nov-10-2025', '10', 'N/A', '57', '3', 'N/A']
    ['izengws2', 'nov-10-2025', '53', 'N/A', '42', '3', 'N/A']
    ['izengws3', 'nov-10-2025', '31', 'N/A', '44', '7', 'N/A']
    ['izengws4', 'nov-10-2025', '80', 'N/A', '30', '5', 'N/A']
    ['izengws5', 'nov-10-2025', '80', 'N/A', '31', '2', 'N/A']
    ['izengws6', 'nov-10-2025', '79', 'N/A', '35', '3', 'N/A']
    ['izengws7', 'nov-10-2025', '41', 'N/A', '28', '3', 'N/A']
    ['izengdss1', 'nov-10-2025', '13', '90', '1', '3', 'N/A']
    ['mx3dss1', 'nov-10-2025', '72', 'N/A', '29', '3', 'N/A']
    ['izopsfep0', 'nov-10-2025', '53', '72', '16', '12', 'Ok']
    ['izopsfep2', 'nov-10-2025', '79', '72', '11', '12', 'Ok']
    ['izopsfep3', 'nov-10-2025', '85', '72', '13', '12', 'Ok']
    ['izopsgs1', 'nov-10-2025', '21', '93', '19', '11', 'Ok']
    ['izopsgs2', 'nov-10-2025', '16', '94', '18', '11', 'Ok']
    ['izopsmc1', 'nov-10-2025', '31', '67', '18', '11', 'Ok']
    ['izopsmc2', 'nov-10-2025', '37', '100', '14', '11', 'Ok']
    ['izengnas0', 'nov-10-2025', '76', '27', '29', '10', 'Revisar']
    ['izengnas2', 'nov-10-2025', '77', '27', '20', '9', 'Revisar']
    ['izengnas3', 'nov-10-2025', '93', '35', '20', '9', 'Revisar']
    ['izenggs1', 'nov-10-2025', '15', '63', '33', '10', 'Ok']
    ['izenggs2', 'nov-10-2025', '18', '63', '54', '10', 'Ok']
    ['izengfep1', 'nov-10-2025', '45', '80', '25', '10', 'Ok']
    ['izengarc1', 'nov-10-2025', '95', '79', '7', '10', 'Ok']
    ['izengcds1', 'nov-10-2025', '39', '10', '26', '2', 'Ok']
    ['izengcps1', 'nov-10-2025', '2', '98', '17', '9', 'Ok']
    ['izm3tmc1', 'nov-10-2025', '71', '97', '18', '10', 'Ok']
    ['izm3tmc2', 'nov-10-2025', '47', '90', '36', '10', 'Revisar']
    ['mnc_a_mexcity', 'nov-10-2025', '53', '61', '9', '11', 'Ok']
    ['mnc_b_mexcity', 'nov-10-2025', '44', '46', '13', '11', 'Ok']
    

## Intercambiando columnas


```python
for i in new_list:
    #print(i)
    i[0], i[1] = i[1], i[0]
    print(i)
#new_list[0], new_list[1] = new_list[1], new_list[0]


```

    ['nov-10-2025', 'izopsws1', '67', 'N/A', '60', '6', 'N/A']
    ['nov-10-2025', 'izopsws2', '71', 'N/A', '54', '5', 'N/A']
    ['nov-10-2025', 'izopsws3', '76', 'N/A', '44', '7', 'N/A']
    ['nov-10-2025', 'izopsws4', '81', 'N/A', '34', '5', 'N/A']
    ['nov-10-2025', 'izopsws5', '80', 'N/A', '48', '2', 'N/A']
    ['nov-10-2025', 'izengws1', '10', 'N/A', '57', '3', 'N/A']
    ['nov-10-2025', 'izengws2', '53', 'N/A', '42', '3', 'N/A']
    ['nov-10-2025', 'izengws3', '31', 'N/A', '44', '7', 'N/A']
    ['nov-10-2025', 'izengws4', '80', 'N/A', '30', '5', 'N/A']
    ['nov-10-2025', 'izengws5', '80', 'N/A', '31', '2', 'N/A']
    ['nov-10-2025', 'izengws6', '79', 'N/A', '35', '3', 'N/A']
    ['nov-10-2025', 'izengws7', '41', 'N/A', '28', '3', 'N/A']
    ['nov-10-2025', 'izengdss1', '13', '90', '1', '3', 'N/A']
    ['nov-10-2025', 'mx3dss1', '72', 'N/A', '29', '3', 'N/A']
    ['nov-10-2025', 'izopsfep0', '53', '72', '16', '12', 'Ok']
    ['nov-10-2025', 'izopsfep2', '79', '72', '11', '12', 'Ok']
    ['nov-10-2025', 'izopsfep3', '85', '72', '13', '12', 'Ok']
    ['nov-10-2025', 'izopsgs1', '21', '93', '19', '11', 'Ok']
    ['nov-10-2025', 'izopsgs2', '16', '94', '18', '11', 'Ok']
    ['nov-10-2025', 'izopsmc1', '31', '67', '18', '11', 'Ok']
    ['nov-10-2025', 'izopsmc2', '37', '100', '14', '11', 'Ok']
    ['nov-10-2025', 'izengnas0', '76', '27', '29', '10', 'Revisar']
    ['nov-10-2025', 'izengnas2', '77', '27', '20', '9', 'Revisar']
    ['nov-10-2025', 'izengnas3', '93', '35', '20', '9', 'Revisar']
    ['nov-10-2025', 'izenggs1', '15', '63', '33', '10', 'Ok']
    ['nov-10-2025', 'izenggs2', '18', '63', '54', '10', 'Ok']
    ['nov-10-2025', 'izengfep1', '45', '80', '25', '10', 'Ok']
    ['nov-10-2025', 'izengarc1', '95', '79', '7', '10', 'Ok']
    ['nov-10-2025', 'izengcds1', '39', '10', '26', '2', 'Ok']
    ['nov-10-2025', 'izengcps1', '2', '98', '17', '9', 'Ok']
    ['nov-10-2025', 'izm3tmc1', '71', '97', '18', '10', 'Ok']
    ['nov-10-2025', 'izm3tmc2', '47', '90', '36', '10', 'Revisar']
    ['nov-10-2025', 'mnc_a_mexcity', '53', '61', '9', '11', 'Ok']
    ['nov-10-2025', 'mnc_b_mexcity', '44', '46', '13', '11', 'Ok']
    


```python
for i in new_list:
    print (i)
```

    ['nov-10-2025', 'izopsws1', '67', 'N/A', '60', '6', 'N/A']
    ['nov-10-2025', 'izopsws2', '71', 'N/A', '54', '5', 'N/A']
    ['nov-10-2025', 'izopsws3', '76', 'N/A', '44', '7', 'N/A']
    ['nov-10-2025', 'izopsws4', '81', 'N/A', '34', '5', 'N/A']
    ['nov-10-2025', 'izopsws5', '80', 'N/A', '48', '2', 'N/A']
    ['nov-10-2025', 'izengws1', '10', 'N/A', '57', '3', 'N/A']
    ['nov-10-2025', 'izengws2', '53', 'N/A', '42', '3', 'N/A']
    ['nov-10-2025', 'izengws3', '31', 'N/A', '44', '7', 'N/A']
    ['nov-10-2025', 'izengws4', '80', 'N/A', '30', '5', 'N/A']
    ['nov-10-2025', 'izengws5', '80', 'N/A', '31', '2', 'N/A']
    ['nov-10-2025', 'izengws6', '79', 'N/A', '35', '3', 'N/A']
    ['nov-10-2025', 'izengws7', '41', 'N/A', '28', '3', 'N/A']
    ['nov-10-2025', 'izengdss1', '13', '90', '1', '3', 'N/A']
    ['nov-10-2025', 'mx3dss1', '72', 'N/A', '29', '3', 'N/A']
    ['nov-10-2025', 'izopsfep0', '53', '72', '16', '12', 'Ok']
    ['nov-10-2025', 'izopsfep2', '79', '72', '11', '12', 'Ok']
    ['nov-10-2025', 'izopsfep3', '85', '72', '13', '12', 'Ok']
    ['nov-10-2025', 'izopsgs1', '21', '93', '19', '11', 'Ok']
    ['nov-10-2025', 'izopsgs2', '16', '94', '18', '11', 'Ok']
    ['nov-10-2025', 'izopsmc1', '31', '67', '18', '11', 'Ok']
    ['nov-10-2025', 'izopsmc2', '37', '100', '14', '11', 'Ok']
    ['nov-10-2025', 'izengnas0', '76', '27', '29', '10', 'Revisar']
    ['nov-10-2025', 'izengnas2', '77', '27', '20', '9', 'Revisar']
    ['nov-10-2025', 'izengnas3', '93', '35', '20', '9', 'Revisar']
    ['nov-10-2025', 'izenggs1', '15', '63', '33', '10', 'Ok']
    ['nov-10-2025', 'izenggs2', '18', '63', '54', '10', 'Ok']
    ['nov-10-2025', 'izengfep1', '45', '80', '25', '10', 'Ok']
    ['nov-10-2025', 'izengarc1', '95', '79', '7', '10', 'Ok']
    ['nov-10-2025', 'izengcds1', '39', '10', '26', '2', 'Ok']
    ['nov-10-2025', 'izengcps1', '2', '98', '17', '9', 'Ok']
    ['nov-10-2025', 'izm3tmc1', '71', '97', '18', '10', 'Ok']
    ['nov-10-2025', 'izm3tmc2', '47', '90', '36', '10', 'Revisar']
    ['nov-10-2025', 'mnc_a_mexcity', '53', '61', '9', '11', 'Ok']
    ['nov-10-2025', 'mnc_b_mexcity', '44', '46', '13', '11', 'Ok']
    


```python
original_list = [[1, 2, 3, 4],
                 [5, 6, 7, 8],
                 [9, 10, 11, 12]]

# Swap column at index 1 with column at index 3 in-place
for row in original_list:
    row[1], row[3] = row[3], row[1]

print(original_list)
```

    [[1, 4, 3, 2], [5, 8, 7, 6], [9, 12, 11, 10]]
    


```python
t= [1, 2, 3, 4]
print(t)

t[1], t[3] = t[3], t[1]


print(t)
```

    [1, 2, 3, 4]
    [1, 4, 3, 2]
    


```python
### Para computadoras ###

for n in range(14):
    print(new_list[n])
    new_list[n].insert(1, "N/A")
```

    ['nov-10-2025', 'izopsws1', '67', 'N/A', '60', '6', 'N/A']
    ['nov-10-2025', 'izopsws2', '71', 'N/A', '54', '5', 'N/A']
    ['nov-10-2025', 'izopsws3', '76', 'N/A', '44', '7', 'N/A']
    ['nov-10-2025', 'izopsws4', '81', 'N/A', '34', '5', 'N/A']
    ['nov-10-2025', 'izopsws5', '80', 'N/A', '48', '2', 'N/A']
    ['nov-10-2025', 'izengws1', '10', 'N/A', '57', '3', 'N/A']
    ['nov-10-2025', 'izengws2', '53', 'N/A', '42', '3', 'N/A']
    ['nov-10-2025', 'izengws3', '31', 'N/A', '44', '7', 'N/A']
    ['nov-10-2025', 'izengws4', '80', 'N/A', '30', '5', 'N/A']
    ['nov-10-2025', 'izengws5', '80', 'N/A', '31', '2', 'N/A']
    ['nov-10-2025', 'izengws6', '79', 'N/A', '35', '3', 'N/A']
    ['nov-10-2025', 'izengws7', '41', 'N/A', '28', '3', 'N/A']
    ['nov-10-2025', 'izengdss1', '13', '90', '1', '3', 'N/A']
    ['nov-10-2025', 'mx3dss1', '72', 'N/A', '29', '3', 'N/A']
    


```python
for i in new_list:
    print(i)
```

    ['nov-10-2025', 'N/A', 'izopsws1', '67', 'N/A', '60', '6', 'N/A']
    ['nov-10-2025', 'N/A', 'izopsws2', '71', 'N/A', '54', '5', 'N/A']
    ['nov-10-2025', 'N/A', 'izopsws3', '76', 'N/A', '44', '7', 'N/A']
    ['nov-10-2025', 'N/A', 'izopsws4', '81', 'N/A', '34', '5', 'N/A']
    ['nov-10-2025', 'N/A', 'izopsws5', '80', 'N/A', '48', '2', 'N/A']
    ['nov-10-2025', 'N/A', 'izengws1', '10', 'N/A', '57', '3', 'N/A']
    ['nov-10-2025', 'N/A', 'izengws2', '53', 'N/A', '42', '3', 'N/A']
    ['nov-10-2025', 'N/A', 'izengws3', '31', 'N/A', '44', '7', 'N/A']
    ['nov-10-2025', 'N/A', 'izengws4', '80', 'N/A', '30', '5', 'N/A']
    ['nov-10-2025', 'N/A', 'izengws5', '80', 'N/A', '31', '2', 'N/A']
    ['nov-10-2025', 'N/A', 'izengws6', '79', 'N/A', '35', '3', 'N/A']
    ['nov-10-2025', 'N/A', 'izengws7', '41', 'N/A', '28', '3', 'N/A']
    ['nov-10-2025', 'N/A', 'izengdss1', '13', '90', '1', '3', 'N/A']
    ['nov-10-2025', 'N/A', 'mx3dss1', '72', 'N/A', '29', '3', 'N/A']
    ['nov-10-2025', 'izopsfep0', '53', '72', '16', '12', 'Ok']
    ['nov-10-2025', 'izopsfep2', '79', '72', '11', '12', 'Ok']
    ['nov-10-2025', 'izopsfep3', '85', '72', '13', '12', 'Ok']
    ['nov-10-2025', 'izopsgs1', '21', '93', '19', '11', 'Ok']
    ['nov-10-2025', 'izopsgs2', '16', '94', '18', '11', 'Ok']
    ['nov-10-2025', 'izopsmc1', '31', '67', '18', '11', 'Ok']
    ['nov-10-2025', 'izopsmc2', '37', '100', '14', '11', 'Ok']
    ['nov-10-2025', 'izengnas0', '76', '27', '29', '10', 'Revisar']
    ['nov-10-2025', 'izengnas2', '77', '27', '20', '9', 'Revisar']
    ['nov-10-2025', 'izengnas3', '93', '35', '20', '9', 'Revisar']
    ['nov-10-2025', 'izenggs1', '15', '63', '33', '10', 'Ok']
    ['nov-10-2025', 'izenggs2', '18', '63', '54', '10', 'Ok']
    ['nov-10-2025', 'izengfep1', '45', '80', '25', '10', 'Ok']
    ['nov-10-2025', 'izengarc1', '95', '79', '7', '10', 'Ok']
    ['nov-10-2025', 'izengcds1', '39', '10', '26', '2', 'Ok']
    ['nov-10-2025', 'izengcps1', '2', '98', '17', '9', 'Ok']
    ['nov-10-2025', 'izm3tmc1', '71', '97', '18', '10', 'Ok']
    ['nov-10-2025', 'izm3tmc2', '47', '90', '36', '10', 'Revisar']
    ['nov-10-2025', 'mnc_a_mexcity', '53', '61', '9', '11', 'Ok']
    ['nov-10-2025', 'mnc_b_mexcity', '44', '46', '13', '11', 'Ok']
    


```python
def test():
    print("Test")

test()
```

    Test
    


```python

```
