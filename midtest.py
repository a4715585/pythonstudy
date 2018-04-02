import numpy as np
with open ('c:/Users/alex/Desktop/report.txt') as f:
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
    data1.insert(0, data[0])
    for score in data [1:]:
        if int(score)<60:
            sum += int(score)
            score = '不及格'
            data1.append(score)
        else:
            data1.append(score)
            sum += int(score)
    avr =int(sum/lens)
    data1.append(sum)
    data1.append(avr)
    results.append(data1)
results11 = sorted(results,key=lambda x:x[11],reverse=True)
i = 0
for xxx in results11:
    xxx.insert(0,i)
    i+=1
summ = 0
for i in a:
    result_2 =int('%d\n' %  (i/30))
    results_avr.append(result_2)
    summ += int(i/30)
print ('results_avr:',results_avr)
avrr = int(summ/9)
results_avr.append(summ)
results_avr.append(avrr)
results_avr.insert(0,'0,平均')
results_avr.append('\n')
results_avr = np.array(results_avr)
results_avr = results_avr.astype('str')
results111=','.join(results_avr)
print(results111)
output = open('results.txt','w')
output.write('名次,姓名,语文,数学,英语,物理,化学,生物,政治,历史,地理,总分,平均分'+'\n')
output.writelines(results111)
for xxxx in results11:
    #print (xxxx)
    output.writelines(str(xxxx))
    output.write('\n')
output.close()
