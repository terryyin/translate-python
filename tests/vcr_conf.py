#!/usr/bin/env python
import os

from vcr import VCR

FIXTURES_DIR = os.path.join(os.path.dirname(__file__), "fixtures")


vcr = VCR(
    record_mode='once',
    serializer='yaml',
    cassette_library_dir=os.path.join(FIXTURES_DIR, 'cassettes'),
    path_transformer=VCR.ensure_suffix('.yaml'),
)
