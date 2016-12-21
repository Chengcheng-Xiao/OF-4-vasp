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
#########################################################################################

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
        if inc > 0 and next == end+0.000000000000001: #some precision problem, using this 0.000...1 to overcome, not so elegant.
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

#test this sub
#print frange(2,3,0.01)

############################################################################################
