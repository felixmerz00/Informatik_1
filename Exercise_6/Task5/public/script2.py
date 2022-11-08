
def analyze(posts):

    possible_hashtags = []
    out_dict = {}

    for post in posts:
        hashtag = ""
        pos_hashtags = post.split("#")
        pos_hashtags.pop(0)                 

        for word in pos_hashtags:
            for i in range(len(word)):
                if i + 1 == len(word) and word[i].isalnum():
                    hashtag = word
                if not word[i].isalnum():
                    hashtag = word[:i]
                    break
            if hashtag:
                if hashtag[0].isalpha():
                    possible_hashtags.append(hashtag)

    for hashtag in possible_hashtags:
        out_dict[hashtag] = possible_hashtags.count(hashtag)

    return out_dict

posts = [
    "hi #weekend",
    "good morning #zurich #limmat",
    "spend my #weekend in #zurich",
    "#zurich <3"]
# print(analyze(posts))