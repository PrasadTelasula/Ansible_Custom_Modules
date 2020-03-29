#!/usr/bin/python
from ansible.module_utils.basic import AnsibleModule

def run_module():
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        name=dict(type='str', required=True)
    )

    
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )


    
    result = dict(
        changed=False,
        original_message='Hello ' + module.params['name'] + ' Welcome to Ansible custom Module Demo.',
    )

    
    module.exit_json(**result)

def main():
    run_module()

if __name__ == '__main__':
    main()
