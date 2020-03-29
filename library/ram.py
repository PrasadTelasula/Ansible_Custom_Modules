from ansible.module_utils.basic import AnsibleModule
import platform

def print_ram_util():

    # Memory
    print("Memory Info: ")
    with open("/proc/meminfo", "r") as f:
        lines = f.readlines()

    out = ["" + lines[0].strip()]
    out.append("" + lines[1].strip())
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
        message=print_ram_util(),
    )

    
    module.exit_json(**result)

def main():
    run_module()

if __name__ == '__main__':
    main()
