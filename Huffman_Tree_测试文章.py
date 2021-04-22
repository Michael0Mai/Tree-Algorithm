#coding=utf8
import Huffman_Tree_1

#文章
text = "LISBON, Portugal -- Cristiano Ronaldo has been left off Portugal's national team squad for a pair of upcoming matches, the decision coming as the soccer great fights rape allegations in the United States. Ronaldo has been accused of rape by Kathryn Mayorga, who says the player assaulted her in Las Vegas in 2009. He has denied the accusation.Ronaldo was left off the squad for Portugal's second game in the UEFA Nations League at Poland on Oct. 11 and a friendly match in Glasgow against Scotland three days later. The Juventus forward also missed Portugal's first two post-World Cup matches last month, with coach Fernando Santos saying Ronaldo had only just moved to the Italian club and was still settling down there.Santos used the 33-year-old team captain's absence last month to try out younger players.Mayorga says the alleged assault left her with post-traumatic stress, and she wants an eight-year-old legal settlement of her charges thrown out because she says the psychological injuries made her incompetent to agree to it at the time.Las Vegas police are reopening their investigation into the assault allegations. Mayorga's attorney says his client was inspired by the #MeToo movement and is speaking out now in hopes of encouraging anyone who's suffered sexual assault in their past to come forward, reports CBS News correspondent Jamie Yuccas. Mayorga first told the German publication Der Spiegel about the night in 2009 she says Ronaldo raped her. The night still haunts her, according to her lawyer Leslie Stovall. "

#编码
huffman_key, huffman_codes = Huffman_Tree_1.encode_text(text)#获得编码的字典和编码

#解码
decode_text = Huffman_Tree_1.decode_huffman(huffman_key, huffman_codes)

print(text)
print(huffman_codes)
print(decode_text)

print("长度: %d" %(len(text)*8))

print("长度: %d" %len(huffman_codes))
print((len(huffman_codes)) / (len(text)*8))

for key, value in huffman_key.items():
    print(key, value)