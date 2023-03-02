import numpy as np


def load_z408():
    z408 = r"""
        9%P/Z/UB%kOR=pX=B
        WV+eGYF69HP@K!qYe
        MJY^UIk7qTtNQYD5)
        S(/9#BPORAU%fRlqE
        k^LMZJdr\pFHVWe8Y
        @+qGD9KI)6qX85zS(
        RNtIYElO8qGBTQS#B
        Ld/P#B@XqEHMU^RRk
        cZKqpI)Wq!85LMr9#
        BPDR+j=6\N(eEUHkF
        ZcpOVWI5+tL)l^R6H
        I9DR_TYr\de/@XJQA
        P5M8RUt%L)NVEKH=G
        rI!Jk598LMlNA)Z(P
        zUpkA9#BVW\+VTtOP
        ^=SrlfUe67DzG%%IM
        Nk)ScE/9%%ZfAP#BV
        peXqWq_F#8c+@9A9B
        %OT5RUc+_dYq_^SqW
        VZeGYKE_TYA9%#Lt_
        H!FBX9zXADd\7L!=q
        _ed##6e5PORXQF%Gc
        Z@JTtq_8JI+rBPQW6
        VEXr9WI6qEHM)=UIk
    """
    lines = [list(y) for y in (x.strip() for x in z408.split("\n")) if y]
    return np.array(lines)


z408_flat = load_z408().flatten()
part_size = z408_flat.size // 3

indexes = []
for idx1 in range(part_size):
    idx2, idx3 = idx1 + part_size, idx1 + (part_size * 2)
    indexes.append((idx1, idx2, idx3))


def count_symbol_positions(cipher):
    count = 0
    for idx1, idx2, idx3 in indexes:
        a, b, c = cipher[idx1], cipher[idx2], cipher[idx3]
        if a == b or a == c or b == c:
            count += 1

    return count


def run_test(rounds=10000):
    total = 0.0

    print("Characters that appear in the same position in more than one of three cipher sections")
    print("z408:")
    print(count_symbol_positions(z408_flat))
    
    for i in range(rounds):
        np.random.shuffle(z408_flat)
        total += count_symbol_positions(z408_flat)

    print("{} random shuffles (mean):".format(rounds))
    print(total / rounds)



run_test()