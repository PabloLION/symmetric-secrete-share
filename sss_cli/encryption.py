import codecs
import nacl.utils
import nacl.secret
import nacl.exceptions
import typer


def encrypt(message: str, key: str) -> str:
    """
    Encrypt string with key
    """
    try:
        box = nacl.secret.SecretBox(codecs.encode(key, "utf-8"))
    except nacl.exceptions.ValueError:
        typer.secho("The key must be exactly 32 bytes long ", fg="red")
        raise typer.Abort()
    encrypted = box.encrypt(codecs.encode(message, "utf-8"))
    b64 = codecs.encode(encrypted, "base64").decode("utf-8")
    return b64


def decrypt(encrypted: str, key: str) -> str:
    """
    Encrypt string with key
    """
    try:
        box = nacl.secret.SecretBox(codecs.encode(key, "utf-8"))
    except nacl.exceptions.ValueError:
        typer.secho("The key must be exactly 32 bytes long ", fg="red")
        raise typer.Abort()
    byte_msg = codecs.decode(bytes(encrypted, "utf-8"), "base64")
    try:
        decrypted = box.decrypt(byte_msg).decode("utf-8")
    except nacl.exceptions.CryptoError:
        typer.secho("Decryption failed. Ciphertext failed verification", fg="red")
        raise typer.Abort()
    return decrypted


def test():
    fake_key = "I'm a sentence of 32 characters."
    msg = "i'm a secret message, but not a sentence, very very very long lorem ipsum dolor, very very very long lorem ipsum dolor, very very very long lorem ipsum dolor, very very very long lorem ipsum dolor, very very very long lorem ipsum dolor, very very very long lorem ipsum dolor, very very very long lorem ipsum dolor, very very very long lorem ipsum dolor"

    encrypted = encrypt(msg, fake_key)
    decrypted = decrypt(encrypted, fake_key)

    print(f"encrypted: \n{encrypted}")
    print(f"decrypted: \n{decrypted}")


if __name__ == "__main__":
    test()
