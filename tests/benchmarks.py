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
    results['UUID from str'] = time.time() - timestamp

    timestamp = time.time()
    for _ in range(times):
        cls.UUID(bytes=b'\xc5\xfc\xf0\\c G\xec\x98\xc0\xbe\x84\xfd\xb1\xc3!')
    results['UUID from bytes'] = time.time() - timestamp

    timestamp = time.time()
    for _ in range(times):
        cls.uuid4()
    results['uuid4()'] = time.time() - timestamp

    timestamp = time.time()
    for _ in range(times):
        str(uuid_value)
    results['str(uuid)'] = time.time() - timestamp

    timestamp = time.time()
    for _ in range(times):
        uuid_value.bytes
    results['uuid.bytes'] = time.time() - timestamp

    timestamp = time.time()
    for _ in range(times):
        hash(uuid_value)
    results['hash(uuid)'] = time.time() - timestamp

    timestamp = time.time()
    for _ in range(times):
        uuid_value == other_value
    results['compare UUIDs'] = time.time() - timestamp

    return results


total = time.time()
total = {}
for cls in [uuid, fastuuid, cpp_uuid]:
    total[cls.__name__] = benchmark(cls, TIMES)


print('   * -')
for key in total.keys():
    print(f'     - ``{key}`` (ms)')

tests = list(total['uuid'].keys())

for name in tests:
    print(f'   * - {name}')
    for key in total.keys():
        print(f'     - {int(total[key][name] * 1000)}')
