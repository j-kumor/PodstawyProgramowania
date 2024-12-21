import MyText 

text = "An apple a day keeps the doctor away"

print("Text:", text)
print("Number of words:", MyText.word_count(text))
print("Words from the longest:", ", ".join(MyText.words_ordered_by_length(text)))
print("Words ordered alphabetically:", ", ".join(MyText.words_alphabetically(text)))
