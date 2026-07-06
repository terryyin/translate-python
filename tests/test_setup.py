#!/usr/bin/env python
# encoding: utf-8
import importlib.util
import os
from unittest import mock


def _load_setup_module():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    setup_path = os.path.join(root, 'setup.py')
    spec = importlib.util.spec_from_file_location('project_setup', setup_path)
    setup_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(setup_module)
    return setup_module


def test_setup_declares_python_36_minimum():
    captured = {}

    def fake_setup(**kwargs):
        captured.update(kwargs)

    setup_module = _load_setup_module()
    with mock.patch.object(setup_module, 'setup', side_effect=fake_setup), \
         mock.patch.object(setup_module, 'save_version'):
        setup_module.run()

    assert captured.get('python_requires') == '>=3.6'

    classifiers = captured.get('classifiers', [])
    stale = {
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
    }
    assert not stale.intersection(classifiers)
    assert 'Programming Language :: Python :: 3.6' in classifiers
