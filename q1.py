import nltk
from nltk.corpus import stopwords
from collections import Counter

# uncomment these while running for the first time
# nltk.download("punkt")
# nltk.download("stopwords")


def count_words(filename):
    try:
        with open(filename, "r") as file:
            text = file.read().lower()
            words = nltk.word_tokenize(text)
            words = [word for word in words if word.isalpha()]
            words = [word for word in words if word not in stopwords.words("english")]
            word_counts = Counter(words)
            return word_counts.most_common(5)
    except FileNotFoundError:
        print("File not found.")
        return []
    except Exception as e:
        print("An error occurred:", str(e))
        return []


file_path = input("Enter the path of the text file: ")
top_words = count_words(file_path)
if top_words:
    print("Top 5 most frequently occurring words:")
    for word, count in top_words:
        print(f"{word}: {count}")
else:
    print("No results.")


# if __name__ == "__main__":
#     main()
