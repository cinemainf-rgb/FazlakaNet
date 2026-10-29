import socket
import hashlib
import binascii


class RouterAPI:

    def __init__(self):

        self.sock = None

    def send_cmd(
        self,
        words
    ):

        for w in words:

            if isinstance(
                w,
                str
            ):
                w = w.encode()

            l = len(w)

            if l < 0x80:

                self.sock.send(
                    bytes([l])
                )

            elif l < 0x4000:

                self.sock.send(
                    bytes([
                        l >> 8 | 0x80,
                        l & 0xFF
                    ])
                )

            self.sock.send(w)

        self.sock.send(b'\x00')

    def read_res(self):

        result = []

        try:

            while True:

                b = self.sock.recv(1)

                if not b:
                    break

                length = b[0]

                if length == 0:
                    break

                data = self.sock.recv(
                    length
                )

                result.append(
                    data.decode(
                        'utf-8',
                        errors='ignore'
                    )
                )

        except:
            pass

        return result

    def connect(
        self,
        ip,
        port,
        user,
        password
    ):

        try:

            self.sock = socket.socket(
                socket.AF_INET,
                socket.SOCK_STREAM
            )

            self.sock.connect(
                (
                    ip,
                    int(port)
                )
            )

            self.send_cmd(['/login'])

            result = self.read_res()

            challenge = None

            for item in result:

                if item.startswith(
                    '=ret='
                ):

                    challenge = (
                        binascii.unhexlify(
                            item.split('=')[2]
                        )
                    )

            if challenge:

                md5 = hashlib.md5()

                md5.update(
                    b'\x00'
                    +
                    password.encode()
                    +
                    challenge
                )

                response = (
                    '00'
                    +
                    binascii.hexlify(
                        md5.digest()
                    ).decode()
                )

                self.send_cmd([
                    '/login',
                    '=name='+user,
                    '=response='+response
                ])

                self.read_res()

            return True

        except:

            return False

    def get_profiles(self):

        self.send_cmd([
            '/ip/hotspot/user/profile/print'
        ])

        result = self.read_res()

        profiles = []

        for item in result:

            if item.startswith(
                '=name='
            ):

                profiles.append(
                    item.split(
                        '=',
                        2
                    )[2]
                )

        return profiles

    def create_user(
        self,
        username,
        profile
    ):

        self.send_cmd([
            '/ip/hotspot/user/add',
            f'=name={username}',
            '=password=',
            f'=profile={profile}'
        ])

        return self.read_res()
