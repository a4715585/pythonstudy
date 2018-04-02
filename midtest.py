import os
import numpy as np
file1 = input('enter the file:')
if  not os.path.exists(file1):
    print(file1,"does not exist ")
else:
    with open (file1) as f:
        lines = f.readlines()
    results = []
    results_avr = []
    a =np.array([0, 0, 0, 0, 0, 0, 0, 0, 0])
    for line in lines:
        data1 = []
        data = line.split()
        b = np.array(data[1:])
        b=b.astype('int')
        a=a+b
        lens = len(data) - 1
        sum=0
        data1.insert(0,str(data[0]))
        for score in data [1:]:
            if int(score)<60:
                sum += int(score)
                score = '不及格'
                data1.append(str(score))
            else:
                data1.append(str(score))
                sum += int(score)
        avr =float('%.2f' % (sum/lens))
        data1.append(str(sum))
        data1.append(str(avr))
        results.append(data1)
    results11 = sorted(results,key=lambda x:x[11],reverse=True)
    #print (results11)
    i = 1
    for xxx in results11:
        xxx.insert(0,str(i))
        i+=1
    #print(results11)
    summ = 0
    for i in a:
        result_2 =str('%.2f' %  (i/30))
        results_avr.append(result_2)
        summ += int(i/30)
    print ('results_avr:',results_avr)
    avrr = float('%.2f' % (summ/9))
    results_avr.append(str(summ))
    results_avr.append(str(avrr))
    results_avr.insert(0,'0,平均')
    #results_avr.append('\n')
    #results_avr = np.array(results_avr)
    #results_avr = results_avr.astype('str')
    results111=','.join(results_avr)
    print(results111)
    output = open('results.txt','w')
    output.write('名次,姓名,语文,数学,英语,物理,化学,生物,政治,历史,地理,总分,平均分'+'\n')
    output.writelines(results111)
    output.writelines('\n')
    for xxxx in results11:
        output.writelines(' '.join(xxxx))
        output.writelines('\n')
    output.close()
