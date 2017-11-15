#!/usr/bin/python
#Filename: cal_OPT.py
import math
import os
import sys
#import pyreadline
import readline
import numpy as np

#############################################################################################
def axis_chg(abc_relation,a_sum=None,b_sum=None,c_sum=None,data=None):
    import math
    "this changes axis length"
    if abc_relation=="a=b=c":
        b_sum=a_sum
        c_sum=a_sum
    elif abc_relation=="a=b!=c":
        b_sum=a_sum
    elif abc_relation=="a=c!=b":
        c_sum=a_sum
    elif abc_relation=="a!=b=c":
        c_sum=b_sum
    elif abc_relation=="ALL AXIS ARE DIFFERENT":
        print "all axis different!"
    #=====================a opt================================
    if int(data[0][0])==0:
        if int(data[0][1])==0:
            if data[0][2]>0:
                data[0][2]=a_sum               #if a1=0 and a2=0 then a3 is alone
            elif data[0][2]<0:
                data[0][2]=(-1)*a_sum
        else:                              #if a1=0 and a2<>0 then use a2 as constant
            data_a_2_1=data[0][2]/data[0][1]
            if data[0][1]>0:
                data[0][1]=a_sum/math.sqrt(1+data_a_2_1*data_a_2_1)
            elif data[0][1]<0:
                data[0][1]=(-1)*a_sum/math.sqrt(1+data_a_2_1*data_a_2_1)
            data[0][2]=data[0][1]*data_a_2_1
    else:
        data_a_1_0=data[0][1]/data[0][0]
        data_a_2_0=data[0][2]/data[0][0]
        if data[0][0]>0:
            data[0][0]=a_sum/math.sqrt(1+data_a_2_0*data_a_2_0+data_a_1_0*data_a_1_0)
        elif data[0][0]<0:
            data[0][0]=(-1)*a_sum/math.sqrt(1+data_a_2_0*data_a_2_0+data_a_1_0*data_a_1_0)
        data[0][1]=data[0][0]*data_a_1_0
        data[0][2]=data[0][0]*data_a_2_0
    #======================================

    #=====================b opt================================
    if int(data[1][0])==0:
        if int(data[1][1])==0:
            if data[1][2]>0:
                data[1][2]=b_sum
            elif data[1][2]<0:
                data[1][2]=(-1)*b_sum
        else:
            data_b_2_1=data[1][2]/data[1][1]
            if data[1][1]>0:
                data[1][1]=b_sum/math.sqrt(1+data_b_2_1*data_b_2_1)
            elif data[1][1]<0:
                data[1][1]=(-1)*b_sum/math.sqrt(1+data_b_2_1*data_b_2_1)
            data[1][2]=data[1][1]*data_b_2_1
    else:
        data_b_1_0=data[1][1]/data[1][0]
        data_b_2_0=data[1][2]/data[1][0]
        if data[1][0]>0:
            data[1][0]=b_sum/math.sqrt(1+data_b_2_0*data_b_2_0+data_b_1_0*data_b_1_0)
        elif data[1][0]<0:
            data[1][0]=(-1)*b_sum/math.sqrt(1+data_b_2_0*data_b_2_0+data_b_1_0*data_b_1_0)
        data[1][1]=data[1][0]*data_b_1_0
        data[1][2]=data[1][0]*data_b_2_0
    #======================================

    #=====================c opt================================
    if int(data[2][0])==0:
        if int(data[2][1])==0:
            if data[2][2]>0:
                data[2][2]=c_sum
            elif data[2][2]<0:
                data[2][2]=(-1)*c_sum
        else:
            data_c_2_1=data[2][2]/data[2][1]
            if data[2][1]>0:
                data[2][1]=c_sum/math.sqrt(1+data_c_2_1*data_c_2_1)
            elif data[2][1]<0:
                data[2][1]=(-1)*c_sum/math.sqrt(1+data_c_2_1*data_c_2_1)
            data[2][2]=data[2][1]*data_c_2_1
    else:
        data_c_1_0=data[2][1]/data[2][0]
        data_c_2_0=data[2][2]/data[2][0]
        if data[2][0]>0:
            data[2][0]=c_sum/math.sqrt(1+data_c_2_0*data_c_2_0+data_c_1_0*data_c_1_0)
        elif data[2][0]<0:
            data[2][0]=(-1)*c_sum/math.sqrt(1+data_c_2_0*data_c_2_0+data_c_1_0*data_c_1_0)
        data[2][1]=data[2][0]*data_c_1_0
        data[2][2]=data[2][0]*data_c_2_0
    #======================================

    return data

