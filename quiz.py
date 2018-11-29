from cryptography.fernet import Fernet


key = 'TluxwB3fV_GWuLkR1_BzGs1Zk90TYAuhNMZP_0q4WyM='

# Oh no! The code is going over the edge! What are you going to do?
message = b'gAAAAABb_ye1B8M5nykQIuPgIriZJ5kedxNFMpkpCBULFvSxXGGxxVtXavL1gvr \
            Lx0r_LmuuW8Jk9H8zCpgy5x0du-utBiG_mOzzzcrpozbNER_cCnWRUhf-TfoShK \
            bmehJcepCv3w25CAibWJ0Xngl6pYGgUJ3H0nBeZHBqe7y0JOvzpJmVGcAYQVFZh \
            7AG7T1y_hhkCya0'


def main():
    f = Fernet(key)
    print(f.decrypt(message))


if __name__ == "__main__":
    main()
