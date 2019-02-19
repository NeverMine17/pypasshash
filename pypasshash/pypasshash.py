import binascii
from typing import Optional

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.hashes import SHA256, SHA1, Hash
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


def convert(src: str, src_alphabet: str, dst_alphabet: str) -> str:
    src_base = len(src_alphabet)
    dst_base = len(dst_alphabet)

    wet = src
    val = 0.0
    mlt = 1.0

    while len(wet) > 0:
        digit1 = wet[len(wet) - 1]
        val += int(mlt * src_alphabet.index(digit1))
        wet = wet[0: len(wet) - 1]
        mlt *= src_base

    wet = val
    ret = ""

    while wet >= dst_base:
        digit_val = wet % dst_base
        digit2 = dst_alphabet[int(digit_val)]
        ret = digit2 + ret
        wet /= int(dst_base)

    digit = dst_alphabet[int(wet)]

    return digit + ret


def parse_int(sin):
    """A version of int but fail-safe"""
    return int(sin) if sin.isdigit() else -99


def get_pass(master: str, salt: str, version: Optional[int] = 2) -> str:
    """
    Get derived password from PassHash
    :param master: Master password
    :param salt: Site key (e.g. amazon.com)
    :param version: PassHash version, either 1 or 2 (recommended)
    :return:
    """
    fullpass = ''
    if version not in [1, 2]:
        raise ValueError('Wrong version {}, use either version 1 or 2 '
                         '(you can find them here http://tinyurl.com/y2qlwnxp)')
    if version == 2:
        """In version 2 of PassHash, hash is generated using PBKDF2HMAC-SHA256 using 1000 iterations"""
        pbkdf2_hash = binascii.hexlify(
            PBKDF2HMAC(SHA256, 32, salt.encode(), 1000, default_backend()).derive(master.encode())).decode()
        fullpass = convert(pbkdf2_hash,
                           "0123456789abcdef", "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    if version == 1:
        """In version 1 of PassHash, hash is generated using SHA1(master + salt)"""
        hashobj = Hash(SHA1(), default_backend())
        hashobj.update(master.encode() + salt.encode())
        fullpass = convert(binascii.hexlify(hashobj.finalize()).decode(), "0123456789abcdef",
                           "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    passwd = ""
    chars = 0
    i = 0

    while chars < 12:
        j = i % 12
        if chars == 0 and (fullpass[j:j + 1].upper() != fullpass[j:j + 1]):
            passwd += fullpass[j:j + 1]
            chars += 1
        elif chars == 1 and (parse_int(fullpass[j:j + 1]) != -99):
            passwd += fullpass[j:j + 1]
            chars += 1
        elif chars == 2 and (fullpass[j:j + 1].lower() != fullpass[j:j + 1]):
            passwd += fullpass[j:j + 1]
            chars += 1
        elif chars > 2:
            passwd += fullpass[j:j + 1]
            chars += 1
        elif chars == 0 and i >= len(fullpass):
            passwd += 'f'
            chars += 1
        elif chars == 1 and i >= len(fullpass) * 2:
            passwd += '7'
            chars += 1
        elif chars == 2 and i >= len(fullpass) * 3:
            passwd += 'T'
            chars += 1
        i += 1

    return passwd
