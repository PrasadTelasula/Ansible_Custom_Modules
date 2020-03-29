#!/usr/bin/python
from ansible.module_utils.basic import AnsibleModule

def run_module():
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        name=dict(type='str', required=True)
    )

    # seed the result dict in the object
    # we primarily care about changed and state
    # change is if this module effectively modified the target
    # state will include any data that you want your module to pass back
    # for consumption, for example, in a subsequent task
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )


    username = module.params['name']
    result = dict(
        changed=False,
        original_message='Hello ' + module.params['name'] + ' Welcome to Ansible custom Module Demo.',
    )

    
    module.exit_json(**result)

def main():
    run_module()

if __name__ == '__main__':
    main()
