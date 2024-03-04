S = input()

inTag = False
answer = ""
word = ""
for c in S:
    if inTag:
        answer += c
        if c == ">":
            inTag = False
    else:
        if c == "<":
            inTag = True
            answer += word[::-1] + c
            word = ""
        elif c == " ":
            answer += word[::-1] + " "
            word = ""
        else:
            word += c
answer += word[::-1]
print(answer)




# S = input()

# answer = ""
# word = ""
# isTag = False

# for ch in S:
#     if ch == "<":
#         answer += word[::-1] + ch
#         word = ""
#         isTag = True
#     elif ch == ">":
#         answer += ch
#         isTag = False
#     elif ch == " ":
#         if not isTag:
#             answer += word[::-1]
#             word = ""
#         answer += ch
#     else:
#         if isTag:
#             answer += ch
#         else:
#             word += ch
# answer += word[::-1]
# print(answer)