import json
import re

import pandas as pd
import psutil
import requests

def get_sessions(url, password_or_token):
    sess = requests.Session()
    
    login_url = f'http://{url}/login'
    session_url = f'http://{url}/api/sessions'
    
    sess.get(login_url)
    sess.post(login_url, data={**dict(sess.cookies), **{'password': password_or_token}})
    
    session_list = json.loads(sess.get(session_url).content.decode())
    res_df = pd.DataFrame([{'path': s['path'],
                            'id': s['kernel']['id'],
                            'last_activity': pd.to_datetime(s['kernel']['last_activity']).tz_localize(None),
                            'execution_state': s['kernel']['execution_state']} for s in session_list])
    return res_df

def get_memory_usages():
    procs = []
    for pid in psutil.pids():
        proc = psutil.Process(pid)
        cmd = ' '.join(proc.cmdline())

        if 'jupyter' in cmd:
            mem = round(proc.memory_info()[0] / 1e6, 2)
            kernel_id = re.findall('kernel-([a-z0-9\-]+)\.json', cmd)
            if kernel_id:
                procs.append({'mem_MB': mem, 'id': kernel_id[0]})
                
    return pd.DataFrame(procs)

def profile_memory_usage(url, password_or_token):
    sessions = get_sessions(url, password_or_token)
    memory_usages = get_memory_usages()
    
    return sessions.merge(memory_usages).set_index('path').sort_values(['mem_MB'], ascending=False)

if __name__ == '__main__':
    NOTEBOOK_URL = '127.0.0.1:8888'
    PASSWORD_OR_TOKEN = 'qwerty1234'

    profile_memory_usage(NOTEBOOK_URL, PASSWORD_OR_TOKEN)
