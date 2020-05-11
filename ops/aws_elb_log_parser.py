import gzip
import re

import pandas as pd

pd.options.display.max_columns = None


def gen_parse_elb_log(file):
    prog = re.compile('(?P<type>\S+) (?P<timestamp>\S+) (?P<elb>\S+) (?P<client_port>\S+) '
                  '(?P<target_port>\S+) (?P<request_processing_time>\S+) '
                  '(?P<target_processing_time>\S+) (?P<response_processing_time>\S+) '
                  '(?P<elb_status_code>\S+) (?P<target_status_code>\S+) '
                  '(?P<received_bytes>\S+) (?P<sent_bytes>\S+) '
                  '(?P<request>".*?") (?P<user_agent>".*?") (?P<ssl_cipher>\S+) '
                  '(?P<ssl_protocol>\S+) (?P<target_group_arn>\S+) '
                  '(?P<trace_id>".*?") (?P<domain_name>".*?") '
                  '(?P<chosen_cert_arn>".*?") (?P<matched_rule_priority>\S+) '
                  '(?P<request_creation_time>\S+) (?P<actions_executed>".*?") '
                  '(?P<redirect_url>".*?") (?P<error_reason>".*?") '
                  '(?P<target_port_list>".*?") (?P<target_status_code_list>".*?")')
    
    for line in file:
        yield prog.match(line).groupdict()
        
def read_parse_elb_log_to_df(file_path):
    with gzip.open(file_path, 'rt') as f:
        df = pd.DataFrame(gen_parse_elb_log(f))
        df = df.astype(str)
        df = df.astype({'request_processing_time': float,
                        'target_processing_time': float,
                        'response_processing_time': float,
                        'received_bytes': int,
                        'sent_bytes': int})
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        df['request_creation_time'] = pd.to_datetime(df['request_creation_time'])
        df = df.set_index('timestamp')
        return df
      
a = read_parse_elb_log_to_df('****_elasticloadbalancing_ap-northeast-2_app.retarget-elb.****.log')
a.elb_status_code.value_counts()
