Release
-------

To release a new version:

#. Add an entry to ``CHANGES.rst`` (version is read from the first matching
   heading, e.g. ``3.8.1``). ``setup.py`` syncs that version into
   ``translate/version.py`` on build.

#. Update the version in ``docs/source/conf.py`` if you maintain docs for that
   release.

#. Review ``requirements.txt`` and run ``make build`` locally.

#. Commit the release changes on ``master``.

#. Run ``make release``. This builds sdist/wheel, creates an annotated tag for
   the version from ``CHANGES.rst``, and pushes the tag to GitHub.

#. GitHub Actions (``.github/workflows/release.yml``) builds the package again
   and publishes it to PyPI when the tag is pushed. You do **not** run
   ``twine upload`` locally.

PyPI setup (one time)
---------------------

**Trusted publishing (recommended)**

Log in to PyPI as an owner of the ``translate`` project and add a trusted
publisher:

* **Owner:** ``terryyin``
* **Repository:** ``translate-python``
* **Workflow filename:** ``release.yml``
* **Environment name:** leave empty (the workflow does not use a GitHub
  Environment)

Pre-filled URL:

https://pypi.org/manage/project/translate/settings/publishing/?provider=github&owner=terryyin&repository=translate-python&workflow_filename=release.yml

**Fallback: API token**

If trusted publishing is not configured, create a PyPI API token scoped to the
``translate`` project and add it as the GitHub repository secret
``PYPI_API_TOKEN``. When that secret is set, the publish step uses it; when it
is unset, the step uses OIDC (trusted publishing).

Troubleshooting
---------------

See the `PyPI trusted publishers troubleshooting guide
<https://docs.pypi.org/trusted-publishers/troubleshooting/>`_.
