import xml.etree.ElementTree as ET
import pandas as pd

tree = ET.parse('pivotCacheRecords1.xml')
tree2=ET.parse('pivotCacheDefinition1.xml')
root = tree.getroot()
root2=tree2.getroot()

comb=root2[1][0][0][0]
comb=comb.attrib['v']
ano=root2[1][1][0][0]
ano=ano.attrib['v']
regiao=root2[1][2][0][0]
regiao=regiao.attrib['v']
uf=root2[1][3][0][0]
uf=uf.attrib['v']

list2=[]

for child in root:
    list1=[]
    for subchild in child:
        if subchild.tag=='{http://schemas.openxmlformats.org/spreadsheetml/2006/main}s': 
            continue

        try:
            list1.append(subchild.attrib['v'])
        except Exception:
            pass   
            
        list2.append(list1)

df = pd.DataFrame(list2)
df_column0 = df[0].astype(str).astype(int)
for i in range(len(root2[1][0][0])):
    # REPLACE i por root2[1][0][0][i].attrib['v']
    df_column0 = df_column0.replace(int(i), root2[1][0][0][i].attrib['v'])
df[0] = df_column0

df_column1 = df[1].astype(str).astype(int)
for i in range(len(root2[1][1][0])):
   
    df_column1 = df_column1.replace(int(i), root2[1][1][0][i].attrib['v'])
df[1] = df_column1

df_column2 = df[2].astype(str).astype(int)
for i in range(len(root2[1][2][0])):
    # REPLACE i por root2[1][0][0][i].attrib['v']
    df_column2 = df_column2.replace(int(i), root2[1][2][0][i].attrib['v'])
df[2] = df_column2

df_column3 = df[3].astype(str).astype(int)
for i in range(len(root2[1][3][0])):
    # REPLACE i por root2[1][0][0][i].attrib['v']
    df_column3 = df_column3.replace(int(i), root2[1][3][0][i].attrib['v'])
df[3] = df_column3

df[0]=df[0].astype(str)
df[1]=df[1].astype(int)

dict={0:'product', 1:'year', 2:'region',3:'uf',4:'jan',5:'feb',6:'mar',7:'apr',8:'may',9:'jun',10:'jul',11:'aug',12:'sep',13:'oct',14:'nov',15:'dec',16:'total'}

df.rename(columns=dict,
          inplace=True)



list4=[]

for child2 in iroot:
    list3=[]
    for subchild2 in child2:
        if subchild2.tag=='{http://schemas.openxmlformats.org/spreadsheetml/2006/main}s': 
            continue

        try:
            list3.append(subchild2.attrib['v'])
        except Exception:
            pass   
            
        list4.append(list3)

df2 = pd.DataFrame(list4)

df_column0a = df2[0].astype(str).astype(int)
for i in range(len(iroot2[1][0][0])):
    # REPLACE i por root2[1][0][0][i].attrib['v']
    df_column0a = df_column0a.replace(int(i), iroot2[1][0][0][i].attrib['v'])
df2[0] = df_column0a

df_column1a = df2[1].astype(str).astype(int)
for i in range(len(iroot2[1][1][0])):
   
    df_column1a = df_column1a.replace(int(i), iroot2[1][1][0][i].attrib['v'])
df2[1] = df_column1a

df_column2a = df2[2].astype(str).astype(int)
for i in range(len(iroot2[1][2][0])):
  
    df_column2a = df_column2a.replace(int(i), iroot2[1][2][0][i].attrib['v'])
df2[2] = df_column2a

df_column3a = df2[3].astype(str).astype(int)
for i in range(len(iroot2[1][3][0])):
   
    df_column3a = df_column3a.replace(int(i), iroot2[1][3][0][i].attrib['v'])
df2[3] = df_column3a

dict={0:'product', 1:'year', 2:'region',3:'uf',4:'jan',5:'feb',6:'mar',7:'apr',8:'may',9:'jun',10:'jul',11:'aug',12:'sep',13:'oct',14:'nov',15:'dec',16:'total'}

df2.rename(columns=dict,
          inplace=True)

df=df.drop_duplicates()
df2=df2.drop_duplicates()

df.to_csv('out_file.csv')
df2.to_csv('out_file2.csv')