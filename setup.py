from setuptools import Extension, dist, setup


class BinaryDistribution(dist.Distribution):
    def has_ext_modules(self):
        return super().has_ext_modules()


setup(
    name='cpp-uuid',
    version='1.0.0',
    package_dir={'': 'src'},
    zip_safe=False,
    ext_modules=[
        Extension(
            'cpp_uuid',
            sources=['src/cpp_uuid/uuid.cpp'],
            include_dirs=['src/cpp_uuid/include'],
            extra_compile_args=['-Ofast', '-march=native'],
        )
    ],
    distclass=BinaryDistribution,
)
