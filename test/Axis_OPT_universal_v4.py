#!/usr/bin/python
#Filename: cal_OPT.py
import math
import os

print "##############################################################################\n#This program only produces POSCAR accroding to your specified value(s)\n#\n#Creat dirctories in CURRENT dirctory with name of different lattice parameter\n#\n#WARNING this program is for lattice parameter calclulation ONLY! \n##############################################################################\n"

def frange(start, end=None, inc=None):
    "A range function, that does accept float increments..."

    if end == None:
        end = start + 0.0
        start = 0.0

    if inc == None:
        inc = 1.0

    L = []
    while 1:
        next = start + len(L) * inc
        if inc > 0 and next == end+0.000000000000001:
            L.append(next)
            break
        elif inc > 0 and next > end+0.000000000000001:
            break
        elif inc < 0 and next == end-0.000000000000001:
            L.append(next)
            break
        elif inc < 0 and next < end-0.000000000000001:
            break
        L.append(next)

    return L

#a_min=raw_input("input the value of a_min: ")
#a_max=raw_input("input the value of a_max: ")
#a_step==raw_input("input the value of a_step: ")
#b_min=raw_input("input the value of b_min: ")
#b_max=raw_input("input the value of b_max: ")
#b_step==raw_input("input the value of b_step: ")
#c_min=raw_input("input the value of c_min: ")
#c_max=raw_input("input the value of c_max: ")
#c_step==raw_input("input the value of b_step: ")
submitjobloop=1
submitjob = "WTF"
while submitjobloop==1:
    if submitjob=="yes":
        submit_name="YES"
        submit_script=raw_input("Enter the job submition script:")
        submitjobloop=0
    elif submitjob=="no":
        print "No job will be submitted."
        submitjobloop=0
    else:
        submitjob=raw_input("Do you want to submit all jobs (yes/no):")

if submit_name="YES":
    submit_name=raw_input("Enter the name of your job_submittion script[e.g. run.sh](wether you like it or not):")
else:
    submit_name=" "

POSCAR_file=raw_input("input the name of POSCAR source: ")
print ''
#========================import data=================================
file = open(POSCAR_file, "r")
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

if a_org_n == b_org_n:
    if a_org_n == c_org_n:
        print 'a=b=c\n'
        axis_min=raw_input("input the value of axis_min(all): ")
        axis_max=raw_input("input the value of axis_max(all): ")
        axis_step=raw_input("input the value of axis_step(all): ")
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
    else:
        print 'a=b!=c\n'
        ab_min=raw_input("input the value of a_min and b_min(SAME A AND B): ")
        ab_max=raw_input("input the value of a_max and b_max(SAME A AND B): ")
        ab_step=raw_input("input the value of a_step and b_step(SAME A AND B): ")
        a_step=ab_step
        a_min=ab_min
        a_max=ab_max
        b_step=ab_step
        b_min=ab_min
        b_max=ab_max
        c_min=raw_input("input the value of c_min: ")
        c_max=raw_input("input the value of c_max: ")
        c_step=raw_input("input the value of c_step: ")
if a_org_n == c_org_n:
    if b_org_n != c_org_n:
        print 'a=c!=b\n'
        ac_min=raw_input("input the value of a_min and c_min(SAME A AND C): ")
        ac_max=raw_input("input the value of a_max and c_max(SAME A AND C): ")
        ac_step=raw_input("input the value of a_step and c_step(SAME A AND C): ")
        a_step=ac_step
        a_min=ac_min
        a_max=ac_max
        c_step=ac_step
        c_min=ac_min
        c_max=ac_max
        b_min=raw_input("input the value of b_min: ")
        b_max=raw_input("input the value of b_max: ")
        b_step=raw_input("input the value of b_step: ")
if a_org_n != b_org_n:
    if b_org_n == c_org_n:
        print 'a!=b=c\n'
        bc_min=raw_input("input the value of b_min and c_min(SAME B AND C): ")
        bc_max=raw_input("input the value of b_max and c_max(SAME B AND C): ")
        bc_step=raw_input("input the value of b_step and c_step(SAME B AND C): ")
        b_step=bc_step
        b_min=bc_min
        b_max=bc_max
        c_step=bc_step
        c_min=bc_min
        c_max=bc_max
        a_min=raw_input("input the value of a_min: ")
        a_max=raw_input("input the value of a_max: ")
        a_step=raw_input("input the value of a_step: ")
    else:
        print 'ALL AXIS ARE DIFFERENT\n'
        a_min=raw_input("input the value of a_min: ")
        a_max=raw_input("input the value of a_max: ")
        a_step=raw_input("input the value of a_step: ")
        b_min=raw_input("input the value of b_min: ")
        b_max=raw_input("input the value of b_max: ")
        b_step=raw_input("input the value of b_step: ")
        c_min=raw_input("input the value of c_min: ")
        c_max=raw_input("input the value of c_max: ")
        c_step=raw_input("input the value of b_step: ")

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
#===================================================================================================
if a_org_n == b_org_n:
    if a_org_n == c_org_n:
        print 'a=b=c\n'
        #=====================================
        abc_relation="a=b=c"
        for a_sum in frange(a_min,a_max,a_step):
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


            #starting calculation
            #os.system("./run.sh")                                                      #LOCAL CALCULATION ONLY
            #os.system(yhrun -p TH_BM -n 24 /vol6/home/zjumsejjz4/bin/vasp5.3.5-neb)
            #mvcont='mv CONTCAR'+' CONTCAR'+'_'+str(a_sum)+str(b_sum)+str(c_sum)
            #mvpos='mv POSCAR'+' POSCAR'+'_'+str(a_sum)+str(b_sum)+str(c_sum)
            #mvout='mv OUTCAR'+' OUTCAR'+'_'+str(a_sum)+str(b_sum)+str(c_sum)
            os.system('mkdir'+' '+str(a_sum)+'-'+str(a_sum)+'-'+str(a_sum))
            os.system('cp INCAR POTCAR KPOINTS POSCAR vdw_kernel.bindat'+' '+submit_name+' '+str(a_sum)+'-'+str(a_sum)+'-'+str(a_sum))
            os.chdir('./'+str(a_sum)+'-'+str(a_sum)+'-'+str(a_sum))
