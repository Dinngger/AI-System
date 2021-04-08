from setuptools import setup
from torch.utils.cpp_extension import BuildExtension, CppExtension, CUDAExtension

setup(
    name='mylinear',
    ext_modules=[
        CppExtension('mylinear_cpp', [
            'mylinear.cpp'
        ]),
        CUDAExtension('mylinear_cuda', [
            'mylinear_cuda.cpp',
            'mylinear_cuda_kernel.cu',
        ])
    ],
    cmdclass={
        'build_ext': BuildExtension
    }
)
