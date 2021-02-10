import os

import mock
import utils

from overlays.openstack import get_extended_vm_info

FAKE_MASTER_YAML = os.path.join(utils.TESTS_DIR, "fake_master_yaml")
FAKE_YAML = """
openstack:
  instances:
"""


class TestOverlays(utils.BaseTestCase):

    def setUp(self):
        super().setUp()
        with open(FAKE_MASTER_YAML, 'w') as fd:
            fd.write(FAKE_YAML)

    def tearDown(self):
        super().tearDown()
        os.remove(FAKE_MASTER_YAML)

    @mock.patch.object(get_extended_vm_info.constants, "MASTER_YAML_OUT",
                       FAKE_MASTER_YAML)
    @mock.patch.object(get_extended_vm_info, "VM_INFO", {})
    def test_get_node_instances(self):
        get_extended_vm_info.load_master_yaml_info()
        get_extended_vm_info.get_node_instances()
        self.assertEquals(get_extended_vm_info.VM_INFO, {})