#            os.system('yhbatch -p TH_BM -n 12 -JXCC_OPT run.sh')                       #open this if want to submit job automatically
            if submitjob=="yes":
                os.system(submit_script)
            #os.system('qsub -N '+str(a_sum)+'-'+str(a_sum)+'-'+str(a_sum)+' std.pbs')
            os.chdir('../')
            os.system('rm POSCAR')
            extration.append("'"+str(a_sum)+' '+str(a_sum)+' '+str(a_sum)+"'")
            extration_slash.append("'"+str(a_sum)+'-'+str(a_sum)+'-'+str(a_sum)+"'")
#=================================generate data_extration.py=================================
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

    else:
        print 'a=b!=c\n'
        #=====================================
        abc_relation="a=b=c"
        for a_sum in frange(a_min,a_max,a_step):
            for c_sum in frange(c_min,c_max,c_step):
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


                #starting calculation
                #os.system("./run.sh")                                                      #LOCAL CALCULATION ONLY
                #os.system(yhrun -p TH_BM -n 24 /vol6/home/zjumsejjz4/bin/vasp5.3.5-neb)
                #mvcont='mv CONTCAR'+' CONTCAR'+'_'+str(a_sum)+str(b_sum)+str(c_sum)
                #mvpos='mv POSCAR'+' POSCAR'+'_'+str(a_sum)+str(b_sum)+str(c_sum)
                #mvout='mv OUTCAR'+' OUTCAR'+'_'+str(a_sum)+str(b_sum)+str(c_sum)
                os.system('mkdir'+' '+str(a_sum)+'-'+str(a_sum)+'-'+str(c_sum))
                os.system('cp INCAR POTCAR KPOINTS POSCAR vdw_kernel.bindat'+' '+submit_name+' '+str(a_sum)+'-'+str(a_sum)+'-'+str(c_sum))
                os.chdir('./'+str(a_sum)+'-'+str(a_sum)+'-'+str(c_sum))
#                os.system('yhbatch -p TH_BM -n 12 -JXCC_OPT run.sh')                       #open this if want to submit job automatically
                if submitjob=="yes":
                    os.system(submit_script)
                #os.system('qsub -N '+str(a_sum)+'-'+str(a_sum)+'-'+str(c_sum)+' std.pbs')
                os.chdir('../')
                os.system('rm POSCAR')
                extration.append("'"+str(a_sum)+' '+str(a_sum)+' '+str(c_sum)+"'")
                extration_slash.append("'"+str(a_sum)+'-'+str(a_sum)+'-'+str(c_sum)+"'")
#=================================generate data_extration.py=================================
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


if a_org_n == c_org_n:
    if b_org_n != c_org_n:
        print 'a=c!=b\n'
        #=====================================
        abc_relation="a=c!=b"
        for a_sum in frange(a_min,a_max,a_step):
            for b_sum in frange(b_min,b_max,b_step):
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


                #starting calculation
                #os.system("./run.sh")                                                      #LOCAL CALCULATION ONLY
                #os.system(yhrun -p TH_BM -n 24 /vol6/home/zjumsejjz4/bin/vasp5.3.5-neb)
                #mvcont='mv CONTCAR'+' CONTCAR'+'_'+str(a_sum)+str(b_sum)+str(c_sum)
                #mvpos='mv POSCAR'+' POSCAR'+'_'+str(a_sum)+str(b_sum)+str(c_sum)
                #mvout='mv OUTCAR'+' OUTCAR'+'_'+str(a_sum)+str(b_sum)+str(c_sum)
                os.system('mkdir'+' '+str(a_sum)+'-'+str(b_sum)+'-'+str(a_sum))
                os.system('cp INCAR POTCAR KPOINTS POSCAR vdw_kernel.bindat'+' '+submit_name+' '+str(a_sum)+'-'+str(b_sum)+'-'+str(a_sum))
                os.chdir('./'+str(a_sum)+'-'+str(b_sum)+'-'+str(a_sum))
