# %% tags=["parameters"]
# declare a list tasks whose products you want to use as inputs
upstream = ['read-data']
product = None


# %% [markdown]
# ## Model
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM


# %%
tokenizer = AutoTokenizer.from_pretrained("moussaKam/mbarthez")

model = AutoModelForSeq2SeqLM.from_pretrained("moussaKam/mbarthez")

# %%
def f_decode_input(txt):
    input_ids = tokenizer([txt], return_tensors="pt")["input_ids"]
    logits = model(input_ids).logits
    masked_index = (input_ids[0] == tokenizer.mask_token_id).nonzero().item()
    probs = logits[0, masked_index].softmax(dim=0)
    _, predictions = probs.topk(5)
    return tokenizer.decode(predictions).split()