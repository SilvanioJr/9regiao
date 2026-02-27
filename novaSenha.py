from werkzeug.security import generate_password_hash

senha = "Mota160320"
hash_ = generate_password_hash(
    senha,
    method="scrypt",         # força scrypt
    salt_length=16           # padrão comum do werkzeug
)

print(hash_)
