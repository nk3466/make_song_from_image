import torch
from fastai.text.all import *

from transformers import GPT2LMHeadModel  # Using only GPT2LM Head Model
from transformers import PreTrainedTokenizerFast  # tokenizer


def inference(ko_sentence):
    tokenizer = PreTrainedTokenizerFast.from_pretrained("skt/kogpt2-base-v2", bos_token='</s>', eos_token='</s>',
                                                        unk_token='<unk>', pad_token='<pad>', mask_token='<mask>')
    model = GPT2LMHeadModel.from_pretrained(
        "kogpt_model_finetunned_all_version2")  # GPT2LMHeadModel/ AutoModelWithLMHead 확인
    text = ko_sentence
    input_ids = tokenizer.encode(text)
    gen_ids = model.generate(torch.tensor([input_ids]),
                             max_length=80,
                             repetition_penalty=2.0,
                             pad_token_id=tokenizer.pad_token_id,
                             eos_token_id=tokenizer.eos_token_id,
                             bos_token_id=tokenizer.bos_token_id,
                             use_cache=True
                             )
    generated = tokenizer.decode(gen_ids[0, :].tolist())
    generated_list = generated.split('.')[:-2]
    generated_result = ".".join(generated_list) + '.'

    print(generated_result)

    return generated_result
