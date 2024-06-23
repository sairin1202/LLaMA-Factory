import os
import json
from glob import glob
import random
from copy import deepcopy

sp_dict = {}
cnt = 0
def process_conversations(d):
    global cnt
    session = d['session']
    sp = d['sp']
    messages = [{
                    "role": 'system', 
                    "content":sp, 
                    "mask":0
                }]
    for idx, sess in enumerate(session):

        role = sess['role']
        content = sess['content']
        mask = sess['mask']

        messages.append(
                {
                    "role": role, 
                    "content":content, 
                    "mask":mask
                })
    return {"messages": messages}



with open('base_translated_Japanese.jsonl', 'r') as f:
    data = f.readlines()

new_data = []
for d in data:
    try:
        new_data.append(json.loads(d))
    except:
        print(d)

data = new_data

import random
train_data = []
for d in data:
    d = process_conversations(d)
    train_data.append(d)


random.shuffle(train_data)
print('length:', len(train_data))

with open('character_qwen_multiturn.json', 'w') as file: 
    json.dump(train_data, file, indent=4, ensure_ascii=False)


    


    

