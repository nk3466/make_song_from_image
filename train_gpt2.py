from typing import Optional
import torch
import transformers
from transformers import AutoModelWithLMHead, PreTrainedTokenizerFast
from fastai.text.all import *
import fastai
import re
import torch
from transformers import GPT2LMHeadModel
from transformers import PreTrainedTokenizerFast

tokenizer = PreTrainedTokenizerFast.from_pretrained("skt/kogpt2-base-v2", bos_token='</s>', eos_token='</s>',
                                                    unk_token='<unk>', pad_token='<pad>', mask_token='<mask>')
with open('final.txt', encoding='cp949') as f:
    lines = f.read()
    lines = " ".join(lines.split())
    print(lines)


# model input output tokenizer
class TransformersTokenizer(Transform):
    def __init__(self, tokenizer):
        print('1')
        self.tokenizer = tokenizer

    def encodes(self, x):
        toks = self.tokenizer.tokenize(x)
        print('2')
        return tensor(self.tokenizer.convert_tokens_to_ids(toks))

    def decodes(self, x):
        print('3')
        return TitledStr(self.tokenizer.decode(x.cpu().numpy()))


# split data
train = lines[:int(len(lines) * 0.9)]
test = lines[int(len(lines) * 0.9):]
splits = [[0], [1]]

# init dataloader
tls = TfmdLists([train, test], TransformersTokenizer(tokenizer), splits=splits, dl_type=LMDataLoader)
batch, seq_len = 4, 256  # 배치사이즈 8에서 4로 수정(쿠다 오류때문에 줄여봄)
dls = tls.dataloaders(bs=batch, seq_len=seq_len)


## 데이터 학습
# gpt2 ouput is tuple, we need just one val
class DropOutput(Callback):
    def after_pred(self): self.learn.pred = self.pred[0]


model = GPT2LMHeadModel.from_pretrained('skt/kogpt2-base-v2')

learn = Learner(dls, model, loss_func=CrossEntropyLossFlat(), cbs=[DropOutput], metrics=Perplexity()).to_fp16()
lr = learn.lr_find()
print(lr)
learn.fine_tune(6)

