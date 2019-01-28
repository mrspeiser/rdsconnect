import os, random, string, random

k=''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(79))
with open('.key', 'w') as f:
    f.write(k)