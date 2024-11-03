This repo demonstrates a problem with the signature_crossrefs in mkdocstrings.
Here's how to set it up to reproduce the problem

1. Setup and activate a virtualenv.
2. Run `pip install -e .`
3. Run `mkdocs serve`
4. Go to http://127.0.0.1:8000/ to see the examples.

The examples show that if a class field name matches the field type, the
signature_crossrefs link breaks.
