#【mynote】判斷一個句子的語義是正面的/負面的
from transformers import pipeline

# Allocate a pipeline for sentiment-analysis
classifier = pipeline('sentiment-analysis')
result = classifier('We are very happy to introduce pipeline to the transformers repository.')
print(result) # [{'label': 'POSITIVE', 'score': 0.9996980428695679}]

#【mynote】字串中有「We are very happy」，結果為positive