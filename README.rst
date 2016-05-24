CMSPlugin Image Rollover
========================

A simple plugin that wraps two Bootstrap3ImageCMSPlugin plugins and hides the first when rolled-over.

Requirements
------------

No real requirements, but this is useless without the Aldryn Bootstrap3 package/addon.


Installation
------------

Aldryn
~~~~~~

TODO

Other installations
~~~~~~~~~~~~~~~~~~~

1. Install the package via `pip install cmsplugin-image-rollover`;
2. Add `cmsplugin_image_rollover` to your `INSTALLED_APPS` in the settings.py file for your project;
3. Migrate with `python manage.py migrate cmsplugin_image_rollover`.


Usage
-----

To use, place this plugin into your placeholder. Add two Bootstrap3ImageCMSPlugin plugins
inside it each containing an identically sized image.
