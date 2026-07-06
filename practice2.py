# s=float(input())
# e=float(input())
# a=int(s*10)
# b=int(e*10)
# while a<=b:
#     print(f"{a/10:.1f}^2",end="")
#     a+=2
#     if a<=b:
#         print(", ",end="")
#     else:
#         print(end=".")
#
# l=["Hello","Hii","who',are","you","₯ℳ"]
# for i in l:
#     k=list(map(lambda x:x if not in "AEIOUaeiou" else "",i))
#

# def function_trees(ft,fc):
#     d={"mangoes":2,"apple":3,"oranges":1.5,"banana":1,"grapes":2}
#     def time_taken(mc):
#         total_time=fc/mc
#         return total_time*d[ft]
#     return time_taken
# oranges=function_trees("oranges",15)
# print(oranges(15))



class Book:
    total_books = 0
    def __init__(self, title, author):
        self.title = title
        self.author = author
        Book.total_books += 1
    @classmethod
    def from_string(cls, book_str):
        title, author = book_str.split("-")
        return cls(title, author)

    @staticmethod
    def is_valid_title(title):
        return len(title) >= 3
b1 = Book("Python", "Guido")
if Book.is_valid_title("AI"):
    b2 = Book.from_string("AI-OpenAI")
else:
    print("Invalid title")

print(Book.total_books)