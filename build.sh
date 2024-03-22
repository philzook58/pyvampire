# untested but something like this
git clone  --recurse-submodules https://github.com/vprover/vampire.git vampire_src
cd vampire_src/z3
mkdir build && cd build
cmake .. -DZ3_SINGLE_THREADED=1 -DCMAKE_BUILD_TYPE=Release -DZ3_BUILD_LIBZ3_SHARED=FALSE
make
cd ../..
mkdir build && cd build
cmake .. -DBUILD_SHARED_LIBS=0
make
#cp /bin/vampire* ../../