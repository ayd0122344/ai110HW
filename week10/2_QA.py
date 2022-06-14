from transformers import pipeline

# Allocate a pipeline for question-answering
question_answerer = pipeline('question-answering')
result = question_answerer({
    'question': 'What is the name of the repository ?',
    'context': 'Pipeline has been included in the huggingface/transformers repository'
})
print(result) # {'score': 0.30970096588134766, 'start': 34, 'end': 58, 'answer': 'huggingface/transformers'}

#【mynote】從內文判斷出問題的答案。因每次執行都要重跑一次，所以很耗記憶體。