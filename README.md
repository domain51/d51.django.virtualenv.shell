d51.django.virtualenv.shell
===========================
Provides an isolated Django shell inside virtualenv.


Introduction
------------
You often need to be able to drop into a Django shell while developing.  This
package provides a mechanism for invoking that shell inside of [virtualenv][]
without having the normal Django "project" setup.


Usage
-----
This is meant to be used inside a script that sets up your minimum settings.
You need to, at a minimum, provide it with the settings for your specific
application.

    from d51.django.virtualenv.shell import VirtualEnvironmentShell
    shell = VirtualEnvironmentShell()
    shell.run({
        "INSTALLED_APPS": "my.reusable.app",
    })

This relies on [d51.django.virtualenv.base][] which provides basic behavior.


[virtualenv]: http://virtualenv.openplans.org/
[d51.django.virtualenv.base]: http://github.com/domain51/d51.django.virtualenv.base