############################################################################################
def gen_data(extration=None,extration_slash=None):
    devide = ','
    extration_all = devide.join(extration)
    extration_slash_all = devide.join(extration_slash)
    #print extration_all
    file_extration = open('data_extration.py','a')
    file_extration.write('import os'+'\n')
    file_extration.write('import subprocess'+'\n')
    file_extration.write('data_all = []'+'\n')
    file_extration.write('all_param = ['+extration_all+']'+'\n')
    file_extration.write('for i in ('+extration_slash_all+'):'+'\n')
    #        file_extration.write('    print i'+'\n')
    file_extration.write('    os.chdir(i)'+'\n')
    file_extration.write('''    proc = subprocess.Popen("grep 'energy(sigma->0) =' OUTCAR | tail -1 | awk  -F '      '  '{print $3}'",stdout=subprocess.PIPE,shell=True)'''+'\n')
    file_extration.write('    (out, err) = proc.communicate()'+'\n')
    file_extration.write('''    outwithoutreturn = out.rstrip('''+r"'\n'"+")"+'\n')
    #        file_extration.write('''    out_tot =outwithoutreturn'''+'\n')
    file_extration.write('    data_all.append(outwithoutreturn)'+'\n')
    file_extration.write('''    conv=os.system("grep 'reached required accuracy - stopping structural energy minimisation' OUTCAR >/dev/null")'''+"\n")
    file_extration.write('    if conv!=0:'+'\n')
    file_extration.write("        print ''' -----------------------------------------------------------------------------"+'\n')
    file_extration.write("|                                                                             |"+"\n")
    file_extration.write("|           W    W    AA    RRRRR   N    N  II  N    N   GGGG   !!!           |"+"\n")
    file_extration.write("|           W    W   A  A   R    R  NN   N  II  NN   N  G    G  !!!           |"+"\n")
    file_extration.write("|           W    W  A    A  R    R  N N  N  II  N N  N  G       !!!           |"+"\n")
    file_extration.write("|           W WW W  AAAAAA  RRRRR   N  N N  II  N  N N  G  GGG   !            |"+"\n")
    file_extration.write("|           WW  WW  A    A  R   R   N   NN  II  N   NN  G    G                |"+"\n")
    file_extration.write("|           W    W  A    A  R    R  N    N  II  N    N   GGGG   !!!           |"+"\n")
    file_extration.write("|                                                                             |"+"\n")
    file_extration.write("|                                                                             |"+"\n")
    file_extration.write("'''+"+'''"|          WARNING:"+" "+i+" "+"Did not reach the required EDIFFG!           |"+'''+r"'\n'"+"+''' ----------------------------------------------------------------------------- '''"+'\n')
    file_extration.write("    os.chdir('../')"+'\n')
    file_extration.write("length = len(all_param)"+'\n')
    file_extration.write("file_data = open('data.dat','a')"+'\n')
    file_extration.write("for i_d in range(0,length,1):"+'\n')
    file_extration.write("    file_data.write(all_param[i_d]+' '+data_all[i_d]+"+r"'\n'"+")"+'\n')

############################################################################################

print "#####################################################################################\n\
#   This program only produces POSCAR accroding to your specified value(s)          #\n\
#                                                                                   #\n\
#   Creat dirctories in CURRENT dirctory with name of different lattice parameter   #\n\
#                                                                                   #\n\
#   WARNING this program is for lattice parameter calclulation ONLY!                #\n\
#####################################################################################\n"

submitjobloop=1
submitjob = "WTF"
submit_name = "null"
while submitjobloop==1:
    if submitjob=="yes":
        submit_name="YES"
#        submit_script=raw_input("Enter the job submition script(e.g.qsub -N test run.sh):")
        while True:
            submit_script=raw_input("Enter the job submition command(e.g.qsub -N test run.sh):")
            sure_script=raw_input("RU sure? (yes/no):")
            if sure_script != "yes":
                print "Please re_enter!\n"
                continue
            else:
                print "\n"
                break

        submitjobloop=0
    elif submitjob=="no":
        print "No job will be submitted.\n"
        submitjobloop=0
    else:
        while True:
            submitjob=raw_input("Do you want to submit all jobs (yes/no):")
            if submitjob == "yes":
                print "\n"
                break
            elif submitjob == "no" :
                print "\n"
                break
            else:
                continue

