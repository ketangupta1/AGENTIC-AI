# tiktoken is a package made by openAI which helps to tokenize and de-tokenize the text
import tiktoken

enc = tiktoken.encoding_for_model("gpt-4o")  #encoder

text = "Hey there! my name is Ketan"
tokens = enc.encode(text)  #encoding the text
print("Encoded tokens: ", tokens)

decoded = enc.decode([25216, 1354, 0, 922, 1308, 382, 658, 34322])  #decoding the tokens and converting to text
print("Decoded", decoded)


# Transformers generate text using next-token prediction.
# At each step, the model looks at the existing token sequence,
# predicts the most likely next token, appends it, and repeats
# this process to form a complete output.
