from log_analysis import get_log_file_path_from_cmd_line, filter_log_by_regex

def main():
    log_file = get_log_file_path_from_cmd_line(1)
    #records = filter_log_by_regex(log_file, 'SRC=(.*?) DST=(.*?) LEN=(.*?)', print_summary=True, print_records=True)
    pass



# TODO: Step 8
def tally_port_traffic(log_file):
    dest_port_logs = filter_log_by_regex(log_file, 'DPT=(.+?)')[1]

    dpt_tally = {}
    for dpt in dest_port_logs:
        dpt_tally[dpt] = dpt_tally.get(dpt, 0) + 1
    return

# TODO: Step 9
def generate_port_traffic_report(log_file, port_number):

    regex= r"^(.{6}) (.{8}). *SRC-(.+?) DST=(.+?) .*SPT=(.+?) " + f"DPT=({port_number})"
    return

# TODO: Step 11
def generate_invalid_user_report(log_file):
    return

# TODO: Step 12
def generate_source_ip_log(log_file, ip_address):
    return

if __name__ == '__main__':
    main()