if submit_name=="YES":
    while True:
        readline.parse_and_bind('tab: complete')
        submit_name=raw_input("Enter the name of your job_submittion script[e.g. run.sh](use Tab):")
        sure_submitname=raw_input("RU sure? (yes/no):")
        if sure_submitname != "yes":
            print "Please re_enter!\n"
            continue
        else:
            print "\n"
            break


else:
    submit_name=" "
while True:
    readline.parse_and_bind('tab: complete')
    try:
        POSCAR_file=raw_input("Input the name of POSCAR source(use Tab): ")
        file = open(POSCAR_file, "r")
    except IOError as ioe:
        print "No such File, re enter"
        continue
    else:
        break

print ''
#========================import data=================================

content = [x.rstrip("\n") for x in file]
data = [x.split()[:5] for x in content[2:5]]
file.close()

#convert datatype
for i in (0,1,2):
    for j in (0,1,2):
        data[i][j]=float(data[i][j])

#check symmetry
a_org = math.sqrt(data[0][0]*data[0][0]+data[0][1]*data[0][1]+data[0][2]*data[0][2])
b_org = math.sqrt(data[1][0]*data[1][0]+data[1][1]*data[1][1]+data[1][2]*data[1][2])
c_org = math.sqrt(data[2][0]*data[2][0]+data[2][1]*data[2][1]+data[2][2]*data[2][2])

a_org_n = int(a_org*100000)             #to examine if same
b_org_n = int(b_org*100000)
c_org_n = int(c_org*100000)

while True:
    try:
        if a_org_n == b_org_n:
            if a_org_n == c_org_n:
                print 'a=b=c\n'
                axis_min=float(raw_input("Input the value of axis_min(all): "))
                axis_max=float(raw_input("Input the value of axis_max(all): "))
                axis_step=float(raw_input("How many steps(all): "))
                #set all to same=====================
                a_step=axis_step
                a_min=axis_min
                a_max=axis_max
                b_step=axis_step
                b_min=axis_min
                b_max=axis_max
                c_step=axis_step
                c_min=axis_min
                c_max=axis_max
                sure=raw_input("RU sure? (yes/no:)")
                if sure == "yes":
                    break
                else:
                    print "re_enter!"
                    continue
            else:
                print 'a=b!=c\n'
                ab_min=float(raw_input("Input the value of a_min and b_min(SAME A AND B): "))
                ab_max=float(raw_input("Input the value of a_max and b_max(SAME A AND B): "))
                ab_step=float(raw_input("How many steps for a_step and b_step(SAME A AND B): "))
                a_step=ab_step
                a_min=ab_min
                a_max=ab_max
                b_step=ab_step
                b_min=ab_min
                b_max=ab_max
                c_min=float(raw_input("Input the value of c_min: "))
                c_max=float(raw_input("Input the value of c_max: "))
                c_step=float(raw_input("How many steps for c_step: "))
                sure=raw_input("RU sure? (yes/no:)")
                if sure == "yes":
                    break
                else:
                    print "re_enter!"
                    continue
        if a_org_n == c_org_n:
            if b_org_n != c_org_n:
                print 'a=c!=b\n'
                ac_min=float(raw_input("Input the value of a_min and c_min(SAME A AND C): "))
                ac_max=float(raw_input("Input the value of a_max and c_max(SAME A AND C): "))
                ac_step=float(raw_input("How many steps for a_step and c_step(SAME A AND C): "))
                a_step=ac_step
                a_min=ac_min
                a_max=ac_max
                c_step=ac_step
                c_min=ac_min
                c_max=ac_max
                b_min=float(raw_input("Input the value of b_min: "))
                b_max=float(raw_input("Input the value of b_max: "))
                b_step=float(raw_input("How many steps for b_step: "))
                sure=raw_input("RU sure? (yes/no:)")
                if sure == "yes":
                    break
                else:
                    print "re_enter!"
                    continue
        if a_org_n != b_org_n:
            if b_org_n == c_org_n:
                print 'a!=b=c\n'
                bc_min=float(raw_input("Input the value of b_min and c_min(SAME B AND C): "))
                bc_max=float(raw_input("Input the value of b_max and c_max(SAME B AND C): "))
                bc_step=float(raw_input("How many steps for b_step and c_step(SAME B AND C): "))
                b_step=bc_step
                b_min=bc_min
                b_max=bc_max
                c_step=bc_step
                c_min=bc_min
                c_max=bc_max
                a_min=float(raw_input("Input the value of a_min: "))
                a_max=float(raw_input("Input the value of a_max: "))
                a_step=float(raw_input("How many steps for a_step: "))
                sure=raw_input("RU sure? (yes/no:)")
                if sure == "yes":
                    break
                else:
                    print "re_enter!"
                    continue
            else:
                print 'All axis length are different\n'
                a_min=float(raw_input("Input the value of a_min: "))
                a_max=float(raw_input("Input the value of a_max: "))
                a_step=float(raw_input("How many steps for a_step: "))
                b_min=float(raw_input("Input the value of b_min: "))
                b_max=float(raw_input("Input the value of b_max: "))
                b_step=float(raw_input("How many steps for b_step: "))
                c_min=float(raw_input("Input the value of c_min: "))
                c_max=float(raw_input("Input the value of c_max: "))
                c_step=float(raw_input("How many steps for c_step: "))
                sure=raw_input("RU sure? (yes/no:)")
                if sure == "yes":
                    break
                else:
                    print "re_enter!\n"
                    continue
    except ValueError as ve:
        print "\nLength must be a number!\n"
        continue
    else:
        break
