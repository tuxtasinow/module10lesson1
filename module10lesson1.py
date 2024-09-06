import time
from threading import Thread
from datetime import datetime

time_start = datetime.now()


def wite_words(word_count, file_name):
    with open(file_name, 'a', encoding='UTF-8') as file:
        for i in range(word_count):
            file.write(f'Какое-то слово № {i}' + '\n')
        time.sleep(0.1)
    print(f'Завершилась запись в файл {file}')

func_first = wite_words(10, 'example1.txt')
func_second = wite_words(30, 'example2.txt')
func_third = wite_words(200, 'example3.txt')
func_four = wite_words(100, 'example4.txt')

time_end_1 = datetime.now()
time_res_1 = time_end_1 - time_start
print(time_res_1)

thr_first = Thread(target=wite_words, args=(10, 'example5.txt'))
thr_second = Thread(target=wite_words, args=(30, 'example6.txt'))
thr_third = Thread(target=wite_words, args=(200, 'example7.txt'))
thr_four = Thread(target=wite_words, args=(100, 'example8.txt'))

thr_first.start()
thr_second.start()
thr_third.start()
thr_four.start()

thr_first.join()
thr_second.join()
thr_third.join()
thr_four.join()

time_end_2 = datetime.now()
time_res_2 = time_end_2 - time_start
print(time_res_2)
