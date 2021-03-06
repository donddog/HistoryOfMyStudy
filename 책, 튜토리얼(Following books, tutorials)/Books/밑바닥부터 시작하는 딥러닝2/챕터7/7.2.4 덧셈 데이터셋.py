from DefinitionOfAll import sequence

(x_train, t_train), (x_test, t_test) = \
    sequence.load_data('addition.txt', seed=1984)
char_to_id, id_to_char = sequence.get_vocab()

print(x_train.shape, t_train.shape) #결과 (45000, 7) (45000, 5)
print(x_test.shape, t_test.shape) #결과 (5000, 7) (5000, 5)
print(x_train[0]) #결과 [ 3  0  2  0  0 11  5]
print(t_train[0]) #결과 [ 6  0 11  7  5]
print(''.join([id_to_char[c] for c in x_train[0]])) #결과 71+118
print(''.join([id_to_char[c] for c in t_train[0]])) #결과 _189