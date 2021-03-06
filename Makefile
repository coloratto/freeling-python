
FREELINGDIR = /usr/local
LIBSDIR = /usr/local
PYTHONDIR = /usr/include/python2.6

_libmorfo_python.so: libmorfo_wrap.cxx
	g++ -shared -o _libmorfo_python.so libmorfo_wrap.cxx -lmorfo -ldb_cxx -lpcre -lomlet -lfries -lboost_filesystem-mt -I $(FREELINGDIR)/include -L $(FREELINGDIR)/lib  -I $(LIBSDIR)/include -L $(LIBSDIR)/lib -I $(PYTHONDIR) -fPIC

libmorfo_wrap.cxx: libmorfo_python.i
	swig -python -c++ -o libmorfo_wrap.cxx libmorfo_python.i


clean:
	rm -f libmorfo_wrap.cxx _libmorfo_python.so libmorfo_python.py libmorfo_python.pyc