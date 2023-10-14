SRC_WORD = "1111"

PROGRAMM = [
	">1 -> 1>",
	">0 -> 0>",
	"> -> <",
	"1< -> <0",
	"0< -> 1#",
	"< -> 1#",
	"# -> .",
	" -> >",
]

STEPS_LIMIT = 3000


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