from RSA import RSA


def execute():
    try:
        p_q = input("Enter the prime numbers, p and q: ")
        p_q = p_q.split()
        rsa = RSA()
        public_key, private_key = rsa.generate_public_and_private_keys(int(p_q[0]), int(p_q[1]))
        m = input("Enter the plaintext message m (an integer): ")
        c = rsa.encrypt(int(m), public_key)
        print("The ciphertext c is {}".format(c))
        m = rsa.decrypt(c, private_key)
        print("The plaintext m is {}".format(m))
    except ValueError as e:
        print(e)


if __name__ == '__main__':
    execute()
