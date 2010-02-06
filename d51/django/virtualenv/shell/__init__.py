import pkg_resources
pkg_resources.declare_namespace(__name__)

from d51.django.virtualenv.base import VirtualEnvironment

class VirtualEnvironmentShell(VirtualEnvironment):
    def run_shell(self, my_settings):
        self.activate()
        if hasattr(self.caller, 'setUp'):
            self.caller.setUp()

        self.configure_settings(my_settings)
        self.call_command('shell')

