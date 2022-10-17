import pandas as pd

config = open('config', 'r')
df = pd.read_csv('sample.csv')
statement = ''

linecount = df.shape[0]


for l in config:
    l=l.replace('\n','')
    var = l.split(')(')
    var[0]= var[0].replace('(','')
    var[1] = var[1].replace(')','').replace('\n','')
    demux = var[1].split(',')
    values = '\''
    vec = []
    
    for i in range(linecount):
        for s in demux:
            values = values + df[s].iloc[i]+ '\',\''
            #print(df[s].iloc[i])
        vec.append(values[:-2])
        values = '\''
    print(','.join(demux) +'   '+ (str(vec[0])))
    for s in vec:
        statement = statement + 'insert ('+','.join(demux) +') into table '+ var[0]+' values ('+s +');\n'

result = open('Insert.sql','w')
result.write(statement)
result.close()
config.close()