import os
import sys
fpath = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                     '../fdint/fd.pyx'))

with open(fpath, 'w') as f:
    f.write("""'''
Fermi-Dirac integrals.

This file was generated by `scripts/gen_fd_pyx.py`, and should not
be edited directly.
'''
""")
    f.write('from fdint cimport _fdint\n')
    f.write('import numpy\n')
    for i in range(-9,22,2)+range(0,21,2):
        a = str(i).replace('-','m')
        f.write('''
def fd{a}h(phi, out=None):
    cdef int num
    if isinstance(phi, numpy.ndarray):
        num = phi.shape[0]
        if out is None:
            out = numpy.empty(num)
        else:
            assert isinstance(out, numpy.ndarray) and out.shape[0] == num
        _fdint.vfd{a}h(phi, out)
        return out
    else:
        return _fdint.fd{a}h(phi)
'''.format(a=a))