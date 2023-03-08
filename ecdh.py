import random
random.seed(1)
from ec import EllipticCurveSubGroup, Point

curve = EllipticCurveSubGroup(
    name='secp256k1',
    p=0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffefffffc2f,
    # Curve coefficients.
    a=0,
    b=7,
    # Base point.
    g=(0x79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798,
       0x483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8),
    # Subgroup order.
    n=0xfffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364141,
    # Subgroup cofactor.
    h=1
)


def make_keypair():
    private_key = random.randrange(1, curve.n)
    G = Point(curve, curve.g[0], curve.g[1])
    public_key = private_key*G
    return private_key, public_key


print('Curve:', curve.name)

# Alice generates her own keypair.
alice_private_key, alice_public_key = make_keypair()
print("Alice's private key:", hex(alice_private_key))
print("Alice's public key: (0x{:x}, 0x{:x})".format(*alice_public_key))

# Bob generates his own key pair.
bob_private_key, bob_public_key = make_keypair()
print("Bob's private key:", hex(bob_private_key))
print("Bob's public key: (0x{:x}, 0x{:x})".format(*bob_public_key))

# Alice and Bob exchange their public keys and calculate the shared secret.
s1 = alice_private_key * bob_public_key
s2 = bob_private_key * alice_public_key

assert s1 == s2

print('Shared secret: (0x{:x}, 0x{:x})'.format(*s1))
