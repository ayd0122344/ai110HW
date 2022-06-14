#【mynote】讓電腦做閱讀測驗
from transformers import pipeline

question_answerer = pipeline("question-answering")

#【mynote】SQuAD是為這個問答設計的問答資料庫
context = r"""
Extractive Question Answering is the task of extracting an answer from a text given a question. An example of a
question answering dataset is the SQuAD dataset, which is entirely based on that task. If you would like to fine-tune
a model on a SQuAD task, you may leverage the examples/pytorch/question-answering/run_squad.py script.
"""

#【mynote】程式從文章中抽取一段文字來回答
result = question_answerer(question="What is extractive question answering?", context=context)
print(
    f"Answer: '{result['answer']}', score: {round(result['score'], 4)}, start: {result['start']}, end: {result['end']}"
)
# Answer: 'the task of extracting an answer from a text given a question', score: 0.6177, start: 34, end: 95

result = question_answerer(question="What is a good example of a question answering dataset?", context=context)
print(
    f"Answer: '{result['answer']}', score: {round(result['score'], 4)}, start: {result['start']}, end: {result['end']}"
)
# Answer: 'SQuAD dataset', score: 0.5152, start: 147, end: 160