class RSA:

    @staticmethod
    def __is_prime(num):
        # Method to check if a number is prime
        if num == 2:
            return True
        for i in range(2, (num // 2) + 1):
            if num % i == 0:
                return False
        return True

    def __validate_input(self, p, q):
        # Method to validate p and q
        # Check if p and q are same
        if p == q:
            raise ValueError("P and q cannot be same!")
        # Check p and q are prime
        if not self.__is_prime(p):
            raise ValueError("Value of p i.e {} must be prime!".format(p))
        if not self.__is_prime(q):
            raise ValueError("Value of q i.e {} must be prime!".format(q))

    @staticmethod
    def __gcd(e, r):
        # Method to Check e and n are co prime
        while r != 0:
            e, r = r, e % r
        return e

    def __get_e(self, r):
        # Method to get e
        for e in range(2, r):
            if self.__gcd(e, r) == 1:
                return e

    @staticmethod
    def __get_d(e, r):
        # Method to get d
        for d in range(r):
            if (e * d) % r == 1:
                return d

    def generate_public_and_private_keys(self, p, q):
        # Method to generate  public and private keys
        self.__validate_input(p, q)
        print("Calculating RSA values...")

        n = p * q
        r = (p - 1) * (q - 1)

        e = self.__get_e(r)
        d = self.__get_d(e, r)

        public_key = (e, n)
        private_key = (d, n)

        print("Public RSA key is {}".format(public_key))
        print("Private RSA key is {}".format(private_key))

        return public_key, private_key

    @staticmethod
    def encrypt(m, public_key):
        # Method to encrypt plain text m using public key
        print("Encrypting m...")
        e, n = public_key
        return int((m ** e) % n)

    @staticmethod
    def decrypt(c, private_key):
        # Method to decrypt cipher text c using private key
        print("Decrypting c...")
        d, n = private_key
        return int((c ** d) % n)