#convert data type
a_min=float(a_min)
a_max=float(a_max)
a_step=float(a_step)
b_min=float(b_min)
b_max=float(b_max)
b_step=float(b_step)
c_min=float(c_min)
c_max=float(c_max)
c_step=float(c_step)

extration = []
extration_slash = []
#=======================================Main Part START=========================================
if a_org_n == b_org_n:
    if a_org_n == c_org_n:
        print 'a=b=c\n'
        #=====================================
        abc_relation="a=b=c"
        for a_sum in np.linspace(a_min,a_max,a_step):#frange(a_min,a_max,a_step):
            b_sum=None
            c_sum=None
            axis_chg(abc_relation,a_sum,b_sum,c_sum,data)


            #======================================
            fileHandle = open('POSCAR','a')
            file = open(POSCAR_file,'r')
            lineNum=0
            for line in file.readlines()[0:2]:
                fileHandle.write(line)
            file.close()
            fileHandle.write('      '+str(data[0][0])+'     '+str(data[0][1])+'     '+str(data[0][2])+'\n')
            fileHandle.write('      '+str(data[1][0])+'     '+str(data[1][1])+'     '+str(data[1][2])+'\n')
            fileHandle.write('      '+str(data[2][0])+'     '+str(data[2][1])+'     '+str(data[2][2])+'\n')
            filename = POSCAR_file
            ffopen = open(filename)
            next (ffopen)
            next (ffopen)
            next (ffopen)
            next (ffopen)
            next (ffopen)

            for e in ffopen:            #ffopen opens POSCAR_file, obtain the last few lines.
                fileHandle.write(e)     #write ffopen last lines into POSCAR
            ffopen.close()
            fileHandle.close()


            #starting calculation
            os.system('mkdir'+' '+str(a_sum)+'-'+str(a_sum)+'-'+str(a_sum))
            os.system('cp INCAR POTCAR KPOINTS POSCAR vdw_kernel.bindat'+' '+submit_name+' '+str(a_sum)+'-'+str(a_sum)+'-'+str(a_sum))
            os.chdir('./'+str(a_sum)+'-'+str(a_sum)+'-'+str(a_sum))
            if submitjob=="yes":
                os.system(submit_script)
            os.chdir('../')
            os.system('rm POSCAR')
            extration.append("'"+str(a_sum)+' '+str(a_sum)+' '+str(a_sum)+"'")
            extration_slash.append("'"+str(a_sum)+'-'+str(a_sum)+'-'+str(a_sum)+"'")
