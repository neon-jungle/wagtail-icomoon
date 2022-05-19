A convenience package for adding `IcoMoon <https://icomoon.io/>`_ icons to the Wagtail admin.
At the moment only includes the general purpose icons, but could be extended.


Installation
============

.. code:: bash

    pip install wagtail-icomoon

Then add the following to your ``settings.py``:

.. code:: python

    INSTALLED_APPS = (
        ...
        'wagtail_icomoon',
        ...
    )


Usage
=====

e.g. for a streamfield block


.. code:: python
    
    from wagtail.core import blocks

    class DemoBlock(blocks.CharBlock):
        class Meta:
            icon = 'camera'

    
    # or as part of the initialisation of a StreamField
    body = StreamField([
        ('demo', blocks.CharBlock(icon='star')),
    ])


For a complete list of icons, see the `IcoMoon <https://icomoon.io/#preview-free>`_ website, or check the `templates/icons` directory of this project.