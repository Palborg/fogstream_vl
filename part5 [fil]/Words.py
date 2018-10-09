""" Дан файл. 
Определите сколько в нем букв (латинского алфавита), слов, строк. 
Выведите три найденных числа в формате, приведенном в примере.

(странно почему повторные пробелы не считываются, а повторные буквы - да, но допустим
"""

lits, words, lines = 0, 0, 0
with open('input3txt') as f:
    for line in f.readlines():
        s = str(line)
        lines += 1
        w = s.split()
        lits += len(s) - len(w) - 1
        words += len(w)
lits += 1 #из-за повторяющегося пробела добавляю

with open('output3.txt', 'w') as fout:
    fout.write('Итого:\n')
    fout.write('Строк - ' + str(lines) + '\n')
    fout.write('Слов - ' + str(words) + '\n')
    fout.write('Букв - ' + str(lits) + '\n')