#                os.system('yhbatch -p TH_BM -n 12 -JXCC_OPT run.sh')                       #open this if want to submit job automatically
                if submitjob=="yes":
                        os.system(submit_script)
                #os.system('qsub -N '+str(a_sum)+'-'+str(b_sum)+'-'+str(a_sum)+' std.pbs')
                os.chdir('../')
                os.system('rm POSCAR')
                extration.append("'"+str(a_sum)+' '+str(b_sum)+' '+str(a_sum)+"'")
                extration_slash.append("'"+str(a_sum)+'-'+str(b_sum)+'-'+str(a_sum)+"'")
#=================================generate data_extration.py=================================
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


if a_org_n != b_org_n:
    if b_org_n == c_org_n:
        print '"a!=b=c"\n'
        #=====================================
        abc_relation="a!=b=c"
        for a_sum in frange(a_min,a_max,a_step):
            for b_sum in frange(b_min,b_max,b_step):
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


                #starting calculation
                #os.system("./run.sh")                                                      #LOCAL CALCULATION ONLY
                #os.system(yhrun -p TH_BM -n 24 /vol6/home/zjumsejjz4/bin/vasp5.3.5-neb)
                #mvcont='mv CONTCAR'+' CONTCAR'+'_'+str(a_sum)+str(b_sum)+str(c_sum)
                #mvpos='mv POSCAR'+' POSCAR'+'_'+str(a_sum)+str(b_sum)+str(c_sum)
                #mvout='mv OUTCAR'+' OUTCAR'+'_'+str(a_sum)+str(b_sum)+str(c_sum)
                os.system('mkdir'+' '+str(a_sum)+'-'+str(b_sum)+'-'+str(b_sum))
                os.system('cp INCAR POTCAR KPOINTS POSCAR vdw_kernel.bindat'+' '+submit_name+' '+str(a_sum)+'-'+str(b_sum)+'-'+str(b_sum))
                os.chdir('./'+str(a_sum)+'-'+str(b_sum)+'-'+str(b_sum))
#                os.system('yhbatch -p TH_BM -n 12 -JXCC_OPT run.sh')                       #open this if want to submit job automatically
                if submitjob=="yes":
                    os.system(submit_script)
                #os.system('qsub -N '+str(a_sum)+'-'+str(b_sum)+'-'+str(b_sum)+' std.pbs')
                os.chdir('../')
                os.system('rm POSCAR')
                extration.append("'"+str(a_sum)+' '+str(b_sum)+' '+str(b_sum)+"'")
                extration_slash.append("'"+str(a_sum)+'-'+str(b_sum)+'-'+str(b_sum)+"'")
#=================================generate data_extration.py=================================
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

                #os.system(mvpos)
                #os.system(mvout)
    else:
        print 'ALL AXIS ARE DIFFERENT\n'
        #=====================================
        abc_relation="ALL AXIS ARE DIFFERENT"
        for a_sum in frange(a_min,a_max,a_step):
            for b_sum in frange(b_min,b_max,b_step):
                for c_sum in frange(c_min,c_max,c_step):
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


                    #starting calculation
                    #os.system("./run.sh")                                                      #LOCAL CALCULATION ONLY
                    #os.system(yhrun -p TH_BM -n 24 /vol6/home/zjumsejjz4/bin/vasp5.3.5-neb)
                    #mvcont='mv CONTCAR'+' CONTCAR'+'_'+str(a_sum)+str(b_sum)+str(c_sum)
                    #mvpos='mv POSCAR'+' POSCAR'+'_'+str(a_sum)+str(b_sum)+str(c_sum)
                    #mvout='mv OUTCAR'+' OUTCAR'+'_'+str(a_sum)+str(b_sum)+str(c_sum)
                    os.system('mkdir'+' '+str(a_sum)+'-'+str(b_sum)+'-'+str(c_sum))
                    os.system('cp INCAR POTCAR KPOINTS POSCAR vdw_kernel.bindat'+' '+submit_name+' '+str(a_sum)+'-'+str(b_sum)+'-'+str(c_sum))
                    os.chdir('./'+str(a_sum)+'-'+str(b_sum)+'-'+str(c_sum))
#                    os.system('yhbatch -p TH_BM -n 12 -JXCC_OPT run.sh')                       #open this if want to submit job automatically
                    if submitjob=="yes":
                        os.system(submit_script)
                    #os.system('qsub -N '+str(a_sum)+'-'+str(b_sum)+'-'+str(c_sum)+' std.pbs')
                    os.chdir('../')
                    os.system('rm POSCAR')
                    extration.append("'"+str(a_sum)+' '+str(b_sum)+' '+str(c_sum)+"'")
                    extration_slash.append("'"+str(a_sum)+'-'+str(b_sum)+'-'+str(c_sum)+"'")
#=================================generate data_extration.py=================================
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

#===================================================================================================



print 'done'
