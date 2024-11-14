from time import sleep
import  threading
from datetime import datetime


def write_words(word_count, file_name):
    with open(file_name, 'a', encoding='utf-8') as file:
        for i in range(word_count):
            file.write(f'Какое-то слово № {i+1}\n')
            sleep(0.1)
        print(f'Завершилась запись в файл {file_name}')

time_start = datetime.now()

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

time_stop = datetime.now()
time_fin = time_stop - time_start

print(f'Время работы функций {time_fin}')

time_start2 =datetime.now()

tr1 = threading.Thread(target=write_words, args= (10, 'example5.txt'))
tr2 = threading.Thread(target=write_words, args= (30, 'example6.txt'))
tr3 = threading.Thread(target=write_words, args= (200, 'example7.txt'))
tr4 = threading.Thread(target=write_words, args= (100, 'example8.txt'))

tr1.start()
tr2.start()
tr3.start()
tr4.start()

tr1.join()
tr2.join()
tr3.join()
tr4.join()

time_stop2 = datetime.now()
time_fin2 = time_stop2 - time_start2

print(f'Время работы потоков {time_fin2}')

