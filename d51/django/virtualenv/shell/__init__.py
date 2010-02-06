import pkg_resources
pkg_resources.declare_namespace(__name__)

from d51.django.virtualenv.base import VirtualEnvironment

class VirtualEnvironmentShell(VirtualEnvironment):
    def run(self, my_settings):
        super(VirtualEnvironmentShell, self).run(my_settings)
        self.call_command('shell')

