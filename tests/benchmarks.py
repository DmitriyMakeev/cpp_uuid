import time
import uuid

import cpp_uuid
import fastuuid

TIMES = 1_000_000


def benchmark(cls, times) -> dict:
    results = {}
    uuid_value = cls.UUID('c5fcf05c-6320-47ec-98c0-be84fdb1c321')
    other_value = cls.UUID('c5fcf05c-6320-47ec-98c0-be84fdb1c321')
    timestamp = time.time()
    for _ in range(times):
        cls.UUID('c5fcf05c-6320-47ec-98c0-be84fdb1c321')
    results['uuid_from_string'] = int((time.time() - timestamp) * 1000)

    timestamp = time.time()
    for _ in range(times):
        cls.UUID(bytes=b'\xc5\xfc\xf0\\c G\xec\x98\xc0\xbe\x84\xfd\xb1\xc3!')
    results['uuid_from_bytes'] = int((time.time() - timestamp) * 1000)

    timestamp = time.time()
    for _ in range(times):
        cls.uuid4()
    results['uuid4'] = int((time.time() - timestamp) * 1000)

    timestamp = time.time()
    for _ in range(times):
        str(uuid_value)
    results['to_str'] = int((time.time() - timestamp) * 1000)

    timestamp = time.time()
    for _ in range(times):
        uuid_value.bytes
    results['to_bytes'] = int((time.time() - timestamp) * 1000)

    timestamp = time.time()
    for _ in range(times):
        hash(uuid_value)
    results['hash'] = int((time.time() - timestamp) * 1000)

    timestamp = time.time()
    for _ in range(times):
        uuid_value == other_value
    results['equals'] = int((time.time() - timestamp) * 1000)

    timestamp = time.time()
    for _ in range(times):
        uuid_value > other_value
    results['greater'] = int((time.time() - timestamp) * 1000)

    return results


total = time.time()
total = {}
for cls in [uuid, fastuuid, cpp_uuid]:
    total[cls.__name__] = benchmark(cls, TIMES)


def table_sep():
    print('+'.ljust(20, '='), end='+')
    for _ in total.keys():
        print(''.rjust(10, '='), end='+')
    print()


table_sep()

print('|'.ljust(20), end='|')
for key in total.keys():
    print(key.ljust(10), end='|')
print()

table_sep()

tests = list(total['uuid'].keys())

for name in tests:
    print(f'|{name}'.ljust(20), end='|')
    for key in total.keys():
        print(str(total[key][name]).rjust(10), end='|')
    print()

table_sep()
