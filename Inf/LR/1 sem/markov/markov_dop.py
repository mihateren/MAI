SRC_WORD = "00000010 00000110"

PROGRAMM = [
	"e -> .", # конец программы
	"a0 -> 0a",
	"a1 -> 1a",
	"a  -> #a",
	"a -> b|",
	"0b -> b0",
	" -> a", # запись коретки в начале слова
]

STEPS_LIMIT = 10000


def NAM_interpreter(programmSource: list, word: str) -> str:
	programm = [i.split(" -> ") for i in programmSource]

	for i in range(STEPS_LIMIT):
		for find, replacer in programm:
			if find not in word:
				continue 

			print(word, find, replacer, sep=" ; ")
			word = word.replace(find, replacer.replace(".", ""), 1)

			if replacer[0] == ".":
				return word

			break
		else:
			return word

	return "Опаньки... Марков не отвечает"


print(NAM_interpreter(PROGRAMM, SRC_WORD))