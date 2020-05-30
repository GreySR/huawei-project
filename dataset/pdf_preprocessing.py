import json
import pandas as pd

with open('pdf/title.csv', 'r') as f:
    for i, line in enumerate(f):
        l = line.strip().split('\t')
        with open('pdf/title1.csv', 'a') as f1:
            f1.write("%s\t%s\n" % (l[0].strip(), l[1].strip())) 
			
df = pd.read_csv('pdf/title1.csv', sep='\t', header=None, engine='python')
df.columns = ['No', 'Reference']

text = {}
for i in index:
    try:
        output = subprocess.check_output('python pdf2txt.py ' + 'pdf/' + str(i) + '.pdf', encoding='windows-1251') 
        text[i] = output
    except subprocess.CalledProcessError as e:
        text[i] = e.output
		
with open('dataset.json', 'w') as fw:
    json.dump(text, fw)
with open('dataset.json', 'r') as fr:
    text = json.load(fr)
	
columns=['No', 'title', 'text']
df_dataset1 = pd.DataFrame(columns=columns)

for i, (k, v) in enumerate(text.items()):
    n = int(k.strip())
    v = v.replace('\n', ' ').replace('\x0c', ' ').strip()
    l = v.find('МОСКВА')
    r = v.find('Председатель Правительства')
    if r == -1:
        r = v.find('Исполняющий обязанности')
    txt = v[l+6:r].strip()
    ttl = df[df['No']==n].Reference.values[0]
    df_dataset1 = df_dataset1.append({'No':n, 'title':ttl, 'text':txt}, ignore_index=True)

df_dataset1 = df_dataset1[['title', 'text']]
df_dataset2 = pd.read_csv(r'dataset2.csv', sep=';', header=None)
df_dataset2.columns = ['title', 'text']

df_dataset1 = df_dataset1.dropna()
df_dataset2 = df_dataset2.dropna()

res = pd.concat([df_dataset1, df_dataset2])
res.to_csv('dataset.csv', sep=';', index=False)

    