#=================================generate data_extration.py=================================
        gen_data(extration,extration_slash)

    else:
        print 'a=b!=c\n'
        #=====================================
        abc_relation="a=b!=c"
        for a_sum in np.linspace(a_min,a_max,a_step):#frange(a_min,a_max,a_step):
            for c_sum in np.linspace(c_min,c_max,c_step):#frange(c_min,c_max,c_step):
                b_sum=None
                axis_chg(abc_relation,a_sum,b_sum,c_sum,data)

                #======================================
                fileHandle = open('POSCAR','a')
                file = open(POSCAR_file,'r')
                lineNum=0
                for line in file.readlines()[0:2]:
                    fileHandle.write(line)
                file.close()
                fileHandle.write('      '+str(data[0][0])+'     '+str(data[0][1])+'     '+str(data[0][2])+'\n')
                fileHandle.write('      '+str(data[1][0])+'     '+str(data[1][1])+'     '+str(data[1][2])+'\n')
                fileHandle.write('      '+str(data[2][0])+'     '+str(data[2][1])+'     '+str(data[2][2])+'\n')
                filename = POSCAR_file
                ffopen = open(filename)
                next (ffopen)
                next (ffopen)
                next (ffopen)
                next (ffopen)
                next (ffopen)

                for e in ffopen:
                    fileHandle.write(e)
                ffopen.close()
                fileHandle.close()


                os.system('mkdir'+' '+str(a_sum)+'-'+str(a_sum)+'-'+str(c_sum))
                os.system('cp INCAR POTCAR KPOINTS POSCAR vdw_kernel.bindat'+' '+submit_name+' '+str(a_sum)+'-'+str(a_sum)+'-'+str(c_sum))
                os.chdir('./'+str(a_sum)+'-'+str(a_sum)+'-'+str(c_sum))
                if submitjob=="yes":
                    os.system(submit_script)
                os.chdir('../')
                os.system('rm POSCAR')
                extration.append("'"+str(a_sum)+' '+str(a_sum)+' '+str(c_sum)+"'")
                extration_slash.append("'"+str(a_sum)+'-'+str(a_sum)+'-'+str(c_sum)+"'")
#=================================generate data_extration.py=================================
        gen_data(extration,extration_slash)


if a_org_n == c_org_n:
    if b_org_n != c_org_n:
        print 'a=c!=b\n'
        #=====================================
        abc_relation="a=c!=b"
        for a_sum in np.linspace(a_min,a_max,a_step):#frange(a_min,a_max,a_step):
            for b_sum in np.linspace(b_min,b_max,b_step):#frange(b_min,b_max,b_step):
                c_sum=None
                axis_chg(abc_relation,a_sum,b_sum,c_sum,data)

                #======================================
                fileHandle = open('POSCAR','a')
                file = open(POSCAR_file,'r')
                lineNum=0
                for line in file.readlines()[0:2]:
                    fileHandle.write(line)
                file.close()
                fileHandle.write('      '+str(data[0][0])+'     '+str(data[0][1])+'     '+str(data[0][2])+'\n')
                fileHandle.write('      '+str(data[1][0])+'     '+str(data[1][1])+'     '+str(data[1][2])+'\n')
                fileHandle.write('      '+str(data[2][0])+'     '+str(data[2][1])+'     '+str(data[2][2])+'\n')
                filename = POSCAR_file
                ffopen = open(filename)
                next (ffopen)
                next (ffopen)
                next (ffopen)
                next (ffopen)
                next (ffopen)

                for e in ffopen:
                    fileHandle.write(e)
                ffopen.close()
                fileHandle.close()


                os.system('mkdir'+' '+str(a_sum)+'-'+str(b_sum)+'-'+str(a_sum))
                os.system('cp INCAR POTCAR KPOINTS POSCAR vdw_kernel.bindat'+' '+submit_name+' '+str(a_sum)+'-'+str(b_sum)+'-'+str(a_sum))
                os.chdir('./'+str(a_sum)+'-'+str(b_sum)+'-'+str(a_sum))
                if submitjob=="yes":
                        os.system(submit_script)
                os.chdir('../')
                os.system('rm POSCAR')
                extration.append("'"+str(a_sum)+' '+str(b_sum)+' '+str(a_sum)+"'")
                extration_slash.append("'"+str(a_sum)+'-'+str(b_sum)+'-'+str(a_sum)+"'")
#=================================generate data_extration.py=================================
        gen_data(extration,extration_slash)


