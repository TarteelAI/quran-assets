# Language Models

## Generating a Language Model

### Setup

First, you'll need to build `kenlm` to create a language model.

```sh
git clone https://github.com/kpu/kenlm.git
cd kenlm; mkdir build; cd build
cmake ..
make -j $(nproc)
```

The binaries will be in the `build/bin` file.

### Creating the LM

Example of a 4-gram model

```sh
lmplz --order 4 --text ../text/vocab-UD.txt --arpa 4-gram-UD-lm.arpa
```
