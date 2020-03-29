from ansible.module_utils.basic import AnsibleModule
import platform

def print_system_info():

    # Architecture
    out = ["Architecture: " + platform.architecture()[0]]

    # machine
    out.append("Machine: " + platform.machine())

    # node
    out.append("Node: " + platform.node())

    # system
    out.append("System: " + platform.system())
   
    # distribution
    dist = platform.dist()
    dist = " ".join(x for x in dist)
    out.append("Distribution: " + dist)
    return(out)

def run_module():
    # define available arguments/parameters a user can pass to the module
    module_args = dict()

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    result = dict(
        changed=True,
        message=print_system_info(),
    )

    
    module.exit_json(**result)

def main():
    run_module()

if __name__ == '__main__':
    main()
