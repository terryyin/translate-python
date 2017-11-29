Release
-------

To release a new version, a few steps are required:

* Update version/release number in ``docs/source/conf.py``

* Add entry to ``CHANGES.rst`` and documentation

* Review changes in test requirements ``requirements.txt``

* Test build with ``make build``

* Commit changes

* Release with ``make release``
