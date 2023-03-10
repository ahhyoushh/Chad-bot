# roasts_file = open('roasts.txt', encoding="utf-8")
# roasts = roasts_file.readlines()
# roasts = [roast.strip() for roast in roasts]

# with open('roasts.txt', 'r', encoding="utf-8") as r, open('roast_new.txt', 'w', encoding='utf-8') as o:
# 	for line in r:
# 		if line.strip():
# 			o.write(line)

from cosine import cosine, conv_vec

message = "Ohio moment"
Ohio_sent_list = ["only in ohio", "ohio moment", "bro is born in ohio", 'ohio', 'what', 'bruh', 'bro skipped']
message_vec = conv_vec(message)
for ohio_sentence in Ohio_sent_list:
	ohio_vec = conv_vec(ohio_sentence)
	result = cosine(message_vec, ohio_vec)
	print(result)