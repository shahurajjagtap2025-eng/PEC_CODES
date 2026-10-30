
import gnupg

# Initialize GnuPG
gpg = gnupg.GPG()

# Generate cryptographic keys
key_input = gpg.gen_key_input(
    name_real="Alice",
    name_email="alice@example.com",
    passphrase="alice123"
)

key = gpg.gen_key(key_input)

if not key:
    print("Key generation failed:", key.stderr)
    raise SystemExit

print("Key generated successfully!")
print("Fingerprint:", key.fingerprint)

# Export public key
public_key = gpg.export_keys(key.fingerprint)
print("\nPublic key exported successfully!")

# Original message
message = "Hello Bob, this is a secure PGP message."

# Encrypt message using public key
encrypted = gpg.encrypt(
    message,
    recipients=[key.fingerprint]
)

print("\nEncrypted Message:")
print(encrypted)

# Decrypt message using private key
decrypted = gpg.decrypt(
    str(encrypted),
    passphrase="alice123"
)

print("\nDecrypted Message:")
print(decrypted)

# Create digital signature
signature = gpg.sign(
    message,
    keyid=key.fingerprint,
    passphrase="alice123",
    detach=True
)

print("\nDigital Signature Created Successfully!")

# Verify digital signature
verified = gpg.verify_data(
    str(signature),
    message.encode("utf-8")
)

print("Signature Valid:", verified.valid)
