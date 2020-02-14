def sentence_maker(phrase):
    questions = ('when', 'where', 'why', 'how', 'who')
    capitalize = phrase.capitalize()

    if phrase.startswith(questions):
        return '{}?'.format(capitalize)
    else:
        return '{}.'.format(capitalize)

results = []
while True:
    user_input = input("Say something: ")
    if user_input == "/end":
        break
    else:
        results.append(sentence_maker(user_input))

print(" ".join(results))