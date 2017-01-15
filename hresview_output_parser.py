
# coding: utf-8

# In[63]:

#!/usr/bin/env python2.7
def hresview_output_parser():
    # Input the file location and name to be processed:
    inputname = input('Please enter the name and directory of input file: ')
    fin = open(inputname, 'r')
    # Output the result of processed file to outputname:
    outputname = input('Please enter the name and directory of output file: ')
    fout = open(outputname, 'w')
    fout.write("#HBB thermistor temps\n#1: Time\n#2: HBBapexTemp\n#3: HBBbottomTemp\n#4: HBBtopTemp\n#5: fixed2500ohmResistor\n#6: fixed97KohmResistor\n")
    
    
    # read in all the lines contained in the input file
    lines = fin.readlines()
    fin.close()
    
    
    # extract the lines that we are interested here and collect the lines containing elements of same category into lists. 
    i = 0;
    chn3 = [lines[4], ]
    chn4 = [lines[5], ]
    chn5 = [lines[6], ]
    chn6 = [lines[7], ]
    chn7 = [lines[8], ]
    time_st = [lines[9], ]
    time_ed = [lines[10], ]
    while ((i+17) < len(lines)) :
        i = i + 7
        chn3.append(lines[i+4])
        chn4.append(lines[i+5])
        chn5.append(lines[i+6])
        chn6.append(lines[i+7])
        chn7.append(lines[i+8])
        time_st.append(lines[i+9])
        time_ed.append(lines[i+10])
        
    
    # extract the interesting text in each line and store in another set of lists
    chn3val = [float(chn3[0].split(':')[1]), ]
    chn4val = [float(chn4[0].split(':')[1]), ]
    chn5val = [float(chn5[0].split(':')[1]), ]
    chn6val = [float(chn6[0].split(':')[1]), ]
    chn7val = [float(chn7[0].split(':')[1]), ]
    time_st_val = [time_st[0].split('=')[1], ]
    time_ed_val = [time_ed[0].split('=')[1], ]

    for i in range(1, len(chn3)):
        chn3val.append(float(chn3[i].split(':')[1]))
        chn4val.append(float(chn4[i].split(':')[1]))
        chn5val.append(float(chn5[i].split(':')[1]))
        chn6val.append(float(chn6[i].split(':')[1]))
        chn7val.append(float(chn7[i].split(':')[1]))
        time_st_val.append(time_st[i].split('=')[1])
        time_ed_val.append(time_ed[i].split('=')[1])

    
    # extract starting and ending time digits from the texts and convert to hours
    temp = time_st_val[0].split(':')
    timeInHr = float(temp[0])*3600 + float(temp[1])*60 + float(temp[2])
    timeInHr = timeInHr/3600
    startStamp = [timeInHr, ]
    for i in range(1, len(time_st_val)):
        temp = time_st_val[i].split(':')
        timeInHr = float(temp[0])*3600 + float(temp[1])*60 + float(temp[2])
        timeInHr = timeInHr/3600
        startStamp.append(timeInHr)
        
    temp = time_ed_val[0].split(':')
    timeInHr = float(temp[0])*3600 + float(temp[1])*60 + float(temp[2])
    timeInHr = timeInHr/3600
    endStamp = [timeInHr, ]
    for i in range(1, len(time_st_val)):
        temp = time_ed_val[i].split(':')
        timeInHr = float(temp[0])*3600 + float(temp[1])*60 + float(temp[2])
        timeInHr = timeInHr/3600
        endStamp.append(timeInHr)
        
        
    # compute the average of starting and ending times to get the timestamp that we desire. 
    timeStamp = [round((startStamp[0] + endStamp[0]) / 2, 4), ]
    for i in range(1, len(chn3)):
        timeStamp.append(round((startStamp[i] + endStamp[i]) / 2, 4))
        
     
    # write all the elements we need to output file.
    for i in range(0, len(chn3)):
        fout.write(str(timeStamp[i]) + ', ')
        fout.write(str(chn4val[i]) + ', ')
        fout.write(str(chn5val[i]) + ', ')
        fout.write(str(chn3val[i]) + ', ')
        fout.write(str(chn6val[i]) + ', ')
        fout.write(str(chn7val[i]))
        fout.write('\n')
        
    # ending the function
    fout.close()


# In[ ]:

hresview_output_parser()