if a_org_n != b_org_n:
    if b_org_n == c_org_n:
        print '"a!=b=c"\n'
        #=====================================
        abc_relation="a!=b=c"
        for a_sum in np.linspace(a_min,a_max,a_step):#frange(a_min,a_max,a_step):
            for b_sum in np.linspace(b_min,b_max,b_step):#frange(b_min,b_max,b_step):
                c_sum=None
                axis_chg(abc_relation,a_sum,b_sum,c_sum,data)
                #======================================
                fileHandle = open('POSCAR','a')
                file = open(POSCAR_file,'r')
                lineNum=0
                for line in file.readlines()[0:2]:
                    fileHandle.write(line)
                file.close()
                fileHandle.write('      '+str(data[0][0])+'     '+str(data[0][1])+'     '+str(data[0][2])+'\n')
                fileHandle.write('      '+str(data[1][0])+'     '+str(data[1][1])+'     '+str(data[1][2])+'\n')
                fileHandle.write('      '+str(data[2][0])+'     '+str(data[2][1])+'     '+str(data[2][2])+'\n')
                filename = POSCAR_file
                ffopen = open(filename)
                next (ffopen)
                next (ffopen)
                next (ffopen)
                next (ffopen)
                next (ffopen)

                for e in ffopen:
                    fileHandle.write(e)
                ffopen.close()
                fileHandle.close()


                os.system('mkdir'+' '+str(a_sum)+'-'+str(b_sum)+'-'+str(b_sum))
                os.system('cp INCAR POTCAR KPOINTS POSCAR vdw_kernel.bindat'+' '+submit_name+' '+str(a_sum)+'-'+str(b_sum)+'-'+str(b_sum))
                os.chdir('./'+str(a_sum)+'-'+str(b_sum)+'-'+str(b_sum))
                if submitjob=="yes":
                    os.system(submit_script)
                os.chdir('../')
                os.system('rm POSCAR')
                extration.append("'"+str(a_sum)+' '+str(b_sum)+' '+str(b_sum)+"'")
                extration_slash.append("'"+str(a_sum)+'-'+str(b_sum)+'-'+str(b_sum)+"'")
#=================================generate data_extration.py=================================
        gen_data(extration,extration_slash)

    else:
        print 'All axis length are different\n'
        #=====================================
        abc_relation="ALL AXIS ARE DIFFERENT"
        for a_sum in np.linspace(a_min,a_max,a_step):#frange(a_min,a_max,a_step):
            for b_sum in np.linspace(b_min,b_max,b_step):#frange(b_min,b_max,b_step):
                for c_sum in np.linspace(c_min,c_max,c_step):#frange(c_min,c_max,c_step):
                    axis_chg(abc_relation,a_sum,b_sum,c_sum,data)

                    #======================================
                    fileHandle = open('POSCAR','a')
                    #fileHandle = open(str(a_sum)+str(b_sum)+str(c_sum),'a') #TEST PURPOSE ONLY
                    file = open(POSCAR_file,'r')
                    lineNum=0
                    for line in file.readlines()[0:2]:
                        fileHandle.write(line)
                    file.close()
                    fileHandle.write('      '+str(data[0][0])+'     '+str(data[0][1])+'     '+str(data[0][2])+'\n')
                    fileHandle.write('      '+str(data[1][0])+'     '+str(data[1][1])+'     '+str(data[1][2])+'\n')
                    fileHandle.write('      '+str(data[2][0])+'     '+str(data[2][1])+'     '+str(data[2][2])+'\n')
                    filename = POSCAR_file
                    ffopen = open(filename)
                    next (ffopen)
                    next (ffopen)
                    next (ffopen)
                    next (ffopen)
                    next (ffopen)

                    for e in ffopen:
                        fileHandle.write(e)
                    ffopen.close()
                    fileHandle.close()


                    os.system('mkdir'+' '+str(a_sum)+'-'+str(b_sum)+'-'+str(c_sum))
                    os.system('cp INCAR POTCAR KPOINTS POSCAR vdw_kernel.bindat'+' '+submit_name+' '+str(a_sum)+'-'+str(b_sum)+'-'+str(c_sum))
                    os.chdir('./'+str(a_sum)+'-'+str(b_sum)+'-'+str(c_sum))
                    if submitjob=="yes":
                        os.system(submit_script)
                    os.chdir('../')
                    os.system('rm POSCAR')
                    extration.append("'"+str(a_sum)+' '+str(b_sum)+' '+str(c_sum)+"'")
                    extration_slash.append("'"+str(a_sum)+'-'+str(b_sum)+'-'+str(c_sum)+"'")
#=================================generate data_extration.py=================================
        gen_data(extration,extration_slash)

#=======================================Main Part END=========================================



print 'Goodbye.